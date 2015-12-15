from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from helper.histcalculation import *

def histogram_count(request):
    template_name='RiverDance'
    a=get_template('RiverDance.html')
    a2=a.render()
    word_list=hist_calc(a2)
    t=get_template('histogram_count.html')
    html=t.render(Context({'template_name':template_name,'word_list':word_list}))
    return HttpResponse(html)

