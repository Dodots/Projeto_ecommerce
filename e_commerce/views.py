from django.shortcuts import render

def home_page(request):
    context = {
                    "title": "Home Page",
                    "content": "Bem vindo a Home Page",
              }
    return render(request, "home_page.html", context)