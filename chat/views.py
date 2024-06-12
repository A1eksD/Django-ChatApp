from django.shortcuts import render

def index(request):
    if request.method == 'POST':
        print("Received date " + request.POST['textMessage'])
    return render(request, 'chat/index.html', {'username': 'Aleks'})