# Generated by Django 4.1.5 on 2023-01-20 22:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('is_up', models.BooleanField(default=False)),
                ('since', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Check',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verificationDate', models.DateTimeField(auto_now_add=True)),
                ('is_up', models.BooleanField(default=False)),
                ('message', models.CharField(default='Up', max_length=255)),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='isup.domain')),
            ],
        ),
    ]