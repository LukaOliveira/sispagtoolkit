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


from sispagtoolkit.cnab240.lotes.arquivo.arquivo import Arquivo
from sispagtoolkit.cnab240.liquidacao_boletos import LoteLiquidacaoBoleto
from sispagtoolkit.cnab240.utils.objetos.infoUsuario import infoUsuario
from sispagtoolkit.cnab240.utils.objetos.favorecido import Favorecido
from sispagtoolkit.cnab240.utils.objetos.banco import Banco
from sispagtoolkit.cnab240.utils.objetos.endereco import Endereco
from sispagtoolkit.cnab240.utils.objetos.boleto import Boleto

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


# Inicializa um novo arquivo CNAB240
arquivo_cnab = Arquivo(usuario)

# Cria um novo lote para liquidação de boletos
# O parâmetro '30' é utilizado para boletos emitidos pelo Itaú
loteBoletos = LoteLiquidacaoBoleto(usuario, forma_pagamento = '30') 


########################################################
#                                                      #
# Definindo boletos a serem pagos                      #
#                                                      #
########################################################

# Cria dois objetos Boleto
boleto1 = Boleto(
    cod_barras     = '34191234000001500001750000000100049900123456', # Código de barras do boleto (44 dígitos, sem espaços ou separadores)
    data_pagamento = '12092024', # Data do pagamento no formato DDMMYYYY
    favorecido = Favorecido(
        nome          = "NOME FAVORECIDO", # Nome do favorecido (quem receberá o pagamento)
        identificador = "99999999000199"   # CNPJ/CPF do favorecido
    )
)

boleto2 = Boleto(
    cod_barras     = '34191234000001500001750000000100049900123456', # Código de barras do boleto (44 dígitos, sem espaços ou separadores)
    data_pagamento = '12092024', # Data do pagamento no formato DDMMYYYY
    favorecido = Favorecido(
        nome          = "NOME FAVORECIDO", # Nome do favorecido (quem receberá o pagamento)
        identificador = "99999999000199"   # CNPJ/CPF do favorecido
    )
)


# Array de boletos
boletos = [
    boleto1,
    boleto2
]

for boleto in boletos:
    loteBoletos.novoSegmento(boleto) # Adiciona o boleto ao lote

# Adiciona o lote ao arquivo CNAB
arquivo_cnab.setNovoLote(loteBoletos)


# Salva o arquivo CNAB com a codificação apropriada
with open('SCNAB240.rem', 'w+', encoding='iso-8859-1') as file:
    file.write(arquivo_cnab.getConteudo())

