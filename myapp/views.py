from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime


# A list to store temperature and humidity records in memory
data_records = []
@csrf_exempt
def receive_temperature_humidity(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            temperature = data.get("temp")
            humidity = data.get("hum")

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
