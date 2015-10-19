__author__ = 'phendricks'
from setuptools import setup

setup(name='pyprofilr',
      version='0.1',
      description='Profile data in Python',
      url='http://github.com/paulhendricks/pyprofilr',
      author='Paul Hendricks',
      author_email='paul.hendricks.2013@owu.edu',
      license='MIT',
      packages=['pyprofilr'],
      zip_safe=False, 
      test_suite='nose.collector', 
      tests_require=['nose'])