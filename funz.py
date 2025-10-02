import requests

url = "https://api.openweathermap.org/data/3.0/onecall?lat=47.40&lon=122.71&appid=6a096d384d3a5b5f6d15b7410f31455d"


response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temperature = data['main']['temp']
    print(f"Current temperature in")
else:
    print(f"Error retrieving data: Status code {response.headers}")