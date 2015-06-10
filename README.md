# kodetest

[![build-status-image]][travis]
[![pypi-version]][pypi]
[![wheel]][pypi]

## Overview

Tilhørende tester for programmeringsoppgavene på kodeklubben.github.io

## Installation

Install using `pip`...

```bash
pip install kodetest
```

## Example

TODO: Write example.

## API reference

API reference is at http://kodetest.rtfd.org.

## Development
Install dependencies and link development version of kodetest to pip:
```bash
git clone https://github.com/arve0/kodetest
cd kodetest
pip install -r requirements.txt # install dependencies and kodetest-package
```

### Testing
```bash
tox
```

### Build documentation locally
To build the documentation:
```bash
pip install -r docs/requirements.txt
make docs
```



[build-status-image]: https://secure.travis-ci.org/arve0/kodetest.png?branch=master
[travis]: http://travis-ci.org/arve0/kodetest?branch=master
[pypi-version]: https://pypip.in/version/kodetest/badge.svg
[pypi]: https://pypi.python.org/pypi/kodetest
[wheel]: https://pypip.in/wheel/kodetest/badge.svg
