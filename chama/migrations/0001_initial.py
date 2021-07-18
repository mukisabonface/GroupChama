# Generated by Django 2.1.7 on 2019-04-17 11:16

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone_number', models.CharField(max_length=10, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Chama',
            fields=[
                ('chama_id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular chama across whole app', primary_key=True, serialize=False)),
                ('groupName', models.CharField(max_length=255, unique=True)),
                ('paybillNo', models.PositiveIntegerField(unique=True)),
                ('contribution_amnt', models.DecimalField(decimal_places=2, max_digits=10)),
                ('contribution_interval', models.CharField(blank=True, choices=[('d', 'Daily'), ('w', 'Weekly'), ('m', 'Monthly'), ('q', 'Quartely')], default='d', help_text='Contribution Intervals', max_length=1)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['groupName'],
            },
        ),
        migrations.CreateModel(
            name='ChamaMeetings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meeting_date', models.DateTimeField()),
                ('location', models.TextField(blank=True, max_length=300)),
                ('chama', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='meetings', to='chama.Chama')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='LoanRequests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_approved', models.BooleanField(default=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_paid', models.BooleanField(default=False)),
                ('chama', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='loan_requests', to='chama.Chama')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='my_loan_requests', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateTimeField()),
                ('chama', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chama.Chama')),
                ('member', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('transaction_time', models.DateTimeField()),
                ('phone_number', models.CharField(blank=True, max_length=10)),
                ('transaction_type', models.CharField(blank=True, choices=[('f', 'Fine'), ('d', 'Deposit'), ('l', 'Loan')], default='d', help_text='I am paying for? Deposit,Fine or Loan', max_length=1)),
                ('chama', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='transactions', to='chama.Chama')),
                ('member', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='transactions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='chama',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='chama', through='chama.Membership', to=settings.AUTH_USER_MODEL),
        ),
    ]