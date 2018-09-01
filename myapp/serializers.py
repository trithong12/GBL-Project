from django.conf import settings
from rest_framework import serializers
from myapp import models
from datetime import datetime

class PostAttachmentSerializer(serializers.ModelSerializer):
    #post_attachment_type = serializers.CharField(source='post_attachment_type.post_attachment_type_name')
    class Meta:
        model = models.PostAttachment
        fields = '__all__'
#        fields = ('post_attachment_path_or_link',)

class PostSerializer(serializers.ModelSerializer):
    post_attachment = PostAttachmentSerializer(many=True)
    post_category = serializers.CharField(source='post_category.post_category_name')
    class Meta:
        model = models.Post
        fields = '__all__'
#        fields = ('post_id', 'post_title', 'post_last_modified_datetime', 'post_category', 'post_attachment')
    
    def create(self, validated_data):
        attachments = validated_data.pop('post_attachment')
        category = validated_data.get('post_category')['post_category_name']
        category = models.PostCategory.objects.get(post_category_name=category)
        validated_data['post_category'] = category
        new_post = models.Post.objects.create(**validated_data)
        print(new_post, '\n', type(new_post))
        for attachment in attachments:
            new_attachment = models.PostAttachment()
            new_attachment.post = new_post
            new_attachment.post_attachment_path_or_link = attachment['post_attachment_path_or_link']
            new_attachment.save()
        return new_post

    def update(self, instance, validated_data):
        new_attachments = validated_data.pop('post_attachment')
        old_attachments = (instance.post_attachment).all()
        old_attachments = list(old_attachments)
        instance.post_title = validated_data.get('post_title', instance.post_title)
        instance.post_subtitle = validated_data.get('post_subtitle', instance.post_subtitle)
        instance.post_url = validated_data.get('post_url', instance.post_url)
        instance.post_author = validated_data.get('post_author', instance.post_author)
        instance.post_content = validated_data.get('post_content', instance.post_content)
        instance.post_news_link = validated_data.get('post_news_link', instance.post_news_link)
        instance.post_last_modified_datetime = datetime.now()
        category = validated_data.pop('post_category')['post_category_name']
        category = models.PostCategory.objects.get(post_category_name=category)
        instance.post_category = category
        instance.post_is_public = validated_data.get('post_is_public', instance.post_is_public)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.post_is_top_show = validated_data.get('post_is_top_show', instance.post_is_top_show)
        instance.save()
        for new_attachment in new_attachments:
            attachment = old_attachments.pop(0)
            attachment.post_id = new_attachment.get('post_id', attachment.post_id)
            attachment.post_attachment_path_or_link = new_attachment.get('post_attachment_path_or_link', attachment.post_attachment_path_or_link)
            attachment.save()
        return instance

class EventSerializer(serializers.ModelSerializer):
    event_category = serializers.CharField(source='event_category.event_category_name')
    event_start_datetime = serializers.DateTimeField()
    event_end_datetime = serializers.DateTimeField()
    class Meta:
        model = models.Event
        fields = '__all__'
        
    def create(self, validated_data):
        category = validated_data.get('event_category')['event_category_name']
        category = models.EventCategory.objects.get(event_category_name=category)
        validated_data['event_category'] = category
        event = models.Event.objects.create(**validated_data)
        return event

    def update(self, instance, validated_data):
        instance.event_name = validated_data.get('event_name', instance.event_name)
        category = validated_data.get('event_category')['event_category_name']
        category = models.EventCategory.objects.get(event_category_name=category)
        instance.event_category = category
        instance.event_start_datetime = validated_data.get('event_start_datetime', instance.event_start_datetime)
        instance.event_end_datetime  = validated_data.get('event_end_datetime', instance.event_end_datetime )
        instance.event_description = validated_data.get('event_description', instance.event_description)
        instance.save()
        return instance

class AlbumImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AlbumImage
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    album_category = serializers.CharField(source='album_category.album_category_name')
    album_event_datetime = serializers.DateTimeField(format=settings.DATETIME_FORMAT)
    images = AlbumImageSerializer(many=True)
    class Meta:
        model = models.Album
        fields = '__all__'
#        fields = ('title', 'album_category', 'album_event_datetime', 'images')

class ProductSerializer(serializers.ModelSerializer):
#    product_category = serializers.PrimaryKeyRelatedField(queryset=models.ProductCategory.objects.all())
#    product_category = serializers.CharField(source='product_category.product_category_name')    
    class Meta:
        model = models.Product
        fields = '__all__'
        #fields = ('product_id', 'product_name', 'product_category', 'product_price', 'product_description')
#    def create(self, validated_data):
#        tracks_data = validated_data.pop('tracks')
#        album = Album.objects.create(**validated_data)
#        for track_data in tracks_data:
#            Track.objects.create(album=album, **track_data)
#        return album

class OrderCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderCart
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    order_process = serializers.CharField(source='order_process.order_process_name')
    order_cart = OrderCartSerializer(many=True)
    order_create_datetime = serializers.DateTimeField(format=settings.DATETIME_FORMAT)
    order_last_modified_datetime = serializers.DateTimeField(format=settings.DATETIME_FORMAT)
    order_deleted_datetime = serializers.DateTimeField(format=settings.DATETIME_FORMAT)
    class Meta:
        model = models.Order
        fields = '__all__'

#class MemberIntroducerReferenceSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = models.MemberIntroducerReference
#        fields = '__all__'

class MemberSerializer(serializers.ModelSerializer):
#    member_introducer_reference = serializers.CharField(source='member_introducer_reference.introducer')
    class Meta:
        model = models.Member
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Message
        fields = '__all__'
        
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LoginForm
        fields = '__all__'