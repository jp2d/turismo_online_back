from sqlalchemy import Column, String, Integer, DateTime, Float
from datetime import datetime
from typing import Union
from  model import Base

import random
import string


class Produto(Base):
    __tablename__ = 'produto'

    id = Column(Integer, primary_key = True)
    codigo = Column(String(10), unique = True)
    nome = Column(String(140), unique = True)
    tipo = Column(String(100))
    valor = Column(Float)
    descricao = Column(String(255))
    data_insercao = Column(DateTime, default=datetime.now())


    def __init__(self, nome:str, tipo:str, valor:float, descricao:str,
                 data_insercao:Union[DateTime, None] = None):
        
        self.nome = nome
        self.tipo = tipo
        self.valor = valor
        self.descricao = descricao
        self.codigo = self.gera_codigo()

        if data_insercao:
            self.data_insercao = data_insercao

    
    def gera_codigo(self):

        """ Gerador de código alfa numéricos de 10 caracteres automáticamente
        """
        
        _codigo = ''
        
        #Numeros randomicos
        _numeros = ''.join(str(random.randint(0,9)) for _ in range(5))
            
        #Letras randomicas 
        _codigo = ''.join(random.choice(string.ascii_uppercase) for _ in range(5))
        
        #retorna codigo
        return _codigo + _numeros