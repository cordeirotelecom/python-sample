salario = int(input('salario '))
imposto = (input('Imposto em % (ex: 27.5)? '))

if imposto =='':
	imposto = 27.5
else:
	imposto = float(imposto)

salario_real = (salario - (salario *imposto * 0.01))

print("Valor real: {0}".format(salario_real))