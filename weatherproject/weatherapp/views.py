from django.shortcuts import render 
from django.contrib import messages
import requests
import datetime
# Create your views here.
def climate(request):

    if request.method == "POST":
        city = request.POST.get('city')
    else:
        city = "tamil nadu"

    # continue your API code...
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=dfa0cb9f3746b5b6adf91f4e767386a5'
    PARAMS = {"units": "metric"}

   
    
    try:
        data = requests.get(url,PARAMS).json()
        description=data['weather'][0]['description']
        icon=data['weather'][0]['icon']
        temp=data['main']['temp']
        day=datetime.date.today()
        return render(request, 'index.html', {
       'description': description,
       'icon': icon,
       'temp': temp,
       'day': day,
       'city': city,
       'exception_occurred':False,
       
})

    except:
        Exception_occurred=True
        messages.error(request,'entered data is not available to API')
        day = datetime.date.today()
        return render(request, 'index.html', {
       'description': 'clear sky',
       'icon': 'old',
       'temp': 25,
       'day': day,
       'city': 'tamil nadu',
       'exception_occurred':True
} )