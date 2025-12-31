# Comparação de Algoritmos de Ordenação

Este projeto foi desenvolvido durante a graduação em Sistemas de Informação na Universidade Federal de Viçosa (UFV). O objetivo é comparar o desempenho de diferentes algoritmos de ordenação implementados em Python e C++.

## Autor
[Matheus Breguêz Rocha Vieira](https://eu.mat.br)
Igor Alves

## Estrutura do Projeto

```
.
├── LICENSE
├── a.out
├── algorithms
│   ├── __init__.py
│   ├── heapsort.py
│   ├── insertionsort.py
│   ├── mergesort.py
│   ├── quicksort.py
│   ├── selectionsort.py
│   └── shellsort.py
├── install.sh
├── main.cpp
├── main.py
├── main.sh
└── results
```

## Pré-requisitos e Instalação

Para executar o projeto, você precisará de:
- Python 3
- Compilador C++ (GCC/G++)
- Hyperfine (para benchmarking)
- NumPy

Você pode instalar as dependências utilizando o script `install.sh`:

```bash
./install.sh
```

## Como Usar

### Python (CLI)

O script `main.py` permite executar algoritmos de ordenação via linha de comando.

**Uso:**
```bash
python3 main.py -alg <algoritmo> -is <tamanho_instancia> -o <ordem>
```

**Argumentos:**
- `-alg`, `--algorithm`: Escolha entre `all`, `selection`, `insertion`, `shell`, `merge`, `heap`, `quick`.
- `-is`, `--instancesize`: Tamanho da instância (ex: 10, 1000, 100000, 1000000).
- `-o`, `--order`: Ordem dos dados de entrada (`ASC` para ascendente, `DESC` para descendente, `RAND` para aleatório).

**Exemplo:**
```bash
python3 main.py -alg quick -is 1000 -o RAND
```

### C++ (Interativo)

O arquivo `main.cpp` oferece uma interface interativa via terminal para executar e medir o tempo dos algoritmos.

**Compilação e Execução:**
```bash
g++ main.cpp -o sorting_app
./sorting_app
```
(Ou use `./a.out` se já estiver compilado)

O programa apresentará um menu para escolher o tipo de geração de dados (Aleatório, Crescente, Decrescente) e, em seguida, o algoritmo de ordenação desejado.

### Benchmarking

O script `main.sh` automatiza a execução de benchmarks utilizando a ferramenta `hyperfine`. Ele executa diversos cenários de teste e salva os resultados em formato JSON na pasta `results/`.

**Execução:**
```bash
./main.sh
```
