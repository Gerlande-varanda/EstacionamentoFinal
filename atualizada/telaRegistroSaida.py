
import PySimpleGUI as sg
from crudBanco import *
from banco import Patio, RegistroEntradaSaida
import sys


class TelaRegitroSaida:
    def __init__(self) -> None:
        pass

    def tela(self):
        layout = [
            [sg.Text("Buscar Placa"), sg.Input(
                key="-PLACA-", do_not_clear=False), sg.Button("-BUSCAR-", key='-BUSCAR-')],
            # [sg.Button("Salvar", key='-SALVAR-')]



        ]
        self.janela = sg.Window("Registro De Saida", size=(
            550, 150), layout=layout, finalize=True)
        # self.janela.set_min_size((450,450))

        while True:
            event, values = self.janela.Read()
            if event == sg.WINDOW_CLOSED or event == "Sair":
                break

            if event == "-BUSCAR-":
                placa = values['-PLACA-']

                query = RegistroEntradaSaida.select().where(
                    RegistroEntradaSaida.placa == placa).get()

                if query:
                    titulo = f"Ticket: {query.id}"
                    patio = query.patio.descricao
                    placa = query.placa
                    tipoVeiculo = query.tipoVeiculo.descricao
                    entrada = query.entrada
                    saida = query.saida
                    valor_pagar = query.valor_pagar

                    def Mypopup(title, text):
                        window = sg.Window(title,
                                           [[sg.Text(text)],
                                            [sg.Text("Placa: "),
                                             sg.Text(placa)],
                                               [sg.Text("Tipo: "), sg.Text(
                                                   tipoVeiculo)],
                                               [sg.Text("Entrada: "),
                                                sg.Text(entrada)],
                                               # [sg.DropDown(values, key='-DROP-')],
                                               [sg.Button(
                                                   "Imprimir", key="-SAIDA-")]
                                            ])

                        while True:
                            event, values = window.read()

                            if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == 'Exit') and sg.popup_yes_no('Do you really want to exit?') == 'Yes':
                                break

                            if event == "-SAIDA-":
                                cadastrarSaida(placa)
                                break

                        window.close()

                    def PopupDropDown(title, text):
                        window = sg.Window(title,
                                           [[sg.Text(text)],
                                            [sg.Text("Total: "),
                                             sg.Text(valor_pagar)],
                                               [sg.Button(
                                                   "Registrar Saida", key="-SAIDA-")]
                                            ])
                        event, values = window.read()

                        if event == "-SAIDA-":
                            cadastrarSaida(placa)
                            Mypopup(titulo, titulo)

                        elif event == "-EXIT-":
                            sys.exit()


# -----------------------  Calling your PopupDropDown function -----------------------

                    # values = ['choice {}'.format(x) for x in range(30)]
                    print(PopupDropDown(titulo, titulo))

            if event == '-SALVAR-':
                descricao = values['-DESCRICAO-']
                quantidade = values['-VAGAS-']
                cadastratarPatio(descricao, quantidade)
                [sg.popup('Cadastrado com sucesso !', text_color="#00ff00")]

        return self.janela
