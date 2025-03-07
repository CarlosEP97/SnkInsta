# Django
from django.http import HttpResponse,JsonResponse


# Utilities
from datetime import datetime
import json


def hello_world(request):
    """Return a greeting."""
    return HttpResponse('Oh, hi! Current server time is {now}'.format(now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    ))


def sorted_integers(request):
    """Hi."""
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted successfully.'
    }
    return JsonResponse(data)

def say_hi(request,name,age):
    """Return a greeting."""
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello, {}! Welcome to Platzigram'.format(name)
    return HttpResponse(message)