# Generated by Django 2.0.7 on 2018-07-31 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='todolist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datebegan', models.DateTimeField(auto_now_add=True)),
                ('taskdetails', models.CharField(max_length=255)),
            ],
        ),
    ]
