from django.conf import settings
from rest_framework import serializers
from myapp import models

class PostAttachmentSerializer(serializers.ModelSerializer):
    #post_attachment_type = serializers.CharField(source='post_attachment_type.post_attachment_type_name')
    class Meta:
        model = models.PostAttachment
#        fields = '__all__'
        fields = ('post_attachment_path_or_link',)

class PostSerializer(serializers.ModelSerializer):
    post_attachment = PostAttachmentSerializer(many=True)
    post_category = serializers.CharField(source='post_category.post_category_name')
    class Meta:
        model = models.Post
#        fields = '__all__'
        fields = ('post_id', 'post_title', 'post_last_modified_datetime', 'post_category', 'post_attachment')

class EventSerializer(serializers.ModelSerializer):
    event_category = serializers.CharField(source='event_category.event_category_name')
    event_start_datetime = serializers.DateTimeField(format=settings.DATETIME_FORMAT)
    event_end_datetime = serializers.DateTimeField(format=settings.DATETIME_FORMAT)
    class Meta:
        model = models.Event
        fields = '__all__'

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
        fields = ('title', 'album_category', 'album_event_datetime', 'images')

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