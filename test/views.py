from django.shortcuts import render
import random


def rand():
    return random.randint(1, 100)


def about(request):
    return render(request, 'about.html', {'greeting_text': rand(),
                                          'greeting': 'Hello, world'})
