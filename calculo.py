from decimal import Decimal
from datetime import datetime

ano_atual = datetime.now().year

class Calculo:

    def __init__(self, cadastro):
        self.cadastro = cadastro

    def _input_int(self, mensagem, min_val, max_val):
        while True:
            try:
                valor = int(input(mensagem))
                if min_val <= valor <= max_val:
                    return valor
                print(f"Valor inválido. Digite entre {min_val} e {max_val}.")
            except ValueError:
                print("Entrada inválida. Digite um número.")

    def _validar_data(self, ano, mes, dia):
        try:
            datetime(ano, mes, dia)
            return True
        except ValueError:
            return False

    def total(self):

        if not self.cadastro.contas:
            print("\nNenhuma conta cadastrada.")
            return

        while True:
            try:
                print("\n## Escolha a Forma de Cálculo ##")
                print("[1] Dia do Vencimento")
                print("[2] Mês do Vencimento")
                print("[3] Ano do Vencimento")

                opcao = int(input("Digite sua opção: "))

                # DIA
                if opcao == 1:
                    while True:
                        dia = self._input_int("Dia: ", 1, 31)
                        mes = self._input_int("Mês: ", 1, 12)
                        ano = self._input_int("Ano: ", ano_atual, ano_atual + 20)

                        if self._validar_data(ano, mes, dia):
                            break
                        print("Data inválida.")

                    total = sum(
                        conta.valor
                        for conta in self.cadastro.contas
                        if (
                            conta.dia_vencimento == dia and
                            conta.mes_vencimento == mes and
                            conta.ano_vencimento == ano
                        )
                    )

                    print(f"\nTotal em {dia:02d}/{mes:02d}/{ano}: R$ {total:.2f}\n")
                    break

                # MÊS
                elif opcao == 2:
                    mes = self._input_int("Mês: ", 1, 12)
                    ano = self._input_int("Ano: ", ano_atual, ano_atual + 20)

                    total = sum(
                        conta.valor
                        for conta in self.cadastro.contas
                        if (
                            conta.mes_vencimento == mes and
                            conta.ano_vencimento == ano
                        )
                    )

                    print(f"\nTotal em {mes:02d}/{ano}: R$ {total:.2f}\n")
                    break

                # ANO
                elif opcao == 3:
                    ano = self._input_int("Ano: ", ano_atual, ano_atual + 20)

                    total = sum(
                        conta.valor
                        for conta in self.cadastro.contas
                        if conta.ano_vencimento == ano
                    )

                    print(f"\nTotal no ano {ano}: R$ {total:.2f}\n")
                    break

                else:
                    print("Escolha uma opção válida.")

            except ValueError:
                print("Digite uma opção válida.")