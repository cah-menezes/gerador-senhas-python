import string
import secrets
import time

print ("=== Seja bem-vindo ao Gerador de Senhas 3000 ===")
print ("Aqui ajudamos você a gerar uma senha forte e segura em poucos cliques.")
time.sleep(1)

resposta = int(input("Quantos caracteres você quer sua na senha?\n"))

while resposta <= 7:
    print("O padrão mínimo amplamente aceito para senhas é de 8 caracteres. Poderia tentar novamente?")
    time.sleep(1)
    resposta = int(input("Quantos caracteres você quer sua na senha?\n"))
    time.sleep(1)

print(f"Certo, vou gerar uma senha de {resposta} caracteres")
time.sleep(1)
caracteres =  string.ascii_letters + string.digits + string.punctuation
print("Carregando...")
time.sleep(2)
senha = ""
for i in range(resposta):
    senha = senha + secrets.choice(caracteres)

print(senha)

print("Senha gerada com sucesso! ✅")
time.sleep(1)
print("Guarde em um gerenciador de senhas e nunca compartilhe com ninguém.")
time.sleep(1)
print("Obrigada por usar o Gerador de Senhas 3000. Até a próxima!")


