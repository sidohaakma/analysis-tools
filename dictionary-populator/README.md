# Opal populator

##  Usage
```bash
pip install opal-populator
```


## Develop
Setup virtualenv.

```bash
virtualenv --python=/usr/bin/python env
```

Activate the virtualenv

```bash
source env/bin/activate
```

Deactivate the virtualenv

```bash
deactivate
```

Install the package within the virtual env

```bash
python setup.py install --user
```

## Upgrade Opal client
Please push the new version of the opal-python-client to https://registry.molgenis.org/repository/pypi. 

Build it with:

```
virtualenv --python=/usr/bin/python env
source env/bin/activate

# install with wheel dist
python setup.py bdist_wheel
```
