# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from . import views



urlpatterns = [
    # URL pattern for the ArtistList

    url(
        regex=r'^$',
        view=views.ArtistList.as_view(),
        name='artist-list'
    ),

    # URL pattern for the ArtistDetail

    url(
        regex=r'^detail/(?P<slug>[\w-]+)/$',
        view=views.ArtistDetail.as_view(),
        name='artist-detail'
    ),

]
