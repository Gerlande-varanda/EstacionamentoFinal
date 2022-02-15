
import PySimpleGUI as sg
from crudBanco import *
from banco import Patio


class TelaPatio:
    def __init__(self) -> None:
        pass

    def tela(self):
        layout = [
            [sg.Text("Descricao" , size=(10,1)), sg.Input(
                key="-DESCRICAO-", do_not_clear=False)],
            [sg.Text("Quant. Vagas", size=(10,1)), sg.Input(
                key="-VAGAS-", do_not_clear=False)],
            [sg.Button("Salvar", key='-SALVAR-')]

        ]
        self.janela = sg.Window("Patio", size=(
            450, 150), layout=layout, finalize=True)
        # self.janela.set_min_size((450,450))

        while True:
            event, values = self.janela.Read()
            if event == sg.WINDOW_CLOSED or event == "Sair":
                break

            if event == '-SALVAR-':
                descricao = values['-DESCRICAO-']
                quantidade = values['-VAGAS-']
                desc = descricao.capitalize()
                cadastrado = Patio.select().where(Patio.descricao == desc)

                if cadastrado:
                    [sg.popup("Patio já cadastrado")]

                elif descricao.isnumeric():
                    [sg.popup("Insira apenas caracteres")]
                
                elif descricao == "" or quantidade == "":
                     [sg.popup("Prencha os campos")]

                else:
                    cadastratarPatio(desc, quantidade)
                    [sg.popup('Cadastrado com sucesso !', text_color="#ffa500")]

        return self.janela
