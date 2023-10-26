# Generated by Django 4.2.5 on 2023-09-22 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phishing_simulator', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='phishingattempt',
            options={'ordering': ['-timestamp'], 'verbose_name': 'Phising Attempt', 'verbose_name_plural': 'Phising Attempt'},
        ),
        migrations.AddField(
            model_name='phishingattempt',
            name='attack_type',
            field=models.CharField(default='phishing attack', max_length=255),
            preserve_default=False,
        ),
    ]
