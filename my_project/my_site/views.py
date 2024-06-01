from django.http import HttpResponse
from django.shortcuts import render
from my_site.models import Advert 

def index(request):
    adverts= Advert.objects.all()
    return render(request, "index.html", context={"adverts": adverts})

def create(request):
    if request.method == 'GET':
        return render(request, "create.html")
    if request.method == 'POST':
        name = request.POST.get("name")
        price = request.POST.get("price")
        img = request.POST.get("img")
        description = request.POST.get("description")
        date = request.POST.get("date")
        place = request.POST.get("place")

        new_advert = Advert(title=name,
                            price=int(price),
                            img=img,
                            description=description,
                            date=date,
                            place=place,
                            user_id=0)
        print(new_advert)
        new_advert.save()
        return HttpResponse("объявление создано успешно")