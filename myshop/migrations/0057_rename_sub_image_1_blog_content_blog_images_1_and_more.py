# Generated by Django 4.2 on 2023-04-12 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0056_blog_content_image_info_1_blog_content_image_info_10_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog_content',
            old_name='sub_image_1',
            new_name='blog_images_1',
        ),
        migrations.RenameField(
            model_name='blog_content',
            old_name='sub_image_10',
            new_name='blog_images_2',
        ),
        migrations.RenameField(
            model_name='blog_content',
            old_name='sub_image_11',
            new_name='blog_images_3',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='blog_intro',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='image_info_1',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='image_info_10',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='image_info_11',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='image_info_12',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='image_info_13',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='image_info_2',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='image_info_3',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='image_info_4',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='image_info_5',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='image_info_6',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='image_info_7',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='image_info_8',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='image_info_9',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='sub_body_1',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='sub_body_10',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='sub_body_11',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='sub_body_12',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='sub_body_13',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='sub_body_2',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='sub_body_3',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='sub_body_4',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='sub_body_5',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='sub_body_6',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='sub_body_7',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='sub_body_8',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='sub_body_9',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='sub_heading_1',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='sub_heading_10',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='sub_heading_11',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='sub_heading_12',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='sub_heading_13',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='sub_heading_2',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='sub_heading_3',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='sub_heading_4',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='sub_heading_5',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='sub_heading_6',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='sub_heading_7',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='sub_heading_8',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='sub_heading_9',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='sub_image_12',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='sub_image_13',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='sub_image_2',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='sub_image_3',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='sub_image_4',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='sub_image_5',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='sub_image_6',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='sub_image_7',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='sub_image_8',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='sub_image_9',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='sub_image_ALT_TAG_1',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='sub_image_ALT_TAG_10',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='sub_image_ALT_TAG_11',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='sub_image_ALT_TAG_12',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='sub_image_ALT_TAG_13',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='sub_image_ALT_TAG_2',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='sub_image_ALT_TAG_3',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='sub_image_ALT_TAG_4',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='sub_image_ALT_TAG_5',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='sub_image_ALT_TAG_6',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='sub_image_ALT_TAG_7',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='sub_image_ALT_TAG_8',
        ),
        migrations.RemoveField(
            model_name='blog_content',
            name='sub_image_ALT_TAG_9',
        ),
        migrations.AddField(
            model_name='blog_content',
            name='blog_body_1',
            field=models.TextField(default='Blog Body 1'),
        ),
        migrations.AddField(
            model_name='blog_content',
            name='blog_body_2',
            field=models.TextField(default='Blog Body 2'),
        ),
        migrations.AddField(
            model_name='blog_content',
            name='blog_body_3',
            field=models.TextField(default='Blog Body 3'),
        ),
        migrations.AddField(
            model_name='blog_content',
            name='blog_heading_2',
            field=models.CharField(default='Blog Heading 2', max_length=200),
        ),
        migrations.AddField(
            model_name='blog_content',
            name='blog_heading_3',
            field=models.CharField(default='Blog Heading 3', max_length=200),
        ),
    ]