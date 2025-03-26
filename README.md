# Cifra de Hill

## Autor
Vinicius Lemos de Carvalho

## Disciplina
Elementos de Criptografia e Segurança

## Atividade
Cifra de Hill

## Descrição
Este projeto implementa a Cifra de Hill, um método de criptografia polialfabética baseado em álgebra linear. A cifra utiliza uma matriz-chave para transformar blocos de texto em números, aplicando operações matriciais modulares para cifrar e decifrar mensagens.

## Tecnologias Utilizadas
- Python 3
- Bibliotecas: `numpy`, `sympy`, `argparse`

## Como Executar
O programa opera via linha de comando e permite cifrar e decifrar arquivos de texto.

### Instalação de Dependências
Certifique-se de ter o Python 3 instalado e execute o seguinte comando para instalar as dependências necessárias:

```sh
pip install numpy sympy
```

### Comandos

#### Cifração
Para cifrar um arquivo de texto:
```sh
python cifradehill.py -enc textoclaro.txt -out textocifrado.txt
```

#### Decifração
Para decifrar um arquivo de texto cifrado:
```sh
python cifradehill.py -dec textocifrado.txt -out textoclaro.txt
```

### Exemplo de Uso
Dado um arquivo `mensagem.txt` contendo:
```
CRIPTOGRAFIA
```
Executando:
```sh
python cifradehill.py -enc mensagem.txt -out mensagem_cifrada.txt
```
O arquivo `mensagem_cifrada.txt` conterá o texto cifrado.

Para reverter a cifração:
```sh
python cifradehill.py -dec mensagem_cifrada.txt -out mensagem_decifrada.txt
```
E o arquivo `mensagem_decifrada.txt` conterá o texto original (ou com pequenos ajustes devido ao padding).

## Observações
- A matriz-chave utilizada deve ser invertível no módulo 26 para que a decifração funcione corretamente.
- O código automaticamente ajusta o texto de entrada para estar em maiúsculas e remove espaços.
- Se o tamanho do texto não for múltiplo do tamanho da matriz, caracteres de preenchimento (`X`) são adicionados.

## Licença
Este projeto é de uso acadêmico e educacional. Sinta-se livre para modificá-lo e aprimorá-lo!
