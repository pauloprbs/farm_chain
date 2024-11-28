from django.urls import path
from . import views

urlpatterns = [
    path('new_transaction/', views.new_transaction, name='new_transaction'),
    path('mine_block/', views.mine_block, name='mine_block'),
    path('blockchain/', views.view_blockchain, name='view_blockchain'),
    path('', views.home, name='home'),
]