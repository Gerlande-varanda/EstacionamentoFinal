
import PySimpleGUI as sg
from crudBanco import *


class Registro:
    def __init__(self) -> None:
        pass

    def tela(self):
        tipo = listaTipos()
        lista_tipos = []
        for i in tipo:            
            lista_tipos.append(i.descricao)
        
        layout = [
            [sg.Text("Tipo Veiculo")],
            [sg.Listbox(values=lista_tipos, size=(50, 2), key='-LIST-TIPO-', enable_events=True)],              
            [sg.Text("Placa"), sg.Input(key="-PLACA-", do_not_clear=False)], 
            [sg.Button("Salvar", key='-SALVAR-')]           
         


        ]
        self.janela = sg.Window("Tela Principal", size=(450, 150), layout=layout, finalize=True)
        # self.janela.set_min_size((450,450))

        while True:
            event, values = self.janela.Read()
            if event == sg.WINDOW_CLOSED or event == "Sair":
                break

            if event == '-SALVAR-':
                tipo = values['-LIST-TIPO-'][0]
                query = TipoVeiculo.select(TipoVeiculo.id).where(TipoVeiculo.descricao == tipo)
       
                placa = values['-PLACA-']
                pesquisa = RegistroEntradaSaida.select().where(RegistroEntradaSaida.placa == placa)
                pesquisa2 = RegistroEntradaSaida.select().where(RegistroEntradaSaida.situacao == "Aberta")
                if pesquisa:
                    if pesquisa2:
                        [sg.popup('O veiculo ainda esta no estacionamento!', text_color="#ffa500")]

                elif placa == "":
                     [sg.popup("Prencha os campos")]   

                else:
                    cadastrarEntrada(placa, query)
                    [sg.popup('Cadastrado com sucesso !', text_color="#ffa500")]





        return self.janela
