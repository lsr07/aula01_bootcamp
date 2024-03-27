CONSTANTE_BONUS = 1000
# Digite o nome
nome = input("Digita seu nome cornélios: ")

# Digita seu salário
salario = float(input("Fala quanto que tá o cascalho: "))

#Bônus
bonus = float(input("Fala o valor do bônus, seu animal: "))

#Cálculo valor Bonus
salario_bonus = CONSTANTE_BONUS + salario * bonus

#Msg Personalizada pro corno(A)
print(f"PARABENS CORNÃO {nome}: O SEU BÔNUS É DE: {salario_bonus}")