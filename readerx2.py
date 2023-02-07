import pandas as pd

df = pd.read_excel(r'employee.xls')                                     # convert excel file to Panda Dataframe
df['totalexpense'] = df['expense1'] + df['expense2'] + df['expense3']   # sum only expense# columns to get total into new dataframe column

df.to_csv(r'employee.csv', sep='\t')                                    # use to_csv method to convert dataframe to CSV file with tab delimiter