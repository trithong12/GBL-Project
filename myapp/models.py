# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from model_utils import Choices

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

import uuid
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit

class Album(models.Model):
    album_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=70, verbose_name='相簿名稱/標題')
    album_category = models.ForeignKey('AlbumCategory', models.DO_NOTHING, verbose_name='相簿分類')
    album_event_datetime = models.DateTimeField(blank=True, null=True, verbose_name='活動日期')
    description = models.TextField(max_length=1024, blank=True, null=True, verbose_name='相簿描述')
    thumb = ProcessedImageField(upload_to='albums', processors=[ResizeToFit(300)], format='JPEG', options={'quality': 90}, blank=True, null=True, verbose_name='縮略圖')
    tags = models.CharField(max_length=250, blank=True, null=True, verbose_name='標籤')
    is_visible = models.BooleanField(default=True, verbose_name='可檢視')
    created = models.DateTimeField(auto_now_add=True, verbose_name='建立日期')
    modified = models.DateTimeField(auto_now_add=True, verbose_name='最近修改日期')
    slug = models.SlugField(max_length=50, unique=True)    

    #def get_absolute_url(self):
    #    return reverse('album', kwargs={'slug':self.slug})

    class Meta:
        managed = False
        db_table = 'album'
        verbose_name = '相簿'
        verbose_name_plural = '相簿'
        
    def __str__(self):
        return self.title

class AlbumImage(models.Model):
    image_id = models.AutoField(primary_key=True)
    image = ProcessedImageField(upload_to='albums', processors=[ResizeToFit(1280)], format='JPEG', options={'quality': 70}, verbose_name='照片檔案')
    thumb = ProcessedImageField(upload_to='albums', processors=[ResizeToFit(300)], format='JPEG', options={'quality': 80}, verbose_name='縮略圖')
    album = models.ForeignKey('album', related_name='images', on_delete=models.PROTECT, verbose_name='所屬相簿')
    alt = models.CharField(max_length=255, default=uuid.uuid4, verbose_name='圖片名稱/描述')
    created = models.DateTimeField(auto_now_add=True, verbose_name='建立日期')
    width = models.IntegerField(default=0, verbose_name='寬度')
    height = models.IntegerField(default=0, verbose_name='高度')
    slug = models.SlugField(max_length=70, default=uuid.uuid4, editable=False)
    
    def __str__(self):
        return self.album + '--' + self.alt
    
    class Meta:
        managed = False
        db_table = 'album_image'
        verbose_name = '相簿照片'
        verbose_name_plural = '相簿照片'

#class Album(models.Model):
#    album_id = models.AutoField(primary_key=True)
#    album_name = models.CharField(max_length=50)
#    album_category = models.ForeignKey('AlbumCategory', models.DO_NOTHING)
#    album_event_datetime = models.DateTimeField(blank=True, null=True)
#
#    class Meta:
#        managed = False
#        db_table = 'album'


class AlbumCategory(models.Model):
    album_category_id = models.AutoField(primary_key=True)
    album_category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.album_category_name
    
    class Meta:
        managed = False
        db_table = 'album_category'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Employee(models.Model):
    employee_id = models.CharField(primary_key=True, max_length=45)
    employee_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'employee'


class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=45, verbose_name='活動名稱')
    event_category = models.ForeignKey('EventCategory', models.DO_NOTHING, verbose_name='活動分類')
    event_start_datetime = models.DateTimeField(verbose_name='活動開始時間')
    event_end_datetime = models.DateTimeField(verbose_name='活動結束時間')
    event_description = models.CharField(max_length=1000, blank=True, null=True, verbose_name='活動描述')
#    event_is_deleted = models.TextField()  # This field type is a guess.
    
    def __str__(self):
        return self.event_name    
    
    class Meta:
        managed = False
        db_table = 'event'
        verbose_name = '活動'
        verbose_name_plural = '活動'


class EventCategory(models.Model):
    event_category_id = models.AutoField(primary_key=True)
    event_category_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.event_category_name
    
    class Meta:
        managed = False
        db_table = 'event_category'


