from django.shortcuts import render
from django.views import View

# Create your views here


class Loginview(View):
    
    template_name = 'auth/login.html'

    def get(self, request):
        return render(request, self.template_name)
