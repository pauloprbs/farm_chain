from django.urls import path
from .views import BlockchainView, NewTransactionView, MineBlockView

urlpatterns = [
    path('api/blockchain/', BlockchainView.as_view(), name='get_blockchain'),
    path('blockchain/', BlockchainView.as_view(), name='blockchain'),
    path('new_transaction/', NewTransactionView.as_view(), name='new_transaction'),
    path('mine_block/', MineBlockView.as_view(), name='mine_block'),
]

