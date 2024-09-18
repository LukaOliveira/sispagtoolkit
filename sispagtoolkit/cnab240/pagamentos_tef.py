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


from .lotes.pagamentos_e_transferencias.segmentos.head_lote import HeadLote
from .lotes.pagamentos_e_transferencias.segmentos.segmento_a import SegmentoA
from .lotes.pagamentos_e_transferencias.segmentos.segmento_b import SegmentoB
from .lotes.pagamentos_e_transferencias.segmentos.trailer_lote import TrailerLote

class LotePagamentoTEF():
    def __init__(self, info_usuario):
        
        self.head         = HeadLote()
        self.trailer      = TrailerLote()
        self.segmentos    = []
        
        self.info_usuario = info_usuario
        
        self.setHeadInfo()
        
        
    def novoSegmento(self, transacao):
        
        segmento = PagamentoTEF(self.info_usuario, transacao)
        segmento.atualizarSequencia(len(self.segmentos)+1)
        
        self.segmentos.append(segmento)
        
    def setHeadInfo(self):
        
        self.head.setBanco(self.info_usuario.banco)
        self.head.setTipoPagamento('20')
        self.head.setFormaPagamento('01') #Campo variavel
        self.head.setInfoEmpresa(self.info_usuario)
        self.head.setInfoBanco(self.info_usuario.banco)
        self.head.setEndereco(self.info_usuario.endereco)
        
    def setTrailerInfo(self, valor_total):
               
        self.trailer.setBanco(self.info_usuario.banco)
        self.trailer.setTotalRegistros(len(self.segmentos)*2+2)
        self.trailer.setValorTotal(valor_total)
        
    def getQuantidadeRegistros(self):
        return len(self.segmentos)*2+2
    
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



class PagamentoTEF():
    def __init__(self,  info_usuario, transacao):
        
        self.segmentoa = SegmentoA()
        self.segmentob = SegmentoB()
        self.info_usuario = info_usuario
        
        self.defSegmentoA(transacao)
        self.defSegmentoB(transacao)

    def defSegmentoA(self, transacao):
        
        self.valor = float(f'{transacao.valor_pagmnto[:-2]}.{transacao.valor_pagmnto[-2:]}')
        
        self.segmentoa.setBanco(self.info_usuario.banco)
        self.segmentoa.setFavorecido(transacao.favorecido)
        self.segmentoa.setPagamento(transacao)
        self.segmentoa.setCamara('0')
        self.segmentoa.setSeuNumero(transacao.seu_numero)
        
    def defSegmentoB(self, transacao):
        self.segmentob.setFavorecido(transacao.favorecido)
        self.segmentob.setBanco(self.info_usuario.banco)
        self.segmentob.setEndereco(self.info_usuario.endereco)
        self.segmentob.setEmail(self.info_usuario)


        
    def atualizarSequencia(self, sequencia):
        self.segmentoa.setNumRegistro(sequencia)
        self.segmentob.setNumRegistro(sequencia)
        
    def atualizarLote(self, lote):
        self.segmentoa.setLote(lote)
        self.segmentob.setLote(lote)
    
    
    def getSegmento(self):
        return f'{self.segmentoa.getSegmento()}{break_line}{self.segmentob.getSegmento()}'