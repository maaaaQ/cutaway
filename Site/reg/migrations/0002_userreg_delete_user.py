# Generated by Django 4.2.3 on 2023-09-08 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserReg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('password1', models.CharField(max_length=20)),
                ('password2', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]