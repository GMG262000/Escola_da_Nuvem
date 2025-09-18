'''userReply = input("Você precisa enviar um pacote? (Digite Sim ou Não)")
if userReply == "Sim":
    print("Podemos ajudá-lo enviar esse pacote!")
else :
    print("Volte quando precisdar enviar um pacote!")    '''

usuario = input("Você deseja comprar selos, Comprar envelope ou tirar uma Cópia^? ( Digite Selo , envelope, Copia )")
if usuario =="selo":
    print("Temos muitos designes para escolher.")
elif usuario == "envelope":
    print("Temos vários tamanhos de envelopes para escolher.")   
elif usuario == "copia" :
      copia = input("Quantas cópias deseja fazer?(digite quantas cópias)") 
      print("Aqui está {} cópias".format(copia)) 
else : 
     print("Obrigado, Volte uma outra hora!") 
          