from django.shortcuts import render

def home(request):
    import json, requests
    
    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=36109&distance=150&API_KEY=E537E122-F9FC-4355-9BFE-D5BC0BC080D1")
    
    try:
      api = json.loads(api_request.content)
    except Exception as e:
      api = "Error..."
      
    return render(request, 'home.html', {'api': api})
# Create your views here.

def about(request):
    return render(request, 'about.html', {})