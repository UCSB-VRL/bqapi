# Bisque API for Python 3

[![Upload Python Package](https://github.com/UCSB-VRL/bqapi/actions/workflows/python-publish.yml/badge.svg)](https://github.com/UCSB-VRL/bqapi/actions/workflows/python-publish.yml)

[Full Documentation](https://github.com/UCSB-VRL/bisqueUCSB)

For development, follow [this guide](https://towardsdatascience.com/how-to-upload-your-python-package-to-pypi-de1b363a1b3) and [this repo](https://github.com/gmyrianthous/example-publish-pypi).

# Installing
```
pip install bqapi-ucsb
```

[Pypi link](https://pypi.org/project/bqapi-ucsb)

# Usage
```python
from bqapi.comm import BQSession
from bqapi.util import fetch_blob
```

# Development

For development, follow [this guide](https://towardsdatascience.com/how-to-upload-your-python-package-to-pypi-de1b363a1b3) and [this repo](https://github.com/gmyrianthous/example-publish-pypi).

## Added GitHub Action

### Summary

1. Clone repo
2. Make any necessary changes to source code, setup.py, and setup.cfg
3. Run `python setup.py sdist` on main folder
4. Install twin if not installed, `pip install twine`
5. Make sure to have PyPi account credentials
6. run `twine upload dist/*` from  main folder
7. Enter username and password
