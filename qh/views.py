from django.http import HttpResponse
from django.template import loader
def index(request):
  template = loader.get_template('ttdrm.html')
  return HttpResponse(template.render())
  first_name = form.cleaned_data['first_name']
  last_name = form.cleaned_data['last_name']


   
