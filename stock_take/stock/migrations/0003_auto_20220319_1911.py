# Generated by Django 3.2 on 2022-03-19 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_auto_20220319_1326'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='parts',
            new_name='stock_parts',
        ),
        migrations.CreateModel(
            name='Parts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_required', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.stock')),
                ('product_part_belongs_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.product')),
            ],
        ),
    ]
