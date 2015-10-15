__author__ = 'phendricks'
from setuptools import setup

setup(name='profile',
      version='0.1',
      description='The funniest joke in the world',
      url='http://github.com/paulhendricks/funniest',
      author='Flying Circus',
      author_email='flyingcircus@example.com',
      license='MIT',
      packages=['funniest'],
      zip_safe=False, 
      test_suite='nose.collector', 
      tests_require=['nose'])