from django.shortcuts import render

import requests
import urllib.request # its used for opening and reading urls # we ll have post request to the api endpoint 
import json
# Create your views here.

#----------------------METHOD 1-----------------------------------#
# def home(request):

#   city = request.GET.get('city','paris')
#   url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=91b7d97f511d789a9ca98ab956593984' 
#   data = requests.get(url).json()
#   payload = {
#       # 'city':data['name'],
#       'city':city,
#       'weather':data['weather'][0]['main'],
#       'icon':data['weather'][0]['icon'],
#       'kel_temp':data['main']['temp'],
#       'cel_temp':int(data['main']['temp'] -273),
#       'humidity':data['main']['humidity'], 
#       'wind':data['wind']['speed'],
#     }
#   context = {'data':payload}
#   print(context)
#   return render(request,'home/base.html',context)


#----------------------METHOD 2-----------------------------------#

def index(request):
  if request.method == 'POST':
    try:
      city = request.POST['city'].replace(' ','+')
      source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+ city + '&units=metric&appid=91b7d97f511d789a9ca98ab956593984').read()
      list_of_data = json.loads(source)
      response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=91b7d97f511d789a9ca98ab956593984')
      response.raise_for_status()
      data = {
        'city':str(list_of_data['name']),
        'weather':str(list_of_data['weather'][0]['main']),
        'icon':str(list_of_data['weather'][0]['icon']),
        'cel_temp':str(list_of_data['main']['temp']),
        'humidity':str(list_of_data['main']['humidity']), 
        'wind':str(list_of_data['wind']['speed']),
      }
      print(data)
    except requests.exceptions.HTTPError as e:
      if e.response.status_code == 404:
        return {"error":"City not found."}
      raise
      
  else:
    data = {}
  
  return render(request,'home/base.html',data)
