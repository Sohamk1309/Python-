import requests
import json

# api_key = "c0482f4dc6msh5f0bcff64959854p185fbbjsnb049be4988cd"
# city = "Sangli"
# url = f"https://weatherbit-v1-mashape.p.rapidapi.com/forecast/3hourly?lat=35.5&lon=-78.5&units=imperial&lang=en" 

url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/3hourly"

querystring = {"lat":"35.5","lon":"-78.5","units":"imperial","lang":"en"}

headers = {
	"x-rapidapi-key": "c0482f4dc6msh5f0bcff64959854p185fbbjsnb049be4988cd",
	"x-rapidapi-host": "weatherbit-v1-mashape.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())

if response.status_code == 200:
    data = response.json()
    print(json.dumps(data, indent=4))
    with open("whether_data.json", "w") as file:
        json.dump(data, file)
else:
    print(response.status_code)

