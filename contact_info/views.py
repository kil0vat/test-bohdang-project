from django.shortcuts import render
from contact_info.models import ContactInfo
from django.template import loader, RequestContext
from django.http import HttpResponse 
# Create your views here.

def base(request):
	contact_info_list = ContactInfo.objects.all()
	template = loader.get_template('contact_info/base.html')
	context = RequestContext(request, {
		'contact_info_list': contact_info_list,
	})
	return HttpResponse(template.render(context))
