from cgitb import text
from distutils.command.build import build
from importlib.resources import contents
from turtle import onclick
from typing import Container
from classes import SGP

from typing import Iterable
from bson import BSON
#from pymongo import MongoClient
#from datetime import date

import flet
from flet import (
    alignment,
    ButtonStyle,
    Checkbox,
    colors,
    Column,
    Container,
    Dropdown,
    dropdown,
    ElevatedButton,
    FilledButton,
    FloatingActionButton,
    IconButton,
    Icon,
    icons,
    padding,
    Page,
    Row,
    Tab,
    Tabs,
    Text,
    theme, 
    TextButton,
    TextField,
    UserControl
)

SGP = SGP()  # cria o objeto SGP

class Interface(UserControl):
    def __init__(self):

        self.dropdownPatrimonios = Dropdown(text_size = 18, expand= 1, hint_text= 'selecione patrimonio')
        
        self.dropdownPromotorias = Dropdown(
            text_size = 18,
            expand= 1,
            hint_text= 'selecione unidade'
        )

        for i in SGP.BuscarUnidades():
            self.AtribuirUnidades(i)
        
        self.AtribuirPatrimonios()

        #self.botoesPatrimonios = Column()
        #for i in SGP.BuscarPatrimonios():
        #    self.AtribuirPatrimonios(i)
        
        self.plaquetaPatrimonio = TextField(label="plaqueta", hint_text="Ex: 123456", expand=False)
        self.descriçãoPatrimonio= TextField(label="Descrição",hint_text="Ex: Desktop", expand=False)
        self.marcaPatrimonio = TextField(label="Marca",hint_text="Ex: Dell", expand=True)
        self.modeloPatrimonio = TextField(label="Modelo",hint_text="Ex: Inspiron", expand=True)
        self.corPatrimonio = TextField(label="Cor",hint_text="Ex: Preto", expand=True)
        self.obsPatrimonio = TextField(label="Observação",hint_text="Ex: ...", expand=False)

        self.pesquisarPatrimonio = TextField(hint_text="Ex: 123456", expand=True)
        self.pesquisarMov = TextField(hint_text="Ex: 24/02/2022", expand=True)

        self.botoesMov = Column()

        self.formularioInserirPatrimonio = Column(
            horizontal_alignment="center",
            controls= [
                Column(spacing=20,
                    controls = [
                        Text(),
                        self.plaquetaPatrimonio,
                        self.descriçãoPatrimonio,
                        Row([
                            self.marcaPatrimonio,
                            self.modeloPatrimonio,
                            self.corPatrimonio,],
                        ),
                        self.obsPatrimonio,
                        Row(
                            alignment="end",
                            controls=
                            [ElevatedButton(
                                style=ButtonStyle(
                                    overlay_color=colors.TRANSPARENT,
                                ),
                                width=300,
                                content=Row(
                                    alignment="center",
                                    controls=
                                    [Text(value='Inserir', size=20)]),
                                expand=0,
                                on_click=self.InserirPatrimonio()
                            )]
                        )
                    ]
                ),
            ],
        ),
        
    
    def InserirPatrimonio(self):
        print('apertaram ein')
        SGP.inserirPatrimonio(
            self.plaquetaPatrimonio.value,
            self.descriçãoPatrimonio.value,
            self.marcaPatrimonio.value,
            self.modeloPatrimonio.value,
            self.corPatrimonio.value,
            self.obsPatrimonio.value
        )

    def AtribuirUnidades(self, info):
        self.dropdownPromotorias.options.append(dropdown.Option(str(info['nome'])))

    def AtribuirPatrimonios(self):
        nomeUnidade = self.dropdownPromotorias.value
        for i in SGP.BuscarPatrimonios(nomeUnidade):
            info = i
            for j in info:
                self.dropdownPatrimonios.options.append(dropdown.Option(j))
        

    def ExibirTitulo(self):
        return Column([
            Text(value="Sistema de Controle de Patrimônio", style="headlineLarge"),
            Text(value=""), ])

    def ExibirAbas(self):
        return Tabs(
            selected_index=1,
            tabs=[
                Tab(text="Transferir patrimônio",
                    icon=icons.DOUBLE_ARROW,
                    content=Column(controls=[
                        Text(value=""),
                        Row(
                            alignment="spaceBetween",
                            controls=[
                                self.dropdownPromotorias,
                                self.dropdownPatrimonios,
                            ]
                        )
                    ])
                ),
                Tab(text="Inserir patrimônio",
                    icon=icons.ARROW_DROP_DOWN,
                    content= Column(self.formularioInserirPatrimonio,)
                    ),
                Tab(text="Consultar patrimônio",
                    icon=icons.SEARCH,
                    content=Column(
                        horizontal_alignment="center",
                        controls=[
                            Text(),
                            Row([
                                self.pesquisarPatrimonio,
                                FloatingActionButton(icon=icons.SEARCH),
                            ])
                        ]
                    )
                ),
                Tab(text="Consultar movimentações",
                    icon=icons.SEARCH,
                    content=Column(
                        horizontal_alignment="center",
                        controls=[
                            Text(),
                            Row([
                                self.pesquisarMov,
                                FloatingActionButton(icon=icons.SEARCH, on_click= self.pesquisarMovimentacao()),
                            ])
                        ]
                    )
                )
            ]
        )

    def pesquisarMovimentacao(self):
        for i in SGP.BuscarMovimentacao('plaqueta', self.pesquisarMov.value):
            self.botoesUnidades.controls.append(SGP.ListarMovimentacoes(i['patrimonio'], i['data']))

        '''  
        for i in SGP.BuscarMovimentacao('data', self.pesquisarMov.value):

        for i in SGP.BuscarMovimentacao('unidadeOrigem', self.pesquisarMov.value):

        for i in SGP.BuscarMovimentacao('unidadeDestino', self.pesquisarMov.value):
        '''


def main(page: Page):
    page.title = "Sistema de Controle de Patrimônio"
    page.horizontal_alignment = "center"
    page.theme_mode = 'dark' #'light'
    interface = Interface()
    page.update()

    conteudo = Column(
        width=1100,
        horizontal_alignment="center",
        controls=[
            interface.ExibirTitulo(),
            interface.ExibirAbas(),
        ])

    page.add(conteudo)


flet.app(target=main)
