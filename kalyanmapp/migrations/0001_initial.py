# Generated by Django 4.1.7 on 2023-03-20 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='biodata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=30)),
                ('picture', models.ImageField(upload_to='photos')),
                ('height', models.CharField(max_length=30)),
                ('weight', models.CharField(max_length=30)),
                ('caste', models.CharField(max_length=30)),
                ('income', models.CharField(max_length=30)),
                ('skintone', models.CharField(max_length=30)),
                ('siblings', models.CharField(max_length=30)),
                ('education', models.CharField(max_length=30)),
                ('expectation', models.CharField(max_length=70)),
                ('meternal', models.CharField(max_length=30)),
                ('native', models.CharField(max_length=30)),
                ('mobile', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='city',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cityname', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('subject', models.CharField(max_length=30)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('dp', models.ImageField(upload_to='photos')),
                ('role', models.IntegerField()),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='state',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statename', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='savelist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('bioid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kalyanmapp.biodata')),
                ('lid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kalyanmapp.login')),
            ],
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ratings', models.CharField(max_length=30)),
                ('comment', models.TextField()),
                ('lid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kalyanmapp.login')),
            ],
        ),
        migrations.CreateModel(
            name='detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('dob', models.DateField()),
                ('address', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=30)),
                ('cityid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kalyanmapp.city')),
                ('lid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kalyanmapp.login')),
                ('stateid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kalyanmapp.state')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='stateid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kalyanmapp.state'),
        ),
        migrations.CreateModel(
            name='choices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.CharField(max_length=30)),
                ('weight', models.CharField(max_length=30)),
                ('caste', models.CharField(max_length=30)),
                ('income', models.CharField(max_length=30)),
                ('skintone', models.CharField(max_length=30)),
                ('siblings', models.CharField(max_length=30)),
                ('education', models.CharField(max_length=30)),
                ('expectation', models.CharField(max_length=70)),
                ('meternal', models.CharField(max_length=30)),
                ('native', models.CharField(max_length=30)),
                ('lid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kalyanmapp.login')),
            ],
        ),
        migrations.AddField(
            model_name='biodata',
            name='lid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kalyanmapp.login'),
        ),
    ]
