from email.policy import default
from peewee import *
from datetime import datetime

banco = SqliteDatabase('estacionamento.db', pragmas={'foreign_keys': 1})

class BaseModel(Model):
    
    class Meta:
        database = banco


class TipoVeiculo(BaseModel):
    descricao = CharField()
    preco = FloatField()
       

class Patio(BaseModel):
    descricao = CharField()
    quantidade_vagas = IntegerField()


class RegistroEntradaSaida(BaseModel):
    patio = ForeignKeyField(Patio, backref='registros')
    placa = CharField()
    tipoVeiculo = ForeignKeyField(TipoVeiculo, backref='registros')
    entrada = DateTimeField(default=0.0)
    saida = DateField(default=0.0)
    valor_pagar = FloatField(default=0.0)
    situacao = CharField()


    

banco.create_tables([TipoVeiculo, Patio, RegistroEntradaSaida])
        
        
    