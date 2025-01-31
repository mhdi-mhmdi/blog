# Generated by Django 4.2.7 on 2024-01-05 21:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0012_alter_image_image_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', django_jalali.db.models.jDateField(blank=True, null=True, verbose_name='تاریخ تولد')),
                ('bio', models.TextField(blank=True, null=True, verbose_name='بیو')),
                ('photo', django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format=None, keep_meta=True, quality=60, scale=None, size=[500, 500], upload_to='account/images', verbose_name='تصویر پروفایل')),
                ('job', models.CharField(blank=True, max_length=250, null=True, verbose_name='شغل')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='account', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'اکانت',
                'verbose_name_plural': 'اکانت ها',
            },
        ),
    ]
