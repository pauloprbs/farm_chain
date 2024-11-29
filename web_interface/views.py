from django.shortcuts import render

# Create your views here.
import requests
from django.shortcuts import render, redirect
from django.http import JsonResponse
from blockchain import Blockchain

blockchain = Blockchain()

API_URL = "http://127.0.0.1:8000/api"  # Substitua pelo endpoint correto da sua API REST

def home(request):
    return render(request, 'web_interface/index.html')

def new_transaction(request):
    if request.method == 'POST':
        # Recuperar os dados enviados pelo formulário
        id_medicamento = request.POST.get('id_medicamento')
        nome = request.POST.get('nome')
        lote = request.POST.get('lote')
        data_validade = request.POST.get('data_validade')
        fabricante = request.POST.get('fabricante')
        status = request.POST.get('status')

        # Validar os dados (opcional)
        if not all([id_medicamento, nome, lote, data_validade, fabricante, status]):
            return JsonResponse({'error': 'Todos os campos são obrigatórios!'}, status=400)

        # Simular a criação da transação (substitua com a lógica real da API)
        transaction_data = {
            'id_medicamento': id_medicamento,
            'nome': nome,
            'lote': lote,
            'data_validade': data_validade,
            'fabricante': fabricante,
            'status': status,
        }

        # Aqui você pode integrar com sua API REST usando a variável transaction_data
        # Exemplo: requests.post(API_URL + "/new_transaction/", json=transaction_data)

        return JsonResponse({'message': 'Transação criada com sucesso!', 'data': transaction_data})

    # Renderizar o formulário para métodos GET
    return render(request, 'web_interface/new_transaction.html')

def mine_block(request):
    response = requests.get(f"{API_URL}/mine_block/")
    return render(request, 'web_interface/block_mined.html', {'response': response.json()})

def view_blockchain(request):
    response = requests.get(f"{API_URL}/blockchain/")
    return render(request, 'web_interface/blockchain.html', {'blockchain': response.json()})