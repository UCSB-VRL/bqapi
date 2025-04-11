# Bisque API for Python 3

[![Upload Python Package](https://github.com/UCSB-VRL/bqapi/actions/workflows/python-publish.yml/badge.svg)](https://github.com/UCSB-VRL/bqapi/actions/workflows/python-publish.yml)
[![Pre-commit Checks](https://github.com/UCSB-VRL/bqapi/actions/workflows/pre-commit.yml/badge.svg)](https://github.com/UCSB-VRL/bqapi/actions/workflows/pre-commit.yml)
[![PyPI](https://img.shields.io/pypi/v/bqapi-ucsb?style=flat-square)](https://pypi.org/project/bqapi-ucsb/)
[![Documentation](https://img.shields.io/badge/Documentation-View%20here-brightgreen?style=flat-square)](https://bisque.gitbook.io/docs)
[![PyPi Installs](https://pepy.tech/badge/bqapi-ucsb?style=flat-square)](https://pepy.tech/project/bqapi-ucsb)



## Install
```
pip install bqapi-ucsb
```

## Usage

### Upload Image

Upload your first image to BisQue using our tutorial!

[Upload an Image to BisQue](https://bisque.gitbook.io/docs/bisque-api/upload-an-image)


## Development

For development, follow [this guide](https://towardsdatascience.com/how-to-upload-your-python-package-to-pypi-de1b363a1b3) and [this repo](https://github.com/gmyrianthous/example-publish-pypi).


## Contribute

1. Clone repo
2. Make any necessary changes to source code, setup.py, and setup.cfg
3. Run `python setup.py sdist` on main folder
4. Install twin if not installed, `pip install twine`
5. Make sure to have PyPi account credentials
6. run `twine upload dist/*` from  main folder
7. Enter username and password
