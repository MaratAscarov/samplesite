# from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render

from .models import Bb

# Create your views here.

def index(request):
    # template = loader.get_template('bboard/index.html')
    bbs = Bb.objects.order_by('-published')
    # context = {'bbs': bbs}
    return render(request, 'bboard/index.html', {'bbs': bbs})  
    # return HttpResponse(template.render(context, request))     
    '''
    s = 'Список объявлений \r\n\r\n\r\n'
    for bb in Bb.objects.order_by('-published'):
        s += bb.title + '\r\n' + bb.content + '\r\n\r\n'
    
    return HttpResponse(s, content_type = 'text/plain; charset=utf-8')
    '''
