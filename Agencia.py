"""
Agencia.py

Módulo com classes que representam agências bancárias comuns, premium e virtuais.
"""

from random import randint

class Agencia:
    """
    Classe que representa uma agência bancária.

    Attributes:
        telefone (str): Telefone da agência.
        cnpj (str): CNPJ da agência.
        numero (int): Número da agência.
        clientes (list): Lista de clientes.
        caixa (float): Valor em caixa.
        emprestimo (list): Lista de empréstimos realizados.
    """

    def __init__(self, telefone, cnpj, numero):
        """
        Inicializa a agência.

        Args:
            telefone (str): Telefone da agência.
            cnpj (str): CNPJ da agência.
            numero (int): Número da agência.
        """
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimo = []

    def verifica_caixa(self):
        """Verifica se o caixa está acima do nível recomendado."""
        if self.caixa < 1000000:
            print(f"Caixa abaixo do nível recomendado. Caixa Atual: {format(self.caixa)}")
        else:
            print(f"O valor de caixa está ok. Caixa Atual: {format(self.caixa)}")

    def emprestimo_caixa(self, valor, cpf, juros):
        """
        Realiza um empréstimo caso o caixa tenha saldo suficiente.

        Args:
            valor (float): Valor do empréstimo.
            cpf (str): CPF do cliente.
            juros (float): Juros do empréstimo.
        """
        if self.caixa > valor:
            self.emprestimo.append((valor, cpf, juros))
        else:
            print("Empréstimo não é possível, dinheiro não disponível na caixa")

    def adicionar_cliente(self, nome, cpf, patrimonio):
        """
        Adiciona um cliente à agência.

        Args:
            nome (str): Nome do cliente.
            cpf (str): CPF do cliente.
            patrimonio (float): Patrimônio do cliente.
        """
        self.clientes.append((nome, cpf, patrimonio))

class AgenciaVirtual(Agencia):
    """
    Classe que representa uma agência virtual, herda de Agencia.

    Attributes:
        site (str): Site da agência virtual.
        caixa_paypal (float): Caixa do Paypal.
    """

    def __init__(self, site, cnpj, telefone):
        """
        Inicializa a agência virtual.

        Args:
            site (str): Site da agência.
            cnpj (str): CNPJ da agência.
            telefone (str): Telefone da agência.
        """
        self.site = site
        super().__init__(telefone, cnpj, 1234)
        self.caixa = 1000000
        self.caixa_paypal = 0

    def deposita_paypal(self, valor):
        """
        Deposita um valor no Paypal, retirando do caixa.

        Args:
            valor (float): Valor a ser depositado.
        """
        self.caixa -= valor
        self.caixa_paypal += valor

    def sacar_paypal(self, valor):
        """
        Saca um valor do Paypal, transferindo para o caixa.

        Args:
            valor (float): Valor a ser sacado.
        """
        self.caixa_paypal -= valor
        self.caixa += valor

class AgenciaComum(Agencia):
    """
    Classe que representa uma agência comum, herda de Agencia.
    """

    def __init__(self, telefone, cnpj):
        """
        Inicializa a agência comum.

        Args:
            telefone (str): Telefone da agência.
            cnpj (str): CNPJ da agência.
        """
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa = 1000000

class AgenciaPremium(Agencia):
    """
    Classe que representa uma agência premium, herda de Agencia.
    """

    def __init__(self, telefone, cnpj):
        """
        Inicializa a agência premium.

        Args:
            telefone (str): Telefone da agência.
            cnpj (str): CNPJ da agência.
        """
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa = 10000000

    def adicionar_cliente(self, nome, cpf, patrimonio):
        """
        Adiciona cliente apenas se o patrimônio for superior a 1 milhão.

        Args:
            nome (str): Nome do cliente.
            cpf (str): CPF do cliente.
            patrimonio (float): Patrimônio do cliente.
        """
        if patrimonio > 1000000:
            super().adicionar_cliente(nome, cpf, patrimonio)
        else:
            print('O cliente não tem o patrimônio mínimo necessário para entrar na agência')
