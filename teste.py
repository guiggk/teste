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

#desafio.py 36
from time import sleep
casa=float(input("Digite o valor da casa:\nR$"))
anosp=float(input("Em quantos anos vai querer pagar:\n"))
parcela=anosp * 12
compra= casa / parcela
print("\033[1;33mPROCESSANDO...\033[m")
sleep(1)
print("O valor a pagar ficou por {:.0f}x parcelas de R${:.2f}".format(parcela,compra))
s=float(input("digite seu salário,para a solicitação de um empréstimo:\nR$"))
em=(s*30) / 100
print("\033[1;33mPROCESSANDO...\033[m")
sleep(1)
if  compra < em:
    print("\033[1;32mEmpréstimo CONFIRMADO\033[m")
else:
    print("\033[1;31mEmpréstimo NEGADO\033[m")

#desafio.py 37
n1=int(input("digite um número inteiro:\n"))
print("Escolha a opção de conversão:")
print("\033[1;37m[1]\033[m converter para BINÁRIO")
print("\033[1;37m[2]\033[m converter para OCTAL")
print("\033[1;37m[3]\033[m converter para HEXADECIMAL")
n2=int(input("Sua opção: "))
if n2 == 1:
    print(" {} convertido para BINÁRIO é igual a {}".format(n1,bin(n1)[2:]))
elif n2 == 2:
    print(" {} convertido para OCTAL é igual a {}".format(n1,oct(n1)[2:]))
elif n2 == 3:
    print(" {} convertido para HEXADECIMAL é igual a {}".format(n1,hex(n1)[2:]))
else:
    print("\033[1;31mOpção INVÁLIDA.\nTente novamente.\033[m")

#desafio.py 38
n1=int(input("digite o primeiro número inteiro:\n"))
n2=int(input("digite o segundo número inteiro:\n"))

if n1 < n2:
    print("O número maior é {} e o menor é {}".format(n2,n1))
elif n1 == n2:
    print("Não a diferença númerica, os dois número são iguais")
else:
    print("O número maior é {} e o menor é {}".format(n1,n2))

#desafio.py 39
from datetime import date
print("-"*20)
print("\033[1mALISTAMENTO MILITAR\033[m")
anon=int(input("Digite o ano do seu nascimento:\n"))
genero=str(input("Digite seu gênero:\n")).strip().capitalize().replace(" ","")
al=date.today().year - anon
at=date.today().year

if al == 18 and genero =='Homem':
    print("\033[1;32mTa na hora de se alistar jovem!!!\033[m")
elif al == 18 and genero =='Mulher':
    print("\033[1;33mNão precisa se alistar\033[m")
elif al < 18 and genero =='Homem':
    f = 18 - al
    k= at + f
    print("\033[1;33mNão pode se alistar ainda, faltam {} anos\nlogo poderá se alistar no ano de {}\033[m".format(f,k))
elif al < 18 and genero =='Mulher':
    print("\033[1;33mNão precisa se alistar\033[m")    
elif al > 18 and genero == 'Homem':
    f = al - 18
    k= at - f
    print("\033[1;31mPASSOU DO PRAZO DE ALISTAMENTO,era para você ter se alistado no ano de {}\033[m".format(k))
elif al > 18 and genero == 'Mulher':
    print("\033[1;33mNão precisa se alistar\033[m")
#desafio.py 40
n1=float(input("Digite sua primeira nota:\n"))
n2=float(input("Digite sua segunda nota:\n"))
media=(n1+n2)/2

if media < 5:
    print("\033[1;31mREPROVADO\033[m")
elif media >= 5 or media <= 6.9:
    print("\033[1;33mRECUPERAÇÃO\033[m")
else:
    print("\033[1;32mAPROVADO\033[m")

#desafio.py 41
from datetime import date
ano=date.today().year
atleta=int(input("Digite o ano do seu nascimento:\n"))
idade=ano-atleta
print("Você tem {} anos".format(idade))
if idade <= 9: 
    print("Categoria Mirim")
elif idade<=14: 
    print(" categoria infantil")
elif idade <=19:
    print("categoria Júnior")
elif idade <=25:
    print("categoria sênior")
else:
    print("categoria master")

#desafio.py 42
n1=float(input("digite o primeiro segmento:\n"))
n2=float(input("digite o segundo segmento:\n"))
n3=float(input("digite o terceiro segmento:\n"))

if n1<n2+n3 and n2<n1+n3 and n3<n1+n2:
    print("Esses segmentos formam um triangulo ")
    if n1 == n2 == n3:
        print("EQUILÁTERO")
    elif n1 == n2 !=n3:
        print(" ISÓSCELES")
    else:
        print(" ESCALENO")
