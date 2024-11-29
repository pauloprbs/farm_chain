import hashlib
import json
import time

class Blockchain:
    _instance = None  # Atributo de classe para armazenar a instância

    def __init__(self):
        # implementação da classe
        pass

    def __new__(cls, *args, **kwargs):
        """
        Método para garantir que a blockchain seja uma instância única
        """
        if not cls._instance:
            cls._instance = super(Blockchain, cls).__new__(cls, *args, **kwargs)
            cls._instance.__initialize()
        return cls._instance

    def __initialize(self):
        """Método para inicializar a blockchain e criar o bloco gênesis"""
        self.chain = []
        self.pending_transactions = []
        self.new_block(previous_hash='1', proof=100)  # Bloco gênesis

    def new_block(self, proof, previous_hash=None):
        """
        Cria um novo bloco e o adiciona à cadeia
        :param proof: Prova de trabalho
        :param previous_hash: Hash do bloco anterior
        :return: Novo bloco
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        
        self.pending_transactions = []  # Limpa as transações pendentes
        self.chain.append(block)  # Adiciona o bloco à cadeia
        return block

    def new_transaction(self, id_medicamento, nome, lote, data_validade, fabricante, status):
        """
        Adiciona uma nova transação à lista de transações pendentes.
        :param id_medicamento: ID único do medicamento
        :param nome: Nome do medicamento
        :param lote: Lote do medicamento
        :param data_validade: Data de validade do medicamento
        :param fabricante: Nome do fabricante do medicamento
        :param status: Status da transação (ex: "fabricação", "encaminhado", "vendido", etc.)
        :return: O índice do bloco que armazenará essa transação
        """
        transaction = {
            'id_medicamento': id_medicamento,
            'nome': nome,
            'lote': lote,
            'data_validade': data_validade,
            'fabricante': fabricante,
            'status': status,
        }
        self.pending_transactions.append(transaction)
        return self.last_block['index'] + 1

    def proof_of_work(self, last_proof):
        """
        Algoritmo de prova de trabalho para encontrar a prova de trabalho válida
        :param last_proof: Prova do bloco anterior
        :return: A nova prova de trabalho
        """
        proof = 0
        while not self.valid_proof(last_proof, proof):
            proof += 1
        return proof

    def valid_proof(self, last_proof, proof):
        """
        Verifica se a prova de trabalho é válida
        :param last_proof: Prova do bloco anterior
        :param proof: Prova do bloco atual
        :return: True se a prova for válida, caso contrário False
        """
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    def hash(self, block):
        """
        Gera o hash de um bloco
        :param block: Bloco
        :return: O hash do bloco
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        """
        Retorna o último bloco da cadeia
        :return: Último bloco
        """
        return self.chain[-1]