# -*- encoding: utf8 -*-
from collections import OrderedDict

import textparser
import index
from bs4 import BeautifulSoup
import collections
import configparser

output = open('data.txt')
index = output.read().lower()
output.close()

collections.OrderedDict(index)