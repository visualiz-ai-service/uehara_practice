from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView as BaseLoginView, LogoutView as BaseLogoutView

from .forms import SingUpForm, LoginForm

class IndexView(TemplateView):

    template_name = 'index.html'

class SignupView(CreateView):

    form_class = SingUpForm #作成した登録用フォームを設定
    template_name = "accounts/signup.html"
    success_url =reverse_lazy("accounts:index")

    def form_valid(self, form):

        response = super().form_valid(form)
        account_id = form.cleaned_data.get('account_id')
        password = form.cleaned_data.get('password')
        user = authenticate(account_id = account_id, password = password)

        login(self.request, user)
        return response
    
class LoginView(BaseLoginView):
    from_class = LoginForm
    template_name = "accounts/login.html"

class LogoutView(BaseLogoutView):
    success_url = reverse_lazy("accounts:index")


