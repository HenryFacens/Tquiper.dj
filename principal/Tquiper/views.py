from django.shortcuts import render


def startsite(request):
    return render(request,"page/site/tquiper.html")

def contact(request):
    return render(request,"contato/index/site/base.html")

def about(request):
    return render(request,"about/index/site/base.html")

def time(request):
    return render(request,"time/index/site/base.html")

def gallery(request):
    return render(request,"galeria/index/site/base.html")