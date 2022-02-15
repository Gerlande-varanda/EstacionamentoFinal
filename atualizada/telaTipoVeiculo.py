

import PySimpleGUI as sg
from crudBanco import *
from banco import TipoVeiculo


class TelaTipoVeiculo:
    def __init__(self) -> None:
        pass   


    def tela(self):
        tipo_id = None   
        
        query = TipoVeiculo.select()
            
        
        def atualizaLista():
            lista_tipos = []
            for i in query:            
                lista_tipos.append(i.descricao)           

            return lista_tipos       
        layout = [
            [sg.Text("Tipo Veiculo", size=(10, 1)),sg.Input(key="-TIPO-", do_not_clear=False)],
            [sg.Text("Preco", size=(10, 1)),sg.Input(key="-PRECO-", do_not_clear=False)],  
            [sg.Text('Tipo de Veiculos', size=(15,1), background_color="#fff", text_color="black")], 
            [sg.Listbox(values=atualizaLista(), horizontal_scroll=False,  background_color="#fff", size=(15, 1), key='-LIST-TIPO-', enable_events=True)],          
            [sg.Button("Salvar", key='-SALVAR-'), sg.Button("Editar", key="-EDITAR-") ,sg.Button("Deletar", key="-DELETAR-")]           

        ]
        self.janela = sg.Window("Tipo Veiculo", size=(700, 450), layout=layout, finalize=True)
        # self.janela.set_min_size((450,450))

        while True:
            event, values = self.janela.Read()
            if event == sg.WINDOW_CLOSED or event == "Sair":
                break

            if event == '-SALVAR-':               
                tipo = values['-TIPO-']
                preco = values['-PRECO-']
                desc = tipo.capitalize()

                cadastrado = TipoVeiculo.select().where(TipoVeiculo.descricao == desc)
                if cadastrado:
                    [sg.popup("Tipo de Veiculo ja cadastrado")]

                elif tipo.isnumeric():
                    [sg.popup("Insira apenas caracteres")]
                
                elif tipo == "" or preco == "":
                     [sg.popup("Prencha os campos")]                
                
                else:                                    
                    cadastratarTipoVeiculo(desc, preco)
                    [sg.popup('Cadastrado com sucesso !', text_color="#04BEB3")]

            
            if event == "-LIST-TIPO-":
                tipo = values['-LIST-TIPO-'][0]
                tipo_veiculo = TipoVeiculo.select().where(TipoVeiculo.descricao == tipo).get()
                tipo_id = tipo_veiculo.id
                self.janela['-TIPO-'].update(tipo_veiculo.descricao)
                self.janela['-PRECO-'].update(tipo_veiculo.preco)


            if event == "-EDITAR-":                
                tipo = values['-TIPO-']
                preco = values['-PRECO-']
                atualizarTipo(tipo_id, tipo, preco)
                [sg.popup('Atualizado com sucesso !', text_color="#04BEB3")]
                atualizaLista()

            if event == "-DELETAR-": 
                deleteTipo(tipo_id)               
                [sg.popup('Deletado com sucesso !', text_color="#04BEB3")]
                atualizaLista()


        return self.janela
