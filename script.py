import pandas as pd

violent_crimes_2012_2017 = pd.read_csv('C:/Users/xshee/OneDrive/Área de Trabalho/MyStuff/Projects/MG Data Analysis/CSV Files/Banco Crimes Violentos - Atualizado 2012 a 2017.csv',
                                       sep=';',
                                       encoding='latin1')

violent_crimes_2018_2023 = pd.read_csv('C:/Users/xshee/OneDrive/Área de Trabalho/MyStuff/Projects/MG Data Analysis/CSV Files/Banco Crimes Violentos - Atualizado Abril 2023.csv',
                                       sep=';',
                                       encoding='latin1')

violent_crimes = violent_crimes_2012_2017 + violent_crimes_2018_2023


violent_crimes = violent_crimes.rename(columns={'Registros': 'registers',
                                                                    'Natureza': 'type',
                                                                    'Município': 'city',
                                                                    'Cod IBGE': 'ibge_code',
                                                                    'Mês': 'month',
                                                                    'Ano': 'year'})
print(violent_crimes.columns)