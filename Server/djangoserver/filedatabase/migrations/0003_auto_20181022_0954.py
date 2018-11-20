# Generated by Django 2.1.1 on 2018-10-22 04:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filedatabase', '0002_auto_20181019_0021'),
    ]

    operations = [
        migrations.AddField(
            model_name='filerecord',
            name='parent_path',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='filerecord',
            name='path',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='filerecord',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='filerecord',
            name='parent',
        ),
        migrations.AlterUniqueTogether(
            name='filerecord',
            unique_together={('file_name', 'file_type', 'parent_path')},
        ),
    ]
