import datetime
import warnings
import numpy as np 
import pandas as pd 
import altair as alt
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import statsmodels.api as sm
from pandas_profiling import ProfileReport
from IPython.core.display import display, HTML
from google.colab import auth 


warnings.simplefilter(action='ignore', category=FutureWarning)
sns.set(rc={'figure.figsize':(12, 6)})


def auth():
    auth.authenticate_user()
