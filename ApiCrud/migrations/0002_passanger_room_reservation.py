# Generated by Django 4.2 on 2023-04-16 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ApiCrud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passanger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=205)),
                ('dni', models.CharField(max_length=205)),
                ('tel', models.CharField(max_length=205)),
                ('country', models.CharField(blank=True, max_length=205, null=True)),
                ('city', models.CharField(blank=True, max_length=205, null=True)),
                ('adress', models.CharField(blank=True, max_length=205, null=True)),
                ('email', models.CharField(blank=True, max_length=205, null=True)),
                ('birth_date', models.DateField()),
                ('observations', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_capacity', models.CharField(max_length=205)),
                ('name', models.CharField(max_length=205)),
                ('type_room', models.CharField(choices=[('1', 'Sgl'), ('2', 'Dbl'), ('3', 'Tpl'), ('4', 'Qdpl')], default='1', max_length=4)),
                ('state', models.IntegerField(choices=[(1, 'free'), (2, 'occupied')], default=1)),
                ('status', models.CharField(choices=[('#9bf0ac', 'clean'), ('#fffb8f', 'dirty'), ('#D47777', 'blocked')], default='#9bf0ac', max_length=7)),
                ('observations', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_res', models.CharField(choices=[('1', 'Sgl'), ('2', 'Dbl'), ('3', 'Tpl'), ('4', 'Qdpl')], default='1', max_length=4)),
                ('date_in', models.DateField()),
                ('date_out', models.DateField()),
                ('number', models.IntegerField()),
                ('amount_people', models.IntegerField()),
                ('status_res', models.IntegerField(choices=[(1, 'reserved'), (2, 'check-in'), (3, 'check-out'), (4, 'no-show')], default='not-reserved')),
                ('observations', models.TextField()),
                ('passanger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ApiCrud.passanger')),
                ('room', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='ApiCrud.room')),
            ],
        ),
    ]