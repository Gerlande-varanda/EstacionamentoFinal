
import PySimpleGUI as sg
from telaPatio import TelaPatio
from telaRegistro import Registro
from telaRegistroSaida import TelaRegitroSaida
from telaTipoVeiculo import TelaTipoVeiculo

# from telaRegistroSaida import Saida


class TelaPrincipal():
    def __init__(self) -> None:
        self.entrada = Registro()

    def principal(self):

        menu = [
            ['&Cadastro', ['&Tipo Veiculo', 'Patio']],
            ['&Registro', ['&Entrada', 'Saida']],
        ]

        layout = [
            [sg.Menu(menu, tearoff=False, pad=(
                200, 1), background_color="#fff")],
        ]

        self.janela = sg.Window("Tela Principal EG Estacionamento Rotativo!", size=(
            960, 540), layout=layout, finalize=True)
        self.janela.set_min_size((960, 540))

        return self.janela


tela = TelaPrincipal()
entrada = Registro()
tipo_veiculo = TelaTipoVeiculo()
janela_patio = TelaPatio()
saida = TelaRegitroSaida()


janelaPrincipal, janelaEntrada, janelaSaida, janelaTipo, telaPatio = tela.principal(), None, None, None, None

while True:

    window, event, values = sg.read_all_windows()

    if window == janelaPrincipal and event == sg.WIN_CLOSED:
        break

    elif window == janelaPrincipal and event == "Tipo Veiculo":
        janelaTipo = tipo_veiculo.tela()

    elif window == janelaPrincipal and event == "Patio":
        telaPatio = janela_patio.tela()

    elif window == janelaPrincipal and event == "Entrada":
        janelaEntrada = entrada.tela()

    elif window == janelaPrincipal and event == "Saida":
        janelaSaida = saida.tela()
