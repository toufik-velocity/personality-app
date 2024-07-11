# Generated by Django 4.2.1 on 2023-05-19 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_media', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='mbti',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='ocean',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='type',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='analysis',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='analysis',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='data',
            field=models.TextField(null=True),
        ),
    ]
