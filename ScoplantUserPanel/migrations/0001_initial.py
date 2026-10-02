from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AddDeviceInfo',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('Username', models.CharField(max_length=64)),
                ('Version', models.CharField(max_length=64)),
                ('Name', models.CharField(max_length=64)),
                ('Location', models.CharField(max_length=64)),
                ('Time', models.TimeField(auto_now=True)),
                ('Date', models.CharField(max_length=10)),
                ('Sampling_Rate', models.IntegerField(default=60)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]