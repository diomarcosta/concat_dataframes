'''
1. Importe as biblioteca que serão usadas
'''
import pandas as pd
import numpy as np

'''
Leia ou crie um Dataframe. Neste caso estou criando. Se ler, os dados e as colunas serão importadas do Dataframe lido.

2. Crie os dados do primeiro Datafame com array do numpy
2.1 Os dados podem ser variáveis ou fixos. Se forem variáveis, declare antes.
O array precisa ter a mesma quantidade de colunas do segundo
'''

value_2 = 'value_col2x'
data_of_df1 = np.array(['value_col1x', value_2, 'value_col3x', '', ''])

'''
3. Crie o primeiro dataframe com os primeiros dados (percecente a ele) e com as colunas do segundo
3.1 Essas colunas servirão como cabeçalhos para o segundo dataframe concatenado com o primeiro
3.2 A princípio, as colunas não serão relacionadas aos dados, pois pertencem ao segundo dataframe
3.3 Lembre-se, o data_of_df1 precisa ter a mesma quantidade de colunas do segundo dataframe

Ex.: Se o segundo dataframe tiver 5 colunas, você deve adicionar valores em branco para que o pandas concatene, então
   data_of_df1 = np.array(['valor_'1, valor_2, 'valor_3', '',''])
   df1 = pd.DataFrame(data=[data_of_df1], columns=['col_1', 'col_2', 'col_3', 'col_4', 'col_5])
  
IMPORTANTE = Fique atendo no número de colunas que o segundo Dataframe tem para criar no primeiro e o concat funcionar.
Essa metodologia funciona para Dataframes com colunas de nomes e tamanhos diferentes
'''
df1 = pd.DataFrame(data=[data_of_df1], columns=['col_1y', 'col_2y', 'col_3y', 'col_4y', 'col_5y'])

#4. Crie uma linha para servir de cabeçalho para o primeiro dataframe
df1.loc[-1] = ['col_1x', 'col_2x', 'col_3x', '', '']
#5. Re-ordene os index
df1.index = df1.index + 1  # Subindo o index
df1 = df1.sort_index()

#6. Crie 2 linhas em branco (se você quiser, para separar os dois dataframes) e o cabeçalho para o segundo Dataframe.
df1.loc[len(df1)] = ['', '', '', '', '']
df1.loc[len(df1)] = ['', '', '', '', '']
df1.loc[len(df1)] = ['col_1y', 'col_2y', 'col_3y', 'col_4y', 'col_5y']

#7. Crie ou importe o segundo dataframe, neste caso estarei criando
#Lembre-se, as colunas de df2 são iguais às colunas df1 e a primeira linha de df1 são suas colunas.
data_of_df2 = np.array(['value_col_y1', 'value_col_2y', 'value_col_3y', 'value_col_4y', 'value_col_5y'])
df2 = pd.DataFrame(data=[data_of_df2], columns=['col_1y', 'col_2y', 'col_3y', 'col_4y', 'col_5y'])

#8. Concatene os dois Dataframes
#Você pode criar outro ou apenas substituir por um Datafram existente
df1 = pd.concat ([df1,df2])

#9. Após concatenar, basta exportar para o excel tirando todos os índices e os cabeçalhos. Coloque a extensão .xlsx no final do nome
df1.to_excel('Concatenado.xlsx', index=False, header=None)
