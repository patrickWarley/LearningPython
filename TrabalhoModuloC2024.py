def questao1():

    print("Sistema desenvolvido por Patrick Warley Telles da silva")
    
    valorBase= float(input("Informe o valor Base do plano: R$ "))
    idade= int(input("Informe a idade do Cliente:"))
    porcentagem = 0

    if(idade >=0 and idade<19):porcentagem=1
    elif(idade >= 19 and idade <29 ): porcentagem = 150/100
    elif(idade >= 29 and idade <39 ): porcentagem = 225/100
    elif(idade >= 39 and idade <49 ): porcentagem = 240/100
    elif(idade >= 49 and idade <59 ): porcentagem = 350/100
    else: porcentagem = 600/100
    
    valorMensal =valorBase*porcentagem

    print("O valor mensal do plano é de: R$ %.2f"%(valorMensal))

def questao2():
    
    tamanhosValidos = ('P', 'M', 'G')
    saboresValidos = ('PS', 'PD')
 
    valores = {
        "PS":{
            "P":30,
            "M":45,
            "G":60
        },
        "PD":{
            "P":34,
            "M":48,
            "G":66
        }
    }

    print("--- Bem-vindo a Pizzaria do Patrick Warley Telles da silva ---")
    print("---------------------------Cardápio---------------------------")
    print("----|  Tamanho  |  Pizza Salgada(PS)  |  Pizza Doce(PD)  |----")
    for item in tamanhosValidos:
        print(
            "----|     {}     |       R$ {}.00      |     R$ {}.00     |----"
                .format(item, valores["PS"][item], valores["PD"][item])
        )
    print("--------------------------------------------------------------")
    print("\n")
   
    sabor=""
    tamanho=""
    valorTotal=0

    while(True):
        
        #Eu so peço para o cliente digitar o sabor se o sabor nao tiver sido escolhido ainda
        if(sabor == ""):
            sabor = input('Entre com o sabor desejado (PS/PD): ')
            if sabor not in saboresValidos:
                print('Sabor inválido. Tente novamente\n')
                sabor=""
                continue
        
        if(tamanho == ""):
            tamanho=input('Entre com o tamanho desejado(P/M/G): ')
            if tamanho not in tamanhosValidos:
                print('Tamanho inválido. Tente novamente\n')
                tamanho=""
                continue
        
        #O calculo do valor totalPoderia ser feito da sequinte forma
        #valorTotal += valores[sabor][tamanho]
        
        if(sabor == "PS"):
            if(tamanho == "P"):
                valorTotal+=30
            elif(tamanho == "M"):
                valorTotal+=45
            else:
                valorTotal+=60

        if(sabor == "PD"):
            if(tamanho == "P"):
                valorTotal+=34
            elif(tamanho == "M"):
                valorTotal+=48
            else:
               valorTotal+=66

        print("Você pediu uma Pizza {} no Tamanho {}: R$ {}.00".format(("Salgada" if sabor=="PS" else "Doce"), tamanho, valores[sabor][tamanho]))

        realizarPedido = input("\nDeseja pedir mais alguma coisa? (S/N): ")
        if(realizarPedido == "S"):
            sabor = ""
            tamanho =""
        else: break
    
    print("\nO valor total a ser pago: R$ %.2f"%valorTotal)


