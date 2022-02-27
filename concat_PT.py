'''
PT version
1.
1.1 Importe as bibliotecas que serão usadas
'''
import pandas as pd
import numpy as np

'''
LEIA OU CRIE UM DATAFRAME. NESTE CASO ESTOU CRIANDO. SE CASO FOR LER, OS DADOS E AS COLUNAS SERÃO IMPORTADAS DO DATAFRAME LIDO.

2. Crie os dados do dataframe como array do numpy
2.1 Os dados podem ser variáveis e/ou strings
2.2 Se os dados forem variáveis, declarar antes
2.3 O array teve ter o mesmo tamanho da quantidade de colunas do segundo dataframe
'''
valor_2 = 'valor_col2x'
dados_do_df1 = np.array(['valor_col1x', valor_2, 'valor_col3x', '', ''])

'''
3. Crie o primeiro dataframe com o dados do df1 e as colunas do segundo dataframe
3.1 Estas colunas servirão de headers para que o segundo dataframe se encaixe
3.2 Num primeiro momento, as colunas não terão relação com os dados, pois elas pertecem ao segundo dataframe
3.3 Lembrando que os dados_do_dataframe devem ter a mesma quantidade de colunas que o segundo dataframe
Ex.: Se o segundo dataframe tiver 5 colunas, deve-se acrescentar valores em branco para que o pandas concatene, sendo assim
dados_do_df1 = np.array(['valor_'1, valor_2, 'valor_3', '',''])
df1 = pd.DataFrame(data=[dados_do_df1], columns=['col_1', 'col_2', 'col_3', 'col_4', 'col_5])
IMPORTANTE = Ficar atento a quantidade de colunas que o segundo dataframe tem para criar no primeiro e o concat funcionar
Essa metodologia serve tanto para dataframes com colunas de nomes diferentes quanto para dataframes com quantidade de colunas diferentes
'''
df1 = pd.DataFrame(data=[dados_do_df1], columns=['col_1y', 'col_2y', 'col_3y', 'col_4y', 'col_5y'])

#4. Crie uma linha para servir de cabeçalho para o primeiro dataframe

df1.loc[-1] = ['col_1x', 'col_2x', 'col_3x', '', '']
#8. Re-organize as linhas pelo index
df1.index = df1.index + 1  # shifting index
df1 = df1.sort_index()

# criando 2 linhas em branco (se desejar) e o cabeçalho do 2º dataframe 
df1.loc[len(df1)] = ['', '', '', '', '']
df1.loc[len(df1)] = ['', '', '', '', '']
df1.loc[len(df1)] = ['col_1y', 'col_2y', 'col_3y', 'col_4y', 'col_5y']

#crie ou importe o segundo dataframe, neste caso estarei criando
#lembre que as colunas do df2 são iguais as colunas do df1. A primeira linha do df1 são as colunas dele
dados_do_df2 = np.array(['valor_col_y1', 'valor_col_2y', 'valor_col_3y', 'valor_col_4y', 'valor_col_5y'])
df2 = pd.DataFrame(data=[dados_do_df2], columns=['col_1y', 'col_2y', 'col_3y', 'col_4y', 'col_5y'])

#concatene os dois dataframes
#pode-se criar um novo ou simplesmente substituir um existente
df1 = pd.concat ([df1,df2])

#Visto que os dois dataframes já foram concatenados, basta apenas exportar para o excel tirando os index e os headers. Colocar a extensão .xlsx no final do nome do arquivo
df1.to_excel('Concatenado.xlsx', index=False, header=None)
