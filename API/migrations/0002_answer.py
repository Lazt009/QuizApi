# Generated by Django 3.1.3 on 2021-03-27 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=60)),
                ('questnId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.quizquestion')),
            ],
        ),
    ]
