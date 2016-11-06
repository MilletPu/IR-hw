import textparser
import index
from bs4 import BeautifulSoup


def SPIMI(file):
    file_object = open(file)
    corpus = file_object.read().lower()