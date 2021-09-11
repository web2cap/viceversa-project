from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def reverse(request):
    text = request.POST['text']
    data = {'reverse' : text[::-1],
            'text' : text
            }
    return render(request, 'reverse.html', data)