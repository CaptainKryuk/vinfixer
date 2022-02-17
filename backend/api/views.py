from rest_framework import authentication, permissions, serializers, status
from rest_framework.decorators import action, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from users.models import User
from carfax.service import APIRequest

from .serializers import NewUserSerializer, UserSerializer


class UsersViewSet(ViewSet):
	# permission_classes = [permissions.IsAuthenticated, ]
	# authentication_classes = [JWTTokenUserAuthentication, ]

	def create(self, request):
		"""
		create new user
		"""
		serializer = NewUserSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	
	@authentication_classes([JWTTokenUserAuthentication, ])
	@permission_classes([IsAuthenticated, ])
	def retrieve(self, request, pk=None):
		user = User.objects.filter(pk=pk).first()
		if user:
			serializer = UserSerializer(user)
			return Response(serializer.data)
		return Response(status=status.HTTP_404_NOT_FOUND)


	@action(detail=False, methods=["post"])
	def login(self, request):
		"""
		* user login
		"""
		auth = self.jwt_authenticate_user(request, request.data["username"], request.data["password"]) 

		if auth["token"]:

			# get project via user
			project = self.get_last_project(auth["user"]["id"])

			return Response({"token": auth["token"], "project": project, "user": auth["user"]})
		return Response(auth["error"], status=status.HTTP_400_BAD_REQUEST)



class CarfaxViewSet(ViewSet):

	def retrieve(self, request, pk=None):
		pass

	
	def create(self, request):
		"""
		Send request with vin in data for first checking, after that user in frontend must receive modal 
		window with information about future steps
		"""
		request = APIRequest(request.data)
		result = request.get_report()
		return Response(result)


	@action(detail=False, methods=["post"])
	def preview(self, request):
		request = APIRequest(request.data)
		result = request.get_preview_result()
		return Response(result)
