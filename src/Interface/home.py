import PySimpleGUI as sg
def home():
    sg.theme("Reddit ")  # please make your windows colorful
    layout_esquerda = [
        [sg.OptionMenu(
            ["None","Mover Mouse","Esperar","Clicar","Apertar Tecla(S)", "Escrever","Scroll"],key="--OPCAO--", pad=(15,(50,0)),text_color="#000080")
        ],
        [sg.OptionMenu(
            ["None","Repetir","Parar"],key="--Repetir--", pad=(15,(5,0)),text_color="#000080")
        ],
        [sg.Image(filename="img/add_button.png",
                 size=(64, 64), pad=(15,(30,0)), enable_events=True, key='add',),
         sg.Image(filename="img/remove.png",
                 size=(0, 0), pad=(5,(30,0)), enable_events=True, key='remove',),
         sg.Image(filename="img/help.png",
                 size=(0, 0), pad=(20,(30,0)), enable_events=True, key='help',),
        ]
    ]
    layout_direita = [
        [sg.Text("ALGORITMO RPA",pad=(40,(0,0)),text_color="#000080")],
        [sg.Multiline(s=(50,10), pad=(0,(0,0)), disabled=True, key="algoritmo", font="arial 8 bold",autoscroll=True,text_color="green", background_color="black")],
        [sg.Text("LOG POSICAO MOUSE",pad=(20,(0,0)),text_color="#000080")],
        [sg.Multiline(s=(50,10), pad=(0,(0,0)), disabled=True,key="log",font="arial 8 bold", text_color="green", background_color="black")],
        [sg.Image(filename="img/play.png",
                 size=(64, 64), pad=(10,(0,0)), enable_events=True, key='play',),
         sg.Image(filename="img/clear.png",
                 size=(64, 64), pad=(5,(0,00)), enable_events=True, key='clear',),
         sg.Image(filename="img/newfile_button.png",
                 size=(64, 64), pad=(5,(0,00)), enable_events=True, key='new')]
    ]
    layout_posicao = [
        [sg.Text("TIME: ",pad=(20,(50,0)),font="verdana 11 bold", text_color="#000080"),sg.Slider((0,10), orientation='h', s=(10,15),pad=(20,(30,0)),text_color="#000080",key="--TIME--")],
        [sg.Text("NOME: ",pad=(20,(20,0)),font="verdana 11 bold", text_color="#000080"),sg.Input("",size=(20,15),key="nome_position",pad=(15,(20,0)),font="arial 10")],
        [sg.Checkbox("Minimizar",pad=(150,(0,0)),font="verdana 8 bold", text_color="#000080",key="minimizar")],
        [sg.Image(filename="img/play_position.png",
                 pad=(20,(30,0)), enable_events=True, key='play_position',),
        sg.Image(filename="img/remove.png",
                 size=(64, 64), pad=(10,(30,0)), enable_events=True, key='remove_position',),
         sg.Image(filename="img/help.png",
                 size=(0, 0), pad=(10,(30,0)), enable_events=True, key='help_position',),
        ],
    ]
    from_config = [
        [sg.TabGroup([[sg.Tab('Instruções',layout_esquerda), sg.Tab('Posição Mouse', layout_posicao)]])],
        ]
    
    layout = [
        [sg.Image("img/Screenshot_1.png",size=(80,80),pad=(250,(0,0)))],
        [sg.Text("SAFELLI",font="verdana 13 bold",pad=(250,(0,10)), text_color="#000080")],
        [sg.HSep(color="#000080")],
        [sg.Col(from_config,element_justification='left', justification='left',pad=(10,(0,0)),size=(250,250)),sg.Col(layout_direita,pad=(30,(0,0)))],
        
    ]
    window = sg.Window('Window Title', layout, size=(600,630),finalize=True, font="verdana 11 bold", grab_anywhere = True,icon="")
    return window