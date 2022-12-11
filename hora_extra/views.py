import csv
import json

from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
import xlwt

from .forms import RegistroHoraExtraForm
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import HoraExtra


class HoraExtraList(ListView):
    model = HoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return HoraExtra.objects.filter(funcionario__empresa= empresa_logada)


class HoraExtraEdit(UpdateView):
    model = HoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraEdit, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class HoraExtraDelete(DeleteView):
    model = HoraExtra
    success_url = reverse_lazy('list_hora_extra')


class HoraExtraNovo(CreateView):
    model = HoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraNovo, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class UtilizouHoraExtra(View):
    def post(self, *args, **kwargs):
        response = json.dumps({'mensagem': 'requisição executada'})
        registro_hora_extra = HoraExtra.objects.get(id=kwargs['pk'])
        registro_hora_extra.utilizada = True
        registro_hora_extra.save()
        return HttpResponse(response, content_type='application/json')


class ExportarParaCsv(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefile.csv"'

        registro_he = HoraExtra.objects.filter(utilizado=False)

        writer = csv.writer(response)
        writer.writerow(['ID', 'Motivo', 'Funcionario', 'Horas'])

        for registro in registro_he:
            writer.writerow([registro.id, registro.motivo,
                             registro.funcionario, registro.horas])

        return response

class ExportarExcel(View):
    def get(self, request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="users.xls"'

        wb = xlwt.Workbook(encoding='urf-8')
        ws = wb.add_sheet('Users')

        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold= True

        columns = ['ID', 'Motivo', 'Funcionario', 'Horas']

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        font_style = xlwt.XFStyle()

        registros = HoraExtra.objects.filter(utilizado=False)

        row_num = 1
        for registro in registros:
            ws.write(row_num, 0, registro.id, font_style)
            ws.write(row_num, 1, registro.motivo, font_style)
            ws.write(row_num, 2, registro.funcionario.nome, font_style)
            ws.write(row_num, 3, registro.horas, font_style)
            row_num+= 1

        wb.save(response)
        return  response