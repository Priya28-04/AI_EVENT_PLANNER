# utils/budget.py
EVENT_MAPPING = {
    "Birthday Party": "Birthday",
    "Birthday": "Birthday",

    "Wedding Ceremony": "Wedding",
    "Wedding": "Wedding",

    "Anniversary Party": "Anniversary",
    "Anniversary": "Anniversary",

    "Baby Shower": "Baby Shower",

    "Naming Ceremony": "Naming Ceremony",

    "Graduation Party": "Graduation",
    "Graduation": "Graduation",

    "Corporate Meeting": "Corporate Meeting",

    "Conference": "Conference",

    "Seminar": "Seminar",

    "Workshop": "Workshop",

    "Product Launch": "Product Launch",

    "College Fest": "College Fest",

    "School Annual Day": "School Annual Day",

    "Sports Event": "Sports Event",

    "Music Concert": "Music Concert",

    "Festival Celebration": "Festival",
    "Festival": "Festival",

    "Family Reunion": "Family Reunion"
}
BUDGET_RULES = {

    "Wedding": {
        "Venue": 30,
        "Food": 40,
        "Decoration": 10,
        "Photography": 8,
        "Entertainment": 7,
        "Miscellaneous": 5
    },

    "Birthday": {
        "Venue": 25,
        "Food": 35,
        "Decoration": 15,
        "Cake": 10,
        "Entertainment": 10,
        "Miscellaneous": 5
    },

    "Anniversary": {
        "Venue": 30,
        "Food": 35,
        "Decoration": 15,
        "Photography": 10,
        "Entertainment": 5,
        "Miscellaneous": 5
    },

    "Baby Shower": {
        "Venue": 25,
        "Food": 35,
        "Decoration": 20,
        "Photography": 10,
        "Games": 5,
        "Miscellaneous": 5
    },

    "Naming Ceremony": {
        "Venue": 25,
        "Food": 40,
        "Decoration": 15,
        "Photography": 10,
        "Return Gifts": 5,
        "Miscellaneous": 5
    },

    "Graduation": {
        "Venue": 30,
        "Food": 35,
        "Decoration": 10,
        "Photography": 10,
        "Entertainment": 10,
        "Miscellaneous": 5
    },

    "Corporate Meeting": {
        "Venue": 40,
        "Food": 20,
        "AV Equipment": 20,
        "Marketing": 10,
        "Miscellaneous": 10
    },

    "Conference": {
        "Venue": 35,
        "Food": 25,
        "AV Equipment": 15,
        "Marketing": 15,
        "Miscellaneous": 10
    },

    "Seminar": {
        "Venue": 40,
        "Food": 20,
        "AV Equipment": 20,
        "Certificates": 10,
        "Miscellaneous": 10
    },

    "Workshop": {
        "Venue": 35,
        "Food": 20,
        "Training Materials": 20,
        "AV Equipment": 15,
        "Miscellaneous": 10
    },

    "Product Launch": {
        "Venue": 30,
        "Food": 20,
        "Marketing": 25,
        "Decoration": 10,
        "Photography": 10,
        "Miscellaneous": 5
    },

    "College Fest": {
        "Stage": 20,
        "Food": 20,
        "Decoration": 15,
        "Sound & Lighting": 20,
        "Prizes": 15,
        "Miscellaneous": 10
    },

    "School Annual Day": {
        "Stage": 25,
        "Decoration": 20,
        "Sound System": 20,
        "Certificates": 15,
        "Refreshments": 10,
        "Miscellaneous": 10
    },

    "Sports Event": {
        "Ground": 30,
        "Equipment": 25,
        "Prizes": 15,
        "Refreshments": 15,
        "Medical": 10,
        "Miscellaneous": 5
    },

    "Music Concert": {
        "Stage": 25,
        "Sound & Lighting": 25,
        "Artists": 25,
        "Security": 15,
        "Miscellaneous": 10
    },

    "Festival": {
        "Venue": 20,
        "Decoration": 25,
        "Food": 25,
        "Entertainment": 20,
        "Miscellaneous": 10
    },

    "Family Reunion": {
        "Venue": 30,
        "Food": 40,
        "Games": 10,
        "Photography": 10,
        "Miscellaneous": 10
    }
}

def calculate_budget(event_type, total_budget, guests):

    event_type = EVENT_MAPPING.get(event_type.strip(), event_type.strip())

    if event_type not in BUDGET_RULES:
        return {
            "error": f"Budget rules not available for '{event_type}'"
        }

    rules = BUDGET_RULES[event_type]
    budget = {}

    for category, percentage in rules.items():
        budget[category] = round((percentage / 100) * total_budget)

    budget["Total Budget"] = total_budget
    budget["Guests"] = guests
    budget["Cost Per Guest"] = round(total_budget / guests)

    return budget