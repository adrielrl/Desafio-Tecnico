entrada = input("Digite uma string: ")
contagem = 0

for letra in entrada:
    if letra == 'a' or letra == 'A':
        contagem += 1  

if contagem > 0:
    print("A letra 'a' (maiúscula ou minúscula) aparece", contagem, "vez(es) na string.")
else:
    print("A letra 'a' não está presente na string.")