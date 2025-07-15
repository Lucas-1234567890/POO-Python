"""
contasBanco.py

Módulo com as classes ContaCorrente e CartaoCredito para simulação de operações bancárias.
"""

from datetime import datetime
import pytz
from random import randint


class ContaCorrente:
    """
    Classe que simula uma conta corrente bancária.

    Attributes:
        nome (str): Nome do titular.
        cpf (str): CPF do titular.
        _saldo (float): Saldo da conta.
        _limite (float): Limite do cheque especial.
        __agencia (int): Número da agência.
        _num_conta (int): Número da conta.
        _transacoes (list): Histórico de transações.
        _cartoes (list): Lista de cartões vinculados.
    """

    @staticmethod
    def _data_hora():
        """
        Retorna a data e hora atual no fuso horário do Brasil.

        Returns:
            str: Data e hora formatadas.
        """
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BB = datetime.now(fuso_BR)
        return horario_BB.strftime("%d/%m/%Y %H:%M:%S")

    def __init__(self, nome, cpf, agencia, num_conta):
        """
        Inicializa a conta corrente com os dados do titular.

        Args:
            nome (str): Nome do titular.
            cpf (str): CPF do titular.
            agencia (int): Número da agência.
            num_conta (int): Número da conta.
        """
        self.nome = nome
        self.cpf = cpf
        self._saldo = 0
        self._limite = None
        self.__agencia = agencia
        self._num_conta = num_conta
        self._transacoes = []
        self._cartoes = []

    def consultar_saldo(self):
        """Exibe o saldo atual do cliente."""
        print(f'{self.nome}, seu saldo atual é: R${self._saldo:,.2f}')

    def depositar(self, valor):
        """
        Deposita um valor na conta e registra no histórico.

        Args:
            valor (float): Valor a ser depositado.
        """
        self._saldo += valor
        self._transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))

    def _limite_conta(self):
        """
        Retorna o limite de cheque especial.

        Returns:
            float: Limite da conta.
        """
        self._limite = -1000
        return self._limite

    def sacar_dinheiro(self, valor):
        """
        Realiza o saque se houver saldo ou limite disponível.

        Args:
            valor (float): Valor a ser sacado.
        """
        if self._saldo - valor < self._limite_conta():
            print("Você não tem saldo suficiente para sacar esse valor.")
            self.consultar_saldo()
        else:
            self._saldo -= valor
            self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))

    def consultar_limite_chequeespecial(self):
        """Exibe o limite de cheque especial disponível."""
        print(f"Seu limite de cheque especial é de R${self._limite_conta():,.2f}")

    def consultar_historico_transacoes(self):
        """Exibe o histórico de transações da conta."""
        print(f'Histórico de transações de {self.nome}')
        print('Valor\tSaldo\t\tData e Hora')
        for valor, saldo, data in self._transacoes:
            print(f'R${valor:,.2f}\tR${saldo:,.2f}\t{data}')

    def transferir(self, valor, conta_destino):
        """
        Realiza transferência para outra conta se houver saldo disponível.

        Args:
            valor (float): Valor a ser transferido.
            conta_destino (ContaCorrente): Conta que receberá a transferência.
        """
        if self._saldo - valor < self._limite_conta():
            print("Saldo insuficiente para transferência:")
            self.consultar_saldo()
        else:
            self._saldo -= valor
            self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))
            conta_destino._saldo += valor
            conta_destino._transacoes.append((valor, conta_destino._saldo, ContaCorrente._data_hora()))


class CartaoCredito:
    """
    Classe que representa um cartão de crédito vinculado a uma conta corrente.

    Attributes:
        numero (int): Número do cartão.
        titular (str): Nome do titular.
        validade (str): Validade do cartão.
        cod_seguranca (str): Código de segurança do cartão.
        limite (float): Limite do cartão.
        _senha (str): Senha do cartão.
        conta_corrente (ContaCorrente): Conta corrente vinculada.
    """

    @staticmethod
    def _data_hora():
        """
        Retorna a data e hora atual no fuso horário do Brasil.

        Returns:
            datetime: Data e hora atual.
        """
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BB = datetime.now(fuso_BR)
        return horario_BB

    def __init__(self, titular, conta_corrente):
        """
        Inicializa o cartão de crédito.

        Args:
            titular (str): Nome do titular.
            conta_corrente (ContaCorrente): Conta corrente vinculada.
        """
        self.numero = randint(1000000000000000, 9999999999999999)
        self.titular = titular
        self.validade = f'{CartaoCredito._data_hora().month}/{CartaoCredito._data_hora().year + 4}'
        self.cod_seguranca = f'{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}'
        self.limite = 1000
        self._senha = '1234'
        self.conta_corrente = conta_corrente
        conta_corrente._cartoes.append(self)

    @property
    def senha(self):
        """
        Retorna a senha do cartão.

        Returns:
            str: Senha atual.
        """
        return self._senha

    @senha.setter
    def senha(self, valor):
        """
        Define a senha do cartão se for um valor válido.

        Args:
            valor (str): Nova senha.
        """
        if len(valor) == 4 and valor.isnumeric():
            self._senha = valor
        else:
            print("Senha incorreta!")
