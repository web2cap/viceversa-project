from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def reverse(request):
    usertext = request.POST['usertext']
    reversed = usertext[::-1]
    wcount = len(usertext.split())
    print(wcount)
    data = {
        'reversed' : reversed,
        'wcount'   : wcount,
        'usertext' : usertext
            }
    return render(request,'reverse.html',data)