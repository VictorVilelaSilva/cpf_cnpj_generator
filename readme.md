# Gerador de CPF/CNPJ

Este script em Python gera números aleatórios de CPF (Cadastro de Pessoas Físicas) e CNPJ (Cadastro Nacional da Pessoa Jurídica). Ele também oferece a funcionalidade de alternar entre exibir os números com ou sem formatação.

## Pré-requisitos

Antes de executar o script, certifique-se de ter instalado o seguinte:

- Python 3.x
- pyperclip
- keyboard

## Uso

1. Execute o script.
2. Pressione `Ctrl + 1` para gerar um número de CPF aleatório e copiá-lo para a área de transferência.
3. Pressione `Ctrl + 2` para gerar um número de CNPJ aleatório e copiá-lo para a área de transferência.
4. Pressione `Ctrl + *` (asterisco) para alternar entre exibir números com ou sem formatação.
5. Pressione `Esc` para sair do script.

## Como Funciona

- O script define uma classe `GeradorCpfCnpj` que possui métodos para gerar números de CPF e CNPJ, além de alternar o formato de exibição.
- Números aleatórios são gerados para o CPF e CNPJ, com verificações necessárias para garantir a validade.
- Os números gerados são copiados para a área de transferência.
- Teclas de atalho são configuradas usando a biblioteca `keyboard` para acionar as funções de geração e alternância de formatação.

## Personalização

- Você pode modificar as teclas de atalho alterando as combinações de teclas nas chamadas `add_hotkey`.
- Ajuste a formatação dos números gerados modificando os métodos `generate_cpf` e `generate_cnpj`.

## Licença

Este script é lançado sob a [Licença MIT](LICENSE).
