from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('github', models.CharField(blank=True, max_length=1000, null=True)),
                ('vk', models.CharField(blank=True, max_length=1000, null=True)),
                ('facebook', models.CharField(blank=True, max_length=1000, null=True)),
                ('instagram', models.CharField(blank=True, max_length=1000, null=True)),
                ('twitter', models.CharField(blank=True, max_length=1000, null=True)),
                ('website', models.CharField(blank=True, max_length=1000, null=True)),
                ('youtube', models.CharField(blank=True, max_length=1000, null=True)),
                ('mainLink', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('small', models.CharField(max_length=8000)),
                ('large', models.CharField(max_length=8000)),
            ],
            options={
                'verbose_name_plural': 'Photos',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=1024)),
                ('lookingForAJob', models.BooleanField(default=False)),
                ('lookingForAJobDescription', models.CharField(max_length=1024)),
                ('contacts', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profiles.contacts')),
                ('photos', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profiles.photos')),
            ],
            options={
                'verbose_name_plural': 'Profiles',
            },
        ),
    ]