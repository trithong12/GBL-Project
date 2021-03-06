# -*-coding:utf-8 -*-
#from django.conf import settings
from django.contrib import admin
from django import forms
from myapp import models
from datetime import datetime
#from django.utils.translation import gettext_lazy as _
from bs4 import BeautifulSoup as bs
from django.utils.text import slugify
#from django.core.exceptions import ValidationError
# Register your models here.
#admin.site.register(models.Post)

# 文章管理 =========================================================================
class PostForm(forms.ModelForm):
    MY_CHOICES = (        
        (True, '發佈'),
        (False, '不發佈'),
    )
    post_is_public = forms.ChoiceField(choices=MY_CHOICES, label='發佈文章')
    class Meta:
        model = models.Post
        fields = ['post_title', 'post_subtitle', 'post_author', 'post_content', 'post_news_link', 'post_category', 'post_is_top_show', 'post_is_public']

class PostAdmin(admin.ModelAdmin):
    
    def make_published(modeladmin, request, queryset):
        queryset.update(post_is_public=True)
    make_published.short_description = "發佈所選取之文章"
    
    def make_unpublished(modeladmin, request, queryset):
        queryset.update(post_is_public=False)
    make_unpublished.short_description = "不發佈所選取之文章"
    
    def update_post_url(modeladmin, request, queryset):
        for obj in queryset:
            obj.slug = slugify(str(obj.post_id)+'-'+obj.post_title+'-'+(obj.post_subtitle if obj.post_subtitle else ''))
            obj.post_url = post_url='http://'+request.META['HTTP_HOST']+'/post/'+obj.slug
            obj.save()
    update_post_url.short_description = '更新文章連結'
   
    form = PostForm
    list_display = ('post_title', 'post_subtitle', 'post_author', '_post_url', 'post_category', '_post_is_top_show', '_post_news_link', 'post_content',  'post_last_modified_datetime', '_post_is_public')
    list_filter = ('post_category', 'post_title', 'post_author', 'post_last_modified_datetime', 'post_is_public')
    search_fields = ('post_title', 'post_author')
    actions = [make_published, make_unpublished, update_post_url]
    list_per_page = 10
    ordering = ('-post_is_top_show', '-post_id',)
        
    def save_model(self, request, obj, form, change):
        if obj.post_is_top_show:
            topShowObjects = models.Post.objects.filter(post_category=obj.post_category)
            topShowObjects = topShowObjects.filter(post_is_top_show=True)
            if topShowObjects != None:
                for o in topShowObjects:
                    o.post_is_top_show = False
                    o.save()        
        
        obj.post_last_modified_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        obj.slug = slugify(str(obj.post_id)+'-'+obj.post_title+'-'+(obj.post_subtitle if obj.post_subtitle else ''))
        obj.post_url = 'http://'+request.META['HTTP_HOST']+'/retrieve_post/'+obj.slug
        obj.save()
        
        post_id = obj.post_id
        old_attachments = models.PostAttachment.objects.filter(post_id=post_id).delete()
        post_content = obj.post_content
        soup = bs(post_content, 'html.parser')
        imgs = soup.find_all('img')
        hrefs = soup.find_all('a')
        audios = soup.find_all('audio')
        iframes = soup.find_all('iframe')
        for img in imgs:
            attachment = models.PostAttachment()
            attachment.post = obj
            attachment.post_attachment_path_or_link = firstproject.settings.MEDIA_ROOT+img['src']
            attachment.save()
        for href in hrefs:
            attachment = models.PostAttachment()
            attachment.post = obj
            attachment.post_attachment_path_or_link = href['href']
            attachment.save()
        for audio in audios:
            attachment = models.PostAttachment()
            attachment.post = obj
            attachment.post_attachment_path_or_link = audio['src']
            attachment.save()
        for iframe in iframes:
            attachment = models.PostAttachment()
            attachment.post = obj
            attachment.post_attachment_path_or_link = iframe['src']
            attachment.save()
       
# end文章管理 =========================================================================



# 相簿管理 ============================================================================
import os
import uuid
import zipfile
import firstproject.settings
from zipfile import ZipFile

from django.core.files.base import ContentFile

from PIL import Image

from myapp.models import Album, AlbumImage

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = []

    zip = forms.FileField(required=False, label='相簿照片集(.zip檔)')

class AlbumImageInline(admin.TabularInline):
    model = models.AlbumImage
    fields = ('image', 'thumbnail')
    readonly_fields = ('thumbnail',)
    
class AlbumModelAdmin(admin.ModelAdmin):  
    form = AlbumForm
    inlines = [AlbumImageInline]
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'album_category', 'thumbnail', 'modified',)
    list_filter = ('album_category', 'modified', 'title',)
    search_fields = ('album_category', 'title', 'modified',)
    list_per_page = 10
    ordering = ('-album_id',)

    def save_model(self, request, obj, form, change):
        if form.is_valid():
            album = form.save(commit=False)
            album.modified = datetime.now()
            album.save()

            if form.cleaned_data['zip'] != None:
                zip = zipfile.ZipFile(form.cleaned_data['zip'])
                for filename in sorted(zip.namelist()):

                    file_name = os.path.basename(filename)
                    if not file_name:
                        continue

                    data = zip.read(filename)
                    contentfile = ContentFile(data)

                    img = AlbumImage()
                    img.album = album
                    img.alt = filename.encode('utf-8').decode('utf-8')
                    print(img.alt)
                    filename = '{0}{1}.jpg'.format(album.slug, str(uuid.uuid4())[-13:])
                    img.image.save(filename, contentfile)
                
                    filepath = '{0}/albums/{1}'.format(firstproject.settings.MEDIA_ROOT, filename)
                    with Image.open(filepath) as i:
                        img.width, img.height = i.size

