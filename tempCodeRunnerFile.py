import pandas as pd

violent_crimes_12_17 = pd.read_csv('C:/Users/xshee/OneDrive/Área de Trabalho/MyStuff/Projects/MG Data Analysis/CSV Files/Banco Crimes Violentos - Atualizado 2012 a 2017.csv',
                                       sep=';',
                                       encoding='latin1')

violent_crimes_18_23 = pd.read_csv('C:/Users/xshee/OneDrive/Área de Trabalho/MyStuff/Projects/MG Data Analysis/CSV Files/Banco Crimes Violentos - Atualizado Abril 2023.csv',
                                       sep=';',
                                       encoding='latin1')

violent_crimes_12_17 = violent_crimes_12_17.rename(columns={'Mês ': 'Mês'})
violent_crimes = pd.concat([violent_crimes_12_17, violent_crimes_18_23])

violent_crimes = violent_crimes.rename(columns={'Registros': 'registers',
                                                                    'Natureza': 'type',
                                                                    'Município': 'city',
                                                                    'Cod IBGE': 'ibge_code',
                                                                    'Mês': 'month',
                                                                    'Ano': 'year'})
print(violent_crimes.index)
print(violent_crimes_12_17.index)
print(violent_crimes_18_23.index)
print(violent_crimes.iloc[0])