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


from sispagtoolkit.cnab240.pagamentos_pix import LotePagamentoPIX
from sispagtoolkit.cnab240.utils.objetos.infoUsuario import infoUsuario
from sispagtoolkit.cnab240.utils.objetos.banco import Banco
from sispagtoolkit.cnab240.utils.objetos.pix import PIX
from sispagtoolkit.cnab240.utils.objetos.favorecido import Favorecido
from sispagtoolkit.cnab240.utils.objetos.transacao import Transacao
from sispagtoolkit.cnab240.utils.objetos.endereco import Endereco
from sispagtoolkit.cnab240.lotes.arquivo.arquivo import Arquivo


# Define as informações da empresa que está gerando a remessa
usuario = infoUsuario(
    nome          = "NOME DA SUA EMPRESA",  # Nome completo da empresa
    identificador = "99999999000199",       # CNPJ da empresa
    email         = "contasapagar@suaempresa.com.br", # E-mail contas a pagar
    banco = Banco(
        codigo  = "341",    # Código do banco (341 Itaú)
        agencia = "111",    # Número da agência
        conta   = "11111",  # Número da conta
        dac     = "9",      # Dígito verificador
        nome    = "BCO ITAU S/A" # Nome do banco
    ),
    endereco = Endereco(
        rua    = "RUA DA SUA EMPRESA", # Endereço completo da empresa
        cidade = "SAO PAULO",          # Cidade da empresa
        uf     = "SP",                 # Unidade Federativa (estado)
        cep    = "09999999",           # CEP
        bairro = "LIBERDADE",          # Bairro
        numero = "123"                 # Número
    )
)


transacao = Transacao(
    data_pagmnto          = '20082024',
    valor_pagmnto         = '2',
    data_efetiva_pagmnto  = '20082024',
    valor_efetivo_pagmnto = '2',
    
    favorecido = Favorecido(
        identificador = '12345678912',
        nome          = 'NOME FAVORECIDO',
        banco         = '0',
        agencia       = '0',
        conta         = '0',
        dac           = '0'
    ),
    
    pix = PIX(
        tipo_chave = '03',  #01 - Telefone / 02 - Email / 03 - CPF/CNPJ / 04 - Chave Aleatória
        chave      = '12345678912'
    )

)



arquivo = Arquivo(usuario)

lote = LotePagamentoPIX(usuario)

lote.novoSegmento(
    transacao=transacao
)
   
   
arquivo.setNovoLote(lote)

open('SCNAB240.rem', 'w+').write(arquivo.getConteudo())
