from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Member

# Create your views here.

def index(request):
    members = Member.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(members, 4)
    try:
        members = paginator.page(page)
    except PageNotAnInteger:
        members = paginator.page(1)
    except EmptyPage:
        members = paginator.page(paginator.num_pages)

    #return render(request, 'core/user_list.html', { 'users': users })
    context = {'members': members}
    return render(request, 'crud/index.html', context)



def create(request):
    member = Member(firstname=request.POST['firstname'],
                    lastname=request.POST['lastname'],
                    alamat=request.POST['alamat'],
                    agama=request.POST['agama'],)
    member.save()
    return redirect('/')

def edit(request, id):
    members = Member.objects.get(id=id)
    context = {'members': members}
    return render(request, 'crud/edit.html', context)

def update(request, id):
    member = Member.objects.get(id=id)
    member.firstname = request.POST['firstname']
    member.lastname  = request.POST['lastname']
    member.agama     = request.POST['agama']
    member.alamat    = request.POST['alamat']
    member.save()
    return redirect('/crud/')

def delete(request, id):
    member = Member.objects.get(id=id)
    member.delete()
    return redirect('/crud/')
