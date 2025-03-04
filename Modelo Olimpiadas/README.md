### README.md

# Projeto de Previsão de Medalhas Olímpicas

## 1. Descrição do Projeto

Este projeto visa desenvolver um modelo preditivo para estimar o número de medalhas que um país pode ganhar nas próximas Olimpíadas. Utilizando dados históricos de desempenho olímpico, indicadores socioeconômicos como Produto Interno Bruto (PIB), Índice de Desenvolvimento Humano (HDI), e população, o projeto analisa como esses fatores influenciam o sucesso olímpico de um país.

## 2. Objetivos do Projeto

- **Objetivo Principal**: Criar um modelo de aprendizado de máquina para prever o número de medalhas que cada país pode ganhar nas próximas Olimpíadas.
  
- **Subobjetivos**:
  1. Explorar a relação entre variáveis socioeconômicas e o desempenho olímpico.
  2. Comparar diferentes algoritmos de aprendizado de máquina para identificar o mais eficaz.
  3. Oferecer insights sobre como fatores socioeconômicos influenciam o sucesso olímpico.

## 3. Estrutura do Projeto

O projeto é organizado nos seguintes scripts:

- **`data_loading.py`**: Carrega os dados dos arquivos CSV para dataframes do pandas.
- **`data_preprocessing.py`**: Realiza o pré-processamento dos dados, incluindo remoção de valores ausentes, normalização e combinação dos conjuntos de dados.
- **`model_training.py`**: Treina o modelo Random Forest com os dados de treino.
- **`model_evaluation.py`**: Avalia o desempenho do modelo utilizando métricas como MAE, MSE, RMSE e R².
- **`visualizations.py`**: Cria visualizações, como gráficos de importância das variáveis.
- **`main.py`**: Script principal que orquestra todos os outros scripts e executa o fluxo completo do projeto.

## 4. Dependências

As seguintes bibliotecas Python são necessárias para executar este projeto:

- `pandas`
- `numpy`
- `scikit-learn`
- `matplotlib`

Para instalar todas as dependências, execute:

```bash
pip install -r requirements.txt
```

## 5. Como Executar

1. **Clone o Repositório**:

```bash
git clone https://github.com/seu_usuario/projeto-previsao-medalhas.git
cd projeto-previsao-medalhas
```

2. **Execute o Script Principal**:

Certifique-se de que todos os arquivos de dados necessários estão no diretório correto e execute o script principal:

```bash
python main.py
```

## 6. Dados

Os dados utilizados no projeto são provenientes das seguintes fontes:

1. **GDP by Country 1999-2022.csv**: Dados históricos do PIB por país de 1999 a 2022.
2. **Human Development Index - Full.csv**: Dados sobre o HDI e outros indicadores de desenvolvimento humano.
3. **olympics_medals_country_wise.csv**: Número de medalhas ganhas por cada país nas Olimpíadas.
4. **population_by_country_2020.csv**: Dados de população por país para o ano de 2020.

## 7. Resultados e Discussão

Os modelos foram treinados usando diferentes algoritmos de aprendizado de máquina. O **Random Forest** apresentou o melhor desempenho com as seguintes métricas:

- **MAE**: 2.12
- **MSE**: 21.60
- **RMSE**: 4.65
- **R²**: 0.94
- **R² Médio (Validação Cruzada)**: 0.91

Esses resultados sugerem que o Random Forest é um método eficaz para prever o número de medalhas que um país pode ganhar nas Olimpíadas, capturando bem as interações complexas entre as variáveis.

## 8. Conclusão

O projeto atingiu seu objetivo principal de desenvolver um modelo preditivo eficaz para prever o número de medalhas olímpicas. O modelo de Random Forest foi selecionado como o melhor devido ao seu alto desempenho em termos de precisão e robustez. A análise também revelou que fatores como PIB, HDI e população influenciam significativamente o desempenho olímpico.

## 9. Contribuição

Sinta-se à vontade para contribuir com melhorias para este projeto. Para isso:

1. Faça um fork do repositório.
2. Crie um novo branch (`git checkout -b feature/nova-feature`).
3. Faça o commit das suas mudanças (`git commit -am 'Adiciona nova feature'`).
4. Faça o push para o branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

## 10. Licença

Este projeto é licenciado sob a [MIT License](LICENSE).

---w