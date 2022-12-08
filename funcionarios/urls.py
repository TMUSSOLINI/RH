from django.urls import path
from .views import FuncionariosList, FuncionarioEdit, FuncionarioDelete, FuncionarioNovo, relatorio_funcionario

urlpatterns = [
    path('', FuncionariosList.as_view(), name='list_funcionarios'),
    path('novo/', FuncionarioNovo.as_view(), name='create_funcionario'),
    path('editar/<int:pk>/', FuncionarioEdit.as_view(), name='update_funcionario'),
    path('deletar/<int:pk>/', FuncionarioDelete.as_view(), name='delete_funcionario'),
    path('relatorio-funcionario', relatorio_funcionario, name='relatorio_funcionario'),
]
