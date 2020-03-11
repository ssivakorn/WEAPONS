# WEAPONS
**W**eb **E**ncryption **A**nalysis **P**rogram for **ON**line **S**ervices

## What is WEAPONS?
WEAPONS is a novel black-box testing tool for evaluating the completeness and
correctness of web encryption deployment which includes the deployment
of HTTPS and other web encryption-related mechanisms, namely:

* HTTPS
* HTTPS Redirection
* HSTS (HSTS directives e.g., ``Max-Age``, ``includeSubdomain``)
* HSTS Preload (``Preloaded``)
* Secure Cookie

## Installation
WEAPONS is implemented with Python 3.7+ and mainly built on Selenium Web Driver
(https://selenium-python.readthedocs.io/). Selenium is an open-source browser
automation framework. Please see our ``requirements.txt`` for required
dependencies. We recommend to install WEAPON with virtual environment
(https://docs.python.org/3/library/venv.html).


### Dependencies
Here we list our dependencies. To see the most recent updated, please refer to
``requirements.txt``.

* Python 3.7+
* Selenium (https://pypi.org/project/selenium/)
* Selenium-wire (https://pypi.org/project/selenium-wire/)
* TLDExtract (https://pypi.org/project/tldextract/)
* yattag (https://pypi.org/project/yattag/)

### Web Driver
We opt for Chromium WebDriver, so we can leverage the rich functionality of the browser engine. 
Specifically we build on top of Google Chrome Version 80.0. The WebDriver can
be downloaded from https://chromedriver.chromium.org/downloads.



### Getting Started
To run, navigate to ``src`` and 
```
$ python3 weapons.py <WEBDRIVER> <URL>
```

where
* ``<WEBDRIVER>`` is the location of unzipped downloaded webdriver (see above).
* ``<URL>`` is a URL of testing website e.g.,

```
$ python3 weapons.py webdriver/chromedriver "https://ibanking.bangkokbank.com"
```

We also include our example of output report generated from WEAPONS in
https://github.com/ssivakorn/WEAPONS/tree/master/examples.

## Questions?
Feel free to use issue to contact us for any questions, concerns as well as
report any bugs or suggest new features.

