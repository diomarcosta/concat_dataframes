'''
1. Import the libraries that will be used
'''
import pandas as pd
import numpy as np

'''
Read or create a dataframe. In this case, i'm creating. If read, the data and columns will be imported of readed dataframe

2. Create the data of first dataframe with array of numpy
2.1 the data can be variables and/or fixed. If variables, declare before
The array need to have the same columns quantity of the second one
'''

value_2 = 'value_col2x'
data_of_df1 = np.array(['value_col1x', value_2, 'value_col3x', '', ''])

'''
3. Create the first dataframe with the first data and the second dataframe columns
3.1 That columns will serv as headers for the second dataframe concat with the first
3.2 At first, the columns will not be related to the data, as they belong to the second dataframe
3.3 Remember, the data_of_df1 need to have the same quantity of columns of the second dataframe

Ex.: If the second dataframe has 5 columns, you must add blank values for pandas to concatenate, so
  df1_data = np.array(['value_'1, value_2, 'value_3', '',''])
  df1 = pd.DataFrame(data=[data_do_df1], columns=['col_1', 'col_2', 'col_3', 'col_4', 'col_5])
  
IMPORTANT = Be aware of the number of columns that the second dataframe has, to create in the first and concat works
This methodology works both for dataframes with columns with different names and for dataframes with different numbers of columns.
'''
df1 = pd.DataFrame(data=[data_of_df1], columns=['col_1y', 'col_2y', 'col_3y', 'col_4y', 'col_5y'])

#4. Create a line to serve as a header for the first dataframe

df1.loc[-1] = ['col_1x', 'col_2x', 'col_3x', '', '']
#5. Re-arrange the rows by index
df1.index = df1.index + 1  # Shifting index
df1 = df1.sort_index()

#6. Create 2 blanks rows (if you wish, to separate the two dataframes) and the header for the second dataframe 
df1.loc[len(df1)] = ['', '', '', '', '']
df1.loc[len(df1)] = ['', '', '', '', '']
df1.loc[len(df1)] = ['col_1y', 'col_2y', 'col_3y', 'col_4y', 'col_5y']

#7. Create or import the second dataframe, in this case I'll be creating
# Remember, the columns of df2 is equals of df1 columns and the first row of df1 is its columns.
data_of_df2 = np.array(['value_col_y1', 'value_col_2y', 'value_col_3y', 'value_col_4y', 'value_col_5y'])
df2 = pd.DataFrame(data=[data_of_df2], columns=['col_1y', 'col_2y', 'col_3y', 'col_4y', 'col_5y'])

#8. Concat both Dataframes
#You can create another one or just replace with a existing Dataframe
df1 = pd.concat ([df1,df2])

#9. After concat, just export to excel taking of all of the index and the headers. Put the .xlsx extension in the end of name
df1.to_excel('Concatenado.xlsx', index=False, header=None)
