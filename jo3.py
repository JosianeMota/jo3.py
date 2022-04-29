primeiroNome = input("digite seu primeiro nome:")
("Digite seu salário print no mês de abril: ")
sálarioreais = input("Reais: ")
sálariocentavos = input("centavos: ")
salárioformatado = salárioreais + "," + saláriocentavos
primeiraletra = primeiroNome [0:1].upper()
restantenome = primeiroNome[1:]
primeiroNomeformatado = primeiraletra + restantenome
mensagem = " O salário de "+primeiroNomeformatado + "no mês de maio foi de R$" + salárioformatado + ","
print(mensagem)