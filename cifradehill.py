import numpy as np
import sys
import argparse
import string
from sympy import Matrix

# Configurações
ALPHABET = string.ascii_uppercase  # Alfabeto usado para codificação
N = 3  # Tamanho do bloco da matriz de codificação
MODULO = len(ALPHABET)  # Modulo para operações na cifra

# Matriz fixa para garantir mesma chave na cifração e decifração
KEY_MATRIX = np.array([[19, 17, 14], [12, 25, 23], [23, 18, 12]])
print("Matriz Chave Utilizada:\n", KEY_MATRIX)

# Função para verificar se a matriz tem inversa modular válida
def is_invertible(matrix, mod):
    det = int(round(np.linalg.det(matrix)))  # Determinante da matriz
    det_mod = det % mod
    try:
        Matrix(matrix).inv_mod(mod)
        return True
    except:
        return False

if not is_invertible(KEY_MATRIX, MODULO):
    raise ValueError("A matriz-chave não possui inversa modular válida no módulo 26.")

# Função para converter texto em números
def text_to_numbers(text):
    return [ALPHABET.index(c) for c in text]

# Função para converter números em texto
def numbers_to_text(numbers):
    return ''.join(ALPHABET[i % MODULO] for i in numbers)

# Adiciona padding se necessário
def pad_text(text):
    while len(text) % N != 0:
        text += 'X'  # Usa 'X' como padding
    return text

# Cifra um texto usando a Cifra de Hill
def encrypt(text, key_matrix):
    text = pad_text(text.upper().replace(" ", ""))
    numbers = text_to_numbers(text)
    cipher_text = []
    
    for i in range(0, len(numbers), N):
        block = np.array(numbers[i:i+N]).reshape(N, 1)
        cipher_block = np.dot(key_matrix, block) % MODULO
        cipher_text.extend(cipher_block.flatten())
    
    return numbers_to_text(cipher_text)

# Função para calcular a inversa modular de uma matriz no módulo 26
def mod_inv_matrix(matrix, mod):
    matrix = Matrix(matrix)  # Converte para matriz do SymPy
    return np.array(matrix.inv_mod(mod)).astype(int)  # Obtém a inversa modular corretamente

# Decifra um texto usando a Cifra de Hill
def decrypt(text, key_matrix):
    numbers = text_to_numbers(text.upper())
    plain_text = []
    
    key_inv = mod_inv_matrix(key_matrix, MODULO)  # Usa a inversa modular correta
    
    for i in range(0, len(numbers), N):
        block = numbers[i:i+N]
        if len(block) < N:
            block += [0] * (N - len(block))  # Completa com zeros se necessário
        block = np.array(block).reshape(N, 1)
        plain_block = np.dot(key_inv, block) % MODULO
        plain_text.extend(plain_block.flatten())
    
    return numbers_to_text(plain_text).rstrip('X')  # Remove padding extra

# Leitura e escrita de arquivos
def read_file(filename):
    with open(filename, 'r') as f:
        return f.read().strip()

def write_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)

# Configuração de argumentos de linha de comando
parser = argparse.ArgumentParser(description='Cifra de Hill')
parser.add_argument('-enc', '--encrypt', help='Arquivo de entrada para cifração')
parser.add_argument('-dec', '--decrypt', help='Arquivo de entrada para decifração')
parser.add_argument('-out', '--output', required=True, help='Arquivo de saída')
args = parser.parse_args()

if args.encrypt:
    plaintext = read_file(args.encrypt)
    ciphertext = encrypt(plaintext, KEY_MATRIX)
    write_file(args.output, ciphertext)
    print(f'Texto cifrado salvo em {args.output}')
elif args.decrypt:
    ciphertext = read_file(args.decrypt)
    plaintext = decrypt(ciphertext, KEY_MATRIX)
    write_file(args.output, plaintext)
    print(f'Texto decifrado salvo em {args.output}')
else:
    mode = input("Digite 'E' para cifrar ou 'D' para decifrar: ").strip().upper()
    if mode == 'E':
        text = input("Digite o texto a ser cifrado: ")
        print("Texto Cifrado:", encrypt(text, KEY_MATRIX))
    elif mode == 'D':
        text = input("Digite o texto a ser decifrado: ")
        print("Texto Decifrado:", decrypt(text, KEY_MATRIX))
    else:
        print("Opção inválida.")