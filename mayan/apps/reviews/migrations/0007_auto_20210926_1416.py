# Generated by Django 2.2.23 on 2021-09-26 14:16

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0075_delete_duplicateddocumentold'),
        ('reviews', '0006_auto_20210926_0405'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewform',
            name='documents',
            field=models.ManyToManyField(blank=True, related_name='reviews', to='documents.Document', verbose_name='Documents'),
        ),
        migrations.AddField(
            model_name='reviewform',
            name='level',
            field=models.PositiveIntegerField(default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reviewform',
            name='lft',
            field=models.PositiveIntegerField(default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reviewform',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='reviews.ReviewForm'),
        ),
        migrations.AddField(
            model_name='reviewform',
            name='rght',
            field=models.PositiveIntegerField(default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reviewform',
            name='tree_id',
            field=models.PositiveIntegerField(db_index=True, default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='reviewform',
            unique_together={('parent', 'candidate')},
        ),
    ]