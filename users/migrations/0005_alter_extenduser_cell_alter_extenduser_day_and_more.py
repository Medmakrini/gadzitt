# Generated by Django 4.0.6 on 2022-09-13 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_extenduser_psw'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extenduser',
            name='cell',
            field=models.CharField(choices=[('media', 'media'), ('contact & sponsoring', 'contact & sponsoring'), ('Events', 'Events'), ('Gaming', 'Gaming'), ('Formation', 'Formation')], default='media', max_length=500),
        ),
        migrations.AlterField(
            model_name='extenduser',
            name='day',
            field=models.CharField(choices=[('Premier jour', 'Premier jour'), ('Deuxième jour', 'Deuxième jour')], default='Premier jour', max_length=500),
        ),
        migrations.AlterField(
            model_name='extenduser',
            name='year',
            field=models.CharField(choices=[('1er année', '1er année'), ('2ème année', '2ème année'), ('3ème année', '3ème année'), ('4ème année', '4ème année'), ('5ème année', '5ème année')], default='1er année', max_length=500),
        ),
    ]