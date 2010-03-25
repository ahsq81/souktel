from django.http import HttpResponse
from rapidsms.webui.utils import render_to_response
from models import SrProfile


def index(request):

    try:
        SrProfile_opj = SrProfile.objects.all()
        numberof_M = (float) (SrProfile.objects.filter(sex='M').count())/(SrProfile.objects.count())
        numberof_F = (float) (SrProfile.objects.filter(sex='F').count())/(SrProfile.objects.count())

    except Exception, e:
        print e
        return HttpResponse("Error: %s" % e)


    return render_to_response(request,'survey/index.html',{"profiles":SrProfile_opj, "n_male": numberof_M , "n_female":numberof_F})

def profile(request, userid):
    profile = SrProfile.objects.get(id = userid)
    return render_to_response(request,'survey/index.html',{"profile":profile})