# profile.py
# 
# Copyright (C) 2015
# Paul Hendricks, http://www.paulhendricks.io
# All rights reserved.
#
# This is the core of pyprofilr.

import pandas
import numpy
from sklearn.datasets import load_boston

data = pandas.DataFrame(load_boston().data)
data.describe()

__all__ = ['profile']


def joke():
    return u'Wenn ist das'


def profile():
    return u'Wenn ist das'
