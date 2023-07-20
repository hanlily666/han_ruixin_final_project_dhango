from django.db import models

from django.db.models import UniqueConstraint
from django.contrib.auth.models import User


class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=50)

    def __str__(self):
        return '%s' % self.tag_name

    class Meta:
        ordering = ['tag_name']
        constraints = [
             UniqueConstraint(fields=['tag_name'], name='unique_tag')
        ]


class Album(models.Model):
    album_id = models.AutoField(primary_key=True)
    album_name = models.CharField(max_length=50)

    def __str__(self):
        return '%s' % self.album_name

    class Meta:
        ordering = ['album_name']
        constraints = [
             UniqueConstraint(fields=['album_name'], name='unique_album')
        ]


class PhotoType(models.Model):
    photo_type_id = models.AutoField(primary_key=True)
    photo_type = models.CharField(max_length=20)

    def __str__(self):
        return '%s' % self.photo_type

    class Meta:
        ordering = ['photo_type']
        constraints = [
             UniqueConstraint(fields=['photo_type'], name='unique_phototype')
        ]


class PhotoDate(models.Model):
    photo_date_id = models.AutoField(primary_key=True)
    photo_date = models.CharField(max_length=10)

    def __str__(self):
        return '%s' % self.photo_date

    class Meta:
        ordering = ['photo_date']
        constraints = [
             UniqueConstraint(fields=['photo_date'], name='unique_photodate')
        ]


class PhotoLocation(models.Model):
    photo_location_id = models.AutoField(primary_key=True)
    photo_location = models.CharField(max_length=10)

    def __str__(self):
        return '%s' % self.photo_location

    class Meta:
        ordering = ['photo_location']


class Photo(models.Model):
    photo_id = models.AutoField(primary_key=True)
    photo_caption = models.CharField(max_length=100)
    photo_description = models.CharField(max_length=200)
    photo_type = models.ForeignKey(PhotoType, on_delete=models.PROTECT)
    photo_album = models.ForeignKey(Album, on_delete=models.PROTECT)
    photo_date = models.ForeignKey(PhotoDate, on_delete=models.PROTECT)
    photo_location = models.ForeignKey(PhotoLocation, on_delete=models.PROTECT)

    def __str__(self):
        return '%s' % self.photo_caption

    class Meta:
        ordering = ['photo_caption']
        constraints = [
             UniqueConstraint(fields=['photo_caption'], name='unique_photo')
        ]


class Comments(models.Model):
    comments_id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=200)
    photo = models.ForeignKey(Photo, on_delete=models.PROTECT)

    def __str__(self):
        return '%s - %s' % (self.photo, self.content)

    class Meta:
        ordering = ['content']


class PhotoTag(models.Model):
    photo_tag_id = models.AutoField(primary_key=True)
    photo = models.ForeignKey(Photo, on_delete=models.PROTECT)
    tag = models.ForeignKey(Tag, on_delete=models.PROTECT)

    def __str__(self):
        return '%s - %s' % (self.photo, self.tag)

    class Meta:
        ordering = ['photo', 'tag']
        constraints = [
             UniqueConstraint(fields=['photo', 'tag'], name='unique_phototag')
        ]
