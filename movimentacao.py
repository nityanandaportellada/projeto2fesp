# Importa a classe Conta
from conta import Conta


# Classe que representa o controle do sistema
class Movimentacao:

    def __init__(self, cadastro):
        self.cadastro = cadastro

    # Método para atualizar dados de uma conta
    def atualizar_contas(self):
        #informa se não houver conta cadastrada
        if len(self.cadastro.contas) == 0:
            print("\nNenhuma conta cadastrada.")
            return

        #recebe o nome da conta, converte para carcteres minusculos para possibilitar comparar com a conta cadastrada que será atualziada
        nome_busca = str(input("Digite o nome da conta que deseja atualizar: ").lower())

        #verifica se o nome pesquisado esta cadastrado (utilizando a conversão de minusculos do nome_conta e exibe os resultado)
        for conta in self.cadastro.contas:
            if nome_busca in conta.nome_conta.lower():

                print("\nConta encontrada\n:")
                conta.exibir_dados()

                #exibe a opção para a escolha do que será atualizado
                print("\n#### O que deseja atualizar na Conta? ####")
                print("[1]. Nome")
                print("[2]. Valor")
                print("[3]. Dia de vencimento")
                print("[4]. Mês de vencimento")
                print("[5]. Ano de Vencimento")

                opcao = int(input("Escolha uma opção: "))

                #altera nome
                if opcao == 1:
                    novo_nome = input("Digite o novo nome: ")
                    conta.nome_conta = novo_nome

                #altera valor
                elif opcao == 2:
                    while True:
                        try:
                            novo_valor = float(input("Digite o novo valor: "))
                            conta.valor = novo_valor
                            break
                        except ValueError:
                            print("Valor inválido.")

                #altera dia de vencimento
                elif opcao == 3:
                    while True:
                        try:
                            novo_dia = int(input("Digite o novo dia: "))
                            if novo_dia >= 1 and novo_dia <= 31:
                                conta.dia_vencimento = novo_dia
                                break
                            else:
                                print("Dia inválido, digite o dia corretamente.")
                        except ValueError:
                            print("Entrada inválida. Digite o dia corretamente")

                #altera mes do vencimento
                elif opcao == 4:
                    while True:
                        try:
                            novo_mes = int(input("Digite o novo mês: "))
                            if novo_mes >= 1 and novo_mes <= 12:
                                conta.mes_vencimento = novo_mes
                                break
                            else:
                                print("Mês inválido. digite o mês corretamente")
                        except ValueError:
                            print("Entrada inválida. Digite o mês corretamente")
                
                #altera ano do vencimento
                elif opcao == 5:
                    while True:
                        try:
                            novo_ano = int(input("Digite o novo ano: "))
                            if novo_ano >= 2026:
                                conta.ano_vencimento = novo_ano
                                break
                            else:
                                print("Ano inválido. digite o ano corretamente")
                        except ValueError:
                            print("Entrada inválida. Digite o ano corretamente")

                else:
                    print("Opção inválida.")
                    return

                print("\nConta atualizada com sucesso.")
                return

        print("\nConta não encontrada.")

    # Método para remover uma conta anteriormente cadastrada
    def excluir_contas(self):
        #verifica se há contas cadastradas, se não houver informa o usuário
        if len(self.cadastro.contas) == 0:
            print("\nNenhuma conta cadastrada.")
            return

        #recebe e identifica a conta através do uso de seu nome (convertido em minusculas para permitir comparação)
        nome_busca = str(input("Digite o nome da conta que deseja remover: ").lower())

        #identifica se o nome escolhido foi cadastrado como conta
        for conta in self.cadastro.contas:
            if nome_busca in conta.nome_conta.lower():
                
                #informa que a conta foi encontrada e exibe os dados da conta
                print("\nConta encontrada:")
                conta.exibir_dados()

                #confirma a remção e em caso positivo faz a remoção
                confirmacao = input("\nDeseja realmente remover esta conta? (s/n): ").lower()

                if confirmacao == "s":
                    self.cadastro.contas.remove(conta)
                    print("\nConta removida com sucesso.")
                else:
                    print("\nRemoção cancelada.")

                return

        print("\nConta não encontrada.")