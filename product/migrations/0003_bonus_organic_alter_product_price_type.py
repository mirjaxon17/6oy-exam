# Generated by Django 5.0.4 on 2024-04-20 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bonus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='product/bonus_discount/')),
                ('discount', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('create_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='product/organic/')),
                ('price', models.FloatField()),
                ('price_type', models.CharField(choices=[('$', 'USD'), ('UZS', "so'm")], default='UZS', max_length=10)),
                ('create_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='price_type',
            field=models.CharField(choices=[('$', 'USD'), ('UZS', "so'm")], default='UZS', max_length=10),
        ),
    ]
