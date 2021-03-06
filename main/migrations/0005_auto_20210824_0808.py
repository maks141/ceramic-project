# Generated by Django 3.0 on 2021-08-24 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_partners_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='catalog/images', verbose_name='Фото для статьи')),
                ('text', models.TextField(verbose_name='Текст статьи')),
            ],
        ),
        migrations.RenameModel(
            old_name='Partners',
            new_name='Partner',
        ),
        migrations.RenameModel(
            old_name='Sliders',
            new_name='Slider',
        ),
    ]
