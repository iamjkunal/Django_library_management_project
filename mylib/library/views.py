from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from library.models import Books
from django.contrib.auth.decorators import login_required
# Create your views here.
def homepage (request):
    return render(request,"homepage.html")

def signuppage (request):
    try:
        if request.method == 'POST':
            firstname=request.POST.get("firstname")
            lastname=request.POST.get("lastname")
            usename=request.POST.get('username')
            useremail=request.POST.get('useremail')
            password1=request.POST.get('password1')
            password2=request.POST.get('password2')
            if password1==password2:
                if User.objects.filter(username=usename).exists():
                    messages.warning(request,"username is already used ")
                else:
                    if User.objects.filter(email=useremail).exists():
                        messages.warning(request,"this email is already exists")
                    else:
                        user = User.objects.create_user(usename,useremail,password1)
                        user.first_name=firstname
                        user.last_name=lastname
                        user.save()
                        messages.success (request,f"user {usename} is created please login")
            else:
                messages.warning(request,"password is not matched")
    except:
        pass
    return render(request,"signuppage.html")

def loginpage(request):
    if request.method == "POST":
        inputusername=request.POST.get('username')
        password=request.POST.get('password')
        if User.objects.filter(username=inputusername).exists():
            user = authenticate(request , username=inputusername,password=password)
            if user is not None:
           
                login(request,user)
                print(user)
                return redirect("homepage")
            
            else:
                messages.warning(request,"please enter valid credentials")
                
        else:
            messages.warning(request,"username is not exists")
    return render(request,"loginpage.html")


@login_required
def logoutpage(request):
    logout(request)
    return redirect("/home")

@login_required
def viewbook(request):
    if request.user.is_active:
            booksdata=Books.objects.all()
            if request.method=='POST':
                st=request.POST.get("sear")
                if st!=None:
                    booksdata=Books.objects.filter(book_title__icontains=st)
            return render(request,"viewbook.html",{"book":booksdata})
    else:
        messages.warning(request,"please! login first")
    return render(request,"viewbook.html")


@login_required
def add_book(request):
    try:
        if request.method == "POST":
            title=request.POST.get('booktitle')
            author=request.POST.get('author')
            edition=request.POST.get('edition')
            place=request.POST.get('place')
            publisher=request.POST.get('publisher')
            year=request.POST.get('year')
            print(title,author,edition,place,publisher,year)
            b = Books(book_title=title,book_author=author,book_edition=edition,book_place=place,book_publisher=publisher,book_year=year)
            b.save()
            messages.success(request,f"book name {title} is added to library")
    except:
        pass
    return render(request,"add_book.html")
@login_required
def update_delete(request):
    book_data=Books.objects.all()
    if request.method=='POST':
        st=request.POST.get("searc")
        if st!=None:
            book_data=Books.objects.filter(book_title__icontains=st)
    return render(request,"update_delete.html",{"book":book_data})
@login_required
def update(request,title):
    u=Books.objects.filter(book_title=title)
    if request.method == 'POST':
        newtitle=request.POST.get("booktitle")
        author=request.POST.get("author")
        edition=request.POST.get("edition")
        place=request.POST.get("place")
        publisher=request.POST.get("publisher")
        year=request.POST.get("year")
        print(year)
        Books.objects.filter(book_title=title).update(book_title=newtitle,book_author=author,book_edition=edition,book_place=place,book_publisher=publisher,book_year=year)
        u.book_title=newtitle
        u.book_author=author
        u.book_edition=edition
        u.book_place=place
        u.book_publisher=publisher
        u.book_year=year
        messages.success(request,"book is updated")
        return redirect("/update-delete")  
    return render(request,"update.html",{"detail":u})
@login_required
def delete_book(request,title):
    d=Books.objects.get(book_title=title)
    d.delete()
    messages.success(request,f"book name {title} is delete ")
    return redirect("/update-delete")
@login_required
def about_us(request):
    return render(request,"aboutus.html")