from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .blockchain import Blockchain

class BlockchainView(APIView):
    def get(self, request, format=None):
        """
        Retorna todos os blocos da cadeia
        """
        blockchain = Blockchain()
        return Response({
            'chain': blockchain.chain,
            'length': len(blockchain.chain)
        })

class NewTransactionView(APIView):
    def post(self, request, format=None):
        """
        Adiciona uma nova transação à cadeia (informações detalhadas sobre o medicamento)
        """
        id_medicamento = request.data.get('id_medicamento')
        nome = request.data.get('nome')
        lote = request.data.get('lote')
        data_validade = request.data.get('data_validade')
        fabricante = request.data.get('fabricante')
        status = request.data.get('status')

        blockchain = Blockchain()  # Instância única da blockchain
        blockchain.new_transaction(id_medicamento, nome, lote, data_validade, fabricante, status)

        return Response({
            'message': "Transaction added to the next block."
        }) 


class MineBlockView(APIView):
    def get(self, request, format=None):
        """
        Minerando um novo bloco e adicionando à blockchain
        """
        blockchain = Blockchain()  # Instância única da blockchain
        last_block = blockchain.last_block
        proof = blockchain.proof_of_work(last_block['proof'])
        previous_hash = blockchain.hash(last_block)

        # Minerando um novo bloco
        block = blockchain.new_block(proof, previous_hash)

        return Response({
            'message': "New block mined",
            'block': block
        })

    
