from django.shortcuts import render

from photoinfo.models import Photo, PhotoTag, PhotoDate, PhotoLocation, PhotoType, Comments, Album


def photo_list_view(request):
    photo_list = Photo.objects.all()
    return render(request, 'photoinfo/photo_list.html', {'photo_list': photo_list})


def tag_list_view(request):
    tag_list = PhotoTag.objects.all()
    return render(request, 'photoinfo/tag_list.html', {'tag_list': tag_list})


def date_list_view(request):
    date_list = PhotoDate.objects.all()
    return render(request, 'photoinfo/date_list.html', {'date_list': date_list})


def location_list_view(request):
    location_list = PhotoLocation.objects.all()
    return render(request, 'photoinfo/location_list.html', {'location_list': location_list})


def type_list_view(request):
    type_list = PhotoType.objects.all()
    return render(request, 'photoinfo/type_list.html', {'type_list': type_list})


def comments_list_view(request):
    comments_list = Comments.objects.all()
    return render(request, 'photoinfo/comments_list.html', {'comments_list': comments_list})


def album_list_view(request):
    album_list = Album.objects.all()
    return render(request, 'photoinfo/album_list.html', {'album_list': album_list})

