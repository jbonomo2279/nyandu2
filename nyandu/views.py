from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def index(request):
    return HttpResponse("¡Hola 🌍!, esta es la página de Nyandü (en construcción)")


@login_required
def principal(request):
    return render(
    request,
    'nyandu/principal.html',
     context={},
)

