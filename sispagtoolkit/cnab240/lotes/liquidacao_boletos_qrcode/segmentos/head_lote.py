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

class HeadLote():
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
            (  7,  8,  1,      numeric,   "1"),   #Tipo de registro
            (  8,  9,  1, alphaNumeric,   "C"),   #Tipo de operacao
            ( 13, 16,  3,      numeric,  "30"),   #Versao do Layout
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
    # Tipo de pagamento                                   #
    #                                                     #
    #######################################################    
    def setTipoPagamento(self, tipo):
        estrutura = [
            ( 9, 11, 2, numeric, tipo),
        ]
        self.content = Row.setStructs(structs=estrutura, content=self.content)
        
        
    #######################################################
    #                                                     #
    # Forma de pagamento                                  #
    #                                                     #
    #######################################################    
    def setFormaPagamento(self, forma):
        estrutura = [
            (11, 13, 2, numeric, forma),
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
    # Informações da empresa                              #
    #                                                     #
    #######################################################
    def setInfoEmpresa(self, usuario):
        estrutura = [
            (17, 18, 1,      numeric, "1" if len(usuario.identificador) == 11 else "2"), #Tipo de inscrição
            (18, 32,14,      numeric, usuario.identificador), #Inscrição da empresa
            (72,102,32, alphaNumeric,          usuario.nome), #Nome da empresa
        ]
        self.content = Row.setStructs(structs=estrutura, content=self.content)
    
    
    
    #######################################################
    #                                                     #
    # Informações do banco                                #
    #                                                     #
    #######################################################
    def setInfoBanco(self, banco):
        estrutura = [
            (52, 57, 5, numeric, banco.agencia),
            (58, 70,12, numeric, banco.conta),
            (71, 72, 1, numeric, banco.dac),
        ]
        self.content = Row.setStructs(structs=estrutura, content=self.content)        
    
    
        
    #######################################################
    #                                                     #
    # Endereço da empresa                                 #
    #                                                     #
    #######################################################
    def setEndereco(self, endereco):
        estrutura = [
            (142, 172, 30, alphaNumeric, endereco.rua),
            (172, 177,  5,      numeric, endereco.numero),
            (177, 192, 15, alphaNumeric, endereco.complemento),
            (192, 212, 20, alphaNumeric, endereco.cidade),
            (212, 220,  8,      numeric, endereco.cep),
            (220, 222,  2, alphaNumeric, endereco.uf),
        ]
        self.content = Row.setStructs(structs=estrutura, content=self.content)    
       
        
    #######################################################
    #                                                     #
    # Retorna o segmento                                  #
    #                                                     #
    #######################################################
    def getSegmento(self):
        return self.content