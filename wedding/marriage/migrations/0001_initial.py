# Generated by Django 3.2.12 on 2022-03-16 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('f_name', models.CharField(max_length=30)),
                ('l_name', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('mobile', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=10)),
                ('birth_date', models.DateField()),
                ('qualification', models.CharField(max_length=30)),
                ('mother_tounge', models.CharField(max_length=30)),
                ('cast', models.CharField(max_length=30)),
                ('Religene', models.CharField(max_length=30)),
                ('occupation', models.CharField(max_length=30)),
                ('age', models.IntegerField(null=True)),
                ('sunshine', models.CharField(blank=True, default=None, max_length=30)),
                ('about', models.TextField(blank=True, default=None, max_length=300)),
                ('height', models.IntegerField(blank=True, default=None, null=True)),
                ('image', models.ImageField(blank=True, default=None, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Intrest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interested', models.IntegerField()),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marriage.customer')),
            ],
        ),
    ]
