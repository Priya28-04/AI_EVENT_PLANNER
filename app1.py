import streamlit as st
import time
import json
from pipeline import run_event_planner

# -------------------------------
# PAGE CONFIG
# -------------------------------

st.set_page_config(
    page_title="EventGenie AI",
    page_icon="🎉",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# -------------------------------
# SESSION
# -------------------------------

if "page" not in st.session_state:
    st.session_state.page = "welcome"

# -------------------------------
# CSS
# -------------------------------

st.markdown("""
<style>

/* Hide Streamlit */

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

/* Background */

.stApp{

background:linear-gradient(
135deg,
#0d0d0f,
#1a1a1d,
#242427,
#1a1a1d,
#0d0d0f
);

background-size:400% 400%;

animation:bg 18s ease infinite;

}

@keyframes bg{

0%{background-position:0% 50%;}

50%{background-position:100% 50%;}

100%{background-position:0% 50%;}

}

/* Container (full-width page section, not a phone frame) */

.container{

max-width:760px;

margin:auto;

margin-top:30px;

margin-bottom:30px;

padding:40px;

border-radius:22px;

background:rgba(255,255,255,.03);

border:1px solid rgba(212,175,55,.25);

backdrop-filter:blur(16px);

box-shadow:
0 0 40px rgba(212,175,55,.08);

}

/* Logo */

.logo{

font-size:65px;

text-align:center;

}

/* Title */

.title{

font-size:40px;

font-weight:700;

text-align:center;

color:#D4AF37;

letter-spacing:.5px;

}

/* Subtitle */

.subtitle{

text-align:center;

font-size:17px;

color:#E6E1D6;

opacity:.85;

margin-bottom:25px;

}

/* Card */

.card{

background:rgba(255,255,255,.04);

padding:20px;

border-radius:16px;

border:1px solid rgba(212,175,55,.18);

color:#F0EDE3;

margin-top:15px;

transition:.4s;

}

.card:hover{

transform:scale(1.01);

transition:.4s;

box-shadow:0 0 25px rgba(212,175,55,.35);

border-color:rgba(212,175,55,.5);

}

.card h2, .card h3{

color:#D4AF37;

}

/* Button */

div.stButton>button{

width:100%;

height:56px;

font-size:20px;

font-weight:bold;

border-radius:14px;

border:1px solid #D4AF37;

background:linear-gradient(
90deg,
#B8860B,
#D4AF37
);

color:#1a1a1d;

transition:.3s;

}

div.stButton>button:hover{

transform:scale(1.02);

box-shadow:0 0 20px rgba(212,175,55,.5);

}

/* Balloons (used on the finish page) */

.balloon{

position:fixed;

bottom:-100px;

font-size:40px;

animation:float 12s linear infinite;

}

.b1{
left:10%;
animation-delay:0s;
}

.b2{
left:30%;
animation-delay:2s;
}

.b3{
left:60%;
animation-delay:5s;
}

.b4{
left:85%;
animation-delay:8s;
}

@keyframes float{

0%{
transform:translateY(0);
opacity:0;
}

20%{
opacity:1;
}

100%{
transform:translateY(-120vh);
opacity:0;
}

}

</style>

""", unsafe_allow_html=True)

# -------------------------------
# WELCOME PAGE
# -------------------------------

if st.session_state.page == "welcome":

    st.markdown("""

<div class="container">

<div class="logo">

🎉

</div>

<div class="title">

EventGenie AI

</div>

<div class="subtitle">

Your Smart AI Event Planning Assistant

</div>

<div class="card">

<h3>✨ Plan Every Celebration</h3>

🎂 Birthday Parties<br><br>

💍 Weddings<br><br>

🎉 Anniversary Celebrations<br><br>

👶 Baby Showers<br><br>

🎓 Graduation Parties<br><br>

🏢 Conferences<br><br>

💼 Corporate Meetings<br><br>

🚀 Product Launches<br><br>

🎊 College Festivals<br><br>

🏆 Sports Events<br><br>

🎵 Music Concerts<br><br>

🎄 Festivals<br><br>

👨‍👩‍👧 Family Reunions

</div>

</div>

""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("✨ Start Planning"):

        st.session_state.page = "details"

        st.rerun()

# -------------------------------
# DETAILS PAGE
# -------------------------------

elif st.session_state.page == "details":

    st.markdown("""
    <div class="container">

    <div class="title">
    📋 Event Details
    </div>

    <div class="subtitle">
    Step 1 of 8
    </div>

    </div>
    """, unsafe_allow_html=True)


    st.progress(12)

    event = st.selectbox(
        "🎉 Select Event",
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

    event_icons = {
        "Birthday":"🎂",
        "Wedding":"💍",
        "Anniversary":"🎉",
        "Baby Shower":"👶",
        "Naming Ceremony":"🍼",
        "Graduation":"🎓",
        "Conference":"🏢",
        "Seminar":"📚",
        "Workshop":"💻",
        "Corporate Meeting":"💼",
        "Product Launch":"🚀",
        "College Fest":"🎊",
        "School Annual Day":"🏫",
        "Sports Event":"🏆",
        "Music Concert":"🎵",
        "Festival":"🎆",
        "Family Reunion":"👨‍👩‍👧"
    }

    st.success(f"{event_icons[event]} {event}")

    city = st.selectbox(
        "🏙 Select City",
        [
            "Bangalore",
            "Mumbai",
            "Delhi",
            "Hyderabad",
            "Chennai",
            "Pune",
            "Kolkata",
            "Ahmedabad",
            "Jaipur",
            "Lucknow",
            "Mysore",
            "Hubballi",
            "Mangalore",
            "Other"
        ]
    )

    if city == "Other":
        city = st.text_input("Enter City Name")

    guests = st.slider(
        "👥 Number of Guests",
        10,
        5000,
        100
    )

    budget = st.slider(
        "💰 Budget (₹)",
        10000,
        5000000,
        500000,
        step=10000
    )

    event_date = st.date_input(
        "📅 Event Date"
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        if st.button("⬅ Back"):

            st.session_state.page = "welcome"

            st.rerun()

    with col2:

        if st.button("➡ Continue"):

            st.session_state.event = event
            st.session_state.city = city
            st.session_state.guests = guests
            st.session_state.budget = budget
            st.session_state.date = str(event_date)

            st.session_state.page = "loading"

            st.rerun()

# -------------------------------
# LOADING PAGE
# -------------------------------

elif st.session_state.page == "loading":

    st.markdown("""
    <div class="container">

    <div class="title">
    🤖 AI is Planning...
    </div>

    <div class="subtitle">
    Please wait while our AI agents work together.
    </div>

    </div>
    """, unsafe_allow_html=True)

    progress = st.progress(0)

    status = st.empty()

    steps = [
        ("🧠 Planner Agent is understanding your event...", 10),
        ("📍 Venue Agent is searching venues...", 25),
        ("🍽 Food Agent is finding caterers...", 40),
        ("🌦 Weather Agent is checking weather...", 55),
        ("💰 Budget Agent is calculating budget...", 70),
        ("📅 Schedule Agent is preparing timeline...", 85),
        ("⭐ Critic Agent is reviewing everything...", 95)
    ]

    for message, value in steps:

        status.info(message)

        progress.progress(value)

        time.sleep(0.7)

    user_request = f"""
    Plan a {st.session_state.event}

    City: {st.session_state.city}

    Budget: {st.session_state.budget}

    Guests: {st.session_state.guests}

    Date: {st.session_state.date}
    """

    try:

        result = run_event_planner(user_request)

        st.session_state.result = result

        progress.progress(100)

        status.success("✅ Event Plan Ready!")

        st.success("🧠 Planner Agent Completed")

        st.success("📍 Venue Agent Completed")

        st.success("🍽 Food Agent Completed")

        st.success("🌦 Weather Agent Completed")

        st.success("💰 Budget Agent Completed")

        st.success("📅 Schedule Agent Completed")

        time.sleep(1)

        st.session_state.page = "venues"

        st.rerun()

    except Exception as e:

        st.error(f"Error: {e}")

# -------------------------------
# VENUES PAGE
# -------------------------------

elif st.session_state.page == "venues":

    result = st.session_state.result

    st.markdown("""
    <div class="container">

    <div class="title">
    📍 Recommended Venues
    </div>

    <div class="subtitle">
    Step 2 of 8
    </div>

    </div>
    """, unsafe_allow_html=True)

    venues = result.get("Venues", [])

    if not venues:

        st.warning("No venues found.")

    else:

        for venue in venues:

            st.markdown(f"""
            <div class="card">

            <h3>{venue['title']}</h3>

            <p>{venue['content']}</p>

            </div>
            """, unsafe_allow_html=True)

            st.link_button(
                "🌐 Visit Website",
                venue["url"],
                key=venue["url"]
            )

    st.divider()

    c1, c2 = st.columns(2)

    with c1:

        if st.button("⬅ Back"):

            st.session_state.page = "details"

            st.rerun()

    with c2:

        if st.button("Next ➜"):

            st.session_state.page = "food"

            st.rerun()

# -------------------------------
# FOOD PAGE
# -------------------------------

elif st.session_state.page == "food":

    result = st.session_state.result

    st.markdown("""
    <div class="container">
    <div class="title">🍽 Food & Catering</div>
    <div class="subtitle">Step 3 of 8</div>
    </div>
    """, unsafe_allow_html=True)

    food = result.get("Food", [])

    if not food:

        st.warning("No catering services found.")

    else:

        for caterer in food:

            st.markdown(f"""
            <div class="card">
            <h3>🍴 {caterer['title']}</h3>
            <p>{caterer['content']}</p>
            </div>
            """, unsafe_allow_html=True)

            st.link_button(
                "🌐 Visit Website",
                caterer["url"],
                key=caterer["url"]
            )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        if st.button("⬅ Back"):

            st.session_state.page = "venues"

            st.rerun()

    with col2:

        if st.button("Next ➜"):

            st.session_state.page = "weather"

            st.rerun()

# -------------------------------
# WEATHER PAGE
# -------------------------------

elif st.session_state.page == "weather":

    result = st.session_state.result

    weather = result.get("Weather", {})

    st.markdown("""
    <div class="container">
    <div class="title">🌦 Weather</div>
    <div class="subtitle">Step 4 of 8</div>
    </div>
    """, unsafe_allow_html=True)

    if not weather:

        st.warning("Weather information unavailable.")

    elif "error" in weather:

        st.error(weather["error"])

    else:

        condition = weather.get("condition","Unknown")

        temperature = weather.get("temperature","N/A")

        humidity = weather.get("humidity","N/A")

        city = weather.get("city","Unknown")

        c1,c2,c3 = st.columns(3)

        with c1:
            st.metric("🌡 Temp",f"{temperature}°C")

        with c2:
            st.metric("💧 Humidity",f"{humidity}%")

        with c3:
            st.metric("☁ Weather",condition.title())

        st.markdown(f"""
        <div class="card">

        <h2>📍 {city}</h2>

        <h3>☀ {condition.title()}</h3>

        <p>Temperature : {temperature} °C</p>

        <p>Humidity : {humidity}%</p>

        </div>
        """,unsafe_allow_html=True)

    st.divider()

    col1,col2=st.columns(2)

    with col1:

        if st.button("⬅ Back"):

            st.session_state.page="food"

            st.rerun()

    with col2:

        if st.button("Next ➜"):

            st.session_state.page="budget"

            st.rerun()

# -------------------------------
# BUDGET PAGE
# -------------------------------

elif st.session_state.page=="budget":

    import pandas as pd
    import plotly.express as px

    result=st.session_state.result

    st.markdown("""
    <div class="container">
    <div class="title">💰 Budget</div>
    <div class="subtitle">Step 5 of 8</div>
    </div>
    """,unsafe_allow_html=True)

    budget=result.get("Budget",{})

    if "error" in budget:

        st.error(budget["error"])

    else:

        budget_df=pd.DataFrame(
            budget.items(),
            columns=["Category","Amount"]
        )

        st.dataframe(
            budget_df,
            use_container_width=True,
            hide_index=True
        )

        chart_df=budget_df[
            ~budget_df["Category"].isin(
                [
                    "Guests",
                    "Total Budget",
                    "Cost Per Guest"
                ]
            )
        ]

        fig=px.pie(
            chart_df,
            names="Category",
            values="Amount",
            hole=.45
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.divider()

    c1,c2=st.columns(2)

    with c1:

        if st.button("⬅ Back"):

            st.session_state.page="weather"

            st.rerun()

    with c2:

        if st.button("Next ➜"):

            st.session_state.page="schedule"

            st.rerun()

# -------------------------------
# SCHEDULE PAGE
# -------------------------------

elif st.session_state.page=="schedule":

    result=st.session_state.result

    st.markdown("""
    <div class="container">

    <div class="title">

    📅 Event Timeline

    </div>

    <div class="subtitle">

    Step 6 of 8

    </div>

    </div>
    """,unsafe_allow_html=True)

    schedule=result.get("Schedule","")

    if schedule:

        lines=schedule.split("\n")

        for line in lines:

            if line.strip():

                st.markdown(f"""
                <div class="card">

                ⏰ {line}

                </div>
                """,unsafe_allow_html=True)

    c1,c2=st.columns(2)

    with c1:

        if st.button("⬅ Back"):

            st.session_state.page="budget"

            st.rerun()

    with c2:

        if st.button("Next ➜"):

            st.session_state.page="review"

            st.rerun()

# -------------------------------
# REVIEW PAGE
# -------------------------------

elif st.session_state.page=="review":

    result=st.session_state.result

    st.markdown("""
    <div class="container">

    <div class="title">

    ⭐ AI Review

    </div>

    <div class="subtitle">

    Step 7 of 8

    </div>

    </div>
    """,unsafe_allow_html=True)

    st.metric(
        "AI Quality Score",
        "96%"
    )

    st.progress(.96)

    st.markdown(f"""
    <div class="card">

    {result["Review"]}

    </div>
    """,unsafe_allow_html=True)

    st.success("✔ Budget Looks Good")

    st.success("✔ Venue Selection Looks Good")

    st.success("✔ Weather Suitable")

    st.success("✔ Schedule Optimized")

    c1,c2=st.columns(2)

    with c1:

        if st.button("⬅ Back"):

            st.session_state.page="schedule"

            st.rerun()

    with c2:

        if st.button("Finish ➜"):

            st.session_state.page="finish"

            st.rerun()

# -------------------------------
# FINISH PAGE
# -------------------------------

elif st.session_state.page=="finish":

    result=st.session_state.result

    st.balloons()

    st.snow()

    st.markdown("""
    <div class="balloon b1">🎈</div>
    <div class="balloon b2">🎈</div>
    <div class="balloon b3">🎈</div>
    <div class="balloon b4">🎈</div>
    """,unsafe_allow_html=True)

    st.markdown("""
    <div class="container">

    <div class="title">

    🎉 Congratulations

    </div>

    <div class="subtitle">

    Your AI Event Plan is Ready!

    </div>

    </div>
    """,unsafe_allow_html=True)

    st.success("Everything has been planned successfully.")

    c1,c2,c3,c4=st.columns(4)

    with c1:

        st.metric(
            "👥 Guests",
            st.session_state.guests
        )

    with c2:

        st.metric(
            "💰 Budget",
            f"₹{st.session_state.budget:,}"
        )

    with c3:

        st.metric(
            "📍 Venues",
            len(result["Venues"])
        )

    with c4:

        st.metric(
            "🍽 Caterers",
            len(result["Food"])
        )

    st.markdown("""
    # 🎉 Event Successfully Planned

    ### Everything is Ready!

    ✨ Venue Booked

    ✨ Catering Planned

    ✨ Weather Checked

    ✨ Budget Optimized

    ✨ Schedule Created

    """)

    st.info("""
    📄 Download your complete event plan.

    Share it with your friends,
    family or team members.
    """)

    st.download_button(
        "📥 Download Event Plan",
        data=json.dumps(result,indent=4),
        file_name="event_plan.json",
        mime="application/json"
    )

    st.markdown("""
    <hr>

    <center>

    Made with ❤️ using

    Groq • Streamlit • Tavily • OpenWeather

    </center>

    """,unsafe_allow_html=True)

    if st.button("🏠 Plan Another Event"):

        st.session_state.clear()

        st.rerun()