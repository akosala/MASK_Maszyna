from django.shortcuts import render
from django.http import Http404
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
#import marcin
from django.contrib.auth import login, logout
from .models import US,ZUS,Kontrah
from django.contrib import messages
from django.shortcuts import redirect

#def index(request):
 #   return HttpResponse("Helo, this will be the mask Porojekt for the Meritum Accounting Office")





def index(request):

    return render(request, 'mask/index.html')

def home(request):

    return render(request, 'mask/index.html')

def kontrah_add(request):

    return render(request, 'mask/kontrah.html')

def zus(request):
    zus = ZUS.objects.order_by('c')[:5]
    contex = {'zus': zus, }
    return render(request, 'mask/zus.html', contex)


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
"""
def ZUS(request, pk):
    Zus_add = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10 )
    customer = Customer.objects.get(id=pk)
    formset = Zus_add(queryset=ZUS.objects.none(),instance=kontrah)
 
    if request.method == 'POST':
        
        formset = OrderFormSet(request.POST, instance=kontrah)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'form':formset}
    return render(request, 'accounts/order_form.html', context)"""


