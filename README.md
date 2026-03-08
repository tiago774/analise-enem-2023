# Análise Exploratória dos Dados do ENEM 2023

Este projeto realiza uma análise exploratória dos microdados do ENEM 2023, focando no desempenho dos participantes por diferentes perspectivas como gênero, tipo de escola e localização geográfica.

## Pré-requisitos

### Dados Necessários
- Arquivo `MICRODADOS_ENEM_2023.csv` (disponível no portal do INEP)
- O arquivo deve estar no mesmo diretório do script

### Bibliotecas Python

pip install pandas numpy matplotlib seaborn

## Funcionalidades

O script realiza as seguintes análises:

1. **Carregamento Otimizado dos Dados**
   - Utiliza dtypes específicos para economia de memória
   - Carrega uma amostra de 100.000 linhas para análise rápida

2. **Pré-processamento**
   - Remove participantes sem notas
   - Calcula nota média por participante
   - Análise de valores missing

3. **Visualizações Geradas**
   - Distribuição das notas por área do conhecimento
   - Boxplots comparativos (gênero e tipo de escola)
   - Média de notas por estado
   - Matriz de correlação entre as notas

4. **Insights Estatísticos**
   - Estatísticas descritivas das notas
   - Comparações entre grupos demográficos
   - Análise de correlações

## Estrutura do Código

1. Importação das bibliotecas
2. Configuração do estilo dos gráficos
3. Carregamento dos dados
4. Limpeza e preparação
5. Geração das visualizações
6. Exibição dos insights

## Como Executar

1. **No Jupyter Notebook:**
   - Certifique-se de ter o arquivo CSV no diretório correto
   - Execute as células sequencialmente

2. **Como script Python:**
   - Remova a linha `%matplotlib inline`
   - Execute: `python analise_enem.py`

## Outputs Esperados

O script gera:
- Estatísticas descritivas das notas
- 5 gráficos de visualização:
  - Histogramas das distribuições
  - Boxplots comparativos
  - Gráfico de barras por estado
  - Heatmap de correlações
- Resumo com insights principais

## Observações

- O script carrega apenas 100.000 linhas por padrão (para performance)
- Para análise completa, altere `nrows=100000` para `nrows=None`
- Os dados do ENEM 2023 podem ser obtidos em: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem

## Principais Insights Esperados

- Disparidade educacional entre escolas públicas e privadas
- Diferenças regionais no desempenho
- Padrões de correlação entre as diferentes áreas do conhecimento
- Variações de desempenho por gênero

## Licença

Este projeto é para fins educacionais e de análise de dados. Os microdados do ENEM são de domínio público, disponibilizados pelo INEP.

## Notas Adicionais

- O comando `%matplotlib inline` é essencial apenas para visualização em Jupyter
- Em scripts Python tradicionais, os gráficos serão exibidos em janelas separadas automaticamente
- Para salvar os gráficos em arquivos, você pode adicionar `plt.savefig('nome_do_arquivo.png')` antes de cada `plt.show()`
