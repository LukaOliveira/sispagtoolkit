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

class SegmentoO():
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
            ( 13, 14,  1, alphaNumeric,   "O"),   #Segmento
            ( 14, 17,  3,      numeric,   "0"),   #Tipo de movimento
            (103,106,  3, alphaNumeric, "REA"),   #Moeda
            (106,121, 15,      numeric,   "0"),   #Quantidade moeda
            (144,159, 15,      numeric,   "0"),   #Valor pago
            (162,171,  9,      numeric,   "0"),   #Nota fiscal

        ]
        self.content = Row.setStructs(structs=estrutura, content=self.content)
        
        self.setSeuNumero('1450')
    
    
    
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
    # Código de barras                                    #
    #                                                     #
    #######################################################    
    def setCodigoDeBarras(self, codBarras):
        estrutura = [
            (17, 65, 48, alphaNumeric, codBarras), 

        ]
        self.content = Row.setStructs(structs=estrutura, content=self.content)
    
        
    #######################################################
    #                                                     #
    # Nome do concessionaria                              #
    #                                                     #
    #######################################################
    def setNomeConcessionaria(self, nome):
        estrutura = [
            (65, 95, 30, alphaNumeric, nome),
        ]
        self.content = Row.setStructs(structs=estrutura, content=self.content)    
    
    
    
    #######################################################
    #                                                     #
    # Vencimento Nominal                                  #
    #                                                     #
    #######################################################
    def setVencimentoNominal(self, vencimento_nominal):
        estrutura = [
            (95, 103, 8, numeric, vencimento_nominal),
        ]
        self.content = Row.setStructs(structs=estrutura, content=self.content)    
           
        
           
    #######################################################
    #                                                     #
    # Valor previsto do titulo                            #
    #                                                     #
    #######################################################
    def setValorNominal(self, valor_previsto):
        estrutura = [
            (121,136, 15, numeric, valor_previsto),  #Valor previsto do titulo
        ]
        self.content = Row.setStructs(structs=estrutura, content=self.content) 
      
      
      
    #######################################################
    #                                                     #
    # Pagamento                                           #
    #                                                     #
    #######################################################
    def setPagamento(self, data_pagmnto):
        estrutura = [
            (136, 144, 8,  numeric,  data_pagmnto),  #Data de pagamento
        ]
        self.content = Row.setStructs(structs=estrutura, content=self.content)   
  
    
        
    #######################################################
    #                                                     #
    # Seu número                                          #
    #                                                     #
    #######################################################
    def setSeuNumero(self, seuNumero):
        estrutura = [
            (174,194, 20, alphaNumeric, seuNumero), 
        ]
        self.content = Row.setStructs(structs=estrutura, content=self.content)   
        
        
        
    #######################################################
    #                                                     #
    # Retorna o segmento                                  #
    #                                                     #
    #######################################################
    def getSegmento(self):
        return self.content