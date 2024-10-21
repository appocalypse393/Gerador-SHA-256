import hashlib

def gerar_sha256(texto):
    # Codifica o texto para bytes e gera o hash SHA-256
    hash_object = hashlib.sha256(texto.encode())
    # Converte o hash gerado em hexadecimal
    hash_hex = hash_object.hexdigest()
    return hash_hex

# Entrada do usuário
texto = input("Digite o texto para gerar o SHA-256: ")
hash_resultado = gerar_sha256(texto)

# Exibe o resultado corretamente
print(f"O hash SHA-256 do texto é: {hash_resultado}")