def questao3():
    print("Bem-vindos a Madeireira do Lenhador Patrick Warley Telles da Silva")
    
    def escolha_tipo(): 
        tipo={
            "PIN":("Tora de pinho", 150.40),
            "PER":("Tora de peroba", 170.20),
            "MOG":("Tora de Mogno", 190.90),
            "IPE":("Tora de Ipê", 210.10),
            "IMB":("Tora de Imbuia", 220.70)
        }
        escolha=""

        while(True):
            print("\nEntre com o tipo de madeira desejado")
            for madeira in tipo:
                print("{} - {}".format(madeira, tipo[madeira][0]))
            escolha = input(">>")
            
            if escolha not in tipo:
                print("Escolha inválida, entre com o modelo novamente.")
            else: break;
        return tipo[escolha][1]

    def qtd_toras():
        desconto = 0
        qtd = 0
        while(True):
            try:
                qtd= int(input("\nEntre com a quantidade de toras (m³): "))
                #Quando a quantidade for menor que 100 o desconto e zero como ja esta definido
                #eu so preciso dar break
                if(qtd<100): break
                if(qtd>=100 and qtd<500): 
                    desconto = 4/100
                    break
                elif(qtd>=500 and qtd<1000): 
                    desconto = 9/100
                    break
                elif(qtd>=1000 and qtd<=2000): 
                    desconto = 16/100
                    break
                else: print("Não aceitamos pedidos com essa quantidade de toras.\nPor favor entre com a quantidade novamente.")
            except ValueError:
                print("Por favor digite uma quantidade valida de toras.")
        return qtd, desconto

    def transporte():
        tipo={
            1:("Transporte Rodoviário", 1000),
            2:("Transporte Ferroviário",2000),
            3:("Transporte Hidroviário",2500)
        }
        escolha=0
        while(True):
            print("\nEscolha o tipo de Transporte:")
            for item in tipo:
                print("{} - {} - {}".format(item,tipo[item][0], tipo[item][1]))
            escolha = int(input(">>"))

            if escolha in tipo:
                break
        return tipo[escolha][1]

    valorMadeira = escolha_tipo()
    quantidadeToras, valorDesconto = qtd_toras()
    tipoTransporte = transporte()

    total = ((valorMadeira*quantidadeToras)*(1-valorDesconto))+tipoTransporte

    print("Total: R$ %.2f"%total)

def questao4():
    print('Bem vindos a lista de contatos do Patrick Warley Telles da Silva')

    lista_contatos=[]
    id_global = 4953704
    
    def cadastrar_contato(id):
        contato={}
        print("Id do Contato: {}".format(id))
        contato["nome"]=input("Por favor entre com o nome do Contato: ")
        contato["atividade"]=input("Por favor entre com a Atividade do Contato: ")
        contato["telefone"]=input("Por favor entre com o telefone do Contato: ")
        contato["id"]=id
        
        lista_contatos.append(contato.copy())
    
    def imprimir_contato(contato):
        print("\n")
        for key in contato:
            print("{}: {}".format(key, contato[key]))
        print("\n")

    def consultar_contatos():
        opcoes ={
            1:"Consultar Todos os Contatos",
            2:"Consultar Contato por Id",
            3:"Consultar Contato(s) por Atividade",
            4:"Retornar"
        }
        
        while(True):
            print("\n---------------------------------------")
            print("--------MENU CONSULTAR CONTATOS--------")
            print("Escolha a opção desejada:")
            for item in opcoes:
                print("{} - {}".format(item, opcoes[item]))
            opcao = int(input(">>"))
            
            if(opcao == 1):
                print("----------------------")
                for contato in lista_contatos:
                    imprimir_contato(contato)
                print("----------------------")
            elif(opcao == 2):
                idBuscaContato = int(input("Digite o Id do contato: "))
                print("----------------------")
                for contato in lista_contatos:
                    if(contato["id"] == idBuscaContato):
                        imprimir_contato(contato)
                print("----------------------")
            elif(opcao == 3):
                atividadeContato = input("Digite a Atividade do(s) Contato(s): ")
                print("----------------------")
                for contato in lista_contatos:
                    if(contato["atividade"] == atividadeContato):imprimir_contato(contato)
                print("----------------------")
            elif(opcao == 4):return
            else:
                print("Opção inválida.")
    
    def remover_contato():
        while(True):
            print("\n---------------------------------------")
            print("--------MENU REMOVER CONTATO----------")

            idContato = int(input("Digite o id do contato a ser removido: "))
            success = False
            for contato in lista_contatos:
                if contato["id"] == idContato:
                    success = True
                    lista_contatos.remove(contato)
            if(success):
                print("Contato removido com sucesso!")
                return
            else: print("Id inválido")
    
    opcoes ={
            1:"Cadastrar Contato",
            2:"Consultar Contato",
            3:"Remover Contato",
            4:"Encerrar Programa"
        }
    while(True):
        print("\n---------------------------------------")
        print("--------MENU  PRINCIPAL----------")
        print("Escolha a opção desejada:")
        for item in opcoes:
            print("{} - {}".format(item, opcoes[item]))
        opcao = int(input(">>"))
            
        if(opcao == 1):
            id_global+=1
            cadastrar_contato(id_global)
        elif(opcao == 2):
            consultar_contatos()
        elif(opcao == 3):
            remover_contato()
        elif(opcao == 4):return
        else:
            print("Opção inválida.")

questao4()




