import streamlit as st
import pandas as pd
import plotly.express as px
from pipeline import run_event_planner
from datetime import date
import json

st.set_page_config(
    page_title="AI Smart Event Planner",
    page_icon="🎉",
    layout="wide",
    initial_sidebar_state="expanded"
)
with st.sidebar:

    st.title("🤖 AI Smart Event Planner")

    st.markdown("---")

    st.subheader("AI Agents")

    st.success("🧠 Planner")
    st.success("📍 Venue")
    st.success("🍽 Food")
    st.success("💰 Budget")
    st.success("🌦 Weather")
    st.success("📅 Schedule")
    st.success("⭐ Critic")

    st.markdown("---")

    st.metric("Supported Events", "18+")
    st.metric("AI Agents", "7")
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
""",unsafe_allow_html=True)

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

        [

            "Birthday",

            "Wedding",

            "Anniversary",

            "Baby Shower",

            "Naming Ceremony",

            "Graduation",

            "Conference",

            "Seminar",

            "Workshop",

            "Corporate Meeting",

            "Product Launch",

            "College Fest",

            "School Annual Day",

            "Sports Event",

            "Music Concert",

            "Festival",

            "Family Reunion"

        ]

    )

with col2:
    cities = [
    "Bangalore",
    "Mysore",
    "Hubballi",
    "Mangaluru",
    "Hyderabad",
    "Chennai",
    "Mumbai",
    "Pune",
    "Delhi",
    "Kolkata",
    "Ahmedabad",
    "Jaipur",
    "Other"
    ]

    selected_city = st.selectbox("City", cities)

    if selected_city == "Other":
        city = st.text_input("Enter City")
    else:
        city = selected_city
    

    col3, col4 = st.columns(2)

with col3:

    budget = st.number_input(

        "Budget (₹)",

        min_value=1000,

        value=500000,

        step=1000

    )

with col4:

    guests = st.number_input(

        "Guests",

        min_value=1,

        value=100

    )

date = st.date_input(

    "Event Date"

)

icons = {

    "Birthday":"🎂",

    "Wedding":"💍",

    "Anniversary":"🎉",

    "Baby Shower":"👶",

    "Naming Ceremony":"👶",

    "Graduation":"🎓",

    "Conference":"🏢",

    "Seminar":"📚",

    "Workshop":"🖥",

    "Corporate Meeting":"💼",

    "Product Launch":"🚀",

    "College Fest":"🎊",

    "School Annual Day":"🏫",

    "Sports Event":"🏆",

    "Music Concert":"🎵",

    "Festival":"🎄",

    "Family Reunion":"👨‍👩‍👧"

}

st.markdown(f"# {icons[event]} {event}")

generate = st.button("🚀 Generate Smart Event Plan")
st.snow()

if generate:

    user_request = f"""
    Plan a {event}

    City: {city}

    Budget: {budget}

    Guests: {guests}

    Date: {date}
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

    st.success("Your AI Event Plan is Ready!")

    # -----------------------------
    # TABS
    # -----------------------------

    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
        "📍 Venues",
        "🍽 Food",
        "🌦 Weather",
        "💰 Budget",
        "📅 Schedule",
        "⭐ AI Review",
        "📄 Planner"
    ])

    # =============================
    # VENUES
    # =============================

    with tab1:

        st.subheader("📍 Recommended Venues")

        if result["Venues"]:

            for venue in result["Venues"]:

                with st.container():

                    st.markdown(f"""
                    <div class="card">
                        <h3>{venue['title']}</h3>
                        <p>{venue['content']}</p>
                    </div>
                    """, unsafe_allow_html=True)

                    st.link_button(
                        "🌐 Visit Website",
                        venue["url"]
                    )

                    st.divider()

        else:
            st.warning("No venues found.")
            with st.container():

                st.markdown(f"""
                <div class="card">
                    <h3>{venue['title']}</h3>
                    <p>{venue['content']}</p>
                </div>
                """, unsafe_allow_html=True)

                st.link_button(
                    "🌐 Visit Website",
                    venue["url"]
                )

                st.divider()
    
    with tab2:

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

                    st.link_button(
                        "🌐 Visit Website",
                        caterer["url"],
                        key=caterer["url"]
                    )

                    st.divider()
    
    #============
    #WEATHER
    #============
    with tab3:

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
                st.metric(
                    "🌡 Temperature",
                    f"{weather.get('temperature','N/A')} °C"
                )

            with c2:
                st.metric(
                    "💧 Humidity",
                    f"{weather.get('humidity','N/A')}%"
                )

            with c3:
                st.metric(
                    "☁ Condition",
                    weather.get("condition","Unknown").title()
                )

                

           
    # =============================
    # BUDGET
    # =============================

    with tab4:

        st.subheader("💰 Budget Breakdown")

        budget_data = result["Budget"]

        if "error" in budget_data:
            st.error(budget_data["error"])
        else:
            budget_df = pd.DataFrame(
                budget_data.items(),
                columns=["Category", "Amount"]
            )

            st.dataframe(budget_df, use_container_width=True)

            chart_df = budget_df[
                ~budget_df["Category"].isin(
                    ["Guests", "Total Budget", "Cost Per Guest"]
                )
            ]

            fig = px.pie(
                chart_df,
                names="Category",
                values="Amount",
                hole=0.45,
                title="Budget Distribution"
            )

            st.plotly_chart(fig, use_container_width=True)
                

    # =============================
    # SCHEDULE
    # =============================

    with tab5:

        st.subheader("📅 Event Timeline")

        for line in result["Schedule"].split("\n"):

            st.info(line)

    # =============================
    # REVIEW
    # =============================

    with tab6:

        st.subheader("⭐ AI Review")

        st.write(result.get("Review", "No review available."))

    # =============================
    # PLANNER
    # =============================

    with tab7:

        st.subheader("📄 Planner Output")

        st.json(result.get("Planner", {}))

    # =============================
    # METRICS
    # =============================

    st.divider()

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("👥 Guests", guests)

    with c2:
        st.metric("💰 Budget", f"₹{budget:,}")

    with c3:
        st.metric("📍 Venues Found", len(result["Venues"]))

    with c4:
        st.metric("🎉 Event", event)
    
    c7, c8, c9 = st.columns(3)

    with c7:
        st.metric(
            "📅 Date",
            str(date)
        )

    with c8:
        st.metric(
            "🏙 City",
            city
        )

    with c9:

        weather = result.get("Weather", {})

        if "condition" in weather:
            st.metric(
                "☁ Condition",
                weather["condition"].title()
            )
        else:
            st.metric(
                "☁ Condition",
                "N/A"
            )

    # =============================
    # DOWNLOAD
    # =============================

    st.download_button(
        "📥 Download Event Plan (JSON)",
        data=json.dumps(result, indent=4),
        file_name="event_plan.json",
        mime="application/json"
    )

    st.success("🎉 Event Planned Successfully!")

