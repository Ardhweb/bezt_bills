# Generated by Django 5.0.6 on 2024-07-01 16:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('invoice_id', models.AutoField(primary_key=True, serialize=False)),
                ('random_invoice_id', models.CharField(blank=True, max_length=250, null=True)),
                ('template_name', models.CharField(blank=True, max_length=250, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[(1, 'Pending'), (2, 'Paid'), (3, 'Done')], max_length=255, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(blank=True, max_length=250, null=True)),
                ('qty', models.PositiveIntegerField(db_column='quntity')),
                ('price', models.CharField(blank=True, max_length=250, null=True)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoicemodule.invoice')),
            ],
        ),
    ]
