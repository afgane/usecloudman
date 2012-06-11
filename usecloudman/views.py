# -*- coding: iso-8859-15 -*- needed for ŠĐŽČĆ
from django.template import RequestContext
from django.shortcuts import render_to_response

def home(request):
    pageContext = {'index_content': "content"}
    return render_to_response("index.html", pageContext, 
                              context_instance=RequestContext(request))
