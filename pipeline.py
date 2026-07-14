from agents import (
    planner_agent,
    venue_agent,
    weather_agent,
    food_agent,
    budget_agent,
    schedule_agent,
    critic_agent
)

import json


def run_event_planner(user_request):

    # Step 1: Planner Agent
    planner_output = planner_agent(user_request)

    print("=" * 60)
    print("Planner Output:")
    print(repr(planner_output))
    print("=" * 60)

    planner_output = planner_output.strip()

    if planner_output.startswith("```json"):
        planner_output = planner_output.replace("```json", "").replace("```", "").strip()

    planner_data = json.loads(planner_output)

    city = planner_data["city"]
    event = planner_data["event_type"]
    guests = int(planner_data["guests"])
    budget = int(planner_data["budget"])

    # Step 2: Venue Agent
    venues = venue_agent(city, event)

    # Step 3: Budget Agent
    budget_plan = budget_agent(
        event,
        budget,
        guests
    )

    # Step 4: Weather Agent
    weather = weather_agent(city)
    # Step 5: Food Agent
    food = food_agent(city, event)
    # Step 4: Schedule Agent
    schedule = schedule_agent(event, guests)

    # Step 5: Combine all results
    event_plan = {
        "Planner": planner_data,
        "Venues": venues,
        "Weather": weather,
        "Food": food,
        "Budget": budget_plan,
        "Schedule": schedule
    }

    # Step 6: Critic Agent
    review = critic_agent(event_plan)

    event_plan["Review"] = review

    return event_plan