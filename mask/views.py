from datetime import datetime,timezone
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth import login, logout
from .models import US,ZUS,Kontrah
from django.contrib import messages
from django.shortcuts import redirect
from django.forms import inlineformset_factory
from .forms import ZusForm,UsForm
from .models import Content
from .forms import DocumentForm

#from django.shortcuts import render_to_response
#def index(request):
 #   return HttpResponse("Helo, this will be the mask Porojekt for the Meritum Accounting Office")


"""def widokzus(request):
    device = ZUS.objects.select_related('mask_zus', 'mask_kontrah','mask_slownik2','mask_slownik1').get(46)
    dane = device.devices_data_set.all()
    return render(request, 'widokzus.html',{'device': device, 'dane': dane})"""


def widokzus(request):
  ##  latest_question_list = ZUS.objects.order_by('zus10')
    zus_dane =[p.id for p in ZUS.objects.all()]
    #zus_dane =  ZUS.objects.all()
    kontrah_dane=Kontrah.objects.all()

    razem = (zus_dane , '   dodany ostatni rekord w ZUS ')
    return HttpResponse(razem)





def index(request):

    return render(request, 'mask/index.html')

def home(request):

    return render(request, 'mask/index.html')

def kontrah_add(request):
    if request.method == 'POST':

        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Content(docfile=request.FILES['docfile'])
            newdoc.save()
    return render(request, 'mask/kontrah.html')




def loguj(request):
    """Logowanie użytkownika"""
    from django.contrib.auth.forms import AuthenticationForm
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, "Zostałeś zalogowany!")
            return redirect(reverse('mask:index'))

    kontekst = {'form': AuthenticationForm()}
    return render(request, 'mask/loguj.html', kontekst)


def wyloguj(request):
    """Wylogowanie użytkownika"""
    logout(request)
    messages.info(request, "Zostałeś wylogowany!")
    return redirect(reverse('mask:index'))


def detail(request,pk):
    post = get_object_or_404(ZUS, pk=pk)
    return render(request, 'mask/detail.html', {'form': post})



"""
@cache_page(60 * 15)
@csrf_protect"""
def zusaddoperations(request):
    if request.method == "POST":
        form = ZusForm(request.POST)
        if form.is_valid():
            zus_add = form.save(commit=False)
            zus_add.pracownik = request.user
            zus_add.date = datetime.now(timezone.utc).astimezone()
            zus_add.save()
            zus_get_pk=zus_add.pk
            request.url=form.data.get(zus_add.pk)
            #session['temp_data'] = form.cleaned_data
            return render(request,'mask/detailzus.html')
            #return redirect('detail', pk=zus_add.pk)
    else:
        form = ZusForm()
    return render(request, 'mask/zus.html', {'form': form})


def usaddoperations(request):

    if request.method == "POST":
        form = UsForm(request.POST)
        if form.is_valid():
            us_add = form.save(commit=False)
            us_add.pracownik = request.user
            us_add.date = datetime.now(timezone.utc).astimezone()
            us_add.save()
            return render(request, 'mask/detailus.html')
            #return redirect('post_detail', pk=us_add.pk)
    else:
        form = UsForm()
    return render(request, 'mask/us.html', {'form': form})
