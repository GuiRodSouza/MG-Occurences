import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

bh = violent_crimes[violent_crimes.city == 'BELO HORIZONTE']
bh = bh[['registers', 'year']].groupby(['year']).sum(numeric_only=True).reset_index()
sns.barplot(data=bh, x='year', y='registers')
plt.title('Violent Crimes x Year in the Capital of MG')
plt.ylabel('Registers')
plt.xlabel('Year')
plt.show()