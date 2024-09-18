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


from .head_arquivo import HeadArquivo
from .trailer_arquivo import TrailerArquivo
from ...utils.break_line import break_line


class Arquivo():
    def __init__(self, info_usuario):
        self.head    = HeadArquivo()
        self.trailer = TrailerArquivo()
        self.lotes   = []
        
        self.info_usuario = info_usuario
        
        self.setHead()
        
    def setHead(self):
        self.head.setInfoBanco(self.info_usuario.banco)
        self.head.setInfoEmpresa(self.info_usuario)
        
    def setTrailer(self, total_lotes, total_registros):
        self.trailer.setBanco(self.info_usuario.banco)
        self.trailer.setTotalLotes(total_lotes)
        self.trailer.setTotalRegistros(total_registros)
        
    def setNovoLote(self, lote):
        self.lotes.append(lote)
        
    def sortLotes(self):
        
        tipoA = []
        tipoB = []
        tipoC = []
        tipoD = []
        
        for lote in self.lotes:
            print(type(lote).__name__)
            if(type(lote).__name__ in ('LotePagamentoPIX', 'LotePagamentoTEF')):
                tipoA.append(lote)
                
            elif(type(lote).__name__ in ('LoteLiquidacaoBoleto', 'LoteLiquidacaoPIXQR')):
                tipoB.append(lote)
                
            elif(type(lote).__name__ in ('LotePagamentoConcessionaria')):
                tipoC.append(lote)
                
        self.lotes = tipoA+tipoB+tipoC+tipoD
        
    
    def getConteudo(self):
        
        self.sortLotes()
        
        arquivo_final   = ''
        total_registros = 0
        total_lotes     = 0
        
        arquivo_final += f'{self.head.getSegmento()}{break_line}'
        
        for lote in self.lotes:
            lote.setSequenciaLote(str(total_lotes+1))
            total_lotes += 1
            
            arquivo_final   += f'{lote.getLote()}'
            total_registros += lote.getQuantidadeRegistros()
            
        
        total_registros += 2
        
        total_lotes     = len(self.lotes) 
        
        self.setTrailer(total_lotes, total_registros)
        
        arquivo_final += f'{self.trailer.getSegmento()}{break_line}'
            
        return arquivo_final
    
    

