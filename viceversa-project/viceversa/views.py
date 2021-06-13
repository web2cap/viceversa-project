from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def reverse(request):
    reversed = request.POST['usertext'][::-1]
    data = {'reversed' : reversed}
    return render(request,'reverse.html',data)