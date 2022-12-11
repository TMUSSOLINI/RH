from django.urls import path
from .views import ( HoraExtraList, HoraExtraEdit, HoraExtraDelete,HoraExtraNovo,
                     UtilizouHoraExtra,ExportarParaCsv, ExportarExcel)


urlpatterns = [
    path('', HoraExtraList.as_view(), name='list_hora_extra'),
    path('novo/', HoraExtraNovo.as_view(), name='create_hora_extra'),
    path('editar/<int:pk>/', HoraExtraEdit.as_view(), name='update_hora_extra'),
    path('utilizou-hora-extra/<int:pk>/', UtilizouHoraExtra.as_view(), name='utilizou-hora-extra'),
    path('deletar/<int:pk>/', HoraExtraDelete.as_view(), name='delete_hora_extra'),
    path('exportar-csv', ExportarParaCsv.as_view(), name='exportar_csv'),
    path('exportar-excel', ExportarExcel.as_view(), name='exportar_excel'),
]
