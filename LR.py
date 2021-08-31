
import os
import pandas as pd
import dask.dataframe as dd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.processing import MinMaxScaler
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm
from datetime import datetime, timedelta
from scipy.stats import norm
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import StratifiedKFold
import statsmodels.formula.api as sf


def vif_cal(input_data, dependent_col):
  x_vars = input_data.drop([dependent_col], axis=1)
  xvars_names = x_vars.columns
  
  for i in range(0, xvar_names.shape[0]):
    y = x_vars[xvar_names[i]]
    x = x_vars[xvar_names.drop(xvar_names[i])]
    rsq = sf.ols(formula="y~x", data=x_var).fit().rsquared
    vif=round(1/(1-rsq), 2)
    print(xvar_names[i], " VIF = ", vif)
































