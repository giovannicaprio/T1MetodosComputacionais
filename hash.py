import hashlib

dic = {}
data = []

with open ("dracula.txt", "r") as myfile:
	for line in myfile:
		for word in line.split():
			data.append(word)

print data
print 'quantidade de palavras'
print len(data)

'''
trecho correspondente ao algoritmo extremamente eficiente MD5

for i in range(len(data)):
	#print data[i]
	#print hashlib.md5(data[i]).hexdigest()
	s = hashlib.md5(data[i])
	#i = int(s, 16)
	#print 'DATA00 depois depois do hash e decimal' 
	#k = str(i)[0] + str(i)[1] + str(i)[2] + str(i)[3]
	#print k
	#print s
	if s in dic:
		dic[s] += 1
	else:
		dic[s] = 1
'''

'''
trecho correspondente ao algoritmo de HASH puro, sem algoritmos de criptografia

conflitos = 0
for i in range(len(data)):
	s = hash(data[i])
	teste = str(s)

	if teste[0] == '-':
		print 'negativo'
		s = s * -1
		print s

	if s in dic:
		dic[s] += 1
		conflitos += 1
	else:
		dic[s] = 1


print 'tamanho dic'
print len(dic)

'''
def kaprekar(dic, number):
	
	#quando o algoritmo possuir a ultima posicao igual a 0 o python desconsidera
	#logo, multiplica por 10 para forcar um 0 naquela posicao e seguir a regra kaprekar
	print 'number'
	print number

	
	if len(number) == 3:
		number = number * 10
		#print number
		digits = list(number)
		digits.sort()
		zero = str(0)
		asc = zero + digits[0] + digits[1] + digits[2]
		dsc = digits[3] + digits[2] + digits[1] + zero
	else:
		digits = list(number)
		digits.sort()
		asc = digits[0] + digits[1] + digits[2] + digits[3]
		dsc = digits[3] + digits[2] + digits[1] + digits[0]
	
	asc = int(asc)
	dsc = int(dsc)
	
	#print asc
	#print dsc
	result = dsc - asc
	#print "%s - %s = %s" % (dsc, asc, result)

	#print dic
	num = str(result)
	resultINT = int(result)

	if (resultINT - 6174) != 0:
		if num in dic:
			return kaprekar(dic, num)
		else:
			return num
	else:
		return num

'''
trecho com o hash puro, porem utilizando apenas os 4 primeiros caracteres

conflitos = 0
for i in range(len(data)):
	s = hash(data[i])
	teste = str(s)

	if teste[0] == '-':
		#print 'negativo'
		s = s * -1
	
	#k = str(s)[1] + str(s)[2] + str(s)[3] + str(s)[4]
	k = str(s)[0] + str(s)[1] + str(s)[2] + str(s)[3]
	#k = str(s)[4] + str(s)[5] + str(s)[6] + str(s)[7]


	if k in dic:
		dic[k] += 1
		conflitos += 1
	else:
		dic[k] = 1

'''

'''
trecho com o hash puro, porem utilizando apenas os 4 primeiros caracteres e a rotina kaprekar
'''
conflitos = 0
for i in range(len(data)):
	s = hash(data[i])
	teste = str(s)

	if teste[0] == '-':
		s = s * -1
	print s	
	
	k = str(s)[4] + str(s)[5] + str(s)[6] + str(s)[7]
	#k = str(s)[0] + str(s)[1] + str(s)[2] + str(s)[3]

	if k in dic:
		if(k[0] == k[1] == k[2] == k[3]):
			dic[k] = 1
		else:
			var = kaprekar(dic, k)
			if var in dic:
				dic[var] += 1
				conflitos += 1
			else:
				dic[var] = 1	
	else:
		dic[k] = 1
		

print dic		

print 'tamanho da tabela de dispersao'
print len(dic)

print 'conflitos'
print conflitos

print 'quantidade de x que utilizou a posicao da constante kaprekar'
print dic['6174']


#for key in dic:
#	print key, dic[key]


		



#print 'countUm'
#print countUm

#print 'FINAL'
#print dic  




