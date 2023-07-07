#desafio.py 1
print("olá,mundo!")

#desafio.py 2
nome=input("digite seu nome:")
print("seja muito bem vindo(a),{}!".format(nome))

#desafio.py 3
n1=int(input('digite um número\n'))
n2=int(input('digite mais um número para acontecer a soma\n'))
s=n1+n2
print('sua soma entre {} e {} foi:{}'.format(n1,n2,s))

#desafio.py 4
g=input('digite algo\n')
print(type(g))
print('é numerico?',g.isnumeric())
print('é alfabético?',g.isalpha())
print('é alfanúmerico?',g.isalnum())
print('Está em maiúsculas?',g.isupper())
print('Está em minúsculas?',g.islower())
print('só tem espaços?',g.isspace())
print('Está capitalizada',g.istitle())

#desafio.py 5
n=int(input("digite um número\n"))
print("seu número é {}, logo seu antecessor é {} e seu sucessor é {}".format(n,n-1,n+1))

#desafio.py 6
n=int(input("digite um número\n"))
print('o dobro de {} vale {}\no seu triplo vale {}\ne a raiz é ≈{:.1f}'.format(n,n*2,n*3,n**(1/2)))

#desafio.py 7
n1=float(input("digite sua nota\n"))
n2=float(input("digite sua segunda nota\n"))
print("A média entre {} e {} foi {:.1f}".format(n1,n2,(n1+n2)/2))

#desafio.py 8
m=float(input("digite uma distância em metros\n"))
cm=m*100
mm=m*1000
print("a medida de {}m corresponde a {:.0f}cm e {:.0f}mm".format(m,cm,mm))
#ou
print("a medida de {}m corresponde a {:.0f}cm e {:.0f}mm".format(m,m*100,m*1000))

#desafio.py 9
n=int(input("Digite um número para ver sua tabuada\n"))
print("{}x{:2}={}".format(n,1,n*1))
print("{}x{:2}={}".format(n,2,n*2))
print("{}x{:2}={}".format(n,3,n*3))
print("{}x{:2}={}".format(n,4,n*4))
print("{}x{:2}={}".format(n,5,n*5))
print("{}x{:2}={}".format(n,6,n*6))
print("{}x{:2}={}".format(n,7,n*7))
print("{}x{:2}={}".format(n,8,n*8))
print("{}x{:2}={}".format(n,9,n*9))
print("{}x{:2}={}".format(n,10,n*10))

#desafio.py 10
n=float(input("digite quanto de dinheiro você tem na carteira: R$"))
print("então você tem {:.2f}US$".format(n/4.92))

#desafio.py 11
L=float(input("digite a largura da parede em metros:\n"))
c=float(input("digite a altura da parede em metros:\n"))
print("com base nas informações que o senhor(a) deu, a aréa da parede é de {:.1f}m²".format(L*c),end="")
print(", logo você precisará de {:.2f}l de tinta para pinta-la".format((L*c)/2))

#desafio.py 12
p=float(input("Qual o preço do produto?\n R$"))
print("O produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}".format(p,p-(p*5/100)))

#desafio.py 13
a=float(input("Digite seu antigo salário:\nR$"))
print("Com o aumento de 15%, seu novo salário será R${:.2f}".format(a+(a*15/100)))

#desafio.py 14
G=float(input("digite a temperatura em °C:\n"))
print(" a temperatura de {}°C corresponde a {:.1f}°F".format(G,((9*G)/5)+32))

#desafio.py 15
carro=int(input("digite a quantidade de dias que carro ficou alugado:\n"))
km=float(input("digite a kilometragem que o carro alugado percorreu:\n"))
pd=carro*60
pk=km*0.15
print("de acordo com os dados digitado, o valor do dia ficou por R${:.2f} e pelos km rodados ficou por R${:.2f},".format(pd,pk),end="")
print(" logo o valor total a pagar ficou por R${:.2f}".format(pd+pk))
