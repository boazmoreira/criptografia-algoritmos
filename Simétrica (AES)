from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

# Gerar chave e IV (vetor de inicialização)
key = os.urandom(32)  # 256 bits
iv = os.urandom(16)   # 128 bits

# Texto plano
plaintext = b'Exemplo de texto secreto'

# Criptografar
cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
encryptor = cipher.encryptor()
ciphertext = encryptor.update(plaintext) + encryptor.finalize()

# Decriptografar
decryptor = cipher.decryptor()
decrypted = decryptor.update(ciphertext) + decryptor.finalize()

print("Original:", plaintext)
print("Criptografado:", ciphertext)
print("Decriptado:", decrypted)
