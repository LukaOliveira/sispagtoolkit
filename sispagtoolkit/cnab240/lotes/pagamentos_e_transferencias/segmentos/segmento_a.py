""" 
MIT License

Copyright (c) 2024 Pedro Luka Oliveira

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Original Repository: 
     GitHub: https://github.com/LukaOliveira/sispagtoolkit
     GitLab: https://gitlab.com/lukaoliveira/sispagtoolkit
"""


from ....utils.tipos_dados import *
from ....utils.formatador import Row

class SegmentoA():
    def __init__(self):
        self.content = " "*240
        self.setInfoBase()
        
        
    ##########################################################
    #                                                        #
    # Informações base do lote                               #
    #                                                        #
    ##########################################################
    def setInfoBase(self):
        estrutura = [
            (  7,  8,  1,      numeric,   "3"),   #Tipo de registro
            ( 13, 14,  1, alphaNumeric,   "A"),   #Segmento
            ( 14, 17,  3,      numeric,   "0"),   #Tipo de Movimento
            ( 17, 20,  3,      numeric,   "0"),   #Camara centralizadora
            (101,104,  3, alphaNumeric, "009"),   #Moeda
            (114,119,  5,      numeric,   "0"),   #Zeros
        ]
        self.content = Row.setStructs(structs=estrutura, content=self.content)
        
        self.setCamara('')
    
    
    
    #######################################################
    #                                                     #
    # Código do banco                                     #
    #                                                     #
    #######################################################
    def setBanco(self, banco):
        estrutura = [
            (0, 3, 3, numeric, banco.codigo),  
        ]
        self.content = Row.setStructs(structs=estrutura, content=self.content)
    
    
    
    #######################################################
    #                                                     #
    # Número do lote                                      #
    #                                                     #
    #######################################################
    def setLote(self, lote):
        estrutura = [
            (3, 7, 4, numeric, lote),
        ]
        self.content = Row.setStructs(structs=estrutura, content=self.content)
    
        
        
    #######################################################
    #                                                     #
    # Número de sequencia no lote                         #
    #                                                     #
    #######################################################
    def setNumRegistro(self, num):
        estrutura = [
            (8, 13, 5, numeric, num), 
        ]
        self.content = Row.setStructs(structs=estrutura, content=self.content)
       
       
       
    #######################################################
    #                                                     #
    # Código câmara centralizadora                        #
    #                                                     #
    #######################################################
    def setCamara(self, cod):
        estrutura = [
            (17, 20, 3, numeric, cod), 
        ]
        self.content = Row.setStructs(structs=estrutura, content=self.content)
       
        
        
    #######################################################
    #                                                     #
    # Dados dos favorecidos                               #
    #                                                     #
    #######################################################
    def setFavorecido(self, favorecido):        
        estrutura = [
            ( 20, 23,  3,      numeric,         favorecido.banco), #Banco favorecido
            ( 43, 73, 30, alphaNumeric,          favorecido.nome), #Nome favorecido
            (203,217, 14,      numeric, favorecido.identificador), #Inscricao do favorecido
        ]
        self.content = Row.setStructs(structs=estrutura, content=self.content)   
        
         
        #O posicionamento dos campos muda de caso os bancos sejam diferentes 341 (Itau) ou 409 (Unibanco)
        if(str(favorecido.banco) in ('341', '409')):
            estrutura = [
                (23, 24, 1, numeric,                  0), #Zeros
                (24, 28, 4, numeric, favorecido.agencia), #Agencia Favorecido
                (29, 35, 6, numeric,                  0), #Zeros
                (35, 41, 6, numeric,   favorecido.conta), #Conta Favorecido
                (42, 43, 1, numeric,     favorecido.dac), #Dac conta favorecida
            ]
        
        else:
            estrutura = [
                (23, 28,  5,  numeric, favorecido.agencia), #Agencia Favorecido
                (29, 41, 12,  numeric,   favorecido.conta), #Conta Favorecido
                (41, 43,  2, alphaNumeric, favorecido.dac), #Dac Favorecido
                
            ]

            
        self.content = Row.setStructs(structs=estrutura, content=self.content)   
            
            

    #######################################################
    #                                                     #
    # Numero atribuido pela empresa                       #
    #                                                     #
    #######################################################
    def setSeuNumero(self, seu_numero):
        estrutura = [
            (73, 93, 20, alphaNumeric, seu_numero),
        ]
        self.content = Row.setStructs(structs=estrutura, content=self.content)    
      
      
      
    #######################################################
    #                                                     #
    # Valor e data de pagamento                           #
    #                                                     #
    #######################################################
    def setPagamento(self, transacao):
        estrutura = [
            ( 93, 101,  8, numeric,          transacao.data_pagmnto),  #Data de pagamento
            (119, 134, 15, numeric,         transacao.valor_pagmnto),  #Valor de pagamento
            (154, 162,  8, numeric,  transacao.data_efetiva_pagmnto),  #Data efetiva de pagamento
            (162, 177, 15, numeric, transacao.valor_efetivo_pagmnto),  #Data efetiva de pagamento
        ]
        self.content = Row.setStructs(structs=estrutura, content=self.content)   
  
    
        
    #######################################################
    #                                                     #
    # Identificação de transferencia PIX                  #
    #                                                     #
    #######################################################
    def setIdentificacaoPIX(self, identificacao):
        estrutura = [
            (112,114,  2, alphaNumeric, identificacao), 
        ]
        self.content = Row.setStructs(structs=estrutura, content=self.content)   
        
        
        
    #######################################################
    #                                                     #
    # Finalidade da TED                                   #
    #                                                     #
    #######################################################
    def setFinalidadeTED(self, finalidade):
        estrutura = [
            (219, 224, 5, alphaNumeric, finalidade),
        ]
        self.content = Row.setStructs(structs=estrutura, content=self.content) 
        
        
          
    #######################################################
    #                                                     #
    # Retorna o segmento                                  #
    #                                                     #
    #######################################################
    def getSegmento(self):
        return self.content