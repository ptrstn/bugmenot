[![PyPI version](https://badge.fury.io/py/bugmenot.svg)](https://badge.fury.io/py/bugmenot)
[![Actions Status](https://github.com/ptrstn/bugmenot/workflows/Python%20package/badge.svg)](https://github.com/ptrstn/bugmenot/actions)
[![Build Status](https://travis-ci.com/ptrstn/bugmenot.svg?branch=master)](https://travis-ci.com/ptrstn/bugmenot)
[![codecov](https://codecov.io/gh/ptrstn/bugmenot/branch/master/graph/badge.svg)](https://codecov.io/gh/ptrstn/bugmenot)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# bugmenot

An unofficial Python package to retrieve credentials from [BugMeNot.com](http://bugmenot.com/).

## Installation

```bash
pip install --user git+https://github.com/ptrstn/bugmenot
```

## Usage

### Command-line

```bash
usage: bugmenot [-h] [--version] url

An unofficial BugMeNot.com client

positional arguments:
  url         URL to the website

optional arguments:
  -h, --help  show this help message and exit
  --version   show program's version number and exit
```

### Python

```python
import bugmenot
credentials = bugmenot.get_credentials("<your-website>")
```

## Example

This command returns a list of (subsequently anonymized) bugmenot.com entries in tabular form:

```bash
bugmenot oracle.com
```

```bash
                               username                   password success_rate votes       age 
             fake-example@gvnuclear.com                  BugMeNot3          85%  1555  2 months 
           fake-example-fake-@awdrt.org             sdfdsfdsfd&-45          71%  2130  2 months 
              fake-example-a@wizard.com       sdfdsfdsfdsfsfsdfsdd          60% 13053    1 year 
                     fake-exa@urhen.com        asdfdsafasdfadsfass          60% 11261 12 months 
              fake-exam@rowingbreak.com        sffsdfdsfdsafasdfsa          59%  6274  8 months 
another-fake-example-entry-123@mail.com                  Abcsdfklj          53% 14989   7 years 
```