#                    img.thumb.save('thumb-{0}'.format(filename), contentfile)
                    img.save()
                zip.close() 
            super(AlbumModelAdmin, self).save_model(request, obj, form, change)

# In case image should be removed from album.
class AlbumImageModelAdmin(admin.ModelAdmin):
    list_display = ('thumbnail', 'alt', 'album', 'created',)
    list_filter = ('album', 'created', 'alt')
    search_fields = ('alt', 'album', 'created',)
    list_per_page = 10
    ordering = ('-image_id',)
    
# end相簿管理 =========================================================================


# 會員管理 ===========================================================================
class MemberModelAdmin(admin.ModelAdmin):    
    fs = [f.name for f in models.Member._meta.fields]
    fs.remove('member_password')
    list_display = fs
    list_filter = ('member_joining_date', 'member_zip_code',)
    search_fields = ('member_id', 'member_name', 'member_pid', 'member_birthday', 'member_email')
    ordering = ('-member_id',)
    list_per_page = 10
    
# end會員管理 ========================================================================



# 活動管理 ===========================================================================
class EventModelAdmin(admin.ModelAdmin):
    fs = [f.name for f in models.Event._meta.fields]
    fs.remove('event_id')
    list_display = fs
    list_filter = ('event_start_datetime', 'event_end_datetime', 'event_category', 'event_name',)
    search_fields = ('event_name', 'event_category', 'event_start_datetime', 'event_end_datetime')
    list_per_page = 10
    ordering = ('-event_id',)
    
# end活動管理 ========================================================================


# 商品管理 ===========================================================================
class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        exclude = ['product_created_datetime', 'product_modified_datetime',]

class ProductModelAdmin(admin.ModelAdmin):   
    form = ProductForm
    fs = [f.name for f in models.Product._meta.fields]
    fs = fs[:2] + ['_product_image'] + fs[2:]
    fs.remove('product_image')
    list_display = fs
    list_filter = ('product_category', 'product_price', 'product_name', 'product_created_datetime', 'product_modified_datetime')
    search_fields = ('product_id', 'product_category', 'product_price', 'product_name', 'product_description')
    list_per_page = 10
    ordering = ('-product_id',)
    
    def save_model(self, request, obj, form, change):
        if form.is_valid():
            product = form.save(commit=False)
            product.product_modified_datetime = datetime.now()
            product.save()
    
# end商品管理 ========================================================================


# 訂單管理 ===========================================================================
class OrderForm(forms.ModelForm):
    class Meta:
        model = models.Order
        exclude = ['order_cost_balance', 'order_created_datetime', 'order_modified_datetime', 'order_cancelled_datetime', 'order_is_cancelled']

class OrderCartInline(admin.TabularInline):
    model = models.OrderCart

class OrderModelAdmin(admin.ModelAdmin):
    inlines = [OrderCartInline]
    form = OrderForm
    fs = [f.name for f in models.Order._meta.fields]
    list_display = fs
    list_filter = ('order_payment_method', 'order_payment_is_completed', 'order_receive_method', 'order_process', 'order_modified_datetime',)
    search_fields = ('order_id', 'member', 'order_delivery_address',)
    list_per_page = 10
    ordering = ('-order_id',)
    
    def response_add(self, request, new_object):
        print('response_add called')
        obj = self.after_saving_model_and_related_inlines(new_object)
        return super(OrderModelAdmin, self).response_add(request, obj)

    def response_change(self, request, obj):
        obj = self.after_saving_model_and_related_inlines(obj)
        return super(OrderModelAdmin, self).response_change(request, obj)

    def after_saving_model_and_related_inlines(self, obj):
        total = 0
        for item in obj.order_cart.all():
            total += item.product.product_price * item.amount
        obj.order_cost_balance = total
        print(obj.order_cost_balance)
        obj.save()
        return obj
    
    def save_model(self, request, obj, form, change):
        if not obj.order_is_cancelled and obj.order_process.order_process_id == 5:
            obj.order_cancelled_datetime = datetime.now()
            obj.order_is_cancelled = True
        if obj.order_is_cancelled and obj.order_process.order_process_id != 5:
            obj.order_cancelled_datetime = None
            obj.order_is_cancelled = False
        obj.order_cost_balance = 0
        obj.save()
    
# end訂單管理 ========================================================================
            
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Album, AlbumModelAdmin)
admin.site.register(models.AlbumImage, AlbumImageModelAdmin)
admin.site.register(models.Member, MemberModelAdmin)
admin.site.register(models.Event, EventModelAdmin)
admin.site.register(models.Product, ProductModelAdmin)
admin.site.register(models.Order, OrderModelAdmin)
admin.site.site_header = '佳倍利後台管理'
admin.site.index_title = '後台管理' 
admin.site.site_url = None