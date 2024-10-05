from django.shortcuts import render,redirect
from django.core.paginator import Paginator,EmptyPage




# Create your views here.
#function based view

#create new function
from lybrry.models import Book

"""Normal method"""

# def createBook(request):
#     books=Book.objects.all()
#     if request.method=='POST':
#         title=request.POST.get('title')
#         price=request.POST.get('price')

#         book=Book(title=title,price=price)
#         book.save()

#     return render(request,'admin/book.html',{'books':books})


#list view fuction
#extrnal page output view
def listBook(request):

    books=Book.objects.all()
    paginator=Paginator(books,4)
    page_number=request.GET.get('page')

    try:
        page=paginator.get_page(page_number)

    except EmptyPage:
        page=paginator.page(page_number.num_pages)

    return render(request,'admin/listbook.html',{'books':books,'page':page})

# #view details function
def detailsView(request,book_id):
    book=Book.objects.get(id=book_id)
    return render(request,'admin/detailsview.html',{'book':book})

# #update function
# def updateBook(request,book_id):
#     book=Book.objects.get(id=book_id)
#     if request.method=="POST":
#         title=request.POST.get('title')
#         price=request.POST.get('price')
#         book.title=title
#         book.price=price
#         book.save()
#         return redirect('/')#for go to home page after update
#     return render(request,'admin/update.html',{'book':book})

#delete function
def deleteView(request,book_id):
    book=Book.objects.get(id=book_id)
    if request.method=="POST":
        book.delete()
        return redirect('/')
    return render(request,'admin/delete.html',{'book':book})

#class based views:- in 1st projct

"""Form method only for create and update function"""


from lybrry.forms import Authorform,Bookform

#Create fuction

def createBook(request):
    books=Book.objects.all()
    if request.method=='POST':
        form=Bookform(request.POST,request.FILES)
    
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=Bookform()
    return render(request,'admin/create.html',{'form':form,'books':books})


def createauthor(request):
    if request.method=='POST':
        form=Authorform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    else:
        form=Authorform()
    return render(request,'admin/author.html',{'form':form})
        

#Update function

def updateBook(request,book_id):
    book=Book.objects.get(id=book_id)
    if request.method=="POST":
        form=Bookform(request.POST,request.FILES,instance=book)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=Bookform(instance=book)

    return render(request,'admin/update.html',{'form':form})

def index(request):
    return render(request,'admin/index.html')


from django.db.models import Q
def searchBook(request):
    query=None
    books=None

    if 'q' in request.GET:
        query=request.GET.get('q')
        books=Book.objects.filter(Q(title__icontains=query) | Q(author__name__icontains=query))

    else:
        books=[]

    context={'books':books,'query':query}

    return render(request,'admin/search.html',context)