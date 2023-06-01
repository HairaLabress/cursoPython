lista = []

while (True):
    
    #PRIMEIRO DÍGITO
    cpf = input("Digite seu CPF(somente números): ")
    #verificar que não foi digitado nenhum caractere além de número
    try:
        cpf_formatado = int(cpf)
    except ValueError:
        print("Digite apenas números")
        continue
    except Exception:
        print("Erro dsconhecido")
        continue
    
    #transformando em str para poder dividir
    cpf_formatado = str(cpf)
    
    #transformando em lista de inteiros
    lista = [int(digito) for digito in str(cpf_formatado)]
    lista_inteiro = list(map(int, lista))
    
    #print(lista_inteiro)
    #calculo de multiplicação e soma do cpf
    coeficiente = 10
    calculo1 = 0
    for indice, digito in enumerate(lista_inteiro):
        if indice > 8:
            #print("Saiu do for")
            break
        calculo1 += (digito * coeficiente) 
        coeficiente -=  1
        
    print("O valor final da soma é:", calculo1)
    
    #calculo da multiplicação e resto
    # % divide e e dá como resultado o resto
    calculo2 = (calculo1 * 10) % 11
    print("O valor final é:", calculo2)
   
    #condição
    if calculo2 <= 9:
        print("O valor do primeiro digíto é: ", calculo2)
    else:
        print("O valor do primeiro dígito é 0")
        
    
    #SEGUNDO DÍGITO
    indice = 0
    coeficiente2 = 11
    calculo_2d_1 = 0
    for indice, digito in enumerate(lista_inteiro):
        if indice > 9:
            #print("Saiu do for, indice:", indice)
            break
        calculo_2d_1 += (digito * coeficiente2)
        #print(calculo_2d_1)
        coeficiente2 -=  1
        #print(calculo1)
        
    print("O valor final da soma é:", calculo_2d_1)
    
    #calculo da multiplicação e resto
    # % divide e e dá como resultado o resto
    calculo_2d_2 = (calculo_2d_1 * 10) % 11
    print("O valor final é:", calculo_2d_2)
   
    #condição
    if calculo2 <= 9:
        print("O valor do primeiro digíto é: ", calculo_2d_2)
    else:
        print("O valor do primeiro dígito é 0")
