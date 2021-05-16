from datetime import timezone

from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import login, logout
from .models import US,ZUS,Kontrah
from django.contrib import messages
from django.shortcuts import redirect
from django.forms import inlineformset_factory
from .forms import ZusForm,UsForm

#def index(request):
 #   return HttpResponse("Helo, this will be the mask Porojekt for the Meritum Accounting Office")





def index(request):

    return render(request, 'mask/index.html')

def home(request):

    return render(request, 'mask/index.html')

def kontrah_add(request):

    return render(request, 'mask/kontrah.html')

"""def zus(request):
    zus = ZUS.objects.order_by('c')[:5]
    contex = {'zus': zus, }
    return render(request, 'mask/zus.html', contex)"""


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


"""def zusaddoperations(request):
    form = ZusForm()
    return render(request, 'mask/zus.html' , {'form': form}
                  )"""



def zusaddoperations(request):
    if request.method == "POST":
        form = ZusForm(request.POST)
        if form.is_valid():
            zus_add = form.save(commit=False)
            zus_add.pracownik = request.user
            zus_add.date = timezone.now()
            zus_add.save()
            return redirect('post_detail', pk=zus_add.pk)
    else:
        form = ZusForm()
    return render(request, 'mask/zus.html', {'form': form})

def usaddoperations(request):
    if request.method == "POST":
        form = UsForm(request.POST)
        if form.is_valid():
            us_add = form.save(commit=False)
            us_add.pracownik = request.user
            us_add.date = timezone.now()
            us_add.save()
            return redirect('post_detail', pk=us_add.pk)
    else:
        form = UsForm()
    return render(request, 'mask/us.html', {'form': form})
