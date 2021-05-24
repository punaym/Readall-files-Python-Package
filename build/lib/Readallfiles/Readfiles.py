def Readall():
      import easygui
      import pandas as pd
      import re
      data=easygui.fileopenbox()
      
      if re.search(".csv",data):
          dt=pd.read_csv(data)
          return(dt)
      elif re.search(".xlsx",data):
          dt=pd.read_excel(data)
          return(dt)
      elif re.search(".sas7bpgm",data):
          dt=pd.read_sas(data)
          return(dt)
      elif re.search(".mdf",data):
          dt=pd.read_sql_table(data)
          return(dt)
      elif re.search(".txt",data):
          dt=open(data, "r")
          return(dt)
         
  