class Member(models.Model):
    member_id = models.CharField(primary_key=True, max_length=45, verbose_name='會員代號')
    member_name = models.CharField(max_length=20, verbose_name='姓名')
    member_pid = models.CharField(max_length=11, verbose_name='身份證字號')
    member_birthday = models.DateField(blank=True, null=True, verbose_name='生日')
    member_phone_o = models.CharField(db_column='member_phone_O', max_length=20, blank=True, null=True, verbose_name='機構聯絡電話')  # Field name made lowercase.
    member_phone_h = models.CharField(db_column='member_phone_H', max_length=20, blank=True, null=True, verbose_name='住家聯絡電話')  # Field name made lowercase.
    member_mobile = models.CharField(max_length=20, blank=True, null=True, verbose_name='行動電話')
    member_zip_code = models.IntegerField(blank=True, null=True, verbose_name='郵遞區號')
    member_address = models.CharField(max_length=50, blank=True, null=True, verbose_name='住址')
    member_joining_date = models.DateField(blank=True, null=True, verbose_name='加入日期')
    member_email = models.CharField(max_length=45, blank=True, null=True, verbose_name='電子信箱')
    member_password = models.CharField(max_length=20, blank=True, null=True, verbose_name='密碼')
    member_introducer_name = models.CharField(max_length=20, blank=True, null=True, verbose_name='介紹人')
    member_is_verified = models.BooleanField(verbose_name='已驗證')  # This field type is a guess.

    def __str__(self):
        return self.member_name
    
    class Meta:
        managed = False
        db_table = 'member'
        verbose_name = '會員'
        verbose_name_plural = '會員'
        
    def _member_is_verified(self):
        return bool(self.member_is_verified)
    _member_is_verified.short_description = '已驗證'


#class MemberIntroducerReference(models.Model):
#    member_introducer_reference_id = models.IntegerField(primary_key=True)
#    member = models.ForeignKey(Member, models.DO_NOTHING, related_name='member')
#    introducer = models.ForeignKey(Member, models.DO_NOTHING, blank=True, null=True, related_name='introducer')
#
#    class Meta:
#        managed = False
#        db_table = 'member_introducer_reference'


class Message(models.Model):
    message_id = models.CharField(primary_key=True, max_length=45)
    sender_employee = models.ForeignKey(Employee, models.DO_NOTHING, blank=True, related_name='sender_employee')
    receiver_employee = models.ForeignKey(Employee, models.DO_NOTHING, blank=True, related_name='receiver_employee')
    sender_member = models.ForeignKey(Member, models.DO_NOTHING, blank=True, related_name='sender_member')
    receiver_member = models.ForeignKey(Member, models.DO_NOTHING, blank=True, related_name='receiver_member')
    read_status = models.TextField()  # This field type is a guess.
    message_content = models.CharField(max_length=200)
    message_datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'message'

