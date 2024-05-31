from django.urls import path
from inges_api.views import DirectorView,peliView,serieView

urlpatterns=[
    #URL DIRECTOR
    path('creacionDirector',DirectorView.as_view()), #post
    path('actualizacionDirector/<int:pkid>/', DirectorView.as_view(), name='actualizacion'), #put
    path('eliminacionDirector/<int:pkid>/', DirectorView.as_view(), name='eliminar'), #delete
    
    #URL Peli
    path('creacionPe',peliView.as_view()), #post
    path('actualizacionPeli/<int:pkid>/', peliView.as_view(), name='actualizacion_pelicula'), #put
    path('eliminacionPeli/<int:pkid>/', peliView.as_view(), name='eliminacion'), #delete

    #Url Serie

    path('creacionSe',serieView.as_view()), #post
    path('actualizacionSe/<int:pkid>/', serieView.as_view(), name='actualizacionSe'), #put
    path('eliminacionSe/<int:pkid>/', serieView.as_view(), name='eliminacionSe'), #delete






]