import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def gerar_chaves_rsa():
    chave = RSA.generate(2048)
    return chave, chave.publickey()

def criptografar_rsa(mensagem, chave_publica):
    cipher = PKCS1_OAEP.new(chave_publica)
    return base64.b64encode(cipher.encrypt(mensagem.encode())).decode()

def descriptografar_rsa(mensagem_criptografada, chave_privada):
    cipher = PKCS1_OAEP.new(chave_privada)
    return cipher.decrypt(base64.b64decode(mensagem_criptografada)).decode()

def exemplo_rsa():
    mensagem = "Mensagem com RSA."
    chave_privada, chave_publica = gerar_chaves_rsa()
    criptografada = criptografar_rsa(mensagem, chave_publica)
    descriptografada = descriptografar_rsa(criptografada, chave_privada)

    print("\n🔒 RSA - Mensagem original:", mensagem)
    print("🧪 RSA - Mensagem criptografada:", criptografada)
    print("🔓 RSA - Mensagem descriptografada:", descriptografada)
