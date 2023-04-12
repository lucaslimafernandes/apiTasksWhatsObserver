from hashlib import sha256

senha = input('Digite uma senha:')
res = sha256(senha.encode()).hexdigest()

print(f'O hash SHA256 de sua senha é: {res}')
print(f'Colar o valor na varial TK do arquivo settings.py')
print(f'TK = "{res}"')

