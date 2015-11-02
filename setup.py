try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='pyprofilr',
      version='0.1',
      description='Profile data in Python',
      long_description="""
pyprofilr is a library for profiling data in Python 3.
""",
      url='http://github.com/paulhendricks/pyprofilr',
      author='Paul Hendricks',
      author_email='paul.hendricks.2013@owu.edu',
      maintainer='Paul Hendricks',
      maintainer_email='paul.hendricks.2013@owu.edu',
      license='MIT',
      packages=['pyprofilr', 'pyprofilr.test'],
      zip_safe=False, 
      test_suite='nose.collector', 
      tests_require=['nose'])
