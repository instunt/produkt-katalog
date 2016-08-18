from django.shortcuts import render
from .models import Produkt
from .forms import produktForm
from datetime import datetime
from django.contrib.auth.decorators import login_required

@login_required
def main(request):
  produkty = Produkt.objects.all()
  
  if request.method == 'POST':
    form = produktForm(request.POST)
    data = request.POST
    if form.is_valid():
      produktnew = form.save(commit=False)
      produktnew.nazov = data[u'nazov']
      produktnew.shoplinka = data[u'shoplinka']
      produktnew.obrlinka = data[u'obrlinka']      
      produktnew.vytvoreny = datetime.now()
      produktnew.save()            
  else:
    form = produktForm()        
  
  return render(request, 'main/index.html', {'produkty': produkty, 'form': form })
