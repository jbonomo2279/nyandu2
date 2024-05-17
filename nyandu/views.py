from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Vuelo, Avion
from django.views import generic


def index(request):
    return HttpResponse("¡Hola 🌍!, esta es la página de Nyandü (en construcción)")


@login_required
def principal(request):
    return render(
    request,
    'nyandu/principal.html',
     context={},
)


class VueloListView(generic.ListView):
    model = Vuelo


class VueloDetailView(generic.DetailView):
    model = Vuelo

class AvionListView(generic.ListView):
    model = Avion


class AvionDetailView(generic.DetailView):
    model = Avion