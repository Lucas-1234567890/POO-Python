from contasBanco import *
from Agencia import *

if __name__ == "__main__":
    # Criando uma conta corrente
    conta_lucas = ContaCorrente('Lucas', "111.222.333-44", 1234, 4321)
    conta_lucas.depositar(500)
    conta_lucas.consultar_saldo()
    conta_lucas.sacar_dinheiro(200)
    conta_lucas.consultar_historico_transacoes()

    # Criando um cartão de crédito
    cartao_lucas = CartaoCredito('Lucas', conta_lucas)
    cartao_lucas.senha = '4563'
    print(f'Senha do cartão: {cartao_lucas.senha}')

    # Criando agências
    agencia_comum = AgenciaComum('31-9999-9999', '00.111.222/0001-33')
    agencia_premium = AgenciaPremium('31-9888-8888', '00.111.222/0001-44')
    agencia_virtual = AgenciaVirtual('www.bancovirtual.com', '00.111.222/0001-55', '31-9777-7777')

    # Adicionando clientes nas agências
    agencia_comum.adicionar_cliente('Lucas', '111.222.333-44', 5000)
    agencia_premium.adicionar_cliente('Rico', '555.666.777-88', 2000000)

    # Verificando caixa
    agencia_comum.verifica_caixa()
    agencia_premium.verifica_caixa()
    agencia_virtual.verifica_caixa()

    # Usando paypal da agência virtual
    agencia_virtual.deposita_paypal(50000)
    agencia_virtual.sacar_paypal(20000)

    # Prints finais de demonstração
    print(conta_lucas.__dict__)
    print(cartao_lucas.__dict__)
    print(agencia_comum.__dict__)
    print(agencia_premium.__dict__)
    print(agencia_virtual.__dict__)

    help(ContaCorrente)
    help(Agencia)
