# Generated by Django 3.2 on 2021-12-29 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0001_initial'),
        ('contacts', '0003_remove_contact_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='address',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='addresses.address'),
        ),
    ]
