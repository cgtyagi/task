#Setup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing
import shlex 
sns.set()
sns.set_context("paper", font_scale=10)

#Data Cleaning
data = pd.read_csv('SampleTaskData[42][77][59].csv')
data.head()



