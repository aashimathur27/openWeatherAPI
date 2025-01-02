import requests

city_name= 'New Delhi'
API_key='db451887086237eefe19aa8a57a082ea'
url= f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'

response= requests.get(url)
if response.status_code==200:
    data = response.json()
    print("weather is: ",data['weather'][0]['description'])
    print("current temperature is: ",data['main']['temp'])
    print("current temperature feels like is: ",data['main']['feels_like'])
    print("humidity is: ",data['main']['humidity'])    