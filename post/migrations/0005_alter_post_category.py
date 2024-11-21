# Generated by Django 4.2.16 on 2024-11-21 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('WD', 'Web Development'), ('DT', 'Descktop Development'), ('DS', 'Data Science')], default='Enter Your Choice', max_length=50),
        ),
    ]