class Oauth2ProviderAccesstoken(models.Model):
    id = models.BigAutoField(primary_key=True)
    token = models.CharField(unique=True, max_length=255)
    expires = models.DateTimeField()
    scope = models.TextField()
    application = models.ForeignKey('Oauth2ProviderApplication', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    source_refresh_token = models.ForeignKey('Oauth2ProviderRefreshtoken', models.DO_NOTHING, unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth2_provider_accesstoken'


class Oauth2ProviderApplication(models.Model):
    id = models.BigAutoField(primary_key=True)
    client_id = models.CharField(unique=True, max_length=100)
    redirect_uris = models.TextField()
    client_type = models.CharField(max_length=32)
    authorization_grant_type = models.CharField(max_length=32)
    client_secret = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    skip_authorization = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oauth2_provider_application'


class Oauth2ProviderGrant(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(unique=True, max_length=255)
    expires = models.DateTimeField()
    redirect_uri = models.CharField(max_length=255)
    scope = models.TextField()
    application = models.ForeignKey(Oauth2ProviderApplication, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oauth2_provider_grant'


class Oauth2ProviderRefreshtoken(models.Model):
    id = models.BigAutoField(primary_key=True)
    token = models.CharField(max_length=255)
    access_token = models.ForeignKey(Oauth2ProviderAccesstoken, models.DO_NOTHING, unique=True, blank=True, null=True)
    application = models.ForeignKey(Oauth2ProviderApplication, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    revoked = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth2_provider_refreshtoken'
        unique_together = (('token', 'revoked'),)

class Order(models.Model):
    order_id = models.CharField(primary_key=True, max_length=45, verbose_name='訂單編號')
    member = models.ForeignKey(Member, models.DO_NOTHING, verbose_name='購買者')
    order_cost_balance = models.IntegerField(verbose_name='訂單總額')
    order_payment_method = models.ForeignKey('PaymentMethod', models.DO_NOTHING, null=True, verbose_name='付款方式')
    order_payment_is_completed = models.BooleanField(verbose_name='已付款')  # This field type is a guess.
    order_receive_method = models.ForeignKey('ReceiveMethod', models.DO_NOTHING, blank=True, null=True, verbose_name='收貨方式')
    order_delivery_address = models.CharField(max_length=100, blank=True, null=True, verbose_name='收貨地點')
    order_process = models.ForeignKey('OrderProcess', models.DO_NOTHING, blank=True, verbose_name='訂單狀態')
    order_create_datetime = models.DateTimeField(auto_now_add=True, verbose_name='訂單建立時間')
    order_modified_datetime = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='最近修改時間')
    order_is_cancelled = models.BooleanField(default=False, verbose_name='訂單已被取消')
    order_cancelled_datetime = models.DateTimeField(blank=True, null=True, verbose_name='訂單取消時間')
#    order_is_deleted = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'order'
        verbose_name = '訂單'
        verbose_name_plural = '訂單'


class OrderCart(models.Model):
    order_cart_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, models.CASCADE, related_name='order_cart', verbose_name='訂單編號')
    product = models.ForeignKey('Product', models.DO_NOTHING, verbose_name='商品名稱')
    amount = models.IntegerField(verbose_name='數量')

    class Meta:
        managed = False
        db_table = 'order_cart'
        verbose_name = '購買項目'
        verbose_name_plural = '購買項目'


class OrderProcess(models.Model):
    order_process_id = models.AutoField(primary_key=True)
    order_process_name = models.CharField(max_length=45)

    def __str__(self):
        return self.order_process_name
    
    class Meta:
        managed = False
        db_table = 'order_process'


class PaymentMethod(models.Model):
    payment_method_id = models.AutoField(primary_key=True)
    payment_method_name = models.CharField(max_length=45)

    def __str__(self):
        return self.payment_method_name
    
    class Meta:
        managed = False
        db_table = 'payment_method'


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_title = models.CharField(max_length=50, verbose_name='文章標題')
    post_author = models.CharField(max_length=45, verbose_name='文章作者')
    #post_content = models.CharField(max_length=10000, blank=True, null=True)
    #post_content = RichTextField(max_length=10000, blank=True, null=True)
    post_content = RichTextUploadingField(max_length=10000, blank=True, null=True, verbose_name='文章內容')
    #post_created_datetime = models.DateTimeField()
    post_last_modified_datetime = models.DateTimeField(verbose_name='最近修改日期')
    post_category = models.ForeignKey('PostCategory', models.DO_NOTHING, verbose_name='文章分類')
#    post_is_deleted = models.TextField()  # This field type is a guess.
    post_is_public = models.BooleanField(verbose_name='發佈文章')  # This field type is a guess.
    
    def _post_is_public(self):
        if bool(self.post_is_public):
            return '已發佈'
        else:
            return '未發佈'
    _post_is_public.short_description = '發佈文章'
    
    class Meta:
        managed = False
        db_table = 'post'
        verbose_name = '文章'
        verbose_name_plural = '文章'

class PostAttachment(models.Model):
    post_attachment_id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, models.DO_NOTHING, related_name='post_attachment')
    post_attachment_path_or_link = models.CharField(max_length=200)
    #post_attachment_type = models.ForeignKey('PostAttachmentType', models.DO_NOTHING, related_name='post_attachment_type')

    class Meta:
        managed = False
        db_table = 'post_attachment'


#class PostAttachmentType(models.Model):
#    post_attachment_type_id = models.AutoField(primary_key=True)
#    post_attachment_type_name = models.CharField(max_length=50)
#
#    class Meta:
#        managed = False
#        db_table = 'post_attachment_type'


class PostCategory(models.Model):
    post_category_id = models.AutoField(primary_key=True)
    post_category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.post_category_name
    
    class Meta:
        managed = False
        db_table = 'post_category'


class Product(models.Model):
    product_id = models.CharField(primary_key=True, max_length=45, verbose_name='商品代號')
    product_name = models.CharField(max_length=50, verbose_name='名稱')
    product_category = models.ForeignKey('ProductCategory', models.DO_NOTHING, verbose_name='商品分類')
    product_price = models.IntegerField(blank=True, null=True, verbose_name='單價/價格')
    product_description = models.CharField(max_length=200, blank=True, null=True, verbose_name='描述')
    product_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name='建立日期')
    product_modified_datetime = models.DateTimeField(auto_now_add=True, verbose_name='最近修改日期')
#    product_is_deleted = models.TextField()  # This field type is a guess.

    def __str__(self):
        return self.product_name
    
    class Meta:
        managed = False
        db_table = 'product'
        verbose_name = '商品'
        verbose_name_plural = '商品'


class ProductCategory(models.Model):
    product_category_id = models.AutoField(primary_key=True)
    product_category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.product_category_name

    class Meta:
        managed = False
        db_table = 'product_category'


class ReceiveMethod(models.Model):
    receive_method_id = models.AutoField(primary_key=True)
    receive_method_name = models.CharField(max_length=45)

    def __str__(self):
        return self.receive_method_name
    
    class Meta:
        managed = False
        db_table = 'receive_method'