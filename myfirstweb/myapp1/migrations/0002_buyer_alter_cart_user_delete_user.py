# Generated by Django 5.0.4 on 2024-04-06 09:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('nickname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to='myapp1.buyer'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
