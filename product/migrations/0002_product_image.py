# Generated by Django 5.0.4 on 2024-04-20 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=1, upload_to='product/product/'),
            preserve_default=False,
        ),
    ]
