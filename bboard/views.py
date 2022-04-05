from django.http import HttpResponse
from django.template import loader

from .models import Bb

# Create your views here.

def index(request):
    template = loader.get_template('bboard/index.html')
    bbs = Bb.objects.order_by('-published')
    context = {'bbs': bbs}
    '''
    s = 'Список объявлений \r\n\r\n\r\n'
    for bb in Bb.objects.order_by('-published'):
        s += bb.title + '\r\n' + bb.content + '\r\n\r\n'
    '''
    return HttpResponse(template.render(context, request))     