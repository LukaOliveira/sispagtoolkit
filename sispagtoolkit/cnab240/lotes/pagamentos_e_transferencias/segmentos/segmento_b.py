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

class SegmentoB():
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
            ( 13, 14,  1, alphaNumeric,   "B"),   #Segmento
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
    # Dados dos favorecidos                               #
    #                                                     #
    #######################################################
    def setFavorecido(self, favorecido):
        estrutura = [
            ( 17, 18,  1, numeric,  "1" if len(favorecido.identificador) == 11 else "2"), #Tipo de inscrição favorecido
            ( 18, 32, 14, numeric, favorecido.identificador), #Identificador do favorecido
        ]
        self.content = Row.setStructs(structs=estrutura, content=self.content)   

            
            

    #######################################################
    #                                                     #
    # Endereço da empresa                                 #
    #                                                     #
    #######################################################
    def setEndereco(self, endereco):
        estrutura = [
            ( 32,  62, 30, alphaNumeric, endereco.rua),
            ( 62,  67,  5,      numeric, endereco.numero),
            ( 67,  82, 15, alphaNumeric, endereco.complemento),
            ( 82,  97, 15, alphaNumeric, endereco.bairro),
            ( 97, 117, 20, alphaNumeric, endereco.cidade),
            (117, 125,  8,      numeric, endereco.cep),
            (125, 127,  2, alphaNumeric, endereco.uf),
        ]
        self.content = Row.setStructs(structs=estrutura, content=self.content)     
      
      
      
    #######################################################
    #                                                     #
    # E-mail do usuario                                   #
    #                                                     #
    #######################################################
    def setEmail(self, usuario):
        estrutura = [
            (127,227,100, alphaNumeric, usuario.email),  #E-mail
        ]
        self.content = Row.setStructs(structs=estrutura, content=self.content)   
  
    
        
          
    #######################################################
    #                                                     #
    # Retorna o segmento                                  #
    #                                                     #
    #######################################################
    def getSegmento(self):
        return self.content