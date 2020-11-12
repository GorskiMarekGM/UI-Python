from django.shortcuts import render
from django.http import Http404, HttpResponse
import time
from django.http import JsonResponse

# Create your views here.

def index(request):
    return render(request, "UI/posts.html")

texts = ["Nulla consequat felis vitae molestie sagittis. Aliquam enim enim, cursus sed scelerisque sed, varius ac est.",
        "Ut auctor lacus ac pharetra viverra. Aliquam maximus est vehicula nibh tincidunt, nec varius nibh elementum. ",
        "Donec ut ultricies metus. Nam ullamcorper feugiat iaculis. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Nulla ante tellus, sollicitudin eu libero eget, finibus vestibulum arcu."]

def section(request,num):
    if 1<= num <= 3:
        return HttpResponse(texts[num-1])
    else:
        raise Http404("No such section")

    
def posts(request):

    start = int(request.GET.get("start") or 0)
    end = int(request.GET.get("end") or (start + 9))


    #generate list of posts
    data = []
    for i in range (start, end+1):
        data.append(f"Post #{i}")


    #delay speed of response
    time.sleep(1)

   # Return list of posts
    return JsonResponse({
        "posts": data
    })