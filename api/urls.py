from django.urls import path

from . import views

app_name = 'api'
urlpatterns = [
    #sorry for bad coding, but im going to add api access to the database through pages and crsf
    path('session', views.session, name="api_session"),
    path('checkLogin', views.checkLogin, name="checkLogin"),
    path('extensionSettings', views.extension_settings, name="extensionSettings"),
    path('addTrackSite', views.extension_addTrackSite, name="addTrackSite"),
    path('removeTrackSite', views.extension_removeTrackSite, name="removeTrackSite"),
    path('getDayChart', views.extension_getDayChart, name="getDayChart"),
    path('updateIdentifierStrs', views.extension_updateIdentifierStrs, name="updateIdentifierStrs"),
    path('ping', views.ping, name="ping"),
]
