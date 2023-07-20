from django.contrib import admin

from .models import Album, Tag, Photo, PhotoTag, PhotoDate, PhotoType, PhotoLocation, Comments
admin.site.register(Album)
admin.site.register(Tag)
admin.site.register(Photo)
admin.site.register(PhotoType)
admin.site.register(PhotoDate)
admin.site.register(PhotoTag)
admin.site.register(PhotoLocation)
admin.site.register(Comments)

