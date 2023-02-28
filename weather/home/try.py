# def index(request):
#   if request.method == 'POST':
#     try:
#       city = request.POST['city'].replace(' ','+')
#       source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+ city + '&units=metric&appid=91b7d97f511d789a9ca98ab956593984').read()
#       list_of_data = json.loads(source)
#       response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=91b7d97f511d789a9ca98ab956593984')
#       resp = response.raise_for_status()
#       print(f'the status code raised is {resp}')
#       data = {
#         'city':str(list_of_data['name']),
#         'weather':str(list_of_data['weather'][0]['main']),
#         'icon':str(list_of_data['weather'][0]['icon']),
#         'cel_temp':str(list_of_data['main']['temp']),
#         'humidity':str(list_of_data['main']['humidity']), 
#         'wind':str(list_of_data['wind']['speed']),
#       }
#     except requests.exceptions.HTTPError as e:
#       if e.response.status_code == 404:
#         return {"error":"City not found."}
#       raise
      
#   else:
#     data = {}
  
#   return render(request,'home/base.html',data)