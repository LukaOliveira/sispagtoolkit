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

class HeadArquivo():
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
            (  3,  7,  4,      numeric,   "0"),   #Código do lote
            (  7,  8,  1,      numeric,   "0"),   #Tipo de registro
            ( 14, 17,  3,      numeric,  "80"),   #Layout de arquivo
            (142,143,  1,      numeric,   "1"),   #Código de arquivo
            (157,166,  9,      numeric,   "0"),   #Zeros
            (143,151,  8,      numeric,   datetime.datetime.now().strftime('%d%m%Y')),   #Data de geração
            (151,157,  6,      numeric,   datetime.datetime.now().strftime('%H%M%S')),   #Hora de geração
            (166,171,  5,      numeric,   "0"),   #Unidade de densidade
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
            (72,102,30, alphaNumeric,          usuario.nome), #Nome da empresa
        ]
        self.content = Row.setStructs(structs=estrutura, content=self.content)
        
        
    #######################################################
    #                                                     #
    # Informações do banco                                #
    #                                                     #
    #######################################################
    def setInfoBanco(self, banco):
        estrutura = [
            ( 0, 3,    3, numeric,      banco.codigo),
            ( 52, 57,  5, numeric,      banco.agencia),
            ( 58, 70, 12, numeric,      banco.conta),
            ( 71, 72,  1, numeric,      banco.dac),
            (102,132, 30, alphaNumeric, banco.nome)
        ]
        self.content = Row.setStructs(structs=estrutura, content=self.content)  
       
        
    #######################################################
    #                                                     #
    # Retorna o segmento                                  #
    #                                                     #
    #######################################################
    def getSegmento(self):
        return self.content