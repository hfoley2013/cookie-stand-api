from django.urls import path
from .views import CookieStandList, CookieStandDetail
from .views_front import (
    CookieStandCreateView,
    CookieStandDeleteView,
    CookieStandDetailView,
    CookieStandListView,
    CookieStandUpdateView,
)

urlpatterns = [
    path("", CookieStandList.as_view(), name="cookie_stand_list"),
    path("<int:pk>/", CookieStandDetail.as_view(), name="cookie_stand_detail"),
    path("", CookieStandListView.as_view(), name="cookie_stand_list"),
    path("<int:pk>/", CookieStandDetailView.as_view(), name="cookie_stand_detail"),
    path("create/", CookieStandCreateView.as_view(), name="cookie_stand_create"),
    path("<int:pk>/update/", CookieStandUpdateView.as_view(), name="cookie_stand_update"),
    path("<int:pk>/delete/", CookieStandDeleteView.as_view(), name="cookie_stand_delete"),
]