else:
    print("Não forma um triangulo")

#desafio.py 43
peso=float(input(" Qual é o seu peso?\n"))
altura=float(input("Qual é a sula altura?\n"))
imc= peso/(altura**2)
if imc < 17:
    print("Você está muito abaixo do peso")
elif imc == 17 or imc<=18.49:
    print("Seu imc é {:.2f} você está abaixo do peso".format(imc))
elif imc <= 24.99:
    print("Seu imc é {:.2f} você está com o peso normal".format(imc))
elif imc <= 29.99:
    print("Seu imc é {:.2f} você está acima do peso".format(imc))
elif imc <= 34.99:
    print("Seu imc é {:.2f} você está com obesidade,CUIDADO!".format(imc))
elif imc <= 39.99:
    print("Seu imc é {:.2f} você está com obesidade severa,CUIDADO!".format(imc))
else:
    print("Seu imc é {:.2f} você está com obesidade morbida, CUIDADO!".format(imc))

#desafio.py 44
n1=float(input("digite o preço do produto:\nR$"))
print("\033[1;37m[1]\033[m-á vista dinheiro/cheque")
print("\033[1;37m[2]\033[m-á vista no cartão")
print("\033[1;37m[3]\033[m-2x no cartão sem juros")
print("\033[1;37m[4]\033[m-3x ou mais no cartão com juros de 20%")
n2=int(input("Digite a opção de pagamento:\n").strip())
if n2 == 1:
    d10 = n1-n1*(10/100)
    print("a vista você ganha desconto de 10%, ficando por R${:.2f}".format(d10))
elif n2 == 2:
    d5 = n1-n1*(5/100)
    print("a vista você ganha desconto de 5%, ficando por R${:.2f}".format(d5))
elif n2 == 3:
    vp=int(input("vai parcelar em quantas vezes?\n").strip())
    if vp == 2:
        p=n1 / 2
        print("O preço ficou {}x parcelas de R${:.2f}".format(vp,p))
    else:
        print("\033[1;31mresolução da compra invalida\033[m")
elif n2 == 4:
    p=int(input("vai parcelar em quantas vezes?\n").strip())
    if p >= 3:
        pj=(n1*(20/100)+n1)/p
        print("O preço ficou {}x parcelas de R${:.2f}".format(p,pj))
    else:
        print("\033[1;31mresolução da compra invalida\033[m")
else:
     print("\033[1;31mresolução da compra invalida\033[m")

#desafio.py 45
from random import randint
from time import sleep
print("-*-"*20)
print("\033[1;33mJOKENPOOOO!!\033[m")
print("-*-"*20)
print("\033[1;37m[0]\033[m-PEDRA")
print("\033[1;37m[1]\033[m-PAPEL")
print("\033[1;37m[2]\033[m-TESOURA")
n1=int(input("escolha uma das opções para competir com o computador:\n"))
lista=('Pedra','Papel','Tesoura')
pc=randint(0,2)
print("\033[1;33mJO\033[m")
sleep(1)
print("\033[1;33mKEN\033[m")
sleep(1)
print("\033[1;33mPO\033[m")
sleep(1)
print("você jogou {}".format(lista[n1]))
print("anonimo jogou {}".format(lista[pc]))
if  pc == 0:
    if n1 == 0:
        print("\033[1;33mEMPATE\033[m")
    elif n1 == 1:
        print("\033[1;32mVOCÊ VENCEU,PARABENS!!!\033[m")
    elif n1 ==2:
        print("\033[1;35mAnonimo Venceu, é uma pena\033[m")
    else:
        print("\033[1;31mJOGADA INVALIDA\033[m")
elif pc == 1:
    if n1 == 0:
        ("\033[1;35mAnonimo Venceu, é uma pena\033[m")   
    elif n1 ==1:
        print("\033[1;33mEMPATE\033[m")
    elif n1 == 2:
       print("\033[1;32mVOCÊ VENCEU,PARABENS!!!\033[m")
    else:
        print("\033[1;31mJOGADA INVALIDA\033[m")
elif pc == 2:
    if n1 == 0:
        print("\033[1;32mVOCÊ VENCEU,PARABENS!!!\033[m")   
    elif n1 ==1:
       print("\033[1;35mAnonimo Venceu, é uma pena\033[m")
    elif n1 == 2:
        print("\033[1;33mEMPATE\033[m")
    else:
        print("\033[1;31mJOGADA INVALIDA\033[m")
else:
    print("\033[1;31mJOGADA INVALIDA\033[m")


