import requests as req

import json
from dotenv import load_dotenv
load_dotenv()



city = input("Enter the city")
print(city)

url_weather =f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=7a5b41069424ae8f916e19df3a4d691f"
res_weather = req.get(url_weather)

weather_data = res_weather.json()
print(weather_data)

url ="https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent"
headers={
"x-goog-api-key":os.getenv("OPENWEATER_API_KEY"),
"Content-Type": "application/json"
}

# method = post
data ={
    "contents": [
      {
        "parts": [
          {
            "text": f"""
            act like a weather analyst and tell me what kind of food i need to eat and
            what kind of clothes i need to wear in the city based on weather condition 
            weather : {weather_data}
            """
            
          }
        ]
      }
    ]
  }

res = req.post(url,json=data,headers=headers)
y=res.json()
#print(y["content"]["parts"][0]["text"])
#print(res.json())
print(y)