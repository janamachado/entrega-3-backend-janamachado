from django.shortcuts import render
# from transactions.upload import UploadFile
from django.http import HttpResponse
# # from transactions.function import handle_uploaded_file

from .models import Transaction
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from rest_framework.views import APIView


from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm

# function to handle an uploaded file.
from .function import handle_uploaded_file

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        # print(request.FILES['file'])
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect("/api/list/")
    else:
        form = UploadFileForm()
    return render(request, 'index.html', {'form': form})

class ListTransactionView(APIView):


    def get(self, request):
    
        data = list(Transaction.objects.values(
            "type", "value", "date", "cpf", "hour", "shop_owner", "shop_name"
        ))
        
        return render(request, "list_infos.html", {"data": data})