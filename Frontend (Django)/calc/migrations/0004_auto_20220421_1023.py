# Generated by Django 2.2.4 on 2022-04-21 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0003_registeredchild_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('unique_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='registeredchild',
            name='age',
            field=models.IntegerField(default=7),
            preserve_default=False,
        ),
    ]
