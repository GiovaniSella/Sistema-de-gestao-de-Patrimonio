import flet
from flet import (
    alignment,
    Checkbox,
    Column,
    Container,
    Dropdown,
    ElevatedButton,
    FloatingActionButton,
    Icon,
    IconButton,
    OutlinedButton,
    padding,
    Page,
    Row,
    Tab,
    Tabs,
    Text,
    TextField,
    UserControl,
    colors,
    icons,
    Dropdown,
    dropdown
)

def main(page: Page):
    page.title = "Sistema de Controle de Patrimônio"
    page.horizontal_alignment = "center"
    
    tabs = Tabs(
        width=1100,
        selected_index=1,
        animation_duration=300,
        tabs=[
            Tab(
                text="Transferir patrimônio",
                icon=icons.DOUBLE_ARROW,
                content=Column(
                    alignment="center",
                    controls=[]
                )
            ),
            Tab(
                text="Inserir patrimônio",
                icon=icons.ARROW_DROP_DOWN,
                content=Column(
                    horizontal_alignment="center",
                    controls= [
                        Column(spacing=20,
                            controls = [
                                Text(),
                                TextField(label="plaqueta", hint_text="Ex: 123456", expand=False),
                                TextField(label="Descrição",hint_text="Ex: Desktop", expand=False),
                                Row([
                                    TextField(label="Marca",hint_text="Ex: Dell", expand=True),
                                    TextField(label="Modelo",hint_text="Ex: Inspiron", expand=True),
                                    TextField(label="Cor",hint_text="Ex: Preto", expand=True),],
                                ),
                                TextField(label="Observação",hint_text="Ex: ...", expand=False),
                                Row(
                                    alignment="end",
                                    controls=[
                                        ElevatedButton(
                                            content=Container(
                                                content=Row([
                                                    Text(value="Incluir", size=20),
                                                ]),
                                                padding=padding.only(50, 10, 50, 10)
                                            ),
                                            on_click=InserirPatrimonio
                                        ),
                                    ]
                                )
                            ]
                        ),
                    ],
                ),
            ),
            Tab(
                text="Consultar patrimônio",
                icon=icons.SEARCH,
                content=Column(
                    horizontal_alignment="center",
                    controls=[
                        Text(),
                        Row([
                            TextField(hint_text="Ex: 123456", expand=True),
                            FloatingActionButton(icon=icons.SEARCH, on_click=pesquisarTermo),
                        ])
                    ]
                )
            ),
            Tab(
                text="Consultar movimentações",
                icon=icons.SEARCH,
                content=Column(
                    horizontal_alignment="center",
                    controls=[
                        Text(),
                        Row([
                            TextField(hint_text="Ex: 123456", expand=True),
                            FloatingActionButton(icon=icons.SEARCH, on_click=pesquisarTermo),
                        ])
                    ]
                ),
            ),
        ],
        expand= False,
    )
    

    conteudo = Column(
        width=1100,
        controls=[Column([
            Text(value="Sistema de Controle de Patrimônio", style="headlineLarge"),
            Text(value=""),
            tabs,
            ],
        horizontal_alignment="center",)
        ]
    )
    
    page.add(conteudo)

def pesquisarTermo(e):
    print('o termo pesquisado é:')

def InserirPatrimonio(e):
    print('Botão incluir patrimonio clicado')


flet.app(target=main)