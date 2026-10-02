import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='AccountDevice',
            fields=[
                ('Username', models.CharField(max_length=64, unique=True)),
                ('Version', models.CharField(max_length=64)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('MQTT_ID', models.CharField(max_length=64)),
                ('MQTT_USERNAME', models.CharField(max_length=64)),
                ('MQTT_PASSWORD', models.CharField(max_length=64)),
                ('MQTT_PUB', models.CharField(max_length=64)),
                ('MQTT_SUB', models.CharField(max_length=64)),
                ('Date', models.DateTimeField(auto_now=True)),
                ('Active', models.BooleanField(default=False, editable=False, help_text='Warning! Do Not Active This')),
            ],
        ),
    ]