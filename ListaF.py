#ListaFunções
print("Seja Bem vindo a Lista feita por icaro e carlos.")
print("1 - Saudação.")
print("2 - Par ou Impar.")
print("3 - Maior de dois números.")
print("4 - Tabuada.")
print("5 - Contagem Regressiva.")
print("6 - Media de notas.")
def saudacao(nome):
    print(f"Olá, {nome} Seja bem-vindo ao curso de lógica de programação.")

def impar(x):
    if x % 2 == 0 :
        print("O número é par!")
    else:
        print("O número é impar!")     
  
while True:
    op = int(input("Digite uma opção: (0 para sair): "))
    if op == 0:
        print("Voce saiu do sistema.")
        break
    if op == 1:
        nome = input("Digite seu nome:  ")
        saudacao(nome)
        print("Obrigado por usar o nosso sistema!")
        break
    if op == 2:
        x = int(input("Digite um número:    "))
        impar(x)
        print("Obrigado por usar o nosso sistema!")
        break
    if op == 3:
        n1 = float(input("Digite um número: "))
        n2 = float(input("Digite outro número: "))
        if (n1 > n2):
            print(f"{n1} É o maior numero.")
        else:
            print(f"{n2} É o maior numero.")
        if (n1 == n2):
            print("Os dois numeros sao iguais.")
        print("Obrigado por usar nosso sistema.")
    if op == 4:
            numero = int(input("Digite um número:   "))
            
            for i in range(1 , 11 ):
                print(f"{numero} x {i} = {numero * i}")
    if op == 5:
            contagem = 10
            while contagem >= 1:
                 print(f"A bomba vai explodir em {contagem}...")
                 contagem -= 1
                 if contagem == 0:
                      print("KABUUUUMMMMMMMMM!!!")
                 
    
    if op == 6:
         print("Fazer questao 6")