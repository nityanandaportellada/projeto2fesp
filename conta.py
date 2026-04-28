# Classe que representa uma conta
class Conta:

    # Método construtor da conta
    def __init__(self, nome_conta, dia_vencimento, mes_vencimento, ano_vencimento, valor):
        self.nome_conta = nome_conta
        self.dia_vencimento = dia_vencimento
        self.mes_vencimento = mes_vencimento
        self.ano_vencimento = ano_vencimento
        self.valor = valor

    # Método para exibir os dados da conta após o cadastro
    def exibir_dados(self):
        print("\n### DADOS DA CONTA ###\n")
        print("Nome da Conta: ", self.nome_conta)
        print("Dia do Vencimento: ", self.dia_vencimento)
        print("Mês do Vencimento: ", self.mes_vencimento)
        print("Ano do vencimento: ", self.ano_vencimento)
        print("Valor: ", self.valor)

