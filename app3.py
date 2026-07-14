import streamlit as st
import pandas as pd
import plotly.express as px
from pipeline import run_event_planner
import json

st.set_page_config(
    page_title="AI Smart Event Planner",
    page_icon="🎉",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# SESSION STATE (drives which "page" is shown)
# =====================================================

if "page" not in st.session_state:
    st.session_state.page = "home"          # home -> after generating -> agent pages
if "result" not in st.session_state:
    st.session_state.result = None
if "event" not in st.session_state:
    st.session_state.event = None
if "city" not in st.session_state:
    st.session_state.city = None
if "budget" not in st.session_state:
    st.session_state.budget = None
if "guests" not in st.session_state:
    st.session_state.guests = None
if "event_date" not in st.session_state:
    st.session_state.event_date = None

AGENT_PAGES = {
    "Planner":  "🧠",
    "Venue":    "📍",
    "Food":     "🍽",
    "Budget":   "💰",
    "Weather":  "🌦",
    "Schedule": "📅",
    "Critic":   "⭐",
}

def go_to(page_name):
    st.session_state.page = page_name
    st.rerun()

# =====================================================
# STYLING
# =====================================================

st.markdown("""
<style>

.stApp{
background:linear-gradient(135deg,#eef2ff,#f8fafc,#fdf2f8);
}

.main-title{
font-size:50px;
font-weight:700;
text-align:center;
color:#5b21b6;
}

.subtitle{
text-align:center;
font-size:18px;
color:#6b7280;
margin-bottom:30px;
}

.card{
background:white;
padding:25px;
border-radius:20px;
box-shadow:0px 10px 25px rgba(0,0,0,.08);
margin-bottom:20px;
}

div.stButton>button{
width:100%;
height:55px;
font-size:22px;
border-radius:15px;
background:#6C63FF;
color:white;
font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.title("🤖 AI Smart Event Planner")

    st.markdown("---")

    st.subheader("AI Agents")

    if st.session_state.result is not None:
        # Plan already generated -> agents are clickable, each opens its own page
        for name, icon in AGENT_PAGES.items():
            if st.button(f"{icon} {name}", use_container_width=True, key=f"nav_{name}"):
                go_to(name)
    else:
        # No plan yet -> just show them as "ready" like before
        for name, icon in AGENT_PAGES.items():
            st.success(f"{icon} {name}")

    st.markdown("---")

    st.metric("Supported Events", "18+")
    st.metric("AI Agents", "7")

    if st.session_state.result is not None:
        st.markdown("---")
        if st.button("🏠 Back to Home", use_container_width=True):
            go_to("home")

icons = {
    "Birthday": "🎂",
    "Wedding": "💍",
    "Anniversary": "🎉",
    "Baby Shower": "👶",
    "Naming Ceremony": "👶",
    "Graduation": "🎓",
    "Conference": "🏢",
    "Seminar": "📚",
    "Workshop": "🖥",
    "Corporate Meeting": "💼",
    "Product Launch": "🚀",
    "College Fest": "🎊",
    "School Annual Day": "🏫",
    "Sports Event": "🏆",
    "Music Concert": "🎵",
    "Festival": "🎄",
    "Family Reunion": "👨‍👩‍👧"
}


# =====================================================
# PAGE: HOME (event details form + Generate button)
# =====================================================

def render_home():

    st.markdown("""
    <div style="
    padding:25px;
    border-radius:20px;
    background:linear-gradient(90deg,#6C63FF,#8B5CF6,#EC4899);
    color:white;
    text-align:center;
    ">

    <h1>🎉 AI Smart Event Planner</h1>

    <p>Plan Birthdays • Weddings • Conferences • Festivals • Corporate Events</p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("## 🎯 Event Details")

    col1, col2 = st.columns(2)

    with col1:

        event = st.selectbox(
            "Event Type",
            list(icons.keys())
        )

    with col2:
        cities = [
            "Bangalore", "Mysore", "Hubballi", "Mangaluru", "Hyderabad",
            "Chennai", "Mumbai", "Pune", "Delhi", "Kolkata",
            "Ahmedabad", "Jaipur", "Other"
        ]

        selected_city = st.selectbox("City", cities)

        if selected_city == "Other":
            city = st.text_input("Enter City")
        else:
            city = selected_city

    col3, col4 = st.columns(2)

    with col3:
        budget = st.number_input("Budget (₹)", min_value=1000, value=500000, step=1000)

    with col4:
        guests = st.number_input("Guests", min_value=1, value=100)

    event_date = st.date_input("Event Date")

    st.markdown(f"# {icons[event]} {event}")

    generate = st.button("🚀 Generate Smart Event Plan")
    st.snow()

    if generate:

        user_request = f"""
        Plan a {event}

        City: {city}

        Budget: {budget}

        Guests: {guests}

        Date: {event_date}
        """

        with st.spinner("🤖 AI Agents are working..."):

            progress = st.progress(0)
            status = st.empty()

            status.info("🧠 Planner Agent is analysing your request...")
            progress.progress(15)

            status.info("📍 Venue Agent is searching venues...")
            progress.progress(30)

            status.info("🍽 Food Agent is searching catering services...")
            progress.progress(45)

            status.info("💰 Budget Agent (60%)")
            progress.progress(60)

            status.info("📅 Schedule Agent is creating the event schedule...")
            progress.progress(80)

            status.info("⭐ Critic Agent is reviewing the plan...")
            progress.progress(95)

            result = run_event_planner(user_request)

            progress.progress(100)
            status.success("✅ Event Plan Generated Successfully!")

        # Save everything to session_state so it survives the page switch
        st.session_state.result = result
        st.session_state.event = event
        st.session_state.city = city
        st.session_state.budget = budget
        st.session_state.guests = guests
        st.session_state.event_date = event_date

        # Celebration
        if event == "Birthday":
            st.balloons()
            st.toast("🎂 Happy Birthday!")
        elif event == "Wedding":
            st.toast("💍 Wishing you a wonderful celebration!")
        elif event == "Graduation":
            st.balloons()
            st.toast("🎓 Congratulations!")
        elif event == "Festival":
            st.toast("🎉 Happy Festival!")
        elif event == "Product Launch":
            st.toast("🚀 Product Launch Ready!")
        elif event == "Sports Event":
            st.toast("🏆 Let the Games Begin!")
        elif event == "Music Concert":
            st.toast("🎵 Concert Ready!")
        else:
            st.toast("🎉 Event Planned Successfully!")

        # Jump straight to the results / first agent page
        go_to("Planner")


# =====================================================
# SHARED HEADER + FOOTER FOR EVERY AGENT PAGE
# =====================================================

def render_agent_header(current):
    event = st.session_state.event
    st.markdown(f"""
    <div style="
    padding:20px;
    border-radius:16px;
    background:linear-gradient(90deg,#6C63FF,#8B5CF6,#EC4899);
    color:white;
    text-align:center;
    ">
    <h2>{AGENT_PAGES[current]} {current} Agent — {icons.get(event,'🎉')} {event}</h2>
    </div>
    """, unsafe_allow_html=True)

    # quick agent-to-agent nav strip at the top of every page
    cols = st.columns(len(AGENT_PAGES))
    for col, (name, icon) in zip(cols, AGENT_PAGES.items()):
        with col:
            if name == current:
                st.button(f"{icon} {name}", disabled=True, use_container_width=True, key=f"top_{name}")
            else:
                if st.button(f"{icon} {name}", use_container_width=True, key=f"top_{name}"):
                    go_to(name)

    st.divider()


def render_footer():
    result = st.session_state.result
    event = st.session_state.event
    city = st.session_state.city
    budget = st.session_state.budget
    guests = st.session_state.guests
    event_date = st.session_state.event_date

    st.divider()

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("👥 Guests", guests)
    with c2:
        st.metric("💰 Budget", f"₹{budget:,}")
    with c3:
        st.metric("📍 Venues Found", len(result.get("Venues", [])))
    with c4:
        st.metric("🎉 Event", event)

    c7, c8, c9 = st.columns(3)
    with c7:
        st.metric("📅 Date", str(event_date))
    with c8:
        st.metric("🏙 City", city)
    with c9:
        weather = result.get("Weather", {})
        if "condition" in weather:
            st.metric("☁ Condition", weather["condition"].title())
        else:
            st.metric("☁ Condition", "N/A")

    st.download_button(
        "📥 Download Event Plan (JSON)",
        data=json.dumps(result, indent=4),
        file_name="event_plan.json",
        mime="application/json"
    )

    st.success("🎉 Event Planned Successfully!")


# =====================================================
# PAGE: VENUE AGENT
# =====================================================

def render_venue_page():
    result = st.session_state.result
    render_agent_header("Venue")

    st.subheader("📍 Recommended Venues")

    venues = result.get("Venues", [])

    if venues:
        for venue in venues:
            with st.container():
                st.markdown(f"""
                <div class="card">
                    <h3>{venue['title']}</h3>
                    <p>{venue['content']}</p>
                </div>
                """, unsafe_allow_html=True)

                st.link_button("🌐 Visit Website", venue["url"], key=f"venue_{venue['url']}")
                st.divider()
    else:
        st.warning("No venues found.")

    render_footer()


# =====================================================
# PAGE: FOOD AGENT
# =====================================================

def render_food_page():
    result = st.session_state.result
    render_agent_header("Food")

    st.subheader("🍽 Recommended Catering Services")

    food = result.get("Food", [])

    if not food:
        st.warning("No catering services found.")
    else:
        for caterer in food:
            with st.container():
                st.markdown(f"""
                <div class="card">
                <h3>🍽 {caterer['title']}</h3>
                <p>{caterer['content']}</p>
                </div>
                """, unsafe_allow_html=True)

                st.link_button("🌐 Visit Website", caterer["url"], key=f"food_{caterer['url']}")
                st.divider()

    render_footer()


# =====================================================
# PAGE: WEATHER AGENT
# =====================================================

def render_weather_page():
    result = st.session_state.result
    render_agent_header("Weather")

    st.subheader("🌦 Weather Forecast")

    weather = result.get("Weather", {})

    if not weather:
        st.warning("Weather information not available.")
    elif "error" in weather:
        st.error(weather["error"])
    else:
        condition = weather.get("condition", "").lower()

        if "rain" in condition:
            icon = "🌧"
        elif "cloud" in condition:
            icon = "☁"
        elif "clear" in condition:
            icon = "☀"
        elif "thunder" in condition:
            icon = "⛈"
        elif "snow" in condition:
            icon = "❄"
        elif "mist" in condition or "fog" in condition:
            icon = "🌫"
        else:
            icon = "🌤"

        st.markdown(f"# {icon} {weather.get('city','Unknown')}")

        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric("🌡 Temperature", f"{weather.get('temperature','N/A')} °C")
        with c2:
            st.metric("💧 Humidity", f"{weather.get('humidity','N/A')}%")
        with c3:
            st.metric("☁ Condition", weather.get("condition","Unknown").title())

    render_footer()


# =====================================================
# PAGE: BUDGET AGENT
# =====================================================

def render_budget_page():
    result = st.session_state.result
    render_agent_header("Budget")

    st.subheader("💰 Budget Breakdown")

    budget_data = result.get("Budget", {})

    if "error" in budget_data:
        st.error(budget_data["error"])
    else:
        budget_df = pd.DataFrame(budget_data.items(), columns=["Category", "Amount"])

        st.dataframe(budget_df, use_container_width=True)

        chart_df = budget_df[
            ~budget_df["Category"].isin(["Guests", "Total Budget", "Cost Per Guest"])
        ]

        fig = px.pie(
            chart_df,
            names="Category",
            values="Amount",
            hole=0.45,
            title="Budget Distribution"
        )

        st.plotly_chart(fig, use_container_width=True)

    render_footer()


# =====================================================
# PAGE: SCHEDULE AGENT
# =====================================================

def render_schedule_page():
    result = st.session_state.result
    render_agent_header("Schedule")

    st.subheader("📅 Event Timeline")

    for line in result.get("Schedule", "").split("\n"):
        st.info(line)

    render_footer()


# =====================================================
# PAGE: CRITIC AGENT (Review)
# =====================================================

def render_critic_page():
    result = st.session_state.result
    render_agent_header("Critic")

    st.subheader("⭐ AI Review")

    st.write(result.get("Review", "No review available."))

    render_footer()


# =====================================================
# PAGE: PLANNER AGENT (first page shown after Generate)
# =====================================================

def render_planner_page():
    result = st.session_state.result
    render_agent_header("Planner")

    st.subheader("📄 Planner Output")

    st.json(result.get("Planner", {}))

    render_footer()


# =====================================================
# ROUTER
# =====================================================

if st.session_state.page == "home":
    render_home()
elif st.session_state.page == "Planner":
    render_planner_page()
elif st.session_state.page == "Venue":
    render_venue_page()
elif st.session_state.page == "Food":
    render_food_page()
elif st.session_state.page == "Weather":
    render_weather_page()
elif st.session_state.page == "Budget":
    render_budget_page()
elif st.session_state.page == "Schedule":
    render_schedule_page()
elif st.session_state.page == "Critic":
    render_critic_page()
else:
    st.session_state.page = "home"
    st.rerun()