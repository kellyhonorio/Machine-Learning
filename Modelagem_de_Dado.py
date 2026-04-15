# FRAMEWORK

# Modelagem de dados
import pandas as pd  # Dados
import numpy as np   # Matrizes

# Analises graficas
import matplotlib.pyplot as plt
import seaborn as sns 
import plotly.express as px 

# Avisos
import warnings 
warnings.filterwarnings('ignore')

# Ajustes no pandas
pd.set_option('display.max_rows', 100)   # Linhas
pd.set_option('display.max_columns', 50) # Colunas

# Ajustes no matplot 
plt.rcParams['figure.figsize'] = (15,6) # Tamanho do Gráfico
# plt.style.use('darkgrid')        # Estilo do Gráfico



# LER OS DADOS  
Dados_Livros = pd.read_csv(r'C:\Users\Kelly\Documents\Machine Learning\Machine-Learning\dados\Books.csv')
Dados_Avaliacao = pd.read_csv(r'C:\Users\Kelly\Documents\Machine Learning\Machine-Learning\dados\Ratings.csv')
Dado_Usuario = pd.read_csv(r'C:\Users\Kelly\Documents\Machine Learning\Machine-Learning\dados\Users.csv')
# Dimensões dos dados
Dados_Livros.shape,
print(Dados_Livros.shape)
Dados_Avaliacao.shape, 
print(Dados_Avaliacao.shape)
Dado_Usuario.shape
print(Dado_Usuario.shape)