import hashlib

def gerar_hash_sha256(mensagem):
    hash_obj = hashlib.sha256(mensagem.encode())
    return hash_obj.hexdigest()

def exemplo_sha256():
    mensagem = "Mensagem para SHA-256."
    hash_gerado = gerar_hash_sha256(mensagem)

    print("\n🔐 SHA-256 - Mensagem original:", mensagem)
    print("📎 SHA-256 - Hash gerado:", hash_gerado)
