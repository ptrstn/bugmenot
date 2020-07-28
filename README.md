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

### Command Line

```bash
bugmenot <url>
```

### Python

```python
import bugmenot
credentials = bugmenot.get_credentials("<your-website>")
```
