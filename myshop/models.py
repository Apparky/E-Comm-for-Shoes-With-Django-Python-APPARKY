from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
Product_For = (
        ("N", None),
        ("M", "Men"),
        ("W", "Women"),
        ("K", "Kids")
    )

Product_Type = (
        ("N", None),
        ("FW", "FootWear"),
        ("WC", "Women's Clothing"),
        ("S", "Shoes")
    )


class Background_Image(models.Model):
    title = models.CharField(max_length=200, null=False)
    alt_tag = models.CharField(max_length=300, null=False)
    highlights = models.CharField(max_length=150, null=True)
    bg_image = models.ImageField(null=False, blank=False, upload_to='midea/images/')

    def __str__(self):
        return self.title


class Product_Detail(models.Model):
    status = (
        ('IS', 'In Stock'),
        ('SO', 'Sold Out'),
        ('n', None),
    )
    product_name = models.CharField(max_length=200, null=False)
    product_price_latest = models.PositiveIntegerField(default=0, null=False)
    product_price_previous = models.PositiveIntegerField(default=0, null=False)
    product_quantities = models.PositiveSmallIntegerField(default=0, null=False)
    product_size = models.CharField(max_length=50, default=None, null=False)
    product_type = models.CharField(max_length=10, choices=Product_Type, default='N', null=False)
    product_for = models.CharField(max_length=15, choices=Product_For, default='N', null=False)
    product_rating = models.CharField(max_length=10, null=True)
    product_status = models.CharField(max_length=60, choices=status, default='IS', null=False)
    product_desc = models.TextField(null=False)
    product_slug = models.CharField(max_length=500, null=False, blank=False, default='This-is-product-slug')
    product_alt = models.CharField(max_length=300, null=True, default='Default ALT Tag')
    product_meta_desc = models.CharField(max_length=200, null=True, default="Meta Decs", blank=False)
    images_1 = models.FileField(null=False, blank=False, upload_to='midea/images/')
    images_1_ALT_TAG = models.CharField(max_length=300, null=False, blank=False, default='Image 1 ALT TAG')

    images_2 = models.FileField(null=True, blank=True, upload_to='midea/images/')
    images_2_ALT_TAG = models.CharField(max_length=300, null=True, blank=True, default='Image 2 ALT TAG')

    images_3 = models.FileField(null=True, blank=True, upload_to='midea/images/')
    images_3_ALT_TAG = models.CharField(max_length=300, null=True, blank=True, default='Image 3 ALT TAG')

    images_4 = models.FileField(null=True, blank=True, upload_to='midea/images/')
    images_4_ALT_TAG = models.CharField(max_length=300, null=True, blank=True, default='Image 4 ALT TAG')

    images_5 = models.FileField(null=True, blank=True, upload_to='midea/images/')
    images_5_ALT_TAG = models.CharField(max_length=300, null=True, blank=True, default='Image 5 ALT TAG')

    images_6 = models.FileField(null=True, blank=True, upload_to='midea/images/')
    images_6_ALT_TAG = models.CharField(max_length=300, null=True, blank=True, default='Image 6 ALT TAG')

    def __str__(self):
        return f'{self.product_name}  --  {self.product_for}  --  {self.product_slug}  --  {self.product_status}'


class Product_for_Sale(models.Model):
    product_name = models.CharField(max_length=300, null=False, default='Product Name')
    product_original_price = models.PositiveIntegerField(default=0, null=False)
    discount_percent = models.PositiveIntegerField(default=0, null=False)
    product_quantities = models.PositiveSmallIntegerField(default=0, null=False)
    product_size = models.CharField(max_length=50, default=None, null=False)
    product_type = models.CharField(max_length=10, choices=Product_Type, default='N', null=False)
    product_for = models.CharField(max_length=15, choices=Product_For, default='N', null=False)
    product_rating = models.CharField(max_length=10, null=True)
    product_status = models.BooleanField(default=True, null=False)
    product_mini_desc = models.CharField(default=False, max_length=100, null=False)
    product_desc = models.TextField(null=False)
    product_alt = models.CharField(max_length=300, null=True, default='Default ALT Tag')
    product_meta_desc = models.CharField(max_length=200, null=True, default="Meta Decs", blank=False)
    images = models.FileField(null=False, blank=False, upload_to='midea/images/')

    def __str__(self):
        return self.product_name


