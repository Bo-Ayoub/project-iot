from django.db.models import Max
from django.core.cache import cache
from django.shortcuts import render
from .models import Actionn
from .serializers import ActionnSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Rolee , Utilisateur
from .serializers import RoleeSerializer ,UtilisateurSerializer
from .models import Temperature
from .serializers import TemperatureSerializer
from django.utils.timezone import now , make_aware
from .models import Incident
from .serializers import IncidentSerializer
from .models import Commentaire
from .serializers import CommentaireSerializer

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime, timedelta

# A list to store temperature and humidity records in memory
data_records = []
@csrf_exempt
def receive_temperature_humidity(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            temperature = data.get("temp")
            humidity = data.get("hum")

            new_record = Temperature(
                temprecord=temperature,
                humidityrecord=humidity,
                daterecord=datetime.now()  # Record the current timestamp
            )
            new_record.save()
            if temperature <2 or temperature >10 :
                # Filter users with idRole=1
                users_with_role_1 = Utilisateur.objects.filter(idrole__id=1)

                # To iterate over and display the results
                for user in users_with_role_1:
                    print(user.nom, user.prenom, user.email,user.id)
                users_list = list(users_with_role_1)
                cpt = cache.get('cpt')
                if cpt:
                    cache.set('cpt',cpt+1)
                    if cpt<4:
                        cache.set('cpt',cpt+1)
                    if cpt<7:
                        cache.set('cpt', cpt + 1)
                    if cpt>=7:
                        cache.set('cpt', cpt + 1)

            else :
                cache.set('cpt',0)











            # temperature <2 or > 10 /send to the first opereator , after 3 requests send to the second opeartor

            # Add record to the in-memory data_records list
            data_records.append({
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "temperature": temperature,
                "humidity": humidity,
            })
            print(f"Received Temperature: {temperature}, Humidity: {humidity}")
            return JsonResponse({"status": "success"}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    else:
      #  return JsonResponse({"error": "Only POST method is allowed"}, status=405)
        # Render the table with existing records
        return render(request, "table.html", {"data_records": data_records})




class UserListView(APIView):
    def get(self, request):
        users = Utilisateur.objects.all()
        serializer = UtilisateurSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UtilisateurSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailView(APIView):
    def get(self, request, pk):
        try:
            user = Utilisateur.objects.get(pk=pk)
        except Utilisateur.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UtilisateurSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            user = Utilisateur.objects.get(pk=pk)
        except Utilisateur.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UtilisateurSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            user = Utilisateur.objects.get(pk=pk)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Utilisateur.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        mdp = request.data.get('mdp')

        try:
            user = Utilisateur.objects.get(email=email)
        except Utilisateur.DoesNotExist:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        return  Response({'Message' : 'Login successufl','id' : user.id})
        #if check_password(mdp, user.mdp):  # Ensure passwords are hashed in real-world scenarios
        #    return Response({'message': 'Login successful', 'apiKey': user.apiKey})
        #return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



class RoleListView(APIView):
    def get(self, request):
        roles = Rolee.objects.all()
        serializer = RoleeSerializer(roles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RoleeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RoleDetailView(APIView):
    def get(self, request, id):
        try:
            role = Rolee.objects.get(id=id)
        except Rolee.DoesNotExist:
            return Response({'error': 'Role not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = RoleeSerializer(role)
        return Response(serializer.data)

    def put(self, request, id):
        try:
            role = Rolee.objects.get(id=id)
        except Rolee.DoesNotExist:
            return Response({'error': 'Role not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = RoleeSerializer(role, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            role = Rolee.objects.get(id=id)
            role.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Rolee.DoesNotExist:
            return Response({'error': 'Role not found'}, status=status.HTTP_404_NOT_FOUND)


class TemperatureListView(APIView):
    def get(self, request):
        temperatures = Temperature.objects.all()
        serializer = TemperatureSerializer(temperatures, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TemperatureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TemperatureDetailView(APIView):
    def get(self, request, id):
        try:
            temperature = Temperature.objects.get(id=id)
        except Temperature.DoesNotExist:
            return Response({'error': 'Temperature record not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TemperatureSerializer(temperature)
        return Response(serializer.data)

    def put(self, request, id):
        try:
            temperature = Temperature.objects.get(id=id)
        except Temperature.DoesNotExist:
            return Response({'error': 'Temperature record not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TemperatureSerializer(temperature, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            temperature = Temperature.objects.get(id=id)
            temperature.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Temperature.DoesNotExist:
            return Response({'error': 'Temperature record not found'}, status=status.HTTP_404_NOT_FOUND)



class ActionListView(APIView):
    def get(self, request):
        actions = Actionn.objects.all()
        serializer = ActionnSerializer(actions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ActionnSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ActionDetailView(APIView):
    def get(self, request, id):
        try:
            action = Actionn.objects.get(id=id)
        except Actionn.DoesNotExist:
            return Response({'error': 'Action not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ActionnSerializer(action)
        return Response(serializer.data)

    def put(self, request, id):
        try:
            action = Actionn.objects.get(id=id)
        except Actionn.DoesNotExist:
            return Response({'error': 'Action not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ActionnSerializer(action, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            action = Actionn.objects.get(id=id)
            action.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Actionn.DoesNotExist:
            return Response({'error': 'Action not found'}, status=status.HTTP_404_NOT_FOUND)

class UserActionsView(APIView):
    def get(self, request, user_id):
        actions = Actionn.objects.filter(idUser=user_id)
        serializer = ActionnSerializer(actions, many=True)
        return Response(serializer.data)



class IncidentListView(APIView):
    def get(self, request):
        incidents = Incident.objects.all()
        serializer = IncidentSerializer(incidents, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = IncidentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IncidentDetailView(APIView):
    def get(self, request, id):
        try:
            incident = Incident.objects.get(id=id)
        except Incident.DoesNotExist:
            return Response({'error': 'Incident not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = IncidentSerializer(incident)
        return Response(serializer.data)

    def put(self, request, id):
        try:
            incident = Incident.objects.get(id=id)
        except Incident.DoesNotExist:
            return Response({'error': 'Incident not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = IncidentSerializer(incident, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            incident = Incident.objects.get(id=id)
            incident.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Incident.DoesNotExist:
            return Response({'error': 'Incident not found'}, status=status.HTTP_404_NOT_FOUND)

class ResolvedIncidentsView(APIView):
    def get(self, request):
        incidents = Incident.objects.filter(statusResolved=True)
        serializer = IncidentSerializer(incidents, many=True)
        return Response(serializer.data)

class UnresolvedIncidentsView(APIView):
    def get(self, request):
        incidents = Incident.objects.filter(statusResolved=False)
        serializer = IncidentSerializer(incidents, many=True)
        return Response(serializer.data)



class CommentListView(APIView):
    def get(self, request):
        comments = Commentaire.objects.all()
        serializer = CommentaireSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentaireSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentDetailView(APIView):
    def get(self, request, id):
        try:
            comment = Commentaire.objects.get(id=id)
        except Commentaire.DoesNotExist:
            return Response({'error': 'Comment not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CommentaireSerializer(comment)
        return Response(serializer.data)

    def put(self, request, id):
        try:
            comment = Commentaire.objects.get(id=id)
        except Commentaire.DoesNotExist:
            return Response({'error': 'Comment not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CommentaireSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            comment = Commentaire.objects.get(id=id)
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Commentaire.DoesNotExist:
            return Response({'error': 'Comment not found'}, status=status.HTTP_404_NOT_FOUND)



from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Incident
from .serializers import IncidentSerializer

class UserIncidentsView(APIView):
    def get(self, request, user_id):
        # Filter incidents by user_id
        incidents = Incident.objects.filter(idUser=user_id)
        serializer = IncidentSerializer(incidents, many=True)
        return Response(serializer.data)
class TemperatureIncidentsView(APIView):
    def get(self, request, temperature_id):
        # Filter incidents by the associated temperature ID
        incidents = Incident.objects.filter(idTemp=temperature_id)
        serializer = IncidentSerializer(incidents, many=True)
        return Response(serializer.data)
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Commentaire
from .serializers import CommentaireSerializer

class IncidentCommentsView(APIView):
    def get(self, request, incident_id):
        # Filter comments by the associated incident ID
        comments = Commentaire.objects.filter(idIncident=incident_id)
        serializer = CommentaireSerializer(comments, many=True)
        return Response(serializer.data)

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Commentaire
from .serializers import CommentaireSerializer

class UserCommentsView(APIView):
    def get(self, request, user_id):
        # Filter comments by the associated user ID
        comments = Commentaire.objects.filter(idUser=user_id)
        serializer = CommentaireSerializer(comments, many=True)
        return Response(serializer.data)



class DailyMaxValuesView(APIView):
    def get(self, request):
        today = now().date()  # Current date (naive)
        today_start = make_aware(datetime.combine(today, datetime.min.time()))  # Start of today (aware)
        today_end = make_aware(datetime.combine(today, datetime.max.time()))  # End of today (aware)

        # Debug: Print today's date and start/end datetimes
        print(f"Today's date: {today}")
        print(f"Start of today (timezone-aware): {today_start}")
        print(f"End of today (timezone-aware): {today_end}")

        today_start = datetime.combine(datetime.today(), datetime.min.time())
        today_end = today_start + timedelta(days=1)

        # Query for max temperature and humidity within today's range
        max_values = Temperature.objects.filter(
            daterecord__range=(today_start, today_end)  # Filter by datetime range
        ).aggregate(
            max_temp=Max('temprecord'),
            max_humidity=Max('humidityrecord')
        )

        # Return response
        return Response(max_values, status=status.HTTP_200_OK)


class CurrentMaxValuesView(APIView):
    def get(self, request):
        # Query for the record with the maximum 'id'
        current_max = Temperature.objects.all().order_by('-id').first()  # Get the record with max 'id'

        # Check if a record was found
        if current_max:
            # Return the temperature and humidity with the corresponding max 'id'
            response_data = {
                'temperature': current_max.temprecord,
                'humidity': current_max.humidityrecord
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            # No data found
            return Response({"message": "No data available."}, status=status.HTTP_404_NOT_FOUND)


class UsersWithRole1(APIView):
    def get(self, request):
        # Retrieve users with idrole=1
        users = Utilisateur.objects.filter(idrole__id=1)

        # Serialize the users
        serializer = UtilisateurSerializer(users, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)