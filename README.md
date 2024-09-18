
# SispagToolKit

**SispagToolKit** é uma biblioteca Python que facilita a geração de arquivos de remessa de pagamentos para o sistema SISPAG Itaú, com suporte ao padrão **CNAB240**. A biblioteca foi projetada para auxiliar na automação e integração de processos de pagamento, oferecendo uma maneira simples e eficaz de gerar arquivos para diversas modalidades de pagamento, como boletos, tributos e pagamentos via PIX, TEF entre outros.

## Funcionalidades

- Geração de arquivos no padrão **CNAB240** compatíveis com o sistema SISPAG do Itaú.
- Suporte para:
  - Liquidação de boletos e QR Codes (PIX QR Code).
  - Pagamentos via TEF e PIX.
  - Pagamento de concessionárias.
- Estrutura modular e extensível, permitindo a adaptação e personalização para diferentes tipos de pagamento.
- Validações automáticas de campos, garantindo a conformidade com os layouts do CNAB240.

## Instalação

Você pode instalar a biblioteca diretamente via **pip**:

```bash
pip install SispagToolKit
```

## Exemplos de Uso

Os exemplos de uso da biblioteca podem ser encontrados na pasta `examples` do repositório. Lá você encontrará demonstrações detalhadas de como utilizar a biblioteca para diferentes tipos de pagamentos.

## Arquivos Derivados

Este projeto contém dois arquivos derivados da biblioteca [Febraban Python](https://github.com/starkbank/febraban-python). A utilização desses arquivos está de acordo com os termos da licença original, que pode ser encontrada no [repositório da biblioteca](https://github.com/starkbank/febraban-python/blob/master/LICENSE.txt).

Se houver qualquer questão relacionada ao uso de partes dessa biblioteca, sinta-se à vontade para consultar a licença original ou abrir uma issue no [repositório do GitHub](https://github.com/LukaOliveira/sispagtoolkit) ou no [repositório do GitLab](https://gitlab.com/lukaoliveira/sispagtoolkit).

## Contribuições

Contribuições são bem-vindas! Se você encontrar algum problema, por favor, abra uma issue no [repositório do GitHub](https://github.com/LukaOliveira/sispagtoolkit) ou no [repositório do GitLab](https://gitlab.com/lukaoliveira/sispagtoolkit).

## Licença

Este projeto está licenciado sob a **Licença MIT**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.




