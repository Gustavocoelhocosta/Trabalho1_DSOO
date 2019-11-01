import PySimpleGUI as sg


layout = [
            [sg.Text('Incluir Veículo')],
            [sg.Text('Placa', size=(15,1)), sg.InputText('PLACA')],
            [sg.Text('Modelo', size=(15,1)), sg.InputText('MODELO')],
            [sg.Text('Marca', size=(15, 1)), sg.InputText('MARCA')],
            [sg.Text('Ano de fabricação', size=(15, 1)), sg.InputText('ANO DE FABRICAÇÃO')],
            [sg.Text('Quilometragem atual', size=(15, 1)), sg.InputText('QUILOMETRAGEM ATUAL')],
]