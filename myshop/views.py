from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from myshop.forms import ContactForm
from django.core.files.storage import FileSystemStorage


# Create your views here.
def index(request):
    bg1 = Background_Image.objects.all()
    product = Product_Detail.objects.all()
    sale = Product_for_Sale.objects.all()
    testimonials = Testimonials.objects.all()
    return render(request, 'index.html', {'bg1': bg1, 'product': product, 'sale': sale, 'reviews': testimonials})


def blog(request):
    blog_page = Blog_Page.objects.all()
    blog_contents = Blog_Content.objects.all()
    return render(request, 'blog.html', {'blg_page': blog_page, 'content': blog_contents})


def blog_content(request, slug_):
    blog_slug_ = Blog_Content.objects.filter(blog_slug=slug_)
    return render(request, 'blog_body.html', {'slug': blog_slug_, 'slug_name': slug_})


def cart(request):
    return render(request, 'cart.html')


def faq(request):
    return HttpResponse('This is FAQ Page')


def policies(request):
    return HttpResponse('This is Our Policy Page')


def checkout(request):
    return render(request, 'checkout.html')


def ProductDetails(request, p_slug):
    product_details = Product_Detail.objects.filter(product_slug=p_slug)
    print(product_details)
    return render(request, 'product_details.html', {'product': product_details, 'slug': p_slug})


def shop(request):
    product = Product_Detail.objects.all()
    return render(request, 'shop.html', {'product': product})


def contactus(request):
    if request.method =="POST":
        contact = Contact_US()

        cust_name = request.POST.get('name')
        cust_contact = request.POST.get('contact')
        cust_email = request.POST.get('email')
        cust_location = request.POST.get('location')
        cust_message_subject = request.POST.get('subject')
        cust_message = request.POST.get('message')

        contact.cust_name = cust_name
        contact.cust_contact = cust_contact
        contact.cust_email = cust_email
        contact.cust_location = cust_location
        contact.cust_message_subject = cust_message_subject
        contact.cust_message = cust_message
        contact.action_taken = False

        contact.save()
        return render(request, "contactsubmition.html")

    return render(request, 'contact.html')


def submit(request):
    return render(request, "contactsubmition.html")


def about(request):
    team = Out_Team.objects.all()
    about_ = About_US.objects.all()
    return render(request, 'about - Copy.html', {'ourTeam': team, 'About': about_})
