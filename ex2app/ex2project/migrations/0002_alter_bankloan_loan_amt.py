# Generated by Django 5.1.3 on 2024-11-14 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ex2project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankloan',
            name='Loan_amt',
            field=models.CharField(max_length=40),
        ),
    ]