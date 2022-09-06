from ast import Return
from pymongo import cursor
from pymongo import MongoClient
from datetime import date

from flet import (
    alignment,
    ButtonStyle,
    Checkbox,
    colors,
    Column,
    Container,
    ElevatedButton,
    FilledButton,
    IconButton,
    Icon,
    icons,
    Page,
    Row,
    Tab,
    Tabs,
    Text,
    TextButton,
    TextField,
    UserControl
)

class SGP:
    def __init__(self):
        self.ConectarBD()

    def ConectarBD(self):
        self.CONNECTION_STRING = "mongodb://localhost:27017"
        self.client = MongoClient(self.CONNECTION_STRING)
        self.SGP_db = self.client["SGP_db"]

        print(self.SGP_db.list_collection_names())

        self.movimentacao = self.SGP_db["Movimentacoes"]
        self.unidades = self.SGP_db["Unidades"]

    def DesconectarBD(self):
        self.client.close()

    def inserirPatrimonio(self, plaqueta, descricao, marca='', modelo='', cor='', obs=''):
        print('entrou em inserr patrimonios')
        self.unidades.update_one({"Unidades": {"unidade" : 1}}, {'$set': {"patrimonios": {"plaqueta" : plaqueta}}})
        

    def InserirMovimentacao(self, plaqueta, unidadeOrigem, unidadeDestino, observacao=''):
        dataMov = str(date.today())
        if unidadeDestino != unidadeOrigem and unidadeDestino != 0 and unidadeOrigem != 0:
            self.movimentacao.insert_one({
                "plaqueta" : plaqueta,
                "data" : dataMov, 
                "unidadeOrigem" : unidadeOrigem,
                "unidadeDestino" : unidadeDestino})
            if observacao != '':
                self.movimentacao.update_one({"plaqueta" : plaqueta}, {'$set': {"observacao" : observacao}})

    def ListarMovimentacoes(patrimonio, data):
        movimentacao = ElevatedButton(
            style=ButtonStyle(
                overlay_color=colors.TRANSPARENT,
            ),
            width=300,
            content=Row([
                Text(value='plaqueta:'+ patrimonio),
                Text(value='data:'+ data, color="pink"),
            ]),
            expand=0,
        )
        return Column(controls=[movimentacao])

    def BuscarMovimentacao(self, campo, termo): 
        pesquisa = self.movimentacao.find({campo: termo})
        for i in pesquisa:
            print(i)
        return pesquisa

    def BuscarUnidades(self):
        pesquisa = self.unidades.find({}, {'_id': 0, 'unidade': 1, 'nome': 1, 'local': 1},)
        #print(list(pesquisa))
        return pesquisa

    def BuscarPatrimonios(self, nome):
        pesquisa = self.unidades.find({'nome' : nome}, {'_id': 0, 'unidade': 0, 'nome': 0, 'local': 0, 'atribuicao': 0, 'promotor(a)': 0})
        return pesquisa