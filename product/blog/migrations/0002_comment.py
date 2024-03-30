# Generated by Django 4.2.6 on 2024-03-07 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Наименование')),
                ('description', models.TextField(verbose_name='Описание')),
                ('photo', models.ImageField(blank=True, default=None, null=True, upload_to='photos', verbose_name='Фото')),
            ],
        ),
    ]