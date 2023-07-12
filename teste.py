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

#desafio.py 16
from math import floor,trunc
num=float(input("digite um número real: "))
print("O número digitado {}, sua porção interia desse numero é {}".format(num,floor(num)))
#ou
print("O número digitado {}, sua porção interia desse numero é {:.0f}".format(num,num))
#ou
print("O número digitado {}, sua porção interia desse numero é {}".format(num,trunc(num)))

#desafio.py 17
from math import hypot,trunc
co=float(input("comprimento do cateto oposto: "))
ca=float(input("comprimento do cateto adjacente: "))
hi= hypot(co,ca)
print('A hipotenusa vai medir {}'.format(trunc(hi)))

#desafio.py 18
from math import cos,tan,sin,radians
an=(float(input("digite o angulo: ")))
seno=sin(radians(an))
co=cos(radians(an))
tg=tan(radians(an))
print("o angulo de {}, tem o seno de {:.2f},cosseno de {:.2f} e tangente de {:.2f}".format(an,seno,co,tg))

#desafio.py 19
from random import choice
a1=input("digite o nome do primeiro aluno(a):\n")
a2=input("digite o nome do segundo aluno(a):\n")
a3=input("digite o nome do terceiro aluno(a):\n")
a4=input("digite o nome do quarto aluno(a):\n")
lista=[a1,a2,a3,a4]
escolhido=choice(lista)
print("o aluno escolhido foi {}".format(escolhido))

#desafio.py 20
from random import shuffle
a1=input("digite o nome do primeiro aluno(a):\n")
a2=input("digite o nome do segundo aluno(a):\n")
a3=input("digite o nome do terceiro aluno(a):\n")
a4=input("digite o nome do quarto aluno(a):\n")
lista=[a1,a2,a3,a4]
shuffle(lista)
print("a ordem de apresentação será: ")
print(lista)

#desafio.py 21
import pygame 
pygame.init()
pygame.mixer.music.load("cmp.mp3")
pygame.mixer.music.play()
input()
pygame.event.wait()

#desafio.py 22
nome=str(input('digite seu nome completo:\n')).strip()
div=nome.split()
print('seu nome:')
print('Em maiúsculas é:',nome.upper())
print('Em minúsculas é:',nome.lower())
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
print('O primeiro nome tem {} letras'.format(len(div[0])))

#desafio.py 23
#forma numerica
num=int(input('Informe o número: '))
print('unidade: {}'.format(num//1%10))
print('dezena: {}'.format(num//10%10))
print('centena: {}'.format(num//100%10))
print('milhar: {}'.format(num//1000%10))

#desafio.py 24
cidade=str(input("Em que cidade você nasceu?\n")).strip()
print('santo'in cidade)

#desafio.py 25
nome=str(input('qual é o seu nome completo? ')).strip()
print('seu nome tem silva?\n','silva'in nome.lower())

#desafio.py 26
frase=str(input("digite uma frase:\n")).strip().upper()
print("na sua frase aparece a letra A: {}".format(frase.count('A')))
print('E aparece pela primeira vez na posição: {}'.format(frase.find('A')+1))
print('E a ultima vez que aparece a letra A é: {}'.format(frase.rfind('A')+1))

#desafio.py 27(
nome=str(input("digite seu nome completo:\n")).strip().split()
print("seu primeiro nome é: {}\n e seu ultimo nome é:{}".format(nome[0],nome[len(nome)-1]))

#desafio.py 28
from random import randint
from time import sleep
n=randint(0,5)
n1=int(input("tente acertar o número sorteado, de 0 á 5:\n"))
print("PROCESSANDO...")
sleep(2)
if n1 == n:
    print("você acertou o número, PARABÉNSSS!!!")
else:
    print("você errou!!!, o número era: {}".format(n))

#desafio.py 29
v=float(input("Qual a vélocidade atual do carro?\n"))
if v>80:
    print("Você ultrapassou o limite de velocidade, pague R${:.2f} de multa".format((v-80)*7))
else:
    print("está dentro do limite de velocidade")

#desafio.py 30
n=int(input("digite um número inteiro qualquer:\n"))
if n % 2 == 0:
    print("é um número PAR")
else:
    print("é um número IMPAR")

#desafio.py 31

p=float(input("digite a distância da sua viagem:\n"))
if p<=200:
    print(" o preço da passagem ficou por R${:.2f}".format(p*0.50))
elif p>200:
    print("o preço da passagem ficou por R${:.2f}".format(p*0.45))

print("obrigado por escolher nossa plataforma")

#desafio.py 32
from datetime import date
ano=int(input("digite o ano que deseja analisar:\n obs:caso deseja analisar o ano atual digite 0\n "))
if ano ==0:
    ano= date.today().year    
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("o ano {} é BISSEXTO".format(ano))
else:
    print(" O ano {} não é bissexto".format(ano))

#desafio.py 33
n1=int(input("digite o primeiro número:\n"))
n2=int(input("digite o segundo número:\n"))
n3=int(input("digite o terceiro número:\n"))
if n1 < n2 and n1 < n3:
    menor=n1
if n2 < n1 and n2 < n3:
    menor=n2
if n3 < n1 and n3 < n2:
    menor=n3
if n1 > n2 and n1 > n3:
    maior=n1
if n2 > n1 and n2 > n3:
    maior=n2
if n3 > n1 and n3 > n2:
    maior=n3
print("o menor numero é {} e o maior é {}".format(menor,maior))

#desafio.py 34
s=float(input("digite o salário atual para acontecer o reajuste:\n"))
if s > 1250:
    print("Com base no valor digitado voce terá um aumento de 10%, então seu salário agora é R${:.2f}".format(s+(s*10/100)))
if s <= 1250:
    print("com base no valor digitado voce terá um aumento de 15%, então seu salário agora é R${:.2f}".format(s+(s*15/100)))

#desafio.py 35

n1=float(input("digite o primeiro segmento:\n"))
n2=float(input("digite o segundo segmento:\n"))
n3=float(input("digite o terceiro segmento:\n"))

if n1 < n2+n3 and n2 < n1+n3 and n3 < n1+n2:
    print("pode formar um triângulo")
else:
    print("Não pode formar um triangulo")
