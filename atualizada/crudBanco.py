
from pydoc import describe
from banco import *
from datetime import datetime, timedelta, timezone, date

from banco import RegistroEntradaSaida, TipoVeiculo



# Criando crud
def cadastratarTipoVeiculo(descricao, preco): 
    # Verificar se o tipo de tipo de veiculo já foi inserido
    desc = descricao.capitalize()
    cadastrado = TipoVeiculo.select().where(TipoVeiculo.descricao == desc)
    if cadastrado:
        print('Tipo veiculo ja cadastrado')

    else:
        TipoVeiculo.create(
            descricao = desc,
            preco = preco
        )
        print("Tipo de Veiculo Cadastrado com sucesso!")
    
   
def listaTipos():
    query = TipoVeiculo.select()
    return query

def getTipoId(id):
    tipo = TipoVeiculo.get(TipoVeiculo.id == id)
    return tipo
    
def atualizarTipo(id, descricao, preco):
    
    query = (TipoVeiculo.update(descricao = descricao, preco = preco).where(TipoVeiculo.id == id))
    query.execute()

def deleteTipo(id):
    TipoVeiculo.delete().where(TipoVeiculo.id == id).execute()
    print('Deletado com sucesso')



## Cliente
# def cadastratarCliente(nome):
#     try:
#         Cliente.create(
#         nome = nome
#         )

#         print(sucesso)

#     except Error as e:
#         print(e)

# def listaClientes():
#     query = Cliente.select()
#     return query

# def getClienteId(id):
#     cliente = Cliente.get(Cliente.id == id)
#     return cliente
    
# def atualizarCliente(id, nome):
#     query = (Cliente.update(nome = nome).where(Cliente.id == id))
#     query.execute()

# def deleteTipo(id):
#     Cliente.delete().where(Cliente.id == id).execute()
#     print('Deletado com sucesso')
    

### Patio
def cadastratarPatio(descricao, quantidade):
    try:
        Patio.create(
        descricao = descricao,
        quantidade_vagas = quantidade
        )

    except Exception as e:
        print(e)

def listaPatio():
    query = Patio.select()
    return query

def getPatioId(id):
    patio = Patio.get(Patio.id == id)
    return patio
    
def atualizarPatio(id, nome):
    query = (Patio.update(nome = nome).where(Patio.id == id))
    query.execute()

def deletePatio(id):
    Patio.delete().where(Patio.id == id).execute()
    print('Deletado com sucesso')


### Registro de Entrada


def cadastrarEntrada(placa, tipo_id):    
    tipo = TipoVeiculo.get(TipoVeiculo.id == tipo_id)
    RegistroEntradaSaida.create(
    patio = 1,
    entrada = datetime.now(),
    placa = placa,
    tipoVeiculo_id = tipo,
    situacao = "Aberta"
    )

    patio = Patio.get()
    vaga = patio.quantidade_vagas - 1
    patio.quantidade_vagas = vaga
    patio.save()
    
def cadastrarSaida(placa):
    # Buscar Pela Placa 
    registro = RegistroEntradaSaida.select().where(RegistroEntradaSaida.placa == placa)

    f = '%d/%m/%Y %H:%M'

    for r in registro:
        entrada = r.entrada
        id = r.id
        preco_por_veiculo = r.tipoVeiculo.preco
        print("Id", id)
        print(type(entrada))
        saida = datetime.now()
        print(type(saida))
        result = saida - entrada
        print(type(result))
        print(result)
        dia = result.days
        hora = result.seconds //3600
        # minutos = (result.seconds //60) % 60
        total_horas = (dia * 24) + hora 
        print("Dias", dia)
        print("Horas", hora)
           
        print("Total", total_horas)   
       

        if total_horas > 1:
            registroSaida = RegistroEntradaSaida.select().where(RegistroEntradaSaida.id == id).get()
            
            valor_a_pagar = total_horas * preco_por_veiculo
            valorpagar = valor_a_pagar
            registroSaida.saida = datetime.now().strftime('%d/%m/%Y %H:%M')
            registroSaida.valor_pagar = valorpagar
            registroSaida.situacao = "Fechada"
            registroSaida.save()
            patio = Patio.select().where(Patio.id == 1).get()
            vaga = patio.quantidade_vagas + 1
            patio.quantidade_vagas = vaga
            patio.save()
        
        else:
            registroSaida = RegistroEntradaSaida.select().where(RegistroEntradaSaida.id == id).get()
            registroSaida.saida = datetime.now().strftime('%d/%m/%Y %H:%M')
            valor_a_pagar = total_horas * preco_por_veiculo
            registroSaida.valor_pagar = valor_a_pagar
            registroSaida.situacao = "Fechada"
            registroSaida.save()

            patio = Patio.select().where(Patio.id == 1).get()
            if patio.quantidade_vagas <= 20:
                vaga = patio.quantidade_vagas + 1
                patio.quantidade_vagas = vaga
                patio.save() 
            




