lista = []

while (True):
    opcao = input("Digite [i]nserir, [a]pagar, [l]istar ")
    opcao_tratada = opcao.upper()
    if opcao_tratada == 'I':
        dado = input("Digite o nome da compra: ")
        lista.append(dado)
    elif opcao_tratada == 'A':
        if len(lista) == 0:
            print("Não há nenhum objeto para apagar")
        else:
            for item in enumerate(lista):
                print(item)
            dado = input("Digite o indice que deseja apagar: ")
            try:
                dado_tratado = int(dado)
                del lista[dado_tratado]
                print("Item apagado")
            #Exceção de tipo de dado
            except ValueError:
                print("Por favor, digite um número inteiro")
            #Exceção de indice inexistente na lista
            except IndexError:
                print("Por favor, digite um indice válido")
            #Exceção qualquer 
            except Exception:
                print("Erro desconhecido")
            
    elif opcao_tratada == 'L':
        if len(lista) == 0:
            print("Não há nenhum objeto na lista")
        else:
            print(lista)


    else:
        print("Opcao inválida")
        continue
