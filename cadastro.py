# importa a classe conta
from conta import Conta
from datetime import datetime
from decimal import Decimal

ano_atual = datetime.now().year


# Classe que representa o controle do sistema
class Cadastro:

    # Método construtor
    def __init__(self):
        self.contas = []

    def listar_contas(self):
        return self.contas

    # Método auxiliar para entrada inteira
    def _input_int(self, mensagem, min_val, max_val):
        while True:
            try:
                valor = int(input(mensagem))
                if min_val <= valor <= max_val:
                    return valor
                print(f"Valor inválido. Digite entre {min_val} e {max_val}.")
            except ValueError:
                print("Digite um número válido.")

    # Método para validar data real
    def _validar_data(self, ano, mes, dia):
        try:
            datetime(ano, mes, dia)
            return True
        except ValueError:
            return False

    # Método para cadastrar uma nova conta
    def cadastrar_conta(self):

        # Nome da conta (normalizado)
        nome_conta = input("Digite o nome da conta: ").strip().title()

        # Ano (alinhado com Calculo)
        ano_vencimento = self._input_int(
            "Digite o ano de vencimento: ",
            ano_atual,
            ano_atual + 20
        )

        # Mês
        mes_vencimento = self._input_int("Digite o mês de vencimento: ", 1, 12)

        # Dia (validação real com datetime)
        while True:
            dia_vencimento = self._input_int("Digite o dia do vencimento: ", 1, 31)

            if self._validar_data(ano_vencimento, mes_vencimento, dia_vencimento):
                break

            print("Data inválida. Verifique dia/mês/ano.")

        # Valor com Decimal (padrão financeiro correto)
        while True:
            try:
                valor = Decimal(input("Digite o valor da conta: "))
                if valor > 0:
                    break
                print("Digite um valor maior que zero.")
            except:
                print("Digite um valor válido.")

        # Criação da conta
        conta = Conta(
            nome_conta,
            dia_vencimento,
            mes_vencimento,
            ano_vencimento,
            valor
        )

        self.contas.append(conta)

        print("\nConta cadastrada com sucesso.")

