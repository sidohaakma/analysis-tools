
from setuptools import setup

setup(
    name='opal-populator',
    version='0.0.2',
    packages=['populator', 'populator.ws', 'populator.ws.utils'],
    description='A command line interface to populate versions of datadictionaries in Opal',
    url='https://github.com/lifecycle-project/analysis-tools',
    author='Sido Haakma',
    author_email='sido@haakma.org',
    license='GNU Lesser General Public License 3.0',
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'populator = populator.__main__:main'
        ]
    },
    dependency_links = ["https://registry.molgenis.org/repository/pypi-all/opal-python-client"],
    install_requires=['opal-python-client==2.13.1', 'Click==7.0'] 
    
)