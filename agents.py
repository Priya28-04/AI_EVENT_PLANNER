from langchain_groq import ChatGroq
from config import GROQ_API_KEY
from prompts import PLANNER_PROMPT
from tools import get_weather
from tools import search_venues
from utils.budget import calculate_budget
from tools import get_weather
from tools import search_food
from prompts import SCHEDULE_PROMPT
from prompts import CRITIC_PROMPT

llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model="openai/gpt-oss-20b"
)

def planner_agent(user_request):

    prompt = f"""
{PLANNER_PROMPT}

{user_request}
"""

    response = llm.invoke(prompt)

    return response.content

def venue_agent(city, event_type):
    venues = search_venues(city, event_type)

    return venues

def budget_agent(event_type, total_budget, guests):
    return calculate_budget(event_type, total_budget, guests)

def weather_agent(city):
    return get_weather(city)


def food_agent(city, event_type):
    return search_food(city, event_type)


def schedule_agent(event_type, guests):
    prompt = f"""
{SCHEDULE_PROMPT}

Event: {event_type}

Guests: {guests}
"""

    response = llm.invoke(prompt)

    print("agents.py loaded")
    return response.content


def critic_agent(event_plan):

    prompt = f"""
{CRITIC_PROMPT}

Event Plan:

{event_plan}
"""

    response = llm.invoke(prompt)

    return response.content