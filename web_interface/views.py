from django.shortcuts import render

# Create your views here.
import requests
from django.shortcuts import render, redirect

API_URL = "http://127.0.0.1:8000/api"  # Substitua pelo endpoint correto da sua API REST

def home(request):
    return render(request, '/templates/web_interface/index.html')

def new_transaction(request):
    if request.method == 'POST':
        # Capturar dados do formulário
        sender = request.POST['sender']
        receiver = request.POST['receiver']
        amount = request.POST['amount']

        # Enviar dados para a API REST
        response = requests.post(f"{API_URL}/new_transaction/", json={
            'sender': sender,
            'receiver': receiver,
            'amount': amount
        })
        return render(request, 'web_interface/transaction_result.html', {'response': response.json()})
    return render(request, 'web_interface/new_transaction.html')

def mine_block(request):
    response = requests.get(f"{API_URL}/mine_block/")
    return render(request, 'web_interface/block_mined.html', {'response': response.json()})

def view_blockchain(request):
    response = requests.get(f"{API_URL}/blockchain/")
    return render(request, 'web_interface/blockchain.html', {'blockchain': response.json()})