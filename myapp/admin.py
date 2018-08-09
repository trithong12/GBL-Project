from django.contrib import admin
from django import forms
from myapp import models
from datetime import datetime
# Register your models here.
#admin.site.register(models.Post)

class PostForm(forms.ModelForm):
    MY_CHOICES = (
        (False, '不發佈'),
        (True, '發佈'),
    )
    post_is_public = forms.ChoiceField(choices=MY_CHOICES)
    class Meta:
        model = models.Post
        fields = ['post_title', 'post_author', 'post_content', 'post_category', 'post_is_public']

class PostCategoryChoiceField(forms.ModelChoiceField):
     def label_from_instance(self, obj):
         return obj.post_category_name

class PostAdmin(admin.ModelAdmin):
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'post_category':
            return PostCategoryChoiceField(queryset=models.PostCategory.objects.all())
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    form = PostForm
    list_display = ('post_title', 'post_author', 'post_content', 'post_category', 'post_last_modified_datetime', '_post_is_public')
    list_filter = ('post_title', 'post_author', 'post_last_modified_datetime')
    search_fields = ('post_title', 'post_author')
    list_per_page = 10
    ordering = ('post_id',)
    
#    def post_is_public(self, obj):
#        print('obj.post_is_public:', obj.post_is_public)
#        return obj.post_is_public
#    
#    post_is_public.boolean = True
    
    def save_model(self, request, obj, form, change):
        obj.post_last_modified_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        obj.save()
    
admin.site.register(models.Post, PostAdmin)