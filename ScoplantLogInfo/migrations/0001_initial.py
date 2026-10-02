import uuid
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('ScoplantUserPanel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogInfo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Date_Log', models.DateField(auto_now=True)),
                ('Time_Log', models.CharField(max_length=10)),
                ('Battery_Log', models.CharField(max_length=3)),
                ('Lux_Log', models.CharField(max_length=10)),
                ('Humidity_Log', models.CharField(max_length=10)),
                ('Temperature_Log', models.CharField(max_length=10)),
                ('SoilMoisture_Log', models.CharField(max_length=10)),
                ('SoilTemperature_Log', models.CharField(max_length=10)),
                ('EC_Log', models.CharField(max_length=10)),
                ('id_device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ScoplantUserPanel.adddeviceinfo')),
            ],
        ),
    ]