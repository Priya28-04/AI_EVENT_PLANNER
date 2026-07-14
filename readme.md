# 🎉 AI Smart Event Planner

An AI-powered Multi-Agent Event Planning System built using **Streamlit**, **Groq LLM**, **Tavily Search API**, and **OpenWeather API**.

The application helps users plan different types of events by automatically generating venue recommendations, catering suggestions, weather forecasts, budget distribution, schedules, and an AI-generated review.

---

# Features

- 🎂 Supports Multiple Event Types
  - Birthday
  - Wedding
  - Anniversary
  - Baby Shower
  - Naming Ceremony
  - Graduation
  - Conference
  - Seminar
  - Workshop
  - Corporate Meeting
  - Product Launch
  - College Fest
  - School Annual Day
  - Sports Event
  - Music Concert
  - Festival
  - Family Reunion

- 📍 AI Venue Recommendations
- 🍽 Catering Recommendations
- 🌦 Live Weather Information
- 💰 Smart Budget Distribution
- 📅 AI Event Schedule Generator
- ⭐ AI Quality Review
- 📄 Planner Summary
- 📊 Interactive Budget Pie Chart
- 📥 Download Event Plan as JSON

---

# Technologies Used

- Python
- Streamlit
- LangChain
- Groq (Llama 3.3 70B)
- Tavily Search API
- OpenWeather API
- Plotly
- Pandas

---

# Project Structure

```
ai_event_planner/

│── app.py
│── pipeline.py
│── agents.py
│── prompts.py
│── config.py
│── tools.py
│── requirements.txt
│── .env

│
├── utils/
│   └── budget.py

├── assets/
│   ├── birthday.png
│   ├── wedding.png
│   ├── conference.png
│   ├── festival.png
│   └── ...

```

---

# AI Agents

## 🧠 Planner Agent

- Understands user request
- Extracts event details
- Selects required agents

---

## 📍 Venue Agent

Searches the internet for:

- Event venues
- Party halls
- Convention centers
- Resorts
- Auditoriums

using Tavily Search.

---

## 🍽 Food Agent

Finds:

- Caterers
- Catering Services
- Event Food Providers

based on event type and city.

---

## 🌦 Weather Agent

Uses OpenWeather API to provide:

- Temperature
- Humidity
- Weather Condition

for the selected city.

---

## 💰 Budget Agent

Automatically distributes the budget according to event type.

Example:

Wedding

- Venue
- Food
- Decoration
- Photography
- Entertainment
- Miscellaneous

Birthday

- Venue
- Cake
- Decoration
- Entertainment
- Food

Conference

- Venue
- AV Equipment
- Marketing
- Catering

---

## 📅 Schedule Agent

Generates a professional event timeline using AI.

Examples:

Wedding

- Ceremony
- Reception
- Dinner

Birthday

- Welcome
- Games
- Cake Cutting
- Dinner

Conference

- Registration
- Keynote
- Networking
- Closing Ceremony

---

## ⭐ Critic Agent

Reviews the complete event plan.

Checks

- Budget
- Schedule
- Venues
- Missing Tasks
- Suggestions

---

# Installation

Clone the repository

```bash
git clone https://github.com/yourusername/ai-smart-event-planner.git
```

Move into the project

```bash
cd ai-smart-event-planner
```

Create Virtual Environment

```bash
python -m venv .venv
```

Activate Environment

Windows

```bash
.venv\Scripts\activate
```

Linux / Mac

```bash
source .venv/bin/activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a **.env** file.

```env
GROQ_API_KEY=your_groq_api_key

TAVILY_API_KEY=your_tavily_api_key

OPENWEATHER_API_KEY=your_openweather_api_key
```

---

# Run the Application

```bash
streamlit run app.py
```

or

```bash
uv run streamlit run app.py
```

---

# Workflow

```
User
   │
   ▼
Planner Agent
   │
   ├───────────────┐
   ▼               ▼
Venue Agent     Food Agent
   │               │
   ▼               ▼
Weather Agent   Budget Agent
        │
        ▼
Schedule Agent
        │
        ▼
Critic Agent
        │
        ▼
Final Event Plan
```

---

# Supported Cities

Users can choose any city including:

- Bangalore
- Mysore
- Hubballi
- Hyderabad
- Chennai
- Mumbai
- Delhi
- Pune
- Kolkata
- Jaipur
- Ahmedabad

or enter a custom city.

---

# Future Enhancements

- 🗺 Interactive Maps
- 📧 Email Invitations
- 🎟 Ticket Generation
- 📄 PDF Report Export
- 💳 Cost Optimization
- 🎤 Vendor Comparison
- 📍 Nearby Hotels
- 🚖 Travel Planning
- 🤖 Conversational Chatbot
- 📱 Mobile Responsive UI
- 🔔 Event Reminders
- 📅 Google Calendar Integration

---

# Screenshots

Add screenshots of:

- Home Page
- Event Details
- Venue Recommendations
- Weather Dashboard
- Budget Chart
- Schedule
- AI Review

---

# Author

**Your Name**

AI & Full Stack Developer

---

# License

This project is licensed under the MIT License.