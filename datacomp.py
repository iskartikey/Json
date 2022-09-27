import pandas as pd
import openpyxl
pd.set_option('display.float_format', lambda x: '%.5f' % x)
df1= pd.read_excel("budget nonprod.xlsx")
df2=pd.read_excel("budget prod.xlsx")
combine= df2.merge(df1,left_index=True, right_index=True)
combine['Cumulative Gross Sales_y']=[(float(str(i).replace("-","0")))for i in combine['Cumulative Gross Sales_y']]
combine['Cumulative Gross Sales_x']=[(float(str(i).replace("-","0")))for i in combine['Cumulative Gross Sales_x']]

combine['diff']=combine['Cumulative Gross Sales_y']- combine['Cumulative Gross Sales_x']
combine['percentage']=combine['Cumulative Gross Sales_y']- combine['Cumulative Gross Sales_x']/combine['Cumulative Gross Sales_y']
print("combinedf=",combine)
combine.to_excel("op.xlsx",sheet_name="mainsheet")


