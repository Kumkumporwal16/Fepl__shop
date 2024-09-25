from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView,TemplateView
from django.views import View
from django.urls import reverse
from .models import Category, Product, CartItem, Cart
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import IntegrityError
from twilio.rest import Client
from .forms import LoginForm
import os


def index(request):
    return render(request, 'index.html')

def loginpage(request):
    return render (request,template_name='loginpage.html')

def register(request):
    return render(request,template_name='register.html')

def footwear(request):
    return render(request,template_name='footwear.html')

def jewellery(request):
    return render(request,template_name="jewellery.html")
    
def womenwear(request):
    return render(request,template_name="womenwear.html")

def makeup(request):
    return render(request,template_name="makeup.html")

def product_detail(request):
    return render(request,template_name="product_detail.html")

def newarrivals(request):
    return render (request,template_name="newarrivals.html")

def featuredproduct(request):
    return render(request,template_name="featuredproduct.html")

def electronicgadgets(request):
    return render (request,template_name="electronicgadgets.html")

def trial(request):
    return render (request,template_name="trial.html")

 
class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['products'] = Product.objects.filter(available=True)
        return context


# Category List View
class CategoryListView(ListView):
    model = Category
    template_name = 'index.html'    
    context_object_name = 'categories'
    def get_queryset(self):
        return Category.objects.all()[:5]
     

# Product List View (filtered by category)
class ProductListView(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'], available=True)

def product_detail(request,id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {'product': product})


def footwear_view(request):
    footwear_products = Product.objects.filter(category__name="Footwear")
    context = {
        'footwear_products': footwear_products
    }
    return render(request, 'footwear.html', context)


def Jewellery_view(request):
    Jewellery_products = Product.objects.filter(category__name="Jewellery")
    context = {
        'Jewellery_products': Jewellery_products
    }
    return render(request, 'Jewellery.html', context)

def newarrivals_view(request):
    newarrivals_products = Product.objects.filter(category_name="newarrivalss")
    context={
        'newarrivals_products':newarrivals_products
    }
    return render(request,'newarrivals.html',context)

def Womenwear_view(request):
   
    womenwear_products = Product.objects.filter(category__name="Womenwear")
    context = {
        'womenwear_products': womenwear_products
    }

    return render(request, 'womenwear.html', context)
    

def trial_view(request):
    trial_products = Product.objects.filter(category__name="trial")
    context = {'trial_products':trial_products}
    return render(request,'trial.html',context)


class MakeupView(View):
    def get(self, request):
        makeup_products = Product.objects.filter(category__name="Makeup")
        context = {'makeup_products': makeup_products}
        return render(request, 'makeup.html', context)



def Electronic_gadgets_view(request):
    Electronic_products = Product.objects.filter(category__name="Electronicgadgets")
    print(Electronic_products.query)  # Add this line to see the SQL query
    context={
        'Electronic_products' : Electronic_products
    }
    return render (request,'electronicgadgets.html',context)



# Product Detail View
class ProductDetailView(DetailView):

    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

    def get_object(self):
        return get_object_or_404(Product, slug=self.kwargs['slug'], available=True)



#login ,register,logout

#Register
def register_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        password = request.POST['password']

        # Check if any field is empty
        if not email or not first_name or not last_name or not password:
            messages.error(request, 'Please fill in all the fields.')
            return render(request, 'register.html')

        # Validate email format (optional step)
        if '@' not in email:
            messages.error(request, 'Invalid email address.')
            return render(request, 'register.html')

        try:
            # Create a new user
            user = User.objects.create_user(
                username=email,  # Use email as the username
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            user.save()

            # Automatically log the user in after registration
            login(request, user)
            messages.success(request, 'Account created successfully.')
            return redirect('loginpage')  # Redirect to the home page or any other page

        except IntegrityError:
            messages.error(request, 'An account with this email already exists.')
            return render(request, 'register.html')

    # GET request, render the registration form
    return render(request, 'register.html')

#Login
def loginpage(request):
    return render(request,template_name="loginpage.html")



def loginpage(request):
    if request.method == 'POST':
        # Retrieve email and password from form
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(request, username=email, password=password)

        if user is not None:
            # Log the user in
            login(request, user)
            # Redirect to a success page or user's dashboard
            return redirect('index')  # Change 'index' to your desired URL name
        else:
            # Invalid credentials, show an error message
            messages.error(request, 'Invalid email or password.')
            return redirect('loginpage')  # Redirect back to login page

    # Render the login page template for GET requests
    return render(request, 'loginpage.html')

'''#Cart
def add_to_cart(request, product_id):
    # Fetch the product
    product = get_object_or_404(Product, id=product_id)
    
    # If the user is authenticated, fetch or create their cart
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    
        # Check if the item is already in the cart
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            # If the item exists, just increase the quantity
            cart_item.quantity += 1
        cart_item.save()

        return redirect('cart_detail')  # Redirect to the cart page
    else:
        # If user is not logged in, handle cart using session (optional)
        # You can implement session-based cart for guest users
        return redirect('login')  # Redirect to login page if not authenticated

def cart_detail(request):
    cart = None
    if request.user.is_authenticated:
        cart = Cart.objects.get(user=request.user)
    return render(request, 'cart_detail.html', {'cart': cart})

'''
def accessories(request):
    return render(request,'accessories.html')














