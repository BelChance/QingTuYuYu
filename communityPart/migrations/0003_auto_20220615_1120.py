# Generated by Django 2.2.4 on 2022-06-15 03:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('communityPart', '0002_auto_20220614_2352'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='community',
            options={'ordering': ('-publishDate',), 'verbose_name': '产品', 'verbose_name_plural': '产品'},
        ),
        migrations.AlterModelOptions(
            name='communityimg',
            options={'verbose_name': '产品图片', 'verbose_name_plural': '产品图片'},
        ),
        migrations.AlterField(
            model_name='community',
            name='communityType',
            field=models.CharField(choices=[('足球新闻&小知识', '足球新闻&小知识'), ('足球英语', '足球英语'), ('体育相关政策', '体育相关政策'), ('健康知识', '健康知识')], max_length=50, verbose_name='产品类型'),
        ),
        migrations.AlterField(
            model_name='community',
            name='description',
            field=models.TextField(verbose_name='产品详情描述'),
        ),
        migrations.AlterField(
            model_name='community',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=7, null=True, verbose_name='产品价格'),
        ),
        migrations.AlterField(
            model_name='community',
            name='title',
            field=models.CharField(max_length=50, verbose_name=' 产品标题'),
        ),
        migrations.AlterField(
            model_name='communityimg',
            name='community',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='communityImgs', to='communityPart.community', verbose_name='产品'),
        ),
    ]
