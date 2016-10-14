from django.shortcuts import render
from .models import Produkt, Ceny
from .forms import produktForm, cenyForm
from datetime import datetime
from django.contrib.auth.decorators import login_required
import pdb

@login_required
def main(request):
  form = produktForm()   
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
  produkty = Produkt.objects.all()
  return render(request, 'main/index.html', {'produkty': produkty, 'form': form })

@login_required
def ceny(request):

  datum = datetime.now  
  formc = cenyForm()      
  if request.method == 'POST':
    formc = cenyForm(request.POST)
    datas = request.POST
    if formc.is_valid():
      cenynew = formc.save(commit=False)
      cenynew.nazov = datas[u'nazov']
      cenynew.vyrobca = datas[u'vyrobca']
      cenynew.cena = datas[u'cena']
      cenynew.mena = datas[u'mena']
      cenynew.datum = datas[u'datum']
      cenynew.miesto = datas[u'miesto']
      cenynew.obrlinka = 'n/a'           
      cenynew.save()
      
  else:
    print datum
    
  ceny = Ceny.objects.all()
#  cenys = [i for i in ceny]
  output = []  
  for elem in ceny: 
    
    skip = 0     
    for an in output:
          
      if elem.nazov == an.nazov:
        skip = 1
    if skip == 0:
      output.append(elem)  

  return render(request, 'main/ceny.html', {'output': output, 'formc': formc})
  
@login_required
def cenyDetail(request, uk):

  ceny = Ceny.objects.filter(id=uk)[0]
  nazov = ceny.nazov
  vyrobca = ceny.vyrobca
  
  ceny = Ceny.objects.filter(nazov=nazov)
  
  datum = datetime.now
  formc = cenyForm()
  formc.fields["nazov"].initial = nazov
  formc.fields["vyrobca"].initial = vyrobca
  
  if request.method == 'POST':
    formc = cenyForm(request.POST)
    data = request.POST
    pdb.set_trace()
    if formc.is_valid():
      cenynew = formc.save(commit=False)
      cenynew.nazov = data[u'nazov']
      cenynew.vyrobca = data[u'vyrobca']
      cenynew.cena = data[u'cena']
      cenynew.mena = data[u'mena']
      cenynew.datum = data[u'datum']
      cenynew.miesto = data[u'miesto']                
      cenynew.save()
  else:
      print nazov
      
  return render(request, 'main/cenydetail.html', {'ceny': ceny, 'formc': formc, 'nazov': nazov, 'vyrobca': vyrobca })      