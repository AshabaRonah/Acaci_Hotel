# Generated by Django 3.2.7 on 2023-08-12 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webclass', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(max_length=254)),
                ('user_password', models.CharField(max_length=24)),
            ],
        ),
    ]
