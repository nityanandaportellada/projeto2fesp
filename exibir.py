from decimal import Decimal
from datetime import datetime

class Exibir:

    def __init__(self, cadastro):
        self.cadastro = cadastro

    #função para validação de valor, sem ter que chamar em todas
    def _input_int(self, msg, min_val, max_val):
        while True:
            try:
                valor = int(input(msg))
                if min_val <= valor <= max_val:
                    return valor
                print(f"Digite um valor entre {min_val} e {max_val}")
            except ValueError:
                print("Digite um número válido.")

    # Listar contas
    def listar_contas(self):
        contas = self.cadastro.listar_contas()

        if not contas:
            print("\nNenhuma conta cadastrada.")
            return

        print("\n### LISTA DE CONTAS ###")
        for conta in contas:
            conta.exibir_dados()

    # Pesquisar contas
    def pesquisar_contas(self):

        print("\nEscolha a forma de consulta:\n")
        print("[1] Nome da Conta")
        print("[2] Valor da Conta")
        print("[3] Mês de vencimento")
        print("[4] Dia de vencimento")
        print("[5] Ano de vencimento")

        try:
            opcao = int(input("\nEscolha uma opção: "))
        except ValueError:
            print("Digite um número válido.")
            return

        contas = self.cadastro.listar_contas()

        if not contas:
            print("\nNenhuma conta cadastrada.")
            return

        resultados = []

        
        if opcao == 1:
            nome = input("Digite o nome da conta: ").strip().lower()

            resultados = [
                conta for conta in contas
                if nome in conta.nome_conta.lower()
            ]

        
        elif opcao == 2:
            while True:
                try:
                    valor = Decimal(input("Digite o valor da conta: "))
                    break
                except:
                    print("Valor inválido.")

            resultados = [
                conta for conta in contas
                if conta.valor == valor
            ]

        
        elif opcao == 3:
            mes = self._input_int("Digite o mês: ", 1, 12)

            resultados = [
                conta for conta in contas
                if conta.mes_vencimento == mes
            ]

     
        elif opcao == 4:
            dia = self._input_int("Digite o dia: ", 1, 31)

            resultados = [
                conta for conta in contas
                if conta.dia_vencimento == dia
            ]

        
        elif opcao == 5:
            ano_atual = datetime.now().year
            ano = self._input_int("Digite o ano: ", ano_atual, ano_atual + 20)

            resultados = [
                conta for conta in contas
                if conta.ano_vencimento == ano
            ]

        else:
            print("Opção inválida.")
            return

        # Resultado
        if not resultados:
            print("\nNenhuma conta encontrada.")
        else:
            print("\n### RESULTADOS ###")
            for conta in resultados:
                conta.exibir_dados()
        