from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .forms import Log

BASE = {
'BASE_TITLE' : "ETL",
'BASE_MAIN_TITLE' : "Extract Load Transformation Data System",
'BASE_MODAL_TITLE' : "etl",
'BASE_MODAL_CLOSE' : "Login",
'BASE_FOOTER_TITLE' : "MENU",
'BASE_FOOTER_SUBTITLE' : "ETL SYSTEM",
'BASE_FOOTER_MEDIUM' : "REGRESAR ARRIBA",
'BASE_FOOTER_LAST' : "Diana Hernandez, Felipe Ruiz",
'form' : ''
}

def login(request):
	if request.method == 'POST':
		form = Log(request.POST)
		if form.is_valid():

			if form.cleaned_data['user'] == 'admin' \
			and form.cleaned_data['password'] == '123':

				return HttpResponseRedirect('handle')

			else:
				BASE['form'] = Log()
				BASE['BASE_FOOTER_TITLE'] = "wrong password"
				return render(request, 'etl/login.html', BASE )
		else:
			return HttpResponseRedirect('/wrong/')

	# if a GET (or any other method) we'll create a blank form
	else:
		BASE['form'] = Log()
		return render(request, 'etl/login.html', BASE )

