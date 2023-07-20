# Generated by Django 4.2.2 on 2023-07-15 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0011_electrical_tools_house_tools_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('Description', models.CharField(max_length=255, null=True)),
                ('city', models.CharField(choices=[('مدينة ديرالزور', 'مدينة ديرالزور'), ('موحسن', 'موحسن'), ('ابوعمر', 'ابوعمر'), ('العبد', 'العبد'), ('البوليل', 'البوليل'), ('الطوب', 'الطوب'), ('الزباري', 'الزباري'), ('سعلو', 'سعلو'), ('مدينة الميادين', 'مدينة الميادين'), ('محكان', 'محكان'), ('القورية', 'القورية'), ('عشارة ', 'عشارة '), ('غريبه', 'غريبه'), ('تشرين', 'تشرين'), ('صبيخان', 'صبيخان'), ('دوير', 'دوير'), ('مدينة البوكمال', 'مدينة البوكمال')], max_length=255, null=True)),
                ('neighborhood', models.CharField(max_length=255, null=True)),
                ('screen', models.IntegerField(null=True)),
                ('memory', models.IntegerField(null=True)),
                ('ram', models.IntegerField(null=True)),
                ('main_camera', models.IntegerField(null=True)),
                ('selfie_camera', models.IntegerField(null=True)),
                ('cpu', models.CharField(max_length=255, null=True)),
                ('battery', models.IntegerField(null=True)),
                ('price', models.IntegerField(null=True)),
                ('phone_owner', models.CharField(max_length=10)),
                ('image_one', models.ImageField(blank=True, null=True, upload_to='house')),
                ('image_tow', models.ImageField(blank=True, null=True, upload_to='house')),
                ('image_three', models.ImageField(blank=True, null=True, upload_to='house')),
                ('image_fore', models.ImageField(blank=True, null=True, upload_to='house')),
            ],
        ),
    ]
