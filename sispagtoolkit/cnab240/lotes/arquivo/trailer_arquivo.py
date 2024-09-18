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


from ...utils.tipos_dados import *
from ...utils.formatador import Row

import datetime

class TrailerArquivo():
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
            (  3,  7,  4,      numeric, "9999"),   #Código do lote
            (  7,  8,  1,      numeric,    "9"),   #Tipo de registro
        ]
        self.content = Row.setStructs(structs=estrutura, content=self.content)
    
    
    
    #######################################################
    #                                                     #
    # Informações da empresa                              #
    #                                                     #
    #######################################################
    def setBanco(self, banco):
        estrutura = [
            (0, 3, 3,  numeric, banco.codigo),
        ]
        self.content = Row.setStructs(structs=estrutura, content=self.content)
        
        
    #######################################################
    #                                                     #
    # Quantidade total de lotes                           #
    #                                                     #
    #######################################################
    def setTotalLotes(self, total):
        estrutura = [
            ( 17, 23, 6, numeric, total),
        ]
        self.content = Row.setStructs(structs=estrutura, content=self.content)  
    
    
    
    #######################################################
    #                                                     #
    # Quantidade total de registros                       #
    #                                                     #
    #######################################################
    def setTotalRegistros(self, total):
        estrutura = [
            ( 23, 29, 6, numeric, total),
        ]
        self.content = Row.setStructs(structs=estrutura, content=self.content)   
    
    
    
    #######################################################
    #                                                     #
    # Retorna o segmento                                  #
    #                                                     #
    #######################################################
    def getSegmento(self):
        return self.content