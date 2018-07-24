{'C:\\DjangoEnv\\firstproject\\static'}
/static/
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Album(models.Model):
    album_id = models.AutoField(primary_key=True)
    album_name = models.CharField(max_length=50)
    album_category = models.ForeignKey('AlbumCategory', models.DO_NOTHING)
    album_event_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'album'


class AlbumCategory(models.Model):
    album_category_id = models.AutoField(primary_key=True)
    album_category_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'album_category'


class AlbumPhotos(models.Model):
    album_photos_id = models.AutoField(primary_key=True)
    album = models.ForeignKey(Album, models.DO_NOTHING)
    photo_path = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'album_photos'


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
    event_name = models.CharField(max_length=45)
    event_category = models.ForeignKey('EventCategory', models.DO_NOTHING)
    event_start_datetime = models.DateTimeField()
    event_end_datetime = models.DateTimeField()
    event_description = models.CharField(max_length=1000, blank=True, null=True)
    event_is_deleted = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'event'


class EventCategory(models.Model):
    event_category_id = models.AutoField(primary_key=True)
    event_category_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'event_category'


class Member(models.Model):
    member_id = models.CharField(primary_key=True, max_length=45)
    member_name = models.CharField(max_length=20)
    member_phone = models.CharField(max_length=20)
    member_pid = models.CharField(max_length=11)
    member_email = models.CharField(max_length=45)
    member_introducer_reference_id = models.IntegerField()
    member_is_verified = models.TextField()  # This field type is a guess.
    member_password = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member'


class MemberIntroducerReference(models.Model):
    member_introducer_reference_id = models.IntegerField(primary_key=True)
    member = models.ForeignKey(Member, models.DO_NOTHING)
    introducer = models.ForeignKey(Member, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member_introducer_reference'


class Message(models.Model):
    message_id = models.CharField(primary_key=True, max_length=45)
    sender = models.ForeignKey(Member, models.DO_NOTHING)
    receiver = models.ForeignKey(Member, models.DO_NOTHING)
    read_status = models.TextField()  # This field type is a guess.
    message_content = models.CharField(max_length=200)
    message_datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'message'


class Order(models.Model):
    order_id = models.CharField(primary_key=True, max_length=45)
    member = models.ForeignKey(Member, models.DO_NOTHING)
    order_cost_balance = models.FloatField()
    order_payment_method = models.ForeignKey('PaymentMethod', models.DO_NOTHING)
    order_payment_is_completed = models.TextField()  # This field type is a guess.
    order_receive_method = models.ForeignKey('ReceiveMethod', models.DO_NOTHING, blank=True, null=True)
    order_delivery_address = models.CharField(max_length=100, blank=True, null=True)
    order_process = models.ForeignKey('OrderProcess', models.DO_NOTHING, blank=True, null=True)
    order_create_datetime = models.DateTimeField()
    order_last_modified_datetime = models.DateTimeField(blank=True, null=True)
    order_deleted_datetime = models.DateTimeField(blank=True, null=True)
    order_is_deleted = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'order'


class OrderCart(models.Model):
    order_cart_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, models.DO_NOTHING)
    product = models.ForeignKey('Product', models.DO_NOTHING)
    amount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'order_cart'


class OrderProcess(models.Model):
    order_process_id = models.AutoField(primary_key=True)
    order_process_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'order_process'


class PaymentMethod(models.Model):
    payment_method_id = models.AutoField(primary_key=True)
    payment_method_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'payment_method'


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_title = models.CharField(max_length=50)
    post_author = models.CharField(max_length=45)
    post_content = models.CharField(max_length=10000, blank=True, null=True)
    post_created_datetime = models.DateTimeField()
    post_last_modified_datetime = models.DateTimeField()
    post_category = models.ForeignKey('PostCategory', models.DO_NOTHING)
    post_is_deleted = models.TextField()  # This field type is a guess.
    post_is_public = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'post'


class PostAttachment(models.Model):
    post_attachment_id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, models.DO_NOTHING)
    post_attachment_path_or_link = models.CharField(max_length=200)
    post_attachment_type = models.ForeignKey('PostAttachmentType', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'post_attachment'


class PostAttachmentType(models.Model):
    post_attachment_type_id = models.AutoField(primary_key=True)
    post_attachment_type_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'post_attachment_type'


class PostCategory(models.Model):
    post_category_id = models.AutoField(primary_key=True)
    posts_category_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'post_category'


class Product(models.Model):
    product_id = models.CharField(primary_key=True, max_length=45)
    product_name = models.CharField(max_length=50)
    product_category = models.ForeignKey('ProductCategory', models.DO_NOTHING)
    product_price = models.FloatField(blank=True, null=True)
    product_description = models.CharField(max_length=200, blank=True, null=True)
    product_is_deleted = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'product'


class ProductCategory(models.Model):
    product_category_id = models.AutoField(primary_key=True)
    product_category_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'product_category'


class ReceiveMethod(models.Model):
    receive_method_id = models.AutoField(primary_key=True)
    receive_method_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'receive_method'
