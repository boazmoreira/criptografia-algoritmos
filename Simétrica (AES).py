import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def criptografar_aes(mensagem, chave):
    cipher = AES.new(chave, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(mensagem.encode())
    return base64.b64encode(nonce + tag + ciphertext).decode()

def descriptografar_aes(dados_criptografados, chave):
    dados = base64.b64decode(dados_criptografados)
    nonce, tag, ciphertext = dados[:16], dados[16:32], dados[32:]
    cipher = AES.new(chave, AES.MODE_EAX, nonce=nonce)
    return cipher.decrypt_and_verify(ciphertext, tag).decode()

def exemplo_aes():
    mensagem = "Esta é uma mensagem com AES."
    chave = get_random_bytes(16)
    criptografada = criptografar_aes(mensagem, chave)
    descriptografada = descriptografar_aes(criptografada, chave)

    print("\n🔒 AES - Mensagem original:", mensagem)
    print("🧪 AES - Mensagem criptografada:", criptografada)
    print("🔓 AES - Mensagem descriptografada:", descriptografada)
