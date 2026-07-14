from tavily import TavilyClient
from config import TAVILY_API_KEY
import requests
from config import OPENWEATHER_API_KEY

client = TavilyClient(api_key=TAVILY_API_KEY)

def search_web(query, max_results=5):
    response = client.search(query=query, max_results=max_results)

    results = []

    for item in response["results"]:
        results.append({
            "title": item["title"],
            "url": item["url"],
            "content": item["content"]
        })

    return results

def search_venues(city, event_type):

    queries = {
        "Wedding": f"Best wedding halls in {city}",
        "Birthday": f"Best birthday party halls in {city}",
        "Anniversary": f"Best anniversary party venues in {city}",
        "Baby Shower": f"Best baby shower venues in {city}",
        "Naming Ceremony": f"Best naming ceremony halls in {city}",
        "Graduation": f"Best graduation party venues in {city}",
        "Conference": f"Best conference halls in {city}",
        "Seminar": f"Best seminar halls in {city}",
        "Workshop": f"Best workshop venues in {city}",
        "Corporate Meeting": f"Best meeting rooms in {city}",
        "Product Launch": f"Best product launch venues in {city}",
        "College Fest": f"Best college event venues in {city}",
        "School Annual Day": f"Best school auditoriums in {city}",
        "Sports Event": f"Best sports grounds in {city}",
        "Music Concert": f"Best concert venues in {city}",
        "Festival": f"Best festival venues in {city}",
        "Family Reunion": f"Best family gathering venues in {city}"
    }

    query = queries.get(
        event_type,
        f"Best event venues in {city}"
    )

    return search_web(query)

def get_weather(city):
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    )

    response = requests.get(url)

    print("Status Code:", response.status_code)
    print("Response:", response.text)

    if response.status_code != 200:
        return {"error": response.text}

    data = response.json()

    return {
        "city": city,
        "temperature": data["main"]["temp"],
        "condition": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"]
    }

def search_food(city, event_type):
    queries = {
        "Wedding": f"Best wedding caterers in {city}",
        "Birthday": f"Best birthday catering services in {city}",
        "Anniversary": f"Best anniversary caterers in {city}",
        "Baby Shower": f"Best baby shower catering in {city}",
        "Naming Ceremony": f"Best naming ceremony caterers in {city}",
        "Graduation": f"Best graduation party catering in {city}",
        "Conference": f"Best corporate caterers in {city}",
        "Seminar": f"Best seminar catering in {city}",
        "Workshop": f"Best workshop catering in {city}",
        "Corporate Meeting": f"Best business catering in {city}",
        "Product Launch": f"Best event catering in {city}",
        "College Fest": f"Best college event catering in {city}",
        "School Annual Day": f"Best school event catering in {city}",
        "Sports Event": f"Best sports event catering in {city}",
        "Music Concert": f"Best concert catering in {city}",
        "Festival": f"Best festival catering in {city}",
        "Family Reunion": f"Best family catering services in {city}"
    }

    query = queries.get(
        event_type,
        f"Best caterers in {city}"
    )

    return search_web(query)