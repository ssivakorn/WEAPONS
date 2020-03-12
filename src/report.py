import tldextract
from yattag import Doc


class Report():
    def __init__(self, url):
        self._url = url

        dpart     = tldextract.extract(self._url)
        self._domain    = f'{dpart.domain}.{dpart.suffix}'.lower()
        self._subdomain = f'{dpart.subdomain}.{dpart.domain}.{dpart.suffix}'.lower()


        self._doc, self._tag, self._text = Doc().tagtext()

    def add_request(self, requests):
        self._requests = requests

    @classmethod
    def get_domain(cls, url):
        dpart = tldextract.extract(url)
        return {
            'url'       : url,
            'domain'    : f'{dpart.domain}.{dpart.suffix}'.lower(),
            'subdomain' : f'{dpart.subdomain}.{dpart.domain}.{dpart.suffix}'.lower(),
        }



    def is_subdomain(self, req):
        domain = Report.get_domain(req.path)
        if self._domain == domain["domain"]:
            return True

        return False

    def format_response(self, req):

        #dpart = tldextract.extract(req.path)
        #style = 'color: blue' if self._domain == f'{dpart.domain}.{dpart.suffix}' else ''

        domain = Report.get_domain(req.path)

        style = 'color: blue' if self.is_subdomain(req) else ''
        with self._tag('li', style=style):
            self._text(f'Path: {domain["url"]}')
        with self._tag('li'):
            self._text(f'Domain: {domain["domain"]}')
        with self._tag('li'):
            self._text(f'Subdomain: {domain["subdomain"]}')
        with self._tag('li'):
            self._text(f'HTTP Status Code: {req.response.status_code}')
        with self._tag('li'):
            self._text(f'HTTP Response Header:')
            with self._tag('pre'):
                self._text('\n'.join([f'{name}: {value}' for name, value in req.response.headers.items()]))


    def print_hsts(self):
        hsts = set()

        with self._tag('h2'):
            self._text(f'Strict Transport Security')
        for req in self._requests:
            if not req.response:
                continue
            if not self.is_subdomain(req):
                continue
            for name, value in req.response.headers.items():
                if name.lower() == 'strict-transport-security':
                    # with self._tag('pre'):
                    #     self._text(f'{name}: {value}')
                    hsts.add((f'{Report.get_domain(req.path)["subdomain"]}',
                              f'{name}:{value}'))

        with self._tag('p'):
            with self._tag('ul'):
                for domain, value in hsts:

                    with self._tag('li'):
                        self._text(f'Domain: {domain}')
                        with self._tag('pre'):
                            self._text(value)


    def print_req_response(self):
        response_lst = list()

        with self._tag('h2'):
            self._text(f'Response Headers')

        with self._tag('p'):
            with self._tag('ul'):
                for req in self._requests:
                    if not req.response:
                        continue
                    if not self.is_subdomain(req):
                        response_lst.append(req)
                        continue

                    self.format_response(req)

        with self._tag('h3'):
            self._text(f'Other Response Headers')

        with self._tag('p'):
            with self._tag('ul'):
                for req in response_lst:
                    self.format_response(req)


    def generate(self):

        with self._tag('html'):
            with self._tag('body'):
                with self._tag('h1'):
                    self._text('WEAPONS Report')
                with self._tag('h2'):
                    self._text(f'Requested URL: {self._url}')
                self.print_hsts()
                self.print_req_response()

        with open('output.html', 'w') as fp:
            fp.write(self._doc.getvalue())

        #return doc.getvalue()


