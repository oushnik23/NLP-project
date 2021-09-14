# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 14:14:45 2021

@author: Administrator
"""

import os
os.getcwd()
os.chdir("C:/Users/Administrator/Desktop/PYTHON")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import re
import nltk
import nltk.corpus
print(os.listdir(nltk.data.find("corpora")))

nltk.download('brown')
nltk.download('shakespeare')
nltk.download('gutenberg')
nltk.download('punkt')

from nltk.corpus import brown,shakespeare
brown.words()

nltk.corpus.gutenberg.fileids()

hamlet=nltk.corpus.gutenberg.words('shakespeare-macbeth.txt')
type(hamlet)
for word in hamlet[:500]:
    print(word, sep=' ', end=' ')

from nltk.tokenize import word_tokenize
hamlet_token=word_tokenize(hamlet)
