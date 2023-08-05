# i have created this file --VED

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext=request.GET.get('text', 'off')
    removepunc=request.GET.get('removepunc', 'off')
    fullcaps=request.GET.get('fullcaps', 'off')
    chat_count=request.GET.get('text', 'off')

    print(djtext)
    if removepunc=='on':
        punctuations='''!@#$%^&*()_+"':<>,./?{}[]*/;'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed + char
        print(request.GET.get('removepunc', 'off'))
        param={'purpose':'removed punctuation','analyzed_text':analyzed}
        return render(request,'analyze.html',param)

    elif chat_count=='on':
        count = 0
        for x in djtext.split():
            count += 1
        param = {'purpose': 'capitalize', 'analyzed_text': count}
        return render(request, 'analyze.html', param)

    elif(fullcaps=='on'):
        analyzed=""
        for char in djtext:
            analyzed=analyzed + char.upper()
        print(request.GET.get('removepunc', 'off'))
        param={'purpose':'change to capital letter','analyzed_text':analyzed}
        return render(request,'analyze.html',param)

    else:
        return HttpResponse('<h1>Please tick the checkbox!!'
                            'ERRPR 404'
                            '<body style="background-color:red;"></body><h1>')



def PHONE_NUMBER(request):
    print(request.GET.get('text', 'default'))
    return HttpResponse('<u>'
                        '<h1>your respond has been sent.</h1>'
                        '<h1>we will contact you soon</h1>'
                        '</u>'
                        '<h2>THANK YOU!</h2>'
                        '<button><a href="/">exit</a></button>')