class Contact_US(models.Model):
    Ratings = (
        ("N", None),
        ("W", "Worst"),
        ("B", "Bad"),
        ("O", "OK"),
        ("G", "Good"),
        ("E", "Excellent")
    )
    cust_name = models.CharField(max_length=200, null=False)
    cust_contact = models.CharField(max_length=30, null=False)
    cust_email = models.EmailField(null=False)
    cust_location = models.CharField(max_length=200, null=False, default=True)
    cust_message_subject = models.CharField(max_length=200, null=False)
    cust_message = models.TextField(max_length=1000)
    action_taken = models.BooleanField(null=False, default=False)

    def __str__(self):
        return f"{self.cust_name} {self.cust_message_subject} Action {str(self.action_taken)}"


class About_US(models.Model):
    title = models.CharField(max_length=200, null=False, default='Title Here')
    sub_heading_1 = models.CharField(max_length=300, null=False, default='Sub Heading 1')
    sub_body_1 = models.TextField(null=False, default='Sub Body 1')
    sub_heading_2 = models.CharField(max_length=300, null=False, default='Sub Heading 2')
    sub_body_2 = models.TextField(null=False, default='Sub Body 2')
    sub_heading_3 = models.CharField(max_length=300, null=False, default='Sub Heading 3')
    sub_body_3 = models.TextField(null=False, default='Sub Body 3')
    quote_body = models.CharField(max_length=300, null=True, default='Quote')
    about_desc = models.CharField(max_length=300, null=False, default='About Description')
    about_meta_data = models.CharField(max_length=600, null=False, default='Meta Description for About US')
    about_pic_1 = models.FileField(null=True, upload_to='midea/images/', default=None, blank=True)
    about_pic_1_atl_TAG = models.CharField(max_length=250, null=False, default='Add ALT Tag fro this Picture', blank=True)
    about_pic_2 = models.FileField(null=True, upload_to='midea/images/', default=None, blank=True)
    about_pic_2_atl_TAG = models.CharField(max_length=250, null=False, default='Add ALT Tag fro this Picture', blank=True)
    about_pic_3 = models.FileField(null=True, upload_to='midea/images/', default=None, blank=True)
    about_pic_3_atl_TAG = models.CharField(max_length=250, null=False, default='Add ALT Tag fro this Picture', blank=True)
    about_pic_4 = models.FileField(null=True, upload_to='midea/images/', default=None, blank=True)
    about_pic_4_atl_TAG = models.CharField(max_length=250, null=False, default='Add ALT Tag fro this Picture', blank=True)
    about_pic_5 = models.FileField(null=True, upload_to='midea/images/', default=None, blank=True)
    about_pic_5_atl_TAG = models.CharField(max_length=250, null=False, default='Add ALT Tag fro this Picture', blank=True)
    about_pic_6 = models.FileField(null=True, upload_to='midea/images/', default=None, blank=True)
    about_pic_6_atl_TAG = models.CharField(max_length=250, null=False, default='Add ALT Tag fro this Picture', blank=True)
    about_pic_7 = models.FileField(null=True, upload_to='midea/images/', default=None, blank=True)
    about_pic_7_atl_TAG = models.CharField(max_length=250, null=False, default='Add ALT Tag fro this Picture', blank=True)
    about_pic_8 = models.FileField(null=True, upload_to='midea/images/', default=None, blank=True)
    about_pic_8_atl_TAG = models.CharField(max_length=250, null=False, default='Add ALT Tag fro this Picture', blank=True)

    def __str__(self):
        return self.title


