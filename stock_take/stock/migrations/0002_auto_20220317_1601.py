# Generated by Django 3.2 on 2022-03-17 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parts',
            name='item',
        ),
        migrations.AddField(
            model_name='parts',
            name='item',
            field=models.ManyToManyField(to='stock.Stock'),
        ),
        migrations.RemoveField(
            model_name='product',
            name='parts',
        ),
        migrations.AddField(
            model_name='product',
            name='parts',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='stock.parts'),
            preserve_default=False,
        ),
    ]
