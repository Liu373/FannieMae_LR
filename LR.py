
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
        
        
        print('\n')
        print('{0} is done'.format(f))
        
        
      else:
        print('\n')
        print('{0} still has Null after Data Cleaning'.format(f))
        
        
        
        
        
def LR_Training(Path, Train_File_Name):
  
  File_Path = Path + '\\' + Train_File_Name
  
  Input_File = pd.read_csv(File_Path, low_memory=False)
  Input_File = Input_File.droop('Unnamed: 0', 1)
  
  Input_File_1 = Input_File[Input_File['CSCORE_B'] > 499]
  Input_File_1['OLTV'] = Input_File_1['OLTV'].replace(0, Input_File_1['OLTV'].mean())
  Input_File_1['NUM_BO'] = Input_File_1['NUM_BO'].replace(0, Input_File_1['NUM_BO'].mean())
  Input_File_1['NUM_BO_Min'] = Input_File_1['NUM_BO'].map(lambda x: x if x>0.99999 else 1)
  Input_File_1['DTI'] = Input_File_1['DTI'].replace(0, Input_File_1['DTI'].mean())
  
  X = np.asarray(Input_File_1[["OLTV", "NUM_BO_Min", "CSCORE_B", "CHANNEL_B", "CHANNEL_C", "CHANNEL_R", "OCC_STAT_I", "OCC_STAT_P", "OCC_STAT_S"]])
  
  Y = np.asarray(Input_File_1['Default_5_FM'])
  
  scaler = MinMaxScaler()
  X_normal = scaler.fit_transform(X)
  
  LR = LogisticRegression(C=0.1, solver='liblinear', penalty='l2').fit(X_normal, Y)
  
  print('Intercept is ', LR.intercept_)
  print('Coefficients are ', LR.coef_)
  
  return LR, X_normal, Y



def LR_Testing(Path, Test_File_Name, LR):
  
  # OrigD        = [0.003,    0.006,    0.009,   0.012,    0.015,  0.018,   ......]
  # RecessionD   = [0.009099, 0.032466, 0.05148, 0.067732, 0.0837, 0.09655, ......]
  
  # D_interp = scipy.interpolate.interpld(OrigD, RecessionD)
  
  Period = Test_File_Name[:13][7:]
  File_Path = Path + '\\' + Test_File_Name
  
  Input_File = pd.read_csv(File_Path, low_memory=False)
  
  Input_File['Orig_Date_Str'] = Input_File['ORIG_DATE'].astype(str)
  Input_File['Orig_Date'] = Input_File['Orig_Date_Str'].map(lambda x: datetime(year=int(float(x[-6:])), month=int(x[:2]), day=1) if len(x)==8 else
                                                           (datetime(year=int(float(x[-6:])), month=int(x[:1]), day=1) if len(x)==7 else 0))
  
  
  Input_File['FiveYear_Date'] = Input_File['Orig_Date'] + timedelta(days=1825)
                                                            
  Input_File['Foreclosure_Str'] = Input_File['FORECLOSURE_DATE'].astype(str)
  Input_File['Foreclosure_Date'] = Input_File['Foreclosure_Str'].map(lambda x: datetime(year=int(float(x[-6:])), month=int(x[:2]), day=1) if len(x)==8 else
                                                                    (datetime(year=int(float(x[-6:])), month=int(x[:1]), day=1) if len(x)==7 else
                                                                    datetime(year=1995, month=1, day=1)))
  
  Input_File['Default_5'] = np.where((Input_File['FORECLOSURE_DATE']!=0) & (Input_File['Foreclosure_Date']<Input_File['FiveYear_Date']), 1, 0)
  
  Input_File['Default_5_FM'] = np.where((Input_File['Default_5']==1) & ((Input_File['Zero_Bal_Code']==9) | (Input_File['Zero_Bal_Code']==3)), 1, 0)
  
  Input_File = Input_File.drop('Orig_Date_Str', 1)
  Input_File = Input_File.drop('Foreclosure_Str', 1)
  
  Input_File = Input_File[Input_File['CSCORE_B']>0.999999]
  Input_File = Input_File[Input_File['OLTV']>0.9999999]
  Input_File = Input_File[Input_File['NUM_BO']>0.999999]
  Input_File = Input_File[Input_File['DTI']>0.999999]
  
  X = np.asarray(Input_File[["OLTV", "NUM_BO_Min", "CSCORE_B", "CHANNEL_B", "CHANNEL_C", "CHANNEL_R", "OCC_STAT_I", "OCC_STAT_P", "OCC_STAT_S"]])
  
  Old_LoanID = Input_File['LOAN_ID'].tolist()
  
  scaler = MinMaxScaler()
  X_normal = scaler.fit_transform(X)
  Yhat = LR.predict(X_normal)
  Yhat_Prob = LR.predict_proba(X_normal)[:, 1]
  
  Yhat_Prob_Df = pd.DataFrame(Yhat_Prob, index=Old_LoanID, columns=['Yhat_Prob'])
  Yhat_Prob_Df.index.names = ['LOAN_ID']
  
  Yhat_Df = pd.DataFrame(Yhat, index=Old_LoanID, columns=['Yhat'])
  Yhat_Df.index.names = ['LOAN_ID']
  
  Input_File.set_index('LOAN_ID', inplace=True)
  
  Input_File = Input_File.merge(Yhat_Prob_Df['Yhat_Prob'], on='LOAN_ID')
  Input_File = Input_File.merge(Yhat_Df['Yhat'], on='LOAN_ID')
  
  Input_File['Annualized_Yhat_Prob'] = Input_File['Yhat_Prob'].map(lambda x: 1-((1-x)**(1/5)))
  Input_File['Annualized_Stressed_PD'] = norm.cdf((norm.ppf(Input_File['Annualized_Yhat_Prob']) + np.sqrt(0.15) * norm.ppf(0.999))/np.sqrt(1-0.15))
  Input_File['Stressed_PD'] = Input_File['Annualized_Stressed_PD'].map(lambda x: ((1+x)**5) -1 )
  
  pd_bins = np.linspace(0, 0.06, num=21)
  
  group_pd_7 = (Input_File[['Yhat_Prob', 'Default_5_FM']].groupby([pd.cut(Input_File['Yhat_Prob'], pd_bins)]). agg({'Yhat_Prob': ['count', 'mean'],
                                                                                                                    'Default_5_FM': 'sum'}))
  
  
  group_pd_8 = (Input_File[['Stressed_PD', 'Default_5_FM']].groupby([pd.cut(Input_File['Yhat_Prob'], pd_bins)]). agg({'Stressed_PD': ['count', 'mean'],
                                                                                                                      'Default_5_FM': 'sum'}))
  
  
  
  
  
  
  
  
  
  






























