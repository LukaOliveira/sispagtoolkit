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


from .lotes.pagamentos_concessionarias_tributos.segmentos.head_lote import HeadLote
from .lotes.pagamentos_concessionarias_tributos.segmentos.segmento_o import SegmentoO
from .lotes.pagamentos_concessionarias_tributos.segmentos.trailer_lote import TrailerLote
from .utils.objetos.cod_barras import codBarrasConta

from .utils.break_line import break_line

class LotePagamentoConcessionaria():
    def __init__(self, info_usuario):
        self.head         = HeadLote()
        self.trailer      = TrailerLote()
        self.segmentos    = []
        self.info_usuario = info_usuario
        
        self.setHeadInfo()
        
        
    def novoSegmento(self, conta):
        segmento = PagamentoConcessionaria(conta, self.info_usuario)
        segmento.atualizarSequencia(len(self.segmentos)+1)
        
        self.segmentos.append(segmento)
        
    def setHeadInfo(self):
        self.head.setBanco(self.info_usuario.banco)
        self.head.setTipoPagamento('98')
        self.head.setFormaPagamento('13')
        self.head.setInfoEmpresa(self.info_usuario)
        self.head.setInfoBanco(self.info_usuario.banco)
        self.head.setEndereco(self.info_usuario.endereco)
        
    def setTrailerInfo(self, valor_total):   
        self.trailer.setBanco(self.info_usuario.banco)
        self.trailer.setTotalRegistros(len(self.segmentos)+2)
        self.trailer.setValorTotal(valor_total)
        
    def getQuantidadeRegistros(self):
        return len(self.segmentos)+2
    
    def setSequenciaLote(self, lote):
        self.head.setLote(lote)
        self.trailer.setLote(lote)
    
        for segmento in self.segmentos:
            segmento.atualizarLote(lote)
            
        
    def getLote(self):
        
        lote_final = ''
        valor_tt   = 0
        
        lote_final += f'{self.head.getSegmento()}{break_line}'
        
        for segmento in self.segmentos:
            lote_final += f'{segmento.getSegmento()}{break_line}'
            valor_tt   += segmento.valor
            
        valor_tt = (format(valor_tt, ".2f"))
        self.setTrailerInfo(str(valor_tt).replace('.', ''))
        
        lote_final += f'{self.trailer.getSegmento()}{break_line}'
            
        return lote_final



class PagamentoConcessionaria():
    def __init__(self,  conta, info_usuario):
        self.segmentoo    = SegmentoO()
        self.info_usuario = info_usuario
        
        self.defSegmentoO(conta)


    def defSegmentoO(self, conta):
        
        cod_barras = codBarrasConta(conta.cod_barras)
        
        self.valor = float(f'{cod_barras.valor[:-2]}.{cod_barras.valor[-2:]}')
        
        self.segmentoo.setBanco(self.info_usuario.banco)
        
        self.segmentoo.setCodigoDeBarras(conta.cod_barras)
        self.segmentoo.setNomeConcessionaria(conta.nome_concessionaria)
        
        self.segmentoo.setVencimentoNominal(conta.vencimento_nominal)
        self.segmentoo.setValorNominal(cod_barras.valor)
        
        self.segmentoo.setPagamento(conta.data_pagamento)
        
        
    def atualizarSequencia(self, sequencia):
        self.segmentoo.setNumRegistro(sequencia)
        
    def atualizarLote(self, lote):
        self.segmentoo.setLote(lote)

        
    def getSegmento(self):
        return self.segmentoo.getSegmento()