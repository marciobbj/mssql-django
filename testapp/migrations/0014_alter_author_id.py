# Generated by Django 3.2.5 on 2021-07-28 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0013_alter_author_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
