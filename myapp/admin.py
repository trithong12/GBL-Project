# -*-coding:utf-8 -*-

from django.contrib import admin
from django import forms
from myapp import models
from datetime import datetime
from django.utils.translation import gettext_lazy as _
from bs4 import BeautifulSoup as bs

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
        fields = ['post_title', 'post_author', 'post_content', 'post_category', 'post_is_public']

class PostCategoryChoiceField(forms.ModelChoiceField):
     def label_from_instance(self, obj):
         return obj.post_category_name

class PostAdmin(admin.ModelAdmin):
    
    def make_published(modeladmin, request, queryset):
        queryset.update(post_is_public=True)
    make_published.short_description = "發佈所選取之文章"
    
    def make_unpublished(modeladmin, request, queryset):
        queryset.update(post_is_public=False)
    make_unpublished.short_description = "不發佈所選取之文章"
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'post_category':
            return PostCategoryChoiceField(queryset=models.PostCategory.objects.all(), label='文章分類')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    form = PostForm
    list_display = ('post_title', 'post_author', 'post_content', 'post_category', 'post_last_modified_datetime', '_post_is_public')
    list_filter = ('post_title', 'post_author', 'post_last_modified_datetime', 'post_is_public')
    search_fields = ('post_title', 'post_author')
    actions = [make_published, make_unpublished]
    list_per_page = 10
    ordering = ('post_id',)
    
    def save_model(self, request, obj, form, change):
        obj.post_last_modified_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        obj.save()
        
        post_id = obj.post_id
        post_content = obj.post_content
        soup = bs(post_content, 'html.parser')
        imgs = soup.find_all('img')
        hrefs = soup.find_all('a')
        print(imgs, '\n', hrefs)
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

class AlbumCategoryChoiceField(forms.ModelChoiceField):
     def label_from_instance(self, obj):
         return obj.album_category_name

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = []

    zip = forms.FileField(required=False, label='相簿照片集(.zip檔)')

class AlbumModelAdmin(admin.ModelAdmin):
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'album_category':
            return AlbumCategoryChoiceField(queryset=models.AlbumCategory.objects.all(), label='相簿分類')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    form = AlbumForm
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'album_category', 'thumb', 'modified',)
    list_filter = ('album_category', 'modified', 'thumb', 'title',)
    search_fields = ('album_category', 'title', 'thumb', 'modified',)
    list_per_page = 10

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

                    img.thumb.save('thumb-{0}'.format(filename), contentfile)
                    img.save()
                zip.close() 
            super(AlbumModelAdmin, self).save_model(request, obj, form, change)

# In case image should be removed from album.
class AlbumImageModelAdmin(admin.ModelAdmin):
    list_display = ('alt', 'album', 'created',)
    list_filter = ('album', 'created', 'alt')
    search_fields = ('alt', 'album', 'created',)
    list_per_page = 10
    
# end相簿管理 =========================================================================


# 會員管理 ===========================================================================
class MemberModelAdmin(admin.ModelAdmin):    
    fs = [f.name for f in models.Member._meta.fields]
    fs.remove('member_password')
    list_display = fs
    list_filter = ('member_joining_date', 'member_zip_code',)
    search_fields = ('member_id', 'member_name', 'member_pid', 'member_birthday', 'member_email')
    ordering = ('member_id',)
    list_per_page = 10
    
# end會員管理 ========================================================================



# 活動管理 ===========================================================================
class EventCategoryChoiceField(forms.ModelChoiceField):
     def label_from_instance(self, obj):
         return obj.event_category_name

class EventModelAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'event_category':
            return EventCategoryChoiceField(queryset=models.EventCategory.objects.all(), label='活動分類')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    fs = [f.name for f in models.Event._meta.fields]
    fs.remove('event_id')
    list_display = fs
    list_filter = ('event_start_datetime', 'event_end_datetime', 'event_category', 'event_name',)
    search_fields = ('event_name', 'event_category', 'event_start_datetime', 'event_end_datetime')
    list_per_page = 10
    ordering = ('event_id',)
    
# end活動管理 ========================================================================
    
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Album, AlbumModelAdmin)
admin.site.register(models.AlbumImage, AlbumImageModelAdmin)
admin.site.register(models.Member, MemberModelAdmin)
admin.site.register(models.Event, EventModelAdmin)
admin.site.site_header = '佳倍利後台管理'
admin.site.index_title = '後台管理' 