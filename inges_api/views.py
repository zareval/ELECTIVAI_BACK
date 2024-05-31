from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from inges_api.models import persona,pelicula,serie
from inges_api.serializer import persona_serializer,pelicula_serializer,serie_serializer

class DirectorView(APIView):
    def post(self, request, *args, **kwargs):
        data={
            'nombre':request.data.get('nombre'),
            'nacionalidad':request.data.get('nacionalidad'),
            'f_nacimiento':request.data.get('f_nacimiento'),
            'biografia':request.data.get('biografia')

        }
        serializer = persona_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request,*args,**kwargs):
        lista_directores=persona.objects.all()
        serializer_persona=persona_serializer(lista_directores,many=True)
        return Response(serializer_persona.data,status=status.HTTP_200_OK)
    
    def put(self,request,pkid):
        persona_consultada=persona.objects.filter(id=pkid).update(
            nombre=request.data.get('nombre'),
            nacionalidad=request.data.get('nacionalidad'),
            f_nacimiento=request.data.get('f_nacimiento'),
            biografia=request.data.get('biografia')
        )
        return Response(persona_consultada,status=status.HTTP_200_OK)
    
    
    def delete(self,request,pkid):
        persona_consultada=persona.objects.filter(id=pkid).delete()
        return Response(persona_consultada,status=status.HTTP_200_OK)
    
class peliView(APIView):
    def post(self,request,*args,**kwargs):
        data={
            'nombre':request.data.get('nombre'),
            'genero':request.data.get('genero'),
            'duracion':request.data.get('duracion'),
            'pais':request.data.get('pais'),
            'f_estreno':request.data.get('f_estreno'),
            'trailer':request.data.get('trailer'),
            'e_produccion':request.data.get('e_produccion'),
            'poster':request.data.get('poster'),
            'director':request.data.get('director'),
            'protagonistas':request.data.get('protagonistas')
        }
        serializer=pelicula_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request,*args,**kargs):
        lista_pelis=pelicula.objects.all()
        serializer_pelicula=pelicula_serializer(lista_pelis,many=True)
        return Response(serializer_pelicula.data,status=status.HTTP_200_OK)
    
    def put(self, request, pkid):
        pelicula_consultada = pelicula.objects.filter(id=pkid).update(
            nombre=request.data.get('nombre'),
            genero=request.data.get('genero'),
            duracion=request.data.get('duracion'),
            pais=request.data.get('pais'),
            f_estreno=request.data.get('f_estreno'),
            trailer=request.data.get('trailer'),
            e_produccion=request.data.get('e_produccion'),
            poster=request.data.get('poster'),
            director=request.data.get('director')
        )
        if pelicula_consultada:
            return Response({"detail": "Película actualizada con éxito."}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Película no encontrada."}, status=status.HTTP_404_NOT_FOUND)

    def delete(self,request,pkid):
        pelicula_consultada=pelicula.objects.filter(id=pkid).delete()
        return Response(pelicula_consultada,status=status.HTTP_200_OK)
    
class serieView(APIView):
    def post(self,request,*args,**kwargs):
        data={
            'nombre':request.data.get('nombre'),
            'genero':request.data.get('genero'),
            'duracion':request.data.get('duracion'),
            'pais':request.data.get('pais'),
            'f_estreno':request.data.get('f_estreno'),
            'trailer':request.data.get('trailer'),
            'e_produccion':request.data.get('e_produccion'),
            'poster':request.data.get('poster'),
            'director':request.data.get('director'),
            'protagonistas':request.data.get('protagonistas')
        }
        serializer=serie_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request,*args,**kargs):
        lista_serie=serie.objects.all()
        serializer_serie=serie_serializer(lista_serie,many=True)
        return Response(serializer_serie.data,status=status.HTTP_200_OK)
    
    def put(self, request, pkid):
        serie_consultada = serie.objects.filter(id=pkid).update(
            nombre=request.data.get('nombre'),
            genero=request.data.get('genero'),
            duracion=request.data.get('duracion'),
            pais=request.data.get('pais'),
            f_estreno=request.data.get('f_estreno'),
            trailer=request.data.get('trailer'),
            e_produccion=request.data.get('e_produccion'),
            poster=request.data.get('poster'),
            director=request.data.get('director')
        )
        if serie_consultada:
            return Response({"detail": "Película actualizada con éxito."}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Película no encontrada."}, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self,request,pkid):
        serie_consultada=serie.objects.filter(id=pkid).delete()
        return Response(serie_consultada,status=status.HTTP_200_OK)
    



    



    



