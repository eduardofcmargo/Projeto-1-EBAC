print("Bem Vindo a Calculadora!")
print("Para fazer o calculo utilize: *soma* *subtração* *divisão* *multiplicação*")
operacao = input("Qual tipo de operação iremos fazer?")
if operacao == "multiplicação":
  val1 = int(input("Digite o primeiro valor: "))
  val2 = int(input("Digite o segundo valor: "))
  print("O resultado é: ", val1 * val2)
elif operacao == "divisão":
  val1 = int(input("Digite o primeiro valor: "))
  val2 = int(input("Digite o segundo valor: "))
  print("O resultado é: ", val1 / val2)
elif operacao == "soma":
  val1 = int(input("Digite o primeiro valor: "))
  val2 = int(input("Digite o segundo valor: "))
  print("O resultado é: ", val1 + val2)
elif operacao == "subtração":
  val1 = int(input("Digite o primeiro valor: "))
  val2 = int(input("Digite o segundo valor "))
  print("O resultado é: ", val1 - val2)
else :
  print("Operação inválida")

print("Obrigado por usar a calculadora, tenha um bom dia")