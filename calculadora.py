print("===Calculadora Simples!===")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
print("\nSelecione uma operação: (+, -, *, /) ")
operacao = input("Digite a  operação: ")
if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 != 0:
         resultado = num1 / num2
    else:
        resultado = "Error nao permitido divisão por zero!"
else:
    resultado = "Operação inválida"
print("\nResultado: ",(resultado))                   