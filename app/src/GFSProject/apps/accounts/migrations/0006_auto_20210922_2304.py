# Generated by Django 3.2.7 on 2021-09-22 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certifications', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'certification',
                'verbose_name_plural': 'certifications',
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='desiredqualification',
            field=models.ManyToManyField(to='accounts.Certifications'),
        ),
        migrations.AddField(
            model_name='profile',
            name='get_certified',
            field=models.ManyToManyField(related_name='get_certified', to='accounts.Certifications'),
        ),
    ]