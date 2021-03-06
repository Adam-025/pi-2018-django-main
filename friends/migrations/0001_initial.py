# Generated by Django 3.2 on 2021-12-29 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('first_contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first_friends', to='contacts.contact')),
                ('second_contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='second_friends', to='contacts.contact')),
            ],
            options={
                'unique_together': {('first_contact', 'second_contact')},
            },
        ),
    ]
