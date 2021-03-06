from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from . models import Product
from django.utils import timezone

def home(request):
    products = Product.objects
    return render(request, 'products/home.html', {'products':products})
	
@login_required(login_url="/accounts/SignUp") # if not logged in redirects them to the url in brackets
def create(request):
    if request.method == "POST": # checks for post request 	below checking user has filled out all places in form.
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            product = Product() # making an instance of the model clas product
            product.title = request.POST['title'] # MAKES THE TITLE EQUAL TO WHATEVER IS PASSED IN THE FORM
            product.body = request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):             
                product.url = request.POST['url'] # IF STATEMENT TO CHECK USER AHS TYPED IN A URL
            else:
                product.url = 'http://' + request.POST['url'] # else adds http:// to make sure it becomes one.			
            product.icon = request.FILES['icon']# because user had to add a file in the form	
            product.image = request.FILES['image']
            product.pub_date = timezone.datetime.now()
            product.hunter = request.user# MAKES THE HUNTER OF THE PRODUCT THE CURRENT LOGGED IN USER
            product.save() # saves all this shit into the database.
            return redirect('/products/' + str(product.id))# takes us to our site with our product str is needed			
			
        else:
            return render(request, 'products/create.html', {'error':'Please fill out all parts of the form'})		
    	
	
    else:	
        return render(request, 'products/create.html')

def detail(request, product_id):
    product_detail = get_object_or_404(Product, pk=product_id)
    return render(request,'products/detail.html', {'product':product_detail})

@login_required (login_url="/accounts/SignUp")	
def upvote(request, product_id):
    if request.method == "POST":
        product = get_object_or_404(Product, pk=product_id)		
        product.votes_total += 1
        product.save() # this is needed see earlier comment
        return redirect('/products/' + str(product.id))			

	
