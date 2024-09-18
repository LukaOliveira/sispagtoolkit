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

class SegmentoJ():
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
            ( 13, 14,  1, alphaNumeric,   "J"),   #Segmento
            ( 14, 17,  3,      numeric,   "0"),   #Tipo de Movimento
            (167,182, 15,      numeric,   "0"),   #Zeros
        ]
        self.content = Row.setStructs(structs=estrutura, content=self.content)
    
    
    
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
    # Código de barras                                    #
    #                                                     #
    #######################################################    
    def setCodigoDeBarras(self, codBarras):
        estrutura = [
            (17, 20, 3,  numeric,             codBarras.banco), #Banco Favorecido
            (20, 21, 1,  numeric,             codBarras.moeda), #Moeda
            (21, 22, 1,  numeric,               codBarras.dac), #Digito Verificador do Boleto
            (22, 26, 4,  numeric,  codBarras.fator_vencimento), #Fator de vencimento
            (26, 36, 10, numeric,             codBarras.valor), #Valor codigo de barras
            (36, 61, 25, numeric,       codBarras.campo_livre), #Campo Livre 
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
    # Nome do favorecido                                  #
    #                                                     #
    #######################################################
    def setNomeFavorecido(self, nome):
        estrutura = [
            (61, 91, 30, alphaNumeric, nome),
        ]
        self.content = Row.setStructs(structs=estrutura, content=self.content)    
    
    
    
    #######################################################
    #                                                     #
    # Vencimento Nominal                                  #
    #                                                     #
    #######################################################
    def setVencimentoNominal(self, vencimento_nominal):
        estrutura = [
            (91, 99, 8, numeric, vencimento_nominal),
        ]
        self.content = Row.setStructs(structs=estrutura, content=self.content)    
           
        
           
    #######################################################
    #                                                     #
    # Valores do titulo                                   #
    #                                                     #
    #######################################################
    def setValores(self, valor_nominal, descontos, acrescimos):
        estrutura = [
            (99,  114, 15, numeric, valor_nominal),    #Valor nominal do titulo
            (114, 129, 15, numeric,     descontos),    #Descontos + Abatimentos
            (129, 144, 15, numeric,    acrescimos),    #Acrescimos
        ]
        self.content = Row.setStructs(structs=estrutura, content=self.content) 
      
      
      
    #######################################################
    #                                                     #
    # Pagamento                                           #
    #                                                     #
    #######################################################
    def setPagamento(self, data_pagmnto, valor_pagmnto):
        estrutura = [
            (144, 152, 8,  numeric,  data_pagmnto),  #Data de pagamento
            (152, 167, 15, numeric, valor_pagmnto),  #Valor de pagamento
        ]
        self.content = Row.setStructs(structs=estrutura, content=self.content)   
  
    
        
    #######################################################
    #                                                     #
    # Seu número                                          #
    #                                                     #
    #######################################################
    def setSeuNumero(self, seuNumero):
        estrutura = [
            (182, 202, 20, alphaNumeric, seuNumero), 
        ]
        self.content = Row.setStructs(structs=estrutura, content=self.content)   
        
        
        
    #######################################################
    #                                                     #
    # Seu nosso número                                    #
    #                                                     #
    #######################################################
    def setNossoNumero(self, nossoNumero):
        estrutura = [
            (215, 230, 15, alphaNumeric, nossoNumero),
        ]
        self.content = Row.setStructs(structs=estrutura, content=self.content) 
        
        
        
    #######################################################
    #                                                     #
    # Ocorrências                                         #
    #                                                     #
    #######################################################
    def setOcorrencias(self, ocorrencias):
        estrutura = [
            (230, 240, 10, alphaNumeric, ocorrencias),
        ]
        self.content = Row.setStructs(structs=estrutura, content=self.content)
    
    
        
    #######################################################
    #                                                     #
    # Retorna o segmento                                  #
    #                                                     #
    #######################################################
    def getSegmento(self):
        return self.content