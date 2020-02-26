import tldextract
from yattag import Doc


class Report():
    def __init__(self, url):
        self._url = url

        dpart     = tldextract.extract(self._url)
        self._domain    = f'{dpart.domain}.{dpart.suffix}'
        self._subdomain = f'{dpart.subdomain}.{dpart.domain}.{dpart.suffix}'

        self._doc, self._tag, self._text = Doc().tagtext()

    def add_req_response(self, requests):
        self._requests = requests

    def gen_req_response(self):
        for req in self._requests:
            if req.response:
                with self._tag('p'):
                    with self._tag('ul'):
                        dpart = tldextract.extract(req.path)
                        style = 'color: blue' if self._domain == f'{dpart.domain}.{dpart.suffix}' else ''
                        with self._tag('li', style=style):
                            self._text(f'Path: {req.path}')
                        with self._tag('li'):
                            self._text(f'Domain: {dpart.domain}.{dpart.suffix}')
                        with self._tag('li'):
                            self._text(f'Subdomain: {dpart.subdomain}.{dpart.domain}.{dpart.suffix}')
                        with self._tag('li'):
                            self._text(f'HTTP Status Code: {req.response.status_code}')
                        with self._tag('li'):
                            self._text(f'HTTP Response Header:')
                            with self._tag('pre'):
                                self._text('\n'.join([f'{name}: {value}' for name, value in req.response.headers.items()]))


    def generate(self):

        with self._tag('html'):
            with self._tag('body'):
                with self._tag('h1'):
                    self._text('WEAPONS Report')
                with self._tag('h2'):
                    self._text(f'Requested URL: {self._url}')
                self.gen_req_response()

        with open('output.html', 'w') as fp:
            fp.write(self._doc.getvalue())

        #return doc.getvalue()


