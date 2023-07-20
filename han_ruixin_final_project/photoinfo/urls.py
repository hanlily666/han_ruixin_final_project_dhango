from django.urls import path
from photoinfo.views import (
    photo_list_view,
    tag_list_view,
    date_list_view,
    location_list_view,
    type_list_view,
    comments_list_view,
    album_list_view,
)

urlpatterns = [
    path("photo/", photo_list_view),
    path("tag/", tag_list_view),
    path("date/", date_list_view),
    path("location/", location_list_view),
    path("type/", type_list_view),
    path("comments/", comments_list_view),
    path("album/", album_list_view),

]
