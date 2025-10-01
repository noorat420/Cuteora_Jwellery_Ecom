from django.shortcuts import render,get_object_or_404
from .models import Product,Category,Message,Cart,CartItem,Review
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import ContactForm,SignUpForm,LoginForm,ReviewForm

# Create your views here.

# homepage
def home(request):
    categories =Category.objects.all()
    featuredproducts =Product.objects.filter(is_featured=True) 
    context ={
        'categories':categories,
        'featuredproducts':featuredproducts
    }
    return render(request,'products/home.html',context=context)

def about(request):
 
    return render(request,'products/about.html')



# productlist
def productlist(request):
    products =Product.objects.all()
   
    context ={
        'products':products

    }
    return render(request,'products/productlist.html',context=context)





def productdetail(request, prodid):
    product = get_object_or_404(Product, pk=prodid)

    # Handle review form
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product  # link review to this product
            review.save()
            return redirect('productdetail', prodid=product.id)  # reload page after saving
    else:
        form = ReviewForm()

    # Fetch all reviews for this product
    reviews = Review.objects.filter(product=product).order_by("-id")

    context = {
        'product': product,
        'form': form,
        'reviews': reviews,
    }
    return render(request, 'products/productdetail.html', context)




# contact
def contact(request):
    success = False

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()                  # save the message
            form = ContactForm()         # reset the form
            success = True
    else:
        form = ContactForm() 
    return render(request, 'products/contact.html', {'form': form, 'success': success})


# cart view
@login_required
def cart_detail(request):
    # Get or create cart for logged-in user
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, "products/cart.html", {"cart": cart})

@login_required
def add_to_cart(request, id):
    cart, created = Cart.objects.get_or_create(user=request.user)
    product = get_object_or_404(Product, id=id)

    # Check if item already exists
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        item.quantity += 1
        item.save()

    return redirect("cart")

@login_required
def remove_from_cart(request, id):
    item = get_object_or_404(CartItem, id=id, cart__user=request.user)
    item.delete()
    return redirect("cart")


# SIGNUP
def sign_up_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()

    return render(request, 'products/signup.html', {'form': form})



# LOGIN
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('products')  # <-- redirect to product list after login
    else:
        form = LoginForm()
    return render(request, 'products/login.html', {'form': form})


# LOGOUT
def logout_view(request):
    logout(request)  # This logs out the user
    return redirect('home')      