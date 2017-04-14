from django.shortcuts import redirect
from django.views.generic import TemplateView
from allauth.account import views


class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context

home_view = HomeView.as_view()


class SigninView(views.LoginView):
    template_name = 'signin/index.html'

    def dispatch(self, request, *args, **kwargs):
        response = super(SigninView, self).dispatch(request, *args, **kwargs)
        return response

    def form_valid(self, form):
      user = form.user
      return super(SigninView, self).form_valid(form)

signin_view = SigninView.as_view()


class SignupView(views.SignupView):
    template_name = 'signup/index.html'

    def get_context_data(self, **kwargs):
        context = super(SignupView, self).get_context_data(**kwargs)
        return context

signup_view = SignupView.as_view()


class SignoutView(views.LogoutView):

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            self.logout()
        return redirect('/')

signout_view = SignoutView.as_view()