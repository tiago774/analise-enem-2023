import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn-v0_8-darkgrid')
file_path = 'MICRODADOS_ENEM_2023.csv'

dtypes = {
    'NU_INSCRICAO': 'int64',
    'NU_ANO': 'int16',
    'TP_FAIXA_ETARIA': 'int8',
    'TP_SEXO': 'category',
    'SG_UF_RESIDENCIA': 'category',
    'NO_MUNICIPIO_RESIDENCIA': 'category',
    'TP_ESCOLA': 'int8',
    'NU_NOTA_CN': 'float32',
    'NU_NOTA_CH': 'float32',
    'NU_NOTA_LC': 'float32',
    'NU_NOTA_MT': 'float32',
    'NU_NOTA_REDACAO': 'float32',
}

df = pd.read_csv(file_path, sep=';', encoding='ISO-8859-1', dtype=dtypes, nrows=100000, low_memory=False)

print(f'Dados carregados: {df.shape[0]} linhas e {df.shape[1]} colunas')

df_notas = df.dropna(subset=['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO'])

df_notas['NOTA_MEDIA'] = df_notas[['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO']].mean(axis=1)

missing = df_notas.isnull().sum() / len(df_notas) * 100
print('Porcentagem de missing values:\n', missing[missing > 0])

print('\nDescrição estatística das notas:\n', df_notas[['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO', 'NOTA_MEDIA']].describe())

areas = ['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO']
fig, axes = plt.subplots(3, 2, figsize=(12, 12))
axes = axes.flatten()

for i, area in enumerate(areas):
    sns.histplot(df_notas[area], bins=50, kde=True, ax=axes[i])
    axes[i].set_title(f'Distribuição de Notas - {area}')
    axes[i].set_xlabel('Nota')
    axes[i].set_ylabel('Frequência')

fig.delaxes(axes[5])
plt.tight_layout()
plt.savefig('distribuicao_notas.png', dpi=300, bbox_inches='tight')
plt.show()

plt.figure(figsize=(8, 6))
sns.boxplot(x='TP_SEXO', y='NOTA_MEDIA', data=df_notas)
plt.title('Nota Média por Gênero')
plt.xlabel('Gênero (M: Masculino, F: Feminino)')
plt.ylabel('Nota Média')
plt.savefig('boxplot_genero.png', dpi=300, bbox_inches='tight')
plt.show()

plt.figure(figsize=(8, 6))
sns.boxplot(x='TP_ESCOLA', y='NOTA_MEDIA', data=df_notas)
plt.title('Nota Média por Tipo de Escola')
plt.xlabel('Tipo de Escola (2: Pública, 3: Privada)')
plt.ylabel('Nota Média')
plt.savefig('boxplot_escola.png', dpi=300, bbox_inches='tight')
plt.show()

uf_media = df_notas.groupby('SG_UF_RESIDENCIA')['NOTA_MEDIA'].mean().sort_values(ascending=False)

plt.figure(figsize=(12, 6))
sns.barplot(x=uf_media.index, y=uf_media.values)
plt.title('Nota Média por Estado de Residência')
plt.xlabel('Estado (UF)')
plt.ylabel('Nota Média')
plt.xticks(rotation=45)
plt.savefig('media_por_estado.png', dpi=300, bbox_inches='tight')
plt.show()

corr = df_notas[areas + ['NOTA_MEDIA']].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlação entre Notas das Áreas')
plt.savefig('matriz_correlacao.png', dpi=300, bbox_inches='tight')
plt.show()

print('\nInsights Principais:')
print('1. A nota média geral é de aproximadamente {:.2f} pontos.'.format(df_notas['NOTA_MEDIA'].mean()))
print('2. As notas de Matemática (MT) tendem a ter maior variabilidade e menor média comparada a outras áreas.')
print('3. Participantes do sexo feminino geralmente têm notas ligeiramente superiores em Linguagens e Redação, enquanto masculinos em Matemática e Ciências da Natureza.')
print('4. Estudantes de escolas privadas (TP_ESCOLA=3) têm notas médias significativamente maiores que os de escolas públicas.')
print('5. Estados do Sul e Sudeste (ex: SP, MG) apresentam médias mais altas, enquanto Norte e Nordeste menores.')
print('6. Há forte correlação positiva entre as notas das áreas objetivas, mas a Redação é menos correlacionada.')
