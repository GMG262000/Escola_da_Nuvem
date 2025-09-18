import random # MODULO serve para gerar números  aleatorops


print("Bem-Vindo ao Advinhe o número!")
print("As regras são simples, Vou pensar em número e voce tentará" \
"advinhá-lo.")
numero = random.randint(1, 10)
isGuessRight = False
while isGuessRight != True:
    adivinha = input("Digite um número de 1 a 10:")
    if int(adivinha) == numero:
        print(" Voce e muito bom adivinhou {} o número está correto! Voce ganhou ".format(adivinha))
        isGuessRight = True
    else:
        print(" Voce digitou número  {}. Desculpe voce Errouuu. Tente novamente mais sorte na proxima tentativa. ".format(adivinha))    


