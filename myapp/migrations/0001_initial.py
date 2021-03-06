# Generated by Django 2.0.7 on 2018-07-23 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('album_id', models.AutoField(primary_key=True, serialize=False)),
                ('album_name', models.CharField(max_length=50)),
                ('album_category_id', models.IntegerField()),
                ('album_event_datetime', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'album',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AlbumCategory',
            fields=[
                ('album_category_id', models.AutoField(primary_key=True, serialize=False)),
                ('album_category_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'album_category',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AlbumPhotos',
            fields=[
                ('album_photos_id', models.AutoField(primary_key=True, serialize=False)),
                ('photo_path', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'album_photos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('employee_name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'employee',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=45)),
                ('event_start_datetime', models.DateTimeField()),
                ('event_end_datetime', models.DateTimeField()),
                ('event_description', models.CharField(blank=True, max_length=1000, null=True)),
                ('event_is_deleted', models.TextField()),
            ],
            options={
                'db_table': 'event',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EventCategory',
            fields=[
                ('event_category_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_category_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'event_category',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('member_id', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('member_name', models.CharField(max_length=20)),
                ('member_phone', models.CharField(max_length=20)),
                ('member_pid', models.CharField(max_length=11)),
                ('member_email', models.CharField(max_length=45)),
                ('member_introducer_reference_id', models.IntegerField()),
                ('member_is_verified', models.TextField()),
                ('member_password', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'member',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MemberIntroducerReference',
            fields=[
                ('member_introducer_reference_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'member_introducer_reference',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('message_id', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('read_status', models.TextField()),
                ('message_content', models.CharField(max_length=200)),
                ('message_datetime', models.DateTimeField()),
            ],
            options={
                'db_table': 'message',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('order_cost_balance', models.FloatField()),
                ('order_payment_is_completed', models.TextField()),
                ('order_delivery_address', models.CharField(blank=True, max_length=100, null=True)),
                ('order_create_datetime', models.DateTimeField()),
                ('order_last_modified_datetime', models.DateTimeField(blank=True, null=True)),
                ('order_deleted_datetime', models.DateTimeField(blank=True, null=True)),
                ('order_is_deleted', models.TextField()),
            ],
            options={
                'db_table': 'order',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrderCart',
            fields=[
                ('order_cart_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.IntegerField()),
            ],
            options={
                'db_table': 'order_cart',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrderProcess',
            fields=[
                ('order_process_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_process_name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'order_process',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('payment_method_id', models.AutoField(primary_key=True, serialize=False)),
                ('payment_method_name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'payment_method',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('post_title', models.CharField(max_length=50)),
                ('post_author', models.CharField(max_length=45)),
                ('post_content', models.CharField(blank=True, max_length=10000, null=True)),
                ('post_created_datetime', models.DateTimeField()),
                ('post_last_modified_datetime', models.DateTimeField()),
                ('post_is_deleted', models.TextField()),
            ],
            options={
                'db_table': 'post',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PostAttachment',
            fields=[
                ('post_attachment_id', models.AutoField(primary_key=True, serialize=False)),
                ('post_attachment_path_or_link', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'post_attachment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PostAttachmentType',
            fields=[
                ('post_attachment_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('post_attachment_type_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'post_attachment_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('post_category_id', models.AutoField(primary_key=True, serialize=False)),
                ('posts_category_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'post_category',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50)),
                ('product_price', models.FloatField(blank=True, null=True)),
                ('product_description', models.CharField(blank=True, max_length=200, null=True)),
                ('product_is_deleted', models.TextField()),
            ],
            options={
                'db_table': 'product',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('product_category_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_category_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'product_category',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ReceiveMethod',
            fields=[
                ('receive_method_id', models.AutoField(primary_key=True, serialize=False)),
                ('receive_method_name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'receive_method',
                'managed': False,
            },
        ),
    ]
