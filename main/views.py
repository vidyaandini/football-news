from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406432513',
        'name': 'Vidya Pramudita Andini',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)