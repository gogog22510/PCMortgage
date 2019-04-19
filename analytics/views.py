from django.shortcuts import render
from django.contrib import auth
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from analytics import static_data as stdata
from analytics.change_event import ChangeEventSerializer


# Create your views here.
def index(request):
	data = stdata.load_static_data();
	return render(request, 'analytics/index.html', data)

def test(request):
	print(request.data)
	data = stdata.load_static_data();
	return render(request, 'analytics/index.html', data)

@api_view(['GET', 'PUT'])
def update_table(request, name):
	if request.method == 'PUT':
		event = ChangeEventSerializer(request.data)
		stdata.update_data(event.data)
		return Response(stdata.load_static_data())
	else:
		return Response({}, status=status.HTTP_404_NOT_FOUND)