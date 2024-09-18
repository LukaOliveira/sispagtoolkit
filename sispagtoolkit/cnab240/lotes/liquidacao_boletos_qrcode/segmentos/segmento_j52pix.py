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

class SegmentoJ52PIX():
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
            ( 17, 19,  2,      numeric,  "52"),   #Código do registros

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
    # Informações do sacado                               #
    #                                                     #
    #######################################################
    def setInfoSacado(self, infoUsuario):
        estrutura = [
            (19, 20,  1,      numeric, "1" if len(infoUsuario.identificador) == 11 else "2"), #Tipo de inscricao do sacado
            (20, 35, 15,      numeric,                            infoUsuario.identificador), #Número de inscricao do sacado
            (35, 75,  40, alphaNumeric,                                    infoUsuario.nome), #Nome do sacado
        ]
        self.content = Row.setStructs(structs=estrutura, content=self.content)    
    
    
    
    #######################################################
    #                                                     #
    # Informações do cedente                              #
    #                                                     #
    #######################################################
    def setInfoCedente(self, identificador, nome):
        estrutura = [
            (75, 76,  1,      numeric, "1" if len(identificador) == 11 else "2"), #Tipo de inscricao do sacado
            (76, 91, 15,      numeric,                            identificador), #Número de inscricao do sacado
            (91,131, 40, alphaNumeric,                                    nome), #Nome do sacado
        ]
        self.content = Row.setStructs(structs=estrutura, content=self.content)    
           
        
           
    #######################################################
    #                                                     #
    # Chave de pagamento                                  #
    #                                                     #
    #######################################################
    def setChavePagamento(self, chave):
        estrutura = [
            (131,208, 77,  alphaNumeric, chave), #Chave de pagamento
  
        ]
        self.content = Row.setStructs(structs=estrutura, content=self.content)    
    
        
    #######################################################
    #                                                     #
    # Retorna o segmento                                  #
    #                                                     #
    #######################################################
    def getSegmento(self):
        return self.content