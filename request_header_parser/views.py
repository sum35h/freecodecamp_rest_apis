from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def who_am_i(request):

    if request.method == 'GET':
        ipaddress = request._request.META.get('REMOTE_ADDR')
        language = request._request.headers.get('Accept-Language')
        software = request._request.headers.get('User-Agent')
        response_data={"ipaddress":ipaddress,
                        "language":language,
                    "software":software,
        }
        return Response(response_data)
            
