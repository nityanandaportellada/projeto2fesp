# projeto2fesp

# Sistem de controles de contas a pagar

## Autores

- Danilo Depetris Soares - BSI
- Enzo Gabriel Miranda da Costa - BSI
- Gabriel Weber da Rocha - BSI
- Julia Barbosa de Almeida - BSI
- Luis Gustavo Bueno Taquete - BSI
- Nityananda Portellada - Engenharia de Software

Desenvolvido como trabalho acadêmico - 2026

## Descrição do projeto

Sistema desenvolvido em Python para implementar um sistema de gerenciamento de contas a pagar, permintindo que o cliente realize o cadastro de contas, faça consultas, atualizações e exclusão de contas, bem como proceda com cálculo de valores a pagar com base em datas específicas.

## Estrutura de dados utilizados

### Fonte de dados
- **Origem** - Entrada manual do usuário (CLI)

- **Tipo** - Dados inseridos em tempo real

- **Armazenamento** - Lista de objetos em memória

### Variáveis Relevantes

| Variável         | Tipo    | Descrição                  |
|------------------|---------|----------------------------|
| `nome_conta`     | String  | Nome da conta cadastrada   |
| `dia_vencimento` | Integer | Dia do vencimento da conta |
| `mes_vencimento` | Integer | Mês do vencimento da conta |
| `ano_vencimento` | Integer | Ano do vencimento da conta |
| `valor`          | float   | Valor da conta             |

### Contexto do Problema


**Contexto**:  Em um cenário cotidiano, tanto pessoas físicas quanto pequenas organizações enfrentam dificuldades para manter o controle adequado de suas contas a pagar. A ausência de organização pode resultar em atrasos, pagamento de juros, perda de prazos e dificuldades no planejamento financeiro. Dessa forma, torna-se necessário um sistema simples e eficiente que permita registrar e acompanhar essas informações de maneira estruturada.

**Problema a Resolver**: Diante desse contexto, o problema consiste em desenvolver um sistema capaz de gerenciar contas a pagar, permitindo o cadastro, consulta, atualização e exclusão de registros, além de possibilitar o cálculo automático dos valores totais com base em períodos específicos (dia, mês e ano). O sistema deve garantir a integridade dos dados por meio de validações e oferecer uma forma prática de acesso às informações, contribuindo para um controle financeiro mais eficiente e organizado.

**Aplicação Prática**: 
- Organização e controle de contas a pagar no dia a dia
- Planejamento financeiro mensal e anual
- Evitar atrasos em pagamentos e cobranças de juros
- Visualização do total de gastos por período (dia, mês e ano)
- Auxílio na tomada de decisões financeiras
- Controle de despesas pessoais ou de pequenos negócios

## Arquitetura do Sistema 

```
controle-contas/
│
│
├── conta.py              # Classe que representa uma conta
├── financeiro.py         # Regras de negócio do sistema
├── main.py               # Interface CLI principal
│── README.md             # Este arquivo
```

## Instalação e Configuração

### Requisitos 

- Python 3.8+

### Instalação

1. Baixe o Projeto:

- Baixe os arquivos manualmente ou copie para sua máquina

2. Não há dependências externas necessárias.

3. Execute o sistema:

```bash
- python main.py
```
Este comando irá:
- Inicializar o sistema de controle de contas a pagar
- Exibir o menu interativo no terminal
- Permitir o cadastro, consulta, atualização e exclusão de contas
- Realizar cálculos de valores por dia, mês e ano
- Executar todas as funcionalidades integradas do sistema

## Como Usar

### Modo 1: Interface de Linha de Comando (CLI)

- Execute o sistema:
```bash
- python main.py
```
O sistema exibirá o menu interativo:

1. **Cadastrar conta**

- Opção para que seja realizado o cadastro de novas contas no sistema
   - Inserção de nome, data e valor da conta
   - Validação completa dos dados

2. **Listar conta**

- Exibição de todas as contas cadastradas

3. **Calcular valor para pagamento em um dia**

- Exibição do valor a pagar através da Soma dos valores de contas com mesma data (dia) 

4. **Calcular valor para pagamento em um mês**

- Exibição do valor a pagar através da Soma dos valores de contas com mesma data (mês) 

5. **Calcular valor para pagamento em um ano**

- Soma total das contas no ano informadoExibição do valor a pagar através da Soma dos valores de contas com mesma data (ano) 

6. **Consultar Contas**

- Busca por nome, valor, dia, mês ou ano de vencimento

7. **Atualizar Contas**

- Alteração de dados da conta escolhida

8. **Excluir Contas**

- Remoção da conta escolhida

0. **Sair**

- Encerra o Sistema


## Contribuições

Projeto acadêmico desenvolvido para a disciplina de construção algorítimicas de soluções dirigida pelo professor Tiago Pedra

## Licença

Uso educacional - para fins avaliativos