def listaPatio():
    query = Patio.select()
    return query

def getPatioId(id):
    patio = Patio.get(Patio.id == id)
    return patio
    
def atualizarPatio(id, nome):
    query = (Patio.update(nome = nome).where(Patio.id == id))
    query.execute()

def deletePatio(id):
    Patio.delete().where(Patio.id == id).execute()
    print('Deletado com sucesso')

def listarRegistros():
    regitros = RegistroEntradaSaida.select()
    for r in regitros:
        print(r.placa)

def listarSituacao(situcao):
    situcao = RegistroEntradaSaida.select().where(RegistroEntradaSaida.situacao == situcao)
    for s in situcao:
        print(s.situacao)



    
# def tipoGetId(id):
#     TipoVeiculo.
# def cadastrar_veiculo():
#     try:
#         nome_cli = input('entre com o nome do cliente : ')
#         tipo_veic = input('tipo do veiculo : ')
#         modelo_veic = input("entre com o modelo do veiculo : ")
#         cor_veic = input('entre cor a cor do veiculo : ')
#         placa_veic = input('entre com a placa do veiculo : ')
#         Veiculo.create(nome_cliente = nome_cli, tipo_veiculo=tipo_veic, modelo_veiculo=modelo_veic, cor_veiculo=cor_veic, placa_veiculo=placa_veic)
#         print('entrada de veiculo inserida no sistema')
#     except peewee.OperationalError:
#         print('falha na operação!!!')
      
# def consultar_placa():
#     print('consultar veiculo por placa')
#     print('8 consultar veiculo.')
#     print('9 sair da cnsulta.')
#     opc = int(input('escolha 8 para consultar ou 9 para sair : '))
#     if(opc == 8):
#         placa = input('digite o numero da placa do veiculo : ')
#         res = Veiculo.select().where(Veiculo.placa_veiculo == placa).get()
#         print('-----------------------------------')
#         print('veiculo modelo {}\nproprietario {}'.format(res.modelo_veiculo, res.nome_cliente))
#         print('-----------------------------------')    
#     elif(opc == 9):
#         Break  
#     else:    
#         print('veiculo não encontrado !!')
        
        

     
# def Menu():
    
#     while True:
#         print('1 CADASTRAR VEICULOS. ')
#         print('2 SAIDA DE VEICULOS. ')
#         print('3 CONSULTAR VEICULOS NO PATIO. ')
#         print('5 sair do sistema')
#         opc = int(input("escolha uma opção : "))
        
#         if(opc == 1):
#             cadastrar_veiculo()
#         elif(opc == 2):
#             pass
#         elif(opc == 3):
#             consultar_placa() 
#         elif(opc == 5):
#             print("finalizando o sistema obg !!!")
#             break
        
        
# Menu()
 ### TESTADOS
# patio = cadastratarPatio("Principal", 20)
# cadastratarTipoVeiculo('moto', 3.00)
# cadastratarTipoVeiculo('Carro', 5.00)
# cadastrarEntrada("NIX 7885", 2)

# listarRegistros()

# listarSituacao('Aberta')
    # deleteTipo(2)
    # atualizarTipo(2, "carroça", 50.00)
    # valor = getTipoId(2)

    # print(valor.descricao)



# cadastrarSaida("NIX 999")

query = TipoVeiculo.select()

lista = []

for i in query:
    lista.append(i.descricao)
    lista.append(i.preco)
    
print(lista)
print(query)
print(type(query))



