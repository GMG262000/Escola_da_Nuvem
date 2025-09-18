#ex1
myString = "Isso é uma String"
print(myString)
print(type(myString))
print(myString +" é do tipo de dado " + str(type(myString)))
#fim

#ex2
# Concatenação de variaveis
firstString = "water"
SecondString = "fall"
thirdString = firstString + SecondString
print(thirdString)
#fim


#ex3 e 4
name = input(" Qual é o seu nome? ") 
color = input(" Qual sua cor favorita? ")
animal= input(" Qual é seu animal favorito ? ")
print("{}, voce gosta da cor {} e do animal {}!".format(name,color,animal))
#fim

# Lista 
listaFrutas =["maça","banana","laranja"]
print(listaFrutas)
print(type(listaFrutas))
print(listaFrutas[0])
print(listaFrutas[1])
print(listaFrutas[2])
listaFrutas[0] = "ABACAXI"
print("Minha Liosta DE FRUTAS ALTERADA: ", listaFrutas)

# TUPLA
tuplaFrutas = ("maça", "banana", "laranja")
print("A minha TUPLA de frutas é: ", tuplaFrutas)
print("O tipo de dados da minha TUPLA é: ", type(tuplaFrutas))
print(tuplaFrutas[0])
print(tuplaFrutas[1])
print(tuplaFrutas[2])

# DICIONÁRIO
dicioFrutas = {
    "Ricardo": "Limão",
    "Gustavo": "Uva",
    "Taciara": "Tangerina",
    "Carol": "Manga"
}
print("Meu dicionário de Pessoas e frutas preferidas é: ", dicioFrutas)
print(type(dicioFrutas))
print("A Carol gosta de", dicioFrutas["Carol"])
print(dicioFrutas["Gustavo"])
print(dicioFrutas["Ricardo"])
print(dicioFrutas["Taciara"])

#
