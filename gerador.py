import string
import secrets
import time

print ("=== Seja bem-vindo ao Gerador de Senhas Seguras 3000 ===")
print ("Aqui ajudamos você a gerar uma senha forte e segura em poucos cliques.")
time.sleep(1)

resposta = int(input("Quantos caracteres você quer na sua senha?\n"))

while resposta <= 7:
    print("O padrão mínimo amplamente aceito para senhas é de 8 caracteres. Poderia tentar novamente?")
    time.sleep(1)
    resposta = int(input("Quantos caracteres você quer na sua senha?\n"))
    time.sleep(1)

print(f"Certo, vou gerar 3 opções de senhas de {resposta} caracteres para você. Escolha uma:")
time.sleep(1)
caracteres =  string.ascii_letters + string.digits + string.punctuation
print("Carregando...")
time.sleep(2)

for opcao in range(1, 4):
    senha = ""
    for i in range(resposta):
        senha = senha + secrets.choice(caracteres)
    print(f"{opcao}) {senha}")

# Ideia v2: perguntar se gostou das senhas e gerar de novo se não

print("Opções geradas com sucesso. ✅")
time.sleep(1)
print("Copie e salve em um gerenciador de senhas. Nunca compartilhe com ninguém.")
time.sleep(1)
print("Obrigada por usar o Gerador de Senhas Seguras 3000. Até a próxima!")


