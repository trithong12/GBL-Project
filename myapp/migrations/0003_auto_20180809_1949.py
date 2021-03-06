# Generated by Django 2.0.7 on 2018-08-09 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20180724_0107'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='album',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='albumcategory',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='albumphotos',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='eventcategory',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='member',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='memberintroducerreference',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='ordercart',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='orderprocess',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='paymentmethod',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='postattachment',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='postattachmenttype',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='postcategory',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='receivemethod',
            options={'managed': False},
        ),
    ]
