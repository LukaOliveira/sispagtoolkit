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


from ...utils.calculo_vencimento import calculo_vencimento

class codBarras():
    def __init__(self, cod_barras):
        self.codbarras          = cod_barras
        self.banco              = None
        self.moeda              = None
        self.dac                = None
        self.fator_vencimento   = None
        self.valor              = None
        self.campo_livre        = None
        self.vencimento_nominal = None
        self.defCampos()
        
    def defCampos(self):
        self.banco            = self.codbarras[0:3]
        self.moeda            = self.codbarras[3:4]
        self.dac              = self.codbarras[4:5]
        self.fator_vencimento = self.codbarras[5:9]
        self.valor            = self.codbarras[9:19]
        self.campo_livre      = self.codbarras[19:44]
        
        self.vencimento_nominal = calculo_vencimento(self.fator_vencimento)
    
    
class codBarrasConta():
    def __init__(self, cod_barras):
        self.codbarras          = cod_barras
        self.produto            = None
        self.segmento           = None
        self.ident_valor        = None
        self.dgt_verificador    = None
        self.valor              = None
        self.ident_empresa      = None
        self.campo_livre        = None
        self.defCampos()
        
    def defCampos(self):
        
        barras_sem_dv = self.codbarras
        
        if(len(barras_sem_dv) > 44):
            barras_sem_dv = f'{self.codbarras[0:11]}{self.codbarras[12:23]}{self.codbarras[24:35]}{self.codbarras[36:48]}'

        self.produto            = barras_sem_dv[0:1]
        self.segmento           = barras_sem_dv[1:2]
        self.ident_valor        = barras_sem_dv[2:3]
        self.dgt_verificador    = barras_sem_dv[3:4]
        self.valor              = barras_sem_dv[4:15]
        self.ident_empresa      = barras_sem_dv[15:19]
        self.campo_livre        = barras_sem_dv[19:44]
        