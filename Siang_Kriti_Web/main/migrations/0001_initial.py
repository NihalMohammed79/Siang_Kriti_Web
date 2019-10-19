# Generated by Django 2.2.6 on 2019-10-19 12:36

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import main.file_format


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('created_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='updated at')),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='deleted at')),
                ('is_student', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_department', models.BooleanField(default=False)),
                ('is_club', models.BooleanField(default=False)),
                ('contact', models.CharField(default=False, max_length=20)),
                ('contri', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='updated at')),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='deleted at')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='updated at')),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='deleted at')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='updated at')),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='deleted at')),
                ('document', main.file_format.ContentTypeRestrictedFileField(blank=True, null=True, upload_to='static/notes/')),
                ('title', models.CharField(max_length=100)),
                ('is_approved', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nc', to='main.Course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='note', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MiscNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='updated at')),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='deleted at')),
                ('document', main.file_format.ContentTypeRestrictedFileField(blank=True, null=True, upload_to='static/misc/')),
                ('desc', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('is_approved', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mis', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CourseVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('videofile', models.FileField(null=True, upload_to='static/videos/', verbose_name='')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vc', to='main.Course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Department'),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='updated at')),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='deleted at')),
                ('document', main.file_format.ContentTypeRestrictedFileField(blank=True, null=True, upload_to='static/books/')),
                ('author', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('is_approved', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='user',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dept', to='main.Department'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
