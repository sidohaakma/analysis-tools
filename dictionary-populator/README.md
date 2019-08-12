# Dictionary populator
This python package installs published data dictionaries on your Opal system.

For now we have three LifeCycle tables.

- monthly_repeated_measures
- yearly_repeated_measures
- non_repeated_measures

The versioning of the tables is included in the package.

##  Usage
You first need to install Python on your system. Python 2.7.x to be precise.

### Windows
You need to download this version of Python and install it.

https://www.python.org/downloads/release/python-2716/

Then add Python to the Windows PATH.

```
## Python installation path e.g.
setx PATH "%PATH%;C:\Python27
```

When you installed Python on your system you need to install **pip** by navigating to:

https://bootstrap.pypa.io/get-pip.py

You need to add pip to the Windows PATH as well.

```
## Python installation path e.g.
setx PATH "%PATH%;C:\Python27\Scripts
```

Now your set to install the dictionary-populator. Please navigate to the Windows Commandline interface by clicking on *Start* --> *Search* and type **cmd**.

```pip install dictionary-populator```

### Mac
You need to download this version of Python and install it.

https://www.python.org/downloads/release/python-2716/

When you installed Python on your system you need to navigate to a terminal on the Mac.

Within the terminal you need to follow the instructins below.

![install](https://github.com/lifecycle-project/analysis-tools/raw/master/dictionary-populator/docs/images/mac_install_dictionary_populator.gif "Install dictionary populator on your system")

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

Install the package within the virtual env. First you need to install the opal-client locally

```bash
export PYCURL_SSL_LIBRARY=openssl
export LDFLAGS=-L/usr/local/opt/openssl/lib;export CPPFLAGS=-I/usr/local/opt/openssl/include;pip install opal-python-client --compile --no-cache-dir -i https://registry.molgenis.org/repository/pypi-all/
```

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

# upload it into the molgenis pypi registry
twine 
```



