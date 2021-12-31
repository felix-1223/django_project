from django.shortcuts import redirect, render
from .models import Book
from django.contrib import messages

# Create your views here.
def index(request):
    b = request.user.book.all()
    context = {
        "blist":b
    }
    return render(request, "book/index.html", context)

def create(request):
    if request.method == "POST":
        sn=request.POST.get("sname")
        su=request.POST.get("surl")
        co=request.POST.get("com")
        im=request.POST.get("impo")
        if im:
            im= True
        else:
            im= False
        Book(user=request.user, site_name=sn, comment=co, impo=im).save()
        return redirect("book:index")
    return render(request,"book/create.html")




def delete(request, bpk):
    b=Book.objects.get(id=bpk)
    if request.user == b.user:
        b.delete()
    else:
        messages.warning(request,"FUCK OFF")
    return redirect("book:index")