from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from .serializers import TimestampSerializer
from datetime import datetime,timezone
import time
import re
@api_view(['GET'])
def time_data(request,ts):
    
    if request.method == 'GET':
        utc = None
        if ts.__contains__('-'):
            try:
                utc = datetime.strptime(ts,'%Y-%m-%d').replace(tzinfo=timezone.utc)
            except ValueError:
                data={"error": "Invalid Date"}
                return Response(data)
        else:
            try:
                t=int(ts)//1000
                utc = datetime.utcfromtimestamp(t)
            except ValueError:
                data={"error": "Invalid Date"}
                return Response(data)

        data={
            "unix": int(utc.timestamp())*1000,
            "utc": utc.strftime("%a, %d %b %Y %H:%M:%S GMT")
            }
            
        return Response(data)
            


@api_view(['GET'])
def time_data_now(request):
    
    if request.method == 'GET':
        t= time.time()
        utc = datetime.utcfromtimestamp(t)
           
        
        data={
            "unix": int(utc.timestamp())*1000,
            "utc": utc.strftime("%a, %d %b %Y %H:%M:%S GMT")
            }

        return Response(data)
    
# class time_data(APIView):
#     def get(self,request,time, format=None):
#         data={
#         "unix": 1220302323,
#         "utc": "Fri, 25 Dec 2015 00:00:00 GMT",
#         "time":time
#         }
#         return Response(data)
