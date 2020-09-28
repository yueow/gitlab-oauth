from django.shortcuts import render
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin


class SignInView(SuccessMessageMixin, LoginView):
    template_name = 'signin.html'
    redirect_authenticated_user = True
    success_message = "You logged in successfuly"

class HomeView(View):
    template_name = 'index.html'
    def get(self, request, *args, **kwargs):
        ctx = {}
        return render(request, self.template_name, ctx)