class Our_Core_Team(models.Model):
    roll = (
        ('')
    )
    company_name = models.CharField(max_length=40, null=False, blank=False, default='Apparky')
    name = models.CharField(max_length=300, null=False, default='Member Name', blank=True)
    email = models.EmailField(max_length=300, null=False, default='email ID', blank=True)
    contact = models.CharField(max_length=50, null=False, default='Contact No', blank=True)
    optional_contact = models.CharField(max_length=50, null=True, blank=True)
    address = models.TextField(null=False, default='Put Address Here', blank=True)
    designation = models.CharField(max_length=200, null=False, default='Put Designation Here', blank=True)
    about_designation = models.TextField(null=False, blank=True)
    profile_ID = models.FileField(null=False, upload_to='midea/images/', blank=False)
    profile_alt_TAG = models.CharField(max_length=100, null=True, blank=True, default='Profile ALT Here')
    facebook_profile_Link = models.CharField(max_length=400, null=True, blank=True)
    twitter_profile_Link = models.CharField(max_length=400, null=True, blank=True)
    linkedin_profile_Link = models.CharField(max_length=400, null=True, blank=True)
    Instagram_profile_Link = models.CharField(max_length=400, null=True, blank=True)
    Youtube_Channel_Link = models.CharField(max_length=400, null=True, blank=True)
    Discord_profile_Link = models.CharField(max_length=400, null=True, blank=True)
    RedIT_profile_Link = models.CharField(max_length=400, null=True, blank=True)
    personal_site = models.CharField(max_length=400, null=True, blank=True)

    def __str__(self):
        return f'{self.name} - {self.company_name} - {self.designation}'


class Testimonials(models.Model):
    name = models.CharField(max_length=400, null=False, blank=False)
    email = models.EmailField(max_length=500, null=False, blank=False)
    location = models.CharField(max_length=500, null=False, blank=False, default='City / State')
    testimonial = models.TextField(null=False, blank=False)
    images = models.FileField(null=True, blank=True, upload_to='midea/images/')
    images_ALT_TAG = models.CharField(max_length=400, null=True, blank=True, default='Image ALT Tag')

    def __str__(self):
        return f'{self.name}  --  {self.location}  --  {self.email}'


class Blog_Page(models.Model):
    blog_page_heading = models.CharField(max_length=400, null=False, blank=False)
    blog_page_sub_heading = models.CharField(max_length=700, null=False, blank=False)
    blog_meta_data = models.CharField(max_length=300, null=False, blank=False)
    blog_image = models.FileField(null=False, blank=False, upload_to='midea/images/')
    blog_image_ALT_TAG = models.CharField(max_length=350, null=False, blank=False)

    def __str__(self):
        return self.blog_page_heading


class Blog_Content(models.Model):
    blog_title = models.CharField(max_length=300, null=False, blank=False, default='Blog Title Here')
    blog_sub_title = models.CharField(max_length=450, null=False, blank=False, default='Blog Summary in few Words')
    blog_meta_data = models.CharField(max_length=500, null=False, blank=False, default='Blog Meta Data Here')
    blog_date_posted = models.DateTimeField(blank=False, default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_slug = models.SlugField(null=False, blank=False, default='Blog-Slug-Field')

    blog_title_image = models.FileField(null=True, blank=True, upload_to='midea/images/')
    blog_title_image_ALT_TAG = models.CharField(max_length=400, null=True, blank=True, default='Add Image ALT TAG Here')

    blog_heading_1 = models.CharField(max_length=200, null=False, blank=False, default='Blog Heading 1')
    blog_body_1 = models.TextField(null=False, blank=False, default='Blog Body 1')

    blog_heading_2 = models.CharField(max_length=200, null=True, blank=True, default=' ')
    blog_body_2 = models.TextField(null=True, blank=True, default=' ')

    blog_heading_3 = models.CharField(max_length=200, null=True, blank=True, default=' ')
    blog_body_3 = models.TextField(null=True, blank=True, default=' ')

    blog_images_1 = models.FileField(null=True, blank=True, upload_to='midea/images/')
    blog_images_1_ALT_TAG = models.CharField(max_length=300, null=True, blank=True)

    blog_images_2 = models.FileField(null=True, blank=True, upload_to='midea/images/')
    blog_images_2_ALT_TAG = models.CharField(max_length=300, null=True, blank=True)

    blog_images_3 = models.FileField(null=True, blank=True, upload_to='midea/images/')
    blog_images_3_ALT_TAG = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return f'{self.blog_title} by {self.author}'
