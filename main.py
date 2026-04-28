# Importa a classe financeiro
from cadastro import Cadastro
from movimentacao import Movimentacao
from exibir import Exibir
from calculo import Calculo


# Função principal do sistema
def menu():

    # Cria os objetos principais do sistema
    cadastro = Cadastro ()
    movimentacao = Movimentacao (cadastro)
    exibir = Exibir (cadastro)
    calculo = Calculo (cadastro)

    # Mantém o sistema em execução
    while True:
        try:
            print("\n###################################")
            print("### SMARTFLUX: SISTEMA DE GESTÃO ###")
            print("####################################\n")            
            
            print("[1]. Cadastrar nova conta")
            print("[2]. Listar todas as contas cadastradas")
            print("[3]. Calcular valor a pagar")
            print("[4]. Consultar contas cadastradas")
            print("[5]. Atualizar contas cadastradas")
            print("[6]. Excluir contas cadastradas")
            print("[0]. Sair")

            opcao = int(input("\nEscolha uma opção: "))

            if opcao == 1:
                cadastro.cadastrar_conta()

            elif opcao == 2:
                exibir.listar_contas()

            elif opcao == 3:
                calculo.total()
        
            elif opcao == 4:
                exibir.pesquisar_contas()

            elif opcao == 5:
                movimentacao.atualizar_contas()

            elif opcao == 6:
                movimentacao.excluir_contas()

            elif opcao == 0:
                print("\nSistema encerrado.")
                break

            else:
                print("\nOpção inválida.")
    
        except ValueError:
            print("Digite um valor válido")



menu()