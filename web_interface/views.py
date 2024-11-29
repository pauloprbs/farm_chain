from django.shortcuts import render

# Create your views here.
import requests
import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from blockchain import Blockchain
from django.conf import settings

blockchain = Blockchain()

API_URL = "http://127.0.0.1:8000/api"  # Substitua pelo endpoint correto da sua API REST

def home(request):
    return render(request, 'web_interface/index.html')

def new_transaction(request):
    if request.method == 'POST':
        # Dados da transação
        transaction_data = {
            'id_medicamento': request.POST['id_medicamento'],
            'nome': request.POST['nome'],
            'lote': request.POST['lote'],
            'data_validade': request.POST['data_validade'],
            'fabricante': request.POST['fabricante'],
            'status': request.POST['status'],
        }
        
        # Envia a transação para a API REST
        response = requests.post(f"{API_URL}/new_transaction/", json=transaction_data)
        
        if response.status_code == 200:
            # Sucesso
            return render(request, 'web_interface/transaction_result.html', {
                'message': 'Transação realizada com sucesso!'
            })
        else:
            # Erro
            error_data = response.json()
            return render(request, 'web_interface/transaction_result.html', {
                'error': error_data['error'],
                'details': error_data['details']
            })
    else:
        # Se o método não for POST, renderize o formulário para criar uma transação
        return render(request, 'web_interface/new_transaction.html')

def mine_block(request):
    response = requests.get(f"{API_URL}/mine_block/")
    formatted_block = json.dumps(response.json(), indent=4)  # Formatar com indentação
    return render(request, 'web_interface/block_mined.html', {'block': formatted_block})

def view_blockchain(request):
    # Fazendo a requisição para a API e obtendo os dados da blockchain
    response = requests.get(f"{API_URL}/blockchain/")
    
    # Formatando o JSON obtido com indentação
    formatted_json = json.dumps(response.json(), indent=4)
    
    # Retornando o template com o JSON formatado
    return render(request, 'web_interface/blockchain.html', {'blockchain': formatted_json})