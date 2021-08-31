
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
    
    



def Data_Extraction(Path, Input_Scope, Column_Name):
  
  for f in os.listdir(Path):
    
    if f in Input_Scope:
      
      Input_File   = Path + '\\' + f
      Output_File  = Path + '\\Output\\Output_' + f
      Year = float(f[:4])
      
      df_dd = dd.read_csv(Input_File, sep='/', header=None, names=Column_Name, assume_missing=True, dtype='object')
      df_dd_scope = df_dd[["ORIG_DATE", "LOAN_ID", "LOAN_AGE", "DTI", "STATE", "CURRENT_UPB", "CHANNEL", "OLTV"]]
      
      data_Scope = df_dd_scope.compyte()
      
      OrigDate_Null = data_Scope["ORIG_DATE"].isnull().sum()
      OrigDate_Null_Per = OrigDate_Null / len(data_Scope.index)
      
      DTI_Null = data_Scope["DTI"].isnull().sum()
      DTI_Null_Per = DTI_Null / len(data_Scope.index)
      
      x
      x
      x
      x
      x
      
      if LoanID_Null == 0 and OrigDate_Null == 0 and LoanAge_Null == 0 xxxxxxx:
        
        data_Scope_Not_NA["LOAN_ID"]    = data_Scope_Not_NA["LOAN_ID"].astype(float)
        data_Scope_Not_NA["CHANNEL"]    = data_Scope_Not_NA["CHANNEL"].astype(str)
        x
        x
        x
        x
        x
        # define each column's data type
        
        
        data_Scope_Not_NA_Gp = data_Scope_Not_NA.groupby('LOAN_ID').agg({'ORIG_DATE':         'first',
                                                                         'LOAN_AGE':          'last',
                                                                         'DTI':               'mean'
                                                                         'FORECLOSURE_DATE':  'sum'
                                                                         'Zero_Bal_Code':     'sum'})
        
        data_Scope_Not_NA_Gp['CHANNEL_R'] = data_Scope_Not_NA_Gp['CHANNEL'].map(lambda x: 1 if "R" in x else 0)
        data_Scope_Not_NA_Gp['CHANNEL_B'] = data_Scope_Not_NA_Gp['CHANNEL'].map(lambda x: 1 if "B" in x else 0)
        data_Scope_Not_NA_Gp['CHANNEL_C'] = data_Scope_Not_NA_Gp['CHANNEL'].map(lambda x: 1 if "C" in x else 0)
        
        
        data_Scope_Not_NA_Gp['Orig_Month_Str'] = data_Scope_Not_NA_Gp['Orig_Date_Str'].map(lambda x: x[:2] if len(x) == 8 else x[:1])
        
        data_Scope_Not_NA_Gp['Default'] = data_Scope_Not_NA_Gp['Default_Year_Num'].map(lambda x: 1 if 0<x<Year+5 else 0)

        
        data_Scope_Not_NA_Gp.to_csv(Output_File)






























