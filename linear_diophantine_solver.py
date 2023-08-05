def testa(a,b,c,valor1,valor2):
    if valor1*a + valor2*b == c:
        return(valor1,valor2)
    elif valor2*a + valor1*b == c:
        return (valor2, valor1)
    else:
        print('Algo deu errado!')
        return(0,0)

def mais_solucoes(x,y,a,b):
    solucoes=[]

    num=5
    for i in range(1,num):
        solucao=(int(x+b*i),int(y-a*i))
        solucoes.append(solucao)

    return solucoes

def mdc(a,b):
    if a==0:
        return b
    elif b==0:
        return a
    else:
        if abs(a)>=abs(b):
            menor=b
            maior=a
        else:
            menor=a
            maior=b

        resto= maior%menor
        return mdc(menor,resto)

lista_m=[1,0]
lista_n =[0,1]
lista_quociente=[]
lista_resto=[]

def bezout(a,b):

    if a==0 or b==0:

        i=0

        for resto in lista_resto:

            m=  lista_m[i]- lista_quociente[i]*lista_m[i+1]
            lista_m.append(m)

            n = lista_n[i]- lista_quociente[i]*lista_n[i+1]
            lista_n.append(n)

            i+=1

            if resto==0:
                return lista_m[i],lista_n[i]

    else:
        if a>=b:
            menor=b
            maior=a
        else:
            menor=a
            maior=b

        resto= maior%menor
        quociente = int(maior/menor)


        lista_resto.append(resto)
        lista_quociente.append(quociente)

        return bezout(menor,resto)

def main():

    print("Obs. apenas equações diofantinas lineares com duas variáveis são aceitas")
    equacao = input("\nEscreva a equação: ").split('=')
    c = int(equacao[1].strip())
    coeficientes = equacao[0].split('+')

    for i in range(2):
        valor=''
        for char in coeficientes[i]:
            if char.isdigit():
                valor+=char
            elif char!=' ':
                variavel=char
        valor=int(valor)
        if i==0:
            variavel1= variavel
            a=valor
        else:
            variavel2 = variavel
            b=valor

    max_div= mdc(a,b)

    a_novo=a/max_div
    b_novo=b/max_div
    c_novo= c/max_div

    print(f'mdc({a},{b})= {max_div} ')
    if c % max_div == 0:
        print(f'A equação possui soluções inteiras, pois {c} é divisível por mdc({a},{b})')
        print(f'\nSolução canônica:')
        valor1, valor2= bezout(a_novo,b_novo)
        valor1= int(c_novo* valor1)
        valor2= int(c_novo * valor2)

        valor1,valor2= testa(a,b,c,valor1,valor2)

        print(f'{variavel1}= {valor1}\n{variavel2}= {valor2}')
        print(f'\nOutras soluções possíveis:')
        solucoes=mais_solucoes(valor1,valor2,a_novo,b_novo)
        for solucao in solucoes:
            valor1,valor2=solucao
            print(f'{valor1,valor2}')

    else:
        print(f'A equação não possui soluções inteiras, pois {c} não é divisível por mdc({a},{b})')


if __name__ == '__main__':
    main()