# Generated by Django 4.2.5 on 2023-09-10 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('projects', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.project')),
            ],
        ),
    ]