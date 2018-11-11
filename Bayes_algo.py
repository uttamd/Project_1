import  numpy as np
import  pandas as pd
from  urllib3.request import *
import sklearn
from sklearn.naive_bayes import  BernoulliNB
from sklearn.naive_bayes import GaussianNB
from  sklearn.naive_bayes import  MultinomialNB
from sklearn import metrics
from sklearn.metrics import  accuracy_score


url = "https://archive.ics.uci.edu/m1/machine-learning-databases/spambase/spambase.data"

data =