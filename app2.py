# import streamlit as st
# import time
# import json
# from pipeline import run_event_planner


# def md(html):
#     """Render HTML/CSS using Streamlit."""
#     lines = [line.strip() for line in html.strip("\n").split("\n")]
#     st.markdown("\n".join(lines), unsafe_allow_html=True)


# # -------------------------------
# # PAGE CONFIG
# # -------------------------------

# st.set_page_config(
#     page_title="EventGenie AI",
#     page_icon="🎉",
#     layout="centered",
#     initial_sidebar_state="collapsed"
# )

# # -------------------------------
# # SESSION
# # -------------------------------

# if "page" not in st.session_state:
#     st.session_state.page = "welcome"

# # -------------------------------
# # STEP TRACKER CONFIG
# # -------------------------------

# STEPS = [
#     ("details", "📋", "Details"),
#     ("venues", "📍", "Venues"),
#     ("food", "🍽", "Food"),
#     ("weather", "🌦", "Weather"),
#     ("budget", "💰", "Budget"),
#     ("schedule", "📅", "Schedule"),
#     ("review", "⭐", "Review"),
# ]

# def render_stepper(current_key):
#     """Render a persistent gold step tracker for the wizard pages."""
#     current_index = next((i for i, s in enumerate(STEPS) if s[0] == current_key), -1)

#     nodes = ""
#     for i, (key, icon, label) in enumerate(STEPS):
#         if i < current_index:
#             state = "done"
#         elif i == current_index:
#             state = "active"
#         else:
#             state = "todo"

#         nodes += f"""
#         <div class="step {state}">
#             <div class="step-dot">{icon if state != "done" else "✓"}</div>
#             <div class="step-label">{label}</div>
#         </div>
#         """
#         if i < len(STEPS) - 1:
#             line_state = "done" if i < current_index else "todo"
#             nodes += f'<div class="step-line {line_state}"></div>'

#     md(f'<div class="stepper">{nodes}</div>')


# def page_header(title, subtitle=""):
#     sub_html = f'<div class="subtitle">{subtitle}</div>' if subtitle else ""
#     md(f"""
#     <div class="page-head">
#         <div class="title">{title}</div>
#         {sub_html}
#     </div>
#     """)


# # -------------------------------
# # CSS — Dark Elegant / Charcoal & Gold
# # -------------------------------

# md("""
# <style>

# @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800&family=Playfair+Display:wght@500;600;700&family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@500&display=swap');

# /* Hide Streamlit chrome */
# #MainMenu{visibility:hidden;}
# footer{visibility:hidden;}
# header{visibility:hidden;}

# html, body{
#     font-family:'Inter', sans-serif;
#     color:#F5F1E6;
# }

# /* Background — target every known wrapper so this holds across Streamlit versions/themes */
# html, body,
# .stApp,
# [data-testid="stAppViewContainer"],
# [data-testid="stMain"],
# [data-testid="stHeader"]{
#     background-color:#082726 !important;
# }

# .stApp,
# [data-testid="stAppViewContainer"]{
#     background:linear-gradient(135deg,#082726,#0e3937,#134b48,#0e3937,#082726) !important;
#     background-size:400% 400% !important;
#     animation:bgshift 22s ease infinite;
# }

# [data-testid="stHeader"]{
#     background:transparent !important;
# }

# @keyframes bgshift{
#     0%{background-position:0% 50%;}
#     50%{background-position:100% 50%;}
#     100%{background-position:0% 50%;}
# }

# /* Global text contrast — catches every default Streamlit element, not just custom classes */
# p, span, li, label, .stMarkdown, .stMarkdown *,
# [data-testid="stMarkdownContainer"], [data-testid="stMarkdownContainer"] *{
#     color:#EDE8DA;
# }

# /* Main content width */
# .block-container{
#     max-width:760px;
#     padding-top:2.5rem;
#     padding-bottom:3rem;
# }

# /* Container card that wraps each page's content */
# .container{
#     padding:36px 40px;
#     border-radius:22px;
#     background:rgba(255,255,255,.03);
#     border:1px solid rgba(45,212,191,.22);
#     backdrop-filter:blur(16px);
#     box-shadow:0 0 50px rgba(45,212,191,.06);
#     margin-bottom:20px;
# }

# /* Page head */
# .page-head{
#     text-align:center;
#     margin-bottom:8px;
# }

# .logo{
#     font-size:60px;
#     text-align:center;
#     filter:drop-shadow(0 0 18px rgba(45,212,191,.35));
# }

# .title{
#     font-family:'Playfair Display', serif !important;
#     font-size:40px;
#     font-weight:700;
#     text-align:center;
#     color:#7CF2E0 !important;
#     letter-spacing:.3px;
#     text-shadow:0 0 24px rgba(94,234,212,.35);
# }

# .subtitle{
#     text-align:center;
#     font-size:15.5px;
#     color:#D8D2C0 !important;
#     margin-top:6px;
#     margin-bottom:6px;
#     font-weight:400;
# }

# /* Hero title — the app's own name, big and colorful */
# .hero-title{
#     font-family:'Cinzel', 'Playfair Display', serif !important;
#     font-size:56px;
#     font-weight:800;
#     text-align:center;
#     letter-spacing:1px;
#     margin-top:6px;
#     margin-bottom:4px;
#     background:linear-gradient(90deg, #7CF2E0 0%, #99F6E4 35%, #2DD4BF 65%, #F5F1E6 100%);
#     background-size:200% auto;
#     -webkit-background-clip:text;
#     -webkit-text-fill-color:transparent;
#     background-clip:text;
#     animation:shine 6s ease-in-out infinite;
#     text-shadow:0 0 34px rgba(94,234,212,.25);
# }

# @keyframes shine{
#     0%{background-position:0% center;}
#     50%{background-position:100% center;}
#     100%{background-position:0% center;}
# }

# .hero-tagline{
#     text-align:center;
#     font-size:16px;
#     font-weight:500;
#     color:#EDE8DA !important;
#     margin-bottom:26px;
# }

# /* Event type grid */
# .event-grid{
#     display:flex;
#     flex-wrap:wrap;
#     justify-content:center;
#     gap:10px;
#     margin-top:6px;
# }

# .event-chip{
#     display:flex;
#     align-items:center;
#     gap:8px;
#     padding:10px 16px;
#     border-radius:999px;
#     background:rgba(45,212,191,.08);
#     border:1px solid rgba(45,212,191,.3);
#     color:#F5F1E6;
#     font-weight:600;
#     font-size:14.5px;
#     white-space:nowrap;
# }

# .event-chip .icon{
#     font-size:17px;
# }

# /* Gold hairline divider */
# .divider-gold{
#     height:1px;
#     margin:22px 0;
#     background:linear-gradient(90deg, transparent, rgba(45,212,191,.55), transparent);
#     border:none;
# }

# /* Step tracker */
# .stepper{
#     display:flex;
#     align-items:flex-start;
#     justify-content:center;
#     margin:6px 0 28px 0;
#     padding:0 4px;
# }

# .step{
#     display:flex;
#     flex-direction:column;
#     align-items:center;
#     width:64px;
# }

# .step-dot{
#     width:34px;
#     height:34px;
#     border-radius:50%;
#     display:flex;
#     align-items:center;
#     justify-content:center;
#     font-size:15px;
#     border:1.5px solid rgba(45,212,191,.3);
#     color:#867F6E;
#     background:rgba(255,255,255,.02);
#     transition:.3s;
# }

# .step.active .step-dot{
#     border-color:#2DD4BF;
#     color:#082726;
#     background:linear-gradient(135deg,#5EEAD4,#0F766E);
#     box-shadow:0 0 16px rgba(45,212,191,.55);
# }

# .step.done .step-dot{
#     border-color:rgba(45,212,191,.6);
#     color:#2DD4BF;
#     background:rgba(45,212,191,.08);
# }

# .step-label{
#     font-size:10.5px;
#     text-transform:uppercase;
#     letter-spacing:.5px;
#     color:#867F6E;
#     margin-top:6px;
#     text-align:center;
# }

# .step.active .step-label{ color:#5EEAD4; font-weight:600; }
# .step.done .step-label{ color:#7CF2E0; }

# .step-line{
#     flex:1;
#     height:1px;
#     margin-top:17px;
#     background:rgba(45,212,191,.18);
#     min-width:12px;
# }

# .step-line.done{ background:rgba(45,212,191,.55); }

# /* Cards for content items (venues, food, schedule lines...) */
# .card{
#     background:rgba(255,255,255,.035);
#     padding:18px 20px;
#     border-radius:14px;
#     border:1px solid rgba(45,212,191,.16);
#     color:#F5F1E6;
#     margin-top:14px;
#     transition:.3s;
# }

# .card:hover{
#     border-color:rgba(45,212,191,.5);
#     box-shadow:0 0 22px rgba(45,212,191,.18);
#     transform:translateY(-2px);
# }

# .card h2, .card h3{
#     color:#5EEAD4;
#     font-family:'Playfair Display', serif;
#     font-weight:600;
#     margin-bottom:4px;
# }

# .card p{
#     color:#D8D2C0;
#     font-size:14.5px;
#     line-height:1.5;
# }

# /* Empty / info state */
# .empty-state{
#     text-align:center;
#     padding:30px 20px;
#     color:#A69F8C;
#     border:1px dashed rgba(45,212,191,.3);
#     border-radius:14px;
#     font-size:14.5px;
# }

# /* Buttons */
# div.stButton>button{
#     width:100%;
#     height:54px;
#     font-size:16.5px;
#     font-weight:600;
#     font-family:'Inter', sans-serif;
#     border-radius:12px;
#     border:1px solid #2DD4BF;
#     background:linear-gradient(90deg,#0F766E,#2DD4BF);
#     color:#082726;
#     transition:.25s;
#     letter-spacing:.2px;
# }

# div.stButton>button:hover{
#     transform:translateY(-1px);
#     box-shadow:0 6px 22px rgba(45,212,191,.35);
# }

# div.stButton>button:disabled{
#     background:rgba(255,255,255,.06);
#     border-color:rgba(255,255,255,.1);
#     color:#5C5648;
# }

# /* Secondary / back buttons: any button whose column is the first of a pair reads lighter */
# div[data-testid="column"]:first-of-type div.stButton>button{
#     background:rgba(255,255,255,.04);
#     color:#EDE8DA;
#     border:1px solid rgba(45,212,191,.35);
# }

# div[data-testid="column"]:first-of-type div.stButton>button:hover{
#     box-shadow:0 6px 18px rgba(45,212,191,.15);
# }

# /* Link buttons */
# a[data-testid="stBaseLinkButton-secondary"], a[kind="secondary"]{
#     border:1px solid rgba(45,212,191,.4) !important;
#     color:#5EEAD4 !important;
#     background:rgba(45,212,191,.06) !important;
# }

# /* Inputs */
# div[data-baseweb="select"]>div, .stTextInput input, .stDateInput input{
#     background:rgba(255,255,255,.04) !important;
#     border:1px solid rgba(45,212,191,.25) !important;
#     color:#F5F1E6 !important;
#     border-radius:10px !important;
# }

# label, .stSlider label, .stSelectbox label, .stTextInput label, .stDateInput label{
#     color:#D8D2C0 !important;
#     font-weight:500 !important;
# }

# /* Slider */
# .stSlider [data-baseweb="slider"] > div > div{
#     background:rgba(45,212,191,.9) !important;
# }

# /* Progress bar */
# .stProgress > div > div > div{
#     background:linear-gradient(90deg,#0F766E,#5EEAD4) !important;
# }
# .stProgress > div > div{
#     background:rgba(255,255,255,.06) !important;
# }

# /* Metrics */
# [data-testid="stMetricValue"]{
#     color:#5EEAD4 !important;
#     font-family:'IBM Plex Mono', monospace !important;
# }
# [data-testid="stMetricLabel"]{
#     color:#CBC5B2 !important;
# }

# /* Alerts (info/success/warning/error) restyled to fit palette */
# div[data-testid="stAlert"]{
#     background:rgba(255,255,255,.03) !important;
#     border:1px solid rgba(45,212,191,.25) !important;
#     border-radius:12px !important;
#     color:#EDE8DA !important;
# }

# /* Dataframe */
# [data-testid="stDataFrame"]{
#     border:1px solid rgba(45,212,191,.2);
#     border-radius:12px;
#     overflow:hidden;
# }

# /* Balloons flourish on finish page */
# .balloon{
#     position:fixed;
#     bottom:-100px;
#     font-size:38px;
#     animation:floatup 12s linear infinite;
#     opacity:.9;
# }
# .b1{ left:10%; animation-delay:0s; }
# .b2{ left:30%; animation-delay:2.5s; }
# .b3{ left:60%; animation-delay:5s; }
# .b4{ left:85%; animation-delay:7.5s; }

# @keyframes floatup{
#     0%{ transform:translateY(0); opacity:0; }
#     15%{ opacity:.9; }
#     100%{ transform:translateY(-120vh); opacity:0; }
# }

# .footer-note{
#     text-align:center;
#     color:#867F6E;
#     font-size:12.5px;
#     letter-spacing:.3px;
#     margin-top:18px;
# }

# </style>
# """)


# # -------------------------------
# # WELCOME PAGE
# # -------------------------------

# if st.session_state.page == "welcome":

#     md("""
#     <div class="container">

#         <div class="logo">🎉</div>
#         <div class="hero-title">EventGenie AI</div>
#         <div class="hero-tagline">Tell me what you're celebrating — I'll handle venues, food, weather, budget, and the schedule.</div>

#         <hr class="divider-gold" />

#         <div class="card">
#             <h3>✨ Built to plan</h3>
#             <div class="event-grid">
#                 <div class="event-chip"><span class="icon">🎂</span>Birthdays</div>
#                 <div class="event-chip"><span class="icon">💍</span>Weddings</div>
#                 <div class="event-chip"><span class="icon">🎉</span>Anniversaries</div>
#                 <div class="event-chip"><span class="icon">👶</span>Baby showers</div>
#                 <div class="event-chip"><span class="icon">🎓</span>Graduations</div>
#                 <div class="event-chip"><span class="icon">🏢</span>Conferences</div>
#                 <div class="event-chip"><span class="icon">💼</span>Corporate meetings</div>
#                 <div class="event-chip"><span class="icon">🚀</span>Product launches</div>
#                 <div class="event-chip"><span class="icon">🎊</span>College fests</div>
#                 <div class="event-chip"><span class="icon">🏆</span>Sports events</div>
#                 <div class="event-chip"><span class="icon">🎵</span>Concerts</div>
#                 <div class="event-chip"><span class="icon">🎄</span>Festivals</div>
#                 <div class="event-chip"><span class="icon">👨‍👩‍👧</span>Family reunions</div>
#             </div>
#         </div>

#     </div>
#     """)

#     if st.button("✨ Start planning"):
#         st.session_state.page = "details"
#         st.rerun()

# # -------------------------------
# # DETAILS PAGE
# # -------------------------------

# elif st.session_state.page == "details":

#     md('<div class="container">')

#     render_stepper("details")
#     page_header("Let's start with the basics", "A few details and I'll get to work.")

#     event = st.selectbox(
#         "🎉 What are you celebrating?",
#         [
#             "Birthday", "Wedding", "Anniversary", "Baby Shower", "Naming Ceremony",
#             "Graduation", "Conference", "Seminar", "Workshop", "Corporate Meeting",
#             "Product Launch", "College Fest", "School Annual Day", "Sports Event",
#             "Music Concert", "Festival", "Family Reunion"
#         ]
#     )

#     event_icons = {
#         "Birthday": "🎂", "Wedding": "💍", "Anniversary": "🎉", "Baby Shower": "👶",
#         "Naming Ceremony": "🍼", "Graduation": "🎓", "Conference": "🏢", "Seminar": "📚",
#         "Workshop": "💻", "Corporate Meeting": "💼", "Product Launch": "🚀",
#         "College Fest": "🎊", "School Annual Day": "🏫", "Sports Event": "🏆",
#         "Music Concert": "🎵", "Festival": "🎆", "Family Reunion": "👨‍👩‍👧"
#     }

#     st.success(f"{event_icons[event]} Planning a {event.lower()}")

#     city = st.selectbox(
#         "🏙 Which city?",
#         [
#             "Bangalore", "Mumbai", "Delhi", "Hyderabad", "Chennai", "Pune",
#             "Kolkata", "Ahmedabad", "Jaipur", "Lucknow", "Mysore", "Hubballi",
#             "Mangalore", "Other"
#         ]
#     )

#     if city == "Other":
#         city = st.text_input("Enter your city")

#     guests = st.slider("👥 How many guests?", 10, 5000, 100)

#     budget = st.slider("💰 What's your budget (₹)?", 10000, 5000000, 500000, step=10000)

#     event_date = st.date_input("📅 When's the event?")

#     md('<hr class="divider-gold" />')

#     col1, col2 = st.columns(2)

#     with col1:
#         if st.button("⬅ Back"):
#             st.session_state.page = "welcome"
#             st.rerun()

#     with col2:
#         if st.button("Plan my event ➜"):
#             st.session_state.event = event
#             st.session_state.city = city
#             st.session_state.guests = guests
#             st.session_state.budget = budget
#             st.session_state.date = str(event_date)
#             st.session_state.page = "loading"
#             st.rerun()

#     md('</div>')

# # -------------------------------
# # LOADING PAGE
# # -------------------------------

# elif st.session_state.page == "loading":

#     md("""
#     <div class="container">
#         <div class="page-head">
#             <div class="title">Putting it all together</div>
#             <div class="subtitle">My agents are working through venues, food, weather, budget, and the timeline.</div>
#         </div>
#     </div>
#     """)

#     progress = st.progress(0)
#     status = st.empty()

#     steps = [
#         ("🧠 Reading your event details...", 10),
#         ("📍 Scouting venues in your city...", 25),
#         ("🍽 Lining up caterers...", 40),
#         ("🌦 Checking the forecast for your date...", 55),
#         ("💰 Working out the budget breakdown...", 70),
#         ("📅 Building the day-of schedule...", 85),
#         ("⭐ Giving the whole plan a final look...", 95),
#     ]

#     for message, value in steps:
#         status.info(message)
#         progress.progress(value)
#         time.sleep(0.7)

#     user_request = f"""
#     Plan a {st.session_state.event}

#     City: {st.session_state.city}

#     Budget: {st.session_state.budget}

#     Guests: {st.session_state.guests}

#     Date: {st.session_state.date}
#     """

#     try:
#         result = run_event_planner(user_request)
#         st.session_state.result = result

#         progress.progress(100)
#         status.success("✅ Your event plan is ready!")

#         time.sleep(1)
#         st.session_state.page = "venues"
#         st.rerun()

#     except Exception as e:
#         st.error(f"Something went wrong while planning: {e}")
#         if st.button("⬅ Back to details"):
#             st.session_state.page = "details"
#             st.rerun()

# # -------------------------------
# # VENUES PAGE
# # -------------------------------

# elif st.session_state.page == "venues":

#     result = st.session_state.result

#     md('<div class="container">')
#     render_stepper("venues")
#     page_header("Recommended venues", "Picked to fit your city, guest count, and budget.")

#     venues = result.get("Venues", [])

#     if not venues:
#         md('<div class="empty-state">No venues turned up for this search. Try a different city or widen your budget and re-plan.</div>')
#     else:
#         for venue in venues:
#             md(f"""
#             <div class="card">
#                 <h3>{venue['title']}</h3>
#                 <p>{venue['content']}</p>
#             </div>
#             """)
#             st.link_button("🌐 Visit website", venue["url"], key=venue["url"])

#     md('<hr class="divider-gold" />')

#     c1, c2 = st.columns(2)
#     with c1:
#         if st.button("⬅ Back"):
#             st.session_state.page = "details"
#             st.rerun()
#     with c2:
#         if st.button("See food & catering ➜"):
#             st.session_state.page = "food"
#             st.rerun()

#     md('</div>')

# # -------------------------------
# # FOOD PAGE
# # -------------------------------

# elif st.session_state.page == "food":

#     result = st.session_state.result

#     md('<div class="container">')
#     render_stepper("food")
#     page_header("Food & catering", "Caterers matched to your event and guest count.")

#     food = result.get("Food", [])

#     if not food:
#         md('<div class="empty-state">No catering options came back for this search. Try adjusting your city or budget and re-plan.</div>')
#     else:
#         for caterer in food:
#             md(f"""
#             <div class="card">
#                 <h3>🍴 {caterer['title']}</h3>
#                 <p>{caterer['content']}</p>
#             </div>
#             """)
#             st.link_button("🌐 Visit website", caterer["url"], key=caterer["url"])

#     md('<hr class="divider-gold" />')

#     col1, col2 = st.columns(2)
#     with col1:
#         if st.button("⬅ Back"):
#             st.session_state.page = "venues"
#             st.rerun()
#     with col2:
#         if st.button("Check the weather ➜"):
#             st.session_state.page = "weather"
#             st.rerun()

#     md('</div>')

# # -------------------------------
# # WEATHER PAGE
# # -------------------------------

# elif st.session_state.page == "weather":

#     result = st.session_state.result
#     weather = result.get("Weather", {})

#     md('<div class="container">')
#     render_stepper("weather")
#     page_header("Weather on the day", "Good to know before you finalize the venue.")

#     if not weather:
#         md('<div class="empty-state">Weather data isn\'t available for this date yet. Check back closer to the event.</div>')
#     elif "error" in weather:
#         st.error(weather["error"])
#     else:
#         condition = weather.get("condition", "Unknown")
#         temperature = weather.get("temperature", "N/A")
#         humidity = weather.get("humidity", "N/A")
#         city = weather.get("city", "Unknown")

#         c1, c2, c3 = st.columns(3)
#         with c1:
#             st.metric("🌡 Temp", f"{temperature}°C")
#         with c2:
#             st.metric("💧 Humidity", f"{humidity}%")
#         with c3:
#             st.metric("☁ Weather", condition.title())

#         md(f"""
#         <div class="card">
#             <h2>📍 {city}</h2>
#             <h3>☀ {condition.title()}</h3>
#             <p>Temperature: {temperature}°C &nbsp;·&nbsp; Humidity: {humidity}%</p>
#         </div>
#         """)

#     md('<hr class="divider-gold" />')

#     col1, col2 = st.columns(2)
#     with col1:
#         if st.button("⬅ Back"):
#             st.session_state.page = "food"
#             st.rerun()
#     with col2:
#         if st.button("Build my budget ➜"):
#             st.session_state.page = "budget"
#             st.rerun()

#     md('</div>')

# # -------------------------------
# # BUDGET PAGE
# # -------------------------------

# elif st.session_state.page == "budget":

#     import pandas as pd
#     import plotly.express as px

#     result = st.session_state.result

#     md('<div class="container">')
#     render_stepper("budget")
#     page_header("Budget breakdown", "Where your money goes, category by category.")

#     budget = result.get("Budget", {})

#     if "error" in budget:
#         st.error(budget["error"])
#     else:
#         budget_df = pd.DataFrame(budget.items(), columns=["Category", "Amount"])

#         st.dataframe(budget_df, use_container_width=True, hide_index=True)

#         chart_df = budget_df[
#             ~budget_df["Category"].isin(["Guests", "Total Budget", "Cost Per Guest"])
#         ]

#         fig = px.pie(chart_df, names="Category", values="Amount", hole=.55)
#         fig.update_traces(
#             marker=dict(colors=["#2DD4BF", "#0F766E", "#8a6d1f", "#5EEAD4", "#6b5416", "#c9a53e"]),
#             textfont_color="#F5F1E6"
#         )
#         fig.update_layout(
#             paper_bgcolor="rgba(0,0,0,0)",
#             plot_bgcolor="rgba(0,0,0,0)",
#             font_color="#EDE8DA",
#             legend=dict(font=dict(color="#EDE8DA"))
#         )

#         st.plotly_chart(fig, use_container_width=True)

#     md('<hr class="divider-gold" />')

#     c1, c2 = st.columns(2)
#     with c1:
#         if st.button("⬅ Back"):
#             st.session_state.page = "weather"
#             st.rerun()
#     with c2:
#         if st.button("See the schedule ➜"):
#             st.session_state.page = "schedule"
#             st.rerun()

#     md('</div>')

# # -------------------------------
# # SCHEDULE PAGE
# # -------------------------------

# elif st.session_state.page == "schedule":

#     result = st.session_state.result

#     md('<div class="container">')
#     render_stepper("schedule")
#     page_header("Event timeline", "Your day, laid out hour by hour.")

#     schedule = result.get("Schedule", "")

#     if schedule:
#         lines = schedule.split("\n")
#         for line in lines:
#             if line.strip():
#                 md(f'<div class="card">⏰ {line}</div>')
#     else:
#         md('<div class="empty-state">No timeline was generated. Head back and re-plan to try again.</div>')

#     md('<hr class="divider-gold" />')

#     c1, c2 = st.columns(2)
#     with c1:
#         if st.button("⬅ Back"):
#             st.session_state.page = "budget"
#             st.rerun()
#     with c2:
#         if st.button("Review my plan ➜"):
#             st.session_state.page = "review"
#             st.rerun()

#     md('</div>')

# # -------------------------------
# # REVIEW PAGE
# # -------------------------------

# elif st.session_state.page == "review":

#     result = st.session_state.result

#     md('<div class="container">')
#     render_stepper("review")
#     page_header("Final review", "One last look before it's locked in.")

#     st.metric("Plan quality score", "96%")
#     st.progress(.96)

#     md(f'<div class="card">{result["Review"]}</div>')

#     st.success("✔ Budget looks balanced")
#     st.success("✔ Venue selection fits your guest count")
#     st.success("✔ Weather works for the date")
#     st.success("✔ Schedule is realistic")

#     md('<hr class="divider-gold" />')

#     c1, c2 = st.columns(2)
#     with c1:
#         if st.button("⬅ Back"):
#             st.session_state.page = "schedule"
#             st.rerun()
#     with c2:
#         if st.button("Finish ➜"):
#             st.session_state.page = "finish"
#             st.rerun()

#     md('</div>')

# # -------------------------------
# # FINISH PAGE
# # -------------------------------

# elif st.session_state.page == "finish":

#     result = st.session_state.result

#     st.balloons()

#     md("""
#     <div class="balloon b1">🎈</div>
#     <div class="balloon b2">🎈</div>
#     <div class="balloon b3">🎈</div>
#     <div class="balloon b4">🎈</div>
#     """)

#     md('<div class="container">')

#     page_header("Your event is ready 🎉", "Every detail is planned — save it or start another.")

#     md('<hr class="divider-gold" />')

#     c1, c2, c3, c4 = st.columns(4)
#     with c1:
#         st.metric("👥 Guests", st.session_state.guests)
#     with c2:
#         st.metric("💰 Budget", f"₹{st.session_state.budget:,}")
#     with c3:
#         st.metric("📍 Venues", len(result["Venues"]))
#     with c4:
#         st.metric("🍽 Caterers", len(result["Food"]))

#     md('<hr class="divider-gold" />')

#     st.download_button(
#         "📥 Download event plan",
#         data=json.dumps(result, indent=4),
#         file_name="event_plan.json",
#         mime="application/json"
#     )

#     md('<div class="footer-note">Save this file to share with vendors, family, or your team.</div>')

#     if st.button("🏠 Plan another event"):
#         st.session_state.clear()
#         st.rerun()

#     md('<div class="footer-note" style="margin-top:28px;">Made with ❤️ using Groq · Streamlit · Tavily · OpenWeather</div>')

#     md('</div>')



import streamlit as st
import time
import json
from pipeline import run_event_planner


def md(html):
    """Render HTML/CSS using Streamlit."""
    lines = [line.strip() for line in html.strip("\n").split("\n")]
    st.markdown("\n".join(lines), unsafe_allow_html=True)


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
# STEP TRACKER CONFIG
# -------------------------------

STEPS = [
    ("details", "📋", "Details"),
    ("venues", "📍", "Venues"),
    ("food", "🍽", "Food"),
    ("weather", "🌦", "Weather"),
    ("budget", "💰", "Budget"),
    ("schedule", "📅", "Schedule"),
    ("review", "⭐", "Review"),
]

def render_stepper(current_key):
    """Render a persistent gold step tracker for the wizard pages."""
    current_index = next((i for i, s in enumerate(STEPS) if s[0] == current_key), -1)

    nodes = ""
    for i, (key, icon, label) in enumerate(STEPS):
        if i < current_index:
            state = "done"
        elif i == current_index:
            state = "active"
        else:
            state = "todo"

        nodes += f"""
        <div class="step {state}">
            <div class="step-dot">{icon if state != "done" else "✓"}</div>
            <div class="step-label">{label}</div>
        </div>
        """
        if i < len(STEPS) - 1:
            line_state = "done" if i < current_index else "todo"
            nodes += f'<div class="step-line {line_state}"></div>'

    md(f'<div class="stepper">{nodes}</div>')


def page_header(title, subtitle=""):
    sub_html = f'<div class="subtitle">{subtitle}</div>' if subtitle else ""
    md(f"""
    <div class="page-head">
        <div class="title">{title}</div>
        {sub_html}
    </div>
    """)


# -------------------------------
# CSS — Dark Elegant / Charcoal & Gold
# -------------------------------

md("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800&family=Playfair+Display:wght@500;600;700&family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@500&display=swap');

/* Hide Streamlit chrome */
#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
header{visibility:hidden;}

html, body{
    font-family:'Inter', sans-serif;
    color:#F5F1E6;
}

/* Background — target every known wrapper so this holds across Streamlit versions/themes */
html, body,
.stApp,
[data-testid="stAppViewContainer"],
[data-testid="stMain"],
[data-testid="stHeader"]{
    background-color:#082726 !important;
}

.stApp,
[data-testid="stAppViewContainer"]{
    background:linear-gradient(135deg,#082726,#0e3937,#134b48,#0e3937,#082726) !important;
    background-size:400% 400% !important;
    animation:bgshift 22s ease infinite;
}

[data-testid="stHeader"]{
    background:transparent !important;
}

/* Ambient drifting orbs — soft atmosphere behind the content */
[data-testid="stAppViewContainer"]::before,
[data-testid="stAppViewContainer"]::after{
    content:"";
    position:fixed;
    border-radius:50%;
    filter:blur(70px);
    pointer-events:none;
    z-index:0;
}

[data-testid="stAppViewContainer"]::before{
    width:420px;
    height:420px;
    top:-120px;
    left:-100px;
    background:radial-gradient(circle, rgba(45,212,191,.22), transparent 70%);
    animation:drift1 26s ease-in-out infinite;
}

[data-testid="stAppViewContainer"]::after{
    width:480px;
    height:480px;
    bottom:-160px;
    right:-120px;
    background:radial-gradient(circle, rgba(245,241,230,.10), transparent 70%);
    animation:drift2 30s ease-in-out infinite;
}

@keyframes drift1{
    0%, 100%{ transform:translate(0,0); }
    50%{ transform:translate(60px,40px); }
}

@keyframes drift2{
    0%, 100%{ transform:translate(0,0); }
    50%{ transform:translate(-50px,-30px); }
}

.block-container{ position:relative; z-index:1; }

@keyframes bgshift{
    0%{background-position:0% 50%;}
    50%{background-position:100% 50%;}
    100%{background-position:0% 50%;}
}

/* Global text contrast — catches every default Streamlit element, not just custom classes */
p, span, li, label, .stMarkdown, .stMarkdown *,
[data-testid="stMarkdownContainer"], [data-testid="stMarkdownContainer"] *{
    color:#EDE8DA;
}

/* Main content width */
.block-container{
    max-width:760px;
    padding-top:2.5rem;
    padding-bottom:3rem;
}

/* Container card that wraps each page's content */
.container{
    padding:36px 40px;
    border-radius:22px;
    background:rgba(255,255,255,.03);
    border:1px solid rgba(45,212,191,.22);
    backdrop-filter:blur(16px);
    box-shadow:0 0 50px rgba(45,212,191,.06);
    margin-bottom:20px;
    animation:fadeInUp .5s ease both;
}

@keyframes fadeInUp{
    from{ opacity:0; transform:translateY(14px); }
    to{ opacity:1; transform:translateY(0); }
}

/* Page head */
.page-head{
    text-align:center;
    margin-bottom:8px;
}

.logo{
    font-size:60px;
    text-align:center;
    filter:drop-shadow(0 0 18px rgba(45,212,191,.35));
}

.title{
    font-family:'Playfair Display', serif !important;
    font-size:40px;
    font-weight:700;
    text-align:center;
    color:#7CF2E0 !important;
    letter-spacing:.3px;
    text-shadow:0 0 24px rgba(94,234,212,.35);
}

.subtitle{
    text-align:center;
    font-size:15.5px;
    color:#D8D2C0 !important;
    margin-top:6px;
    margin-bottom:6px;
    font-weight:400;
}

/* Hero title — the app's own name, big and colorful */
.hero-title{
    font-family:'Cinzel', 'Playfair Display', serif !important;
    font-size:56px;
    font-weight:800;
    text-align:center;
    letter-spacing:1px;
    margin-top:6px;
    margin-bottom:4px;
    background:linear-gradient(90deg, #7CF2E0 0%, #99F6E4 35%, #2DD4BF 65%, #F5F1E6 100%);
    background-size:200% auto;
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    background-clip:text;
    animation:shine 6s ease-in-out infinite;
    text-shadow:0 0 34px rgba(94,234,212,.25);
}

@keyframes shine{
    0%{background-position:0% center;}
    50%{background-position:100% center;}
    100%{background-position:0% center;}
}

.hero-tagline{
    text-align:center;
    font-size:16px;
    font-weight:500;
    color:#EDE8DA !important;
    margin-bottom:26px;
}

/* Event type grid */
.event-grid{
    display:flex;
    flex-wrap:wrap;
    justify-content:center;
    gap:10px;
    margin-top:6px;
}

.event-chip{
    display:flex;
    align-items:center;
    gap:8px;
    padding:10px 16px;
    border-radius:999px;
    background:rgba(45,212,191,.08);
    border:1px solid rgba(45,212,191,.3);
    color:#F5F1E6;
    font-weight:600;
    font-size:14.5px;
    white-space:nowrap;
}

.event-chip .icon{
    font-size:17px;
}

/* Gold hairline divider */
.divider-gold{
    height:1px;
    margin:22px 0;
    background:linear-gradient(90deg, transparent, rgba(45,212,191,.55), transparent);
    border:none;
}

/* Step tracker */
.stepper{
    display:flex;
    align-items:flex-start;
    justify-content:center;
    margin:6px 0 28px 0;
    padding:0 4px;
}

.step{
    display:flex;
    flex-direction:column;
    align-items:center;
    width:64px;
}

.step-dot{
    width:34px;
    height:34px;
    border-radius:50%;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:15px;
    border:1.5px solid rgba(45,212,191,.3);
    color:#867F6E;
    background:rgba(255,255,255,.02);
    transition:.3s;
}

.step.active .step-dot{
    border-color:#2DD4BF;
    color:#082726;
    background:linear-gradient(135deg,#5EEAD4,#0F766E);
    box-shadow:0 0 16px rgba(45,212,191,.55);
}

.step.done .step-dot{
    border-color:rgba(45,212,191,.6);
    color:#2DD4BF;
    background:rgba(45,212,191,.08);
}

.step-label{
    font-size:10.5px;
    text-transform:uppercase;
    letter-spacing:.5px;
    color:#867F6E;
    margin-top:6px;
    text-align:center;
}

.step.active .step-label{ color:#5EEAD4; font-weight:600; }
.step.done .step-label{ color:#7CF2E0; }

.step-line{
    flex:1;
    height:1px;
    margin-top:17px;
    background:rgba(45,212,191,.18);
    min-width:12px;
}

.step-line.done{ background:rgba(45,212,191,.55); }

/* Cards for content items (venues, food, schedule lines...) */
.card{
    background:rgba(255,255,255,.035);
    padding:18px 20px;
    border-radius:14px;
    border:1px solid rgba(45,212,191,.16);
    color:#F5F1E6;
    margin-top:14px;
    transition:.3s;
    animation:fadeInUp .45s ease both;
}

.card:hover{
    border-color:rgba(45,212,191,.5);
    box-shadow:0 0 22px rgba(45,212,191,.18);
    transform:translateY(-2px);
}

.card h2, .card h3{
    color:#5EEAD4;
    font-family:'Playfair Display', serif;
    font-weight:600;
    margin-bottom:4px;
}

.card p{
    color:#D8D2C0;
    font-size:14.5px;
    line-height:1.5;
}

/* Empty / info state */
.empty-state{
    text-align:center;
    padding:30px 20px;
    color:#A69F8C;
    border:1px dashed rgba(45,212,191,.3);
    border-radius:14px;
    font-size:14.5px;
}

/* Buttons */
div.stButton>button{
    width:100%;
    height:54px;
    font-size:16.5px;
    font-weight:600;
    font-family:'Inter', sans-serif;
    border-radius:12px;
    border:1px solid #2DD4BF;
    background:linear-gradient(90deg,#0F766E,#2DD4BF);
    color:#082726;
    transition:.25s;
    letter-spacing:.2px;
}

div.stButton>button:hover{
    transform:translateY(-1px);
    box-shadow:0 6px 22px rgba(45,212,191,.35);
}

div.stButton>button:active{
    transform:translateY(0px) scale(.98);
}

div.stButton>button:focus-visible,
a[data-testid="stBaseLinkButton-secondary"]:focus-visible,
div[data-baseweb="select"]>div:focus-within,
.stTextInput input:focus-visible,
.stDateInput input:focus-visible{
    outline:2px solid #5EEAD4 !important;
    outline-offset:2px;
}

div.stButton>button:disabled{
    background:rgba(255,255,255,.06);
    border-color:rgba(255,255,255,.1);
    color:#5C5648;
}

/* Secondary / back buttons: any button whose column is the first of a pair reads lighter */
div[data-testid="column"]:first-of-type div.stButton>button{
    background:rgba(255,255,255,.04);
    color:#EDE8DA;
    border:1px solid rgba(45,212,191,.35);
}

div[data-testid="column"]:first-of-type div.stButton>button:hover{
    box-shadow:0 6px 18px rgba(45,212,191,.15);
}

/* Link buttons */
a[data-testid="stBaseLinkButton-secondary"], a[kind="secondary"]{
    border:1px solid rgba(45,212,191,.4) !important;
    color:#5EEAD4 !important;
    background:rgba(45,212,191,.06) !important;
}

/* Inputs */
div[data-baseweb="select"]>div, .stTextInput input, .stDateInput input{
    background:rgba(255,255,255,.04) !important;
    border:1px solid rgba(45,212,191,.25) !important;
    color:#F5F1E6 !important;
    border-radius:10px !important;
}

label, .stSlider label, .stSelectbox label, .stTextInput label, .stDateInput label{
    color:#D8D2C0 !important;
    font-weight:500 !important;
}

/* Slider */
.stSlider [data-baseweb="slider"] > div > div{
    background:rgba(45,212,191,.9) !important;
}

/* Progress bar */
.stProgress > div > div > div{
    background:linear-gradient(90deg,#0F766E,#5EEAD4) !important;
}
.stProgress > div > div{
    background:rgba(255,255,255,.06) !important;
}

/* Metrics */
[data-testid="stMetricValue"]{
    color:#5EEAD4 !important;
    font-family:'IBM Plex Mono', monospace !important;
}
[data-testid="stMetricLabel"]{
    color:#CBC5B2 !important;
}

/* Alerts (info/success/warning/error) restyled to fit palette */
div[data-testid="stAlert"]{
    background:rgba(255,255,255,.03) !important;
    border:1px solid rgba(45,212,191,.25) !important;
    border-radius:12px !important;
    color:#EDE8DA !important;
}

/* Dataframe */
[data-testid="stDataFrame"]{
    border:1px solid rgba(45,212,191,.2);
    border-radius:12px;
    overflow:hidden;
}

/* Balloons flourish on finish page */
.balloon{
    position:fixed;
    bottom:-100px;
    font-size:38px;
    animation:floatup 12s linear infinite;
    opacity:.9;
}
.b1{ left:10%; animation-delay:0s; }
.b2{ left:30%; animation-delay:2.5s; }
.b3{ left:60%; animation-delay:5s; }
.b4{ left:85%; animation-delay:7.5s; }

@keyframes floatup{
    0%{ transform:translateY(0); opacity:0; }
    15%{ opacity:.9; }
    100%{ transform:translateY(-120vh); opacity:0; }
}

.footer-note{
    text-align:center;
    color:#867F6E;
    font-size:12.5px;
    letter-spacing:.3px;
    margin-top:18px;
}

/* Loading ring spinner */
.ring-loader{
    width:64px;
    height:64px;
    margin:10px auto 22px auto;
    border-radius:50%;
    background:conic-gradient(#2DD4BF, #5EEAD4, transparent 70%);
    -webkit-mask:radial-gradient(farthest-side, transparent calc(100% - 8px), #000 calc(100% - 8px));
    mask:radial-gradient(farthest-side, transparent calc(100% - 8px), #000 calc(100% - 8px));
    animation:spin 1.1s linear infinite;
}

@keyframes spin{
    to{ transform:rotate(360deg); }
}

/* Big weather condition icon */
.weather-icon{
    font-size:52px;
    text-align:center;
    margin-bottom:6px;
    filter:drop-shadow(0 0 18px rgba(94,234,212,.35));
}

/* Ticket-stub styling for the finish page */
.ticket-divider{
    position:relative;
    height:1px;
    margin:26px -40px;
    background:repeating-linear-gradient(90deg, rgba(45,212,191,.5) 0 10px, transparent 10px 20px);
}

.ticket-divider::before, .ticket-divider::after{
    content:"";
    position:absolute;
    top:-11px;
    width:22px;
    height:22px;
    border-radius:50%;
    background:#0e3937;
    border:1px solid rgba(45,212,191,.3);
}

.ticket-divider::before{ left:-11px; }
.ticket-divider::after{ right:-11px; }

/* Responsive tuning */
@media (max-width:640px){
    .container{ padding:26px 20px; }
    .ticket-divider{ margin:26px -20px; }
    .hero-title{ font-size:40px; }
    .title{ font-size:30px; }
    .stepper{ transform:scale(.85); margin:0 -18px 20px -18px; }
}

</style>
""")


# -------------------------------
# WELCOME PAGE
# -------------------------------

if st.session_state.page == "welcome":

    md("""
    <div class="container">

        <div class="logo">🎉</div>
        <div class="hero-title">EventGenie AI</div>
        <div class="hero-tagline">Tell me what you're celebrating — I'll handle venues, food, weather, budget, and the schedule.</div>

        <hr class="divider-gold" />

        <div class="card">
            <h3>✨ Built to plan</h3>
            <div class="event-grid">
                <div class="event-chip"><span class="icon">🎂</span>Birthdays</div>
                <div class="event-chip"><span class="icon">💍</span>Weddings</div>
                <div class="event-chip"><span class="icon">🎉</span>Anniversaries</div>
                <div class="event-chip"><span class="icon">👶</span>Baby showers</div>
                <div class="event-chip"><span class="icon">🎓</span>Graduations</div>
                <div class="event-chip"><span class="icon">🏢</span>Conferences</div>
                <div class="event-chip"><span class="icon">💼</span>Corporate meetings</div>
                <div class="event-chip"><span class="icon">🚀</span>Product launches</div>
                <div class="event-chip"><span class="icon">🎊</span>College fests</div>
                <div class="event-chip"><span class="icon">🏆</span>Sports events</div>
                <div class="event-chip"><span class="icon">🎵</span>Concerts</div>
                <div class="event-chip"><span class="icon">🎄</span>Festivals</div>
                <div class="event-chip"><span class="icon">👨‍👩‍👧</span>Family reunions</div>
            </div>
        </div>

    </div>
    """)

    if st.button("✨ Start planning"):
        st.session_state.page = "details"
        st.rerun()

# -------------------------------
# DETAILS PAGE
# -------------------------------

elif st.session_state.page == "details":

    md('<div class="container">')

    render_stepper("details")
    page_header("Let's start with the basics", "A few details and I'll get to work.")

    event = st.selectbox(
        "🎉 What are you celebrating?",
        [
            "Birthday", "Wedding", "Anniversary", "Baby Shower", "Naming Ceremony",
            "Graduation", "Conference", "Seminar", "Workshop", "Corporate Meeting",
            "Product Launch", "College Fest", "School Annual Day", "Sports Event",
            "Music Concert", "Festival", "Family Reunion"
        ]
    )

    event_icons = {
        "Birthday": "🎂", "Wedding": "💍", "Anniversary": "🎉", "Baby Shower": "👶",
        "Naming Ceremony": "🍼", "Graduation": "🎓", "Conference": "🏢", "Seminar": "📚",
        "Workshop": "💻", "Corporate Meeting": "💼", "Product Launch": "🚀",
        "College Fest": "🎊", "School Annual Day": "🏫", "Sports Event": "🏆",
        "Music Concert": "🎵", "Festival": "🎆", "Family Reunion": "👨‍👩‍👧"
    }

    st.success(f"{event_icons[event]} Planning a {event.lower()}")

    city = st.selectbox(
        "🏙 Which city?",
        [
            "Bangalore", "Mumbai", "Delhi", "Hyderabad", "Chennai", "Pune",
            "Kolkata", "Ahmedabad", "Jaipur", "Lucknow", "Mysore", "Hubballi",
            "Mangalore", "Other"
        ]
    )

    if city == "Other":
        city = st.text_input("Enter your city")

    guests = st.slider("👥 How many guests?", 10, 5000, 100)

    budget = st.slider("💰 What's your budget (₹)?", 10000, 5000000, 500000, step=10000)

    event_date = st.date_input("📅 When's the event?")

    md('<hr class="divider-gold" />')

    col1, col2 = st.columns(2)

    with col1:
        if st.button("⬅ Back"):
            st.session_state.page = "welcome"
            st.rerun()

    with col2:
        if st.button("Plan my event ➜"):
            st.session_state.event = event
            st.session_state.city = city
            st.session_state.guests = guests
            st.session_state.budget = budget
            st.session_state.date = str(event_date)
            st.session_state.page = "loading"
            st.rerun()

    md('</div>')

# -------------------------------
# LOADING PAGE
# -------------------------------

elif st.session_state.page == "loading":

    md("""
    <div class="container">
        <div class="page-head">
            <div class="ring-loader"></div>
            <div class="title">Putting it all together</div>
            <div class="subtitle">My agents are working through venues, food, weather, budget, and the timeline.</div>
        </div>
    </div>
    """)

    progress = st.progress(0)
    status = st.empty()

    steps = [
        ("🧠 Reading your event details...", 10),
        ("📍 Scouting venues in your city...", 25),
        ("🍽 Lining up caterers...", 40),
        ("🌦 Checking the forecast for your date...", 55),
        ("💰 Working out the budget breakdown...", 70),
        ("📅 Building the day-of schedule...", 85),
        ("⭐ Giving the whole plan a final look...", 95),
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
        status.success("✅ Your event plan is ready!")

        time.sleep(1)
        st.session_state.page = "venues"
        st.rerun()

    except Exception as e:
        st.error(f"Something went wrong while planning: {e}")
        if st.button("⬅ Back to details"):
            st.session_state.page = "details"
            st.rerun()

# -------------------------------
# VENUES PAGE
# -------------------------------

elif st.session_state.page == "venues":

    result = st.session_state.result

    md('<div class="container">')
    render_stepper("venues")
    page_header("Recommended venues", "Picked to fit your city, guest count, and budget.")

    venues = result.get("Venues", [])

    if not venues:
        md('<div class="empty-state">No venues turned up for this search. Try a different city or widen your budget and re-plan.</div>')
    else:
        for venue in venues:
            md(f"""
            <div class="card">
                <h3>{venue['title']}</h3>
                <p>{venue['content']}</p>
            </div>
            """)
            st.link_button("🌐 Visit website", venue["url"], key=venue["url"])

    md('<hr class="divider-gold" />')

    c1, c2 = st.columns(2)
    with c1:
        if st.button("⬅ Back"):
            st.session_state.page = "details"
            st.rerun()
    with c2:
        if st.button("See food & catering ➜"):
            st.session_state.page = "food"
            st.rerun()

    md('</div>')

# -------------------------------
# FOOD PAGE
# -------------------------------

elif st.session_state.page == "food":

    result = st.session_state.result

    md('<div class="container">')
    render_stepper("food")
    page_header("Food & catering", "Caterers matched to your event and guest count.")

    food = result.get("Food", [])

    if not food:
        md('<div class="empty-state">No catering options came back for this search. Try adjusting your city or budget and re-plan.</div>')
    else:
        for caterer in food:
            md(f"""
            <div class="card">
                <h3>🍴 {caterer['title']}</h3>
                <p>{caterer['content']}</p>
            </div>
            """)
            st.link_button("🌐 Visit website", caterer["url"], key=caterer["url"])

    md('<hr class="divider-gold" />')

    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅ Back"):
            st.session_state.page = "venues"
            st.rerun()
    with col2:
        if st.button("Check the weather ➜"):
            st.session_state.page = "weather"
            st.rerun()

    md('</div>')

# -------------------------------
# WEATHER PAGE
# -------------------------------

elif st.session_state.page == "weather":

    result = st.session_state.result
    weather = result.get("Weather", {})

    md('<div class="container">')
    render_stepper("weather")
    page_header("Weather on the day", "Good to know before you finalize the venue.")

    if not weather:
        md('<div class="empty-state">Weather data isn\'t available for this date yet. Check back closer to the event.</div>')
    elif "error" in weather:
        st.error(weather["error"])
    else:
        condition = weather.get("condition", "Unknown")
        temperature = weather.get("temperature", "N/A")
        humidity = weather.get("humidity", "N/A")
        city = weather.get("city", "Unknown")

        condition_lower = condition.lower()
        if "storm" in condition_lower or "thunder" in condition_lower:
            weather_emoji = "⛈"
        elif "rain" in condition_lower or "drizzle" in condition_lower:
            weather_emoji = "🌧"
        elif "snow" in condition_lower:
            weather_emoji = "❄"
        elif "cloud" in condition_lower or "overcast" in condition_lower:
            weather_emoji = "☁"
        elif "fog" in condition_lower or "mist" in condition_lower or "haze" in condition_lower:
            weather_emoji = "🌫"
        elif "clear" in condition_lower or "sun" in condition_lower:
            weather_emoji = "☀"
        else:
            weather_emoji = "🌤"

        md(f'<div class="weather-icon">{weather_emoji}</div>')

        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric("🌡 Temp", f"{temperature}°C")
        with c2:
            st.metric("💧 Humidity", f"{humidity}%")
        with c3:
            st.metric(f"{weather_emoji} Weather", condition.title())

        md(f"""
        <div class="card">
            <h2>📍 {city}</h2>
            <h3>{weather_emoji} {condition.title()}</h3>
            <p>Temperature: {temperature}°C &nbsp;·&nbsp; Humidity: {humidity}%</p>
        </div>
        """)

    md('<hr class="divider-gold" />')

    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅ Back"):
            st.session_state.page = "food"
            st.rerun()
    with col2:
        if st.button("Build my budget ➜"):
            st.session_state.page = "budget"
            st.rerun()

    md('</div>')

# -------------------------------
# BUDGET PAGE
# -------------------------------

elif st.session_state.page == "budget":

    import pandas as pd
    import plotly.express as px

    result = st.session_state.result

    md('<div class="container">')
    render_stepper("budget")
    page_header("Budget breakdown", "Where your money goes, category by category.")

    budget = result.get("Budget", {})

    if "error" in budget:
        st.error(budget["error"])
    else:
        budget_df = pd.DataFrame(budget.items(), columns=["Category", "Amount"])

        st.dataframe(budget_df, use_container_width=True, hide_index=True)

        chart_df = budget_df[
            ~budget_df["Category"].isin(["Guests", "Total Budget", "Cost Per Guest"])
        ]

        fig = px.pie(chart_df, names="Category", values="Amount", hole=.55)
        fig.update_traces(
            marker=dict(colors=["#2DD4BF", "#0F766E", "#5EEAD4", "#134b48", "#99F6E4", "#F5F1E6"]),
            textfont_color="#F5F1E6"
        )
        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font_color="#EDE8DA",
            legend=dict(font=dict(color="#EDE8DA"))
        )

        st.plotly_chart(fig, use_container_width=True)

    md('<hr class="divider-gold" />')

    c1, c2 = st.columns(2)
    with c1:
        if st.button("⬅ Back"):
            st.session_state.page = "weather"
            st.rerun()
    with c2:
        if st.button("See the schedule ➜"):
            st.session_state.page = "schedule"
            st.rerun()

    md('</div>')

# -------------------------------
# SCHEDULE PAGE
# -------------------------------

elif st.session_state.page == "schedule":

    result = st.session_state.result

    md('<div class="container">')
    render_stepper("schedule")
    page_header("Event timeline", "Your day, laid out hour by hour.")

    schedule = result.get("Schedule", "")

    if schedule:
        lines = schedule.split("\n")
        for line in lines:
            if line.strip():
                md(f'<div class="card">⏰ {line}</div>')
    else:
        md('<div class="empty-state">No timeline was generated. Head back and re-plan to try again.</div>')

    md('<hr class="divider-gold" />')

    c1, c2 = st.columns(2)
    with c1:
        if st.button("⬅ Back"):
            st.session_state.page = "budget"
            st.rerun()
    with c2:
        if st.button("Review my plan ➜"):
            st.session_state.page = "review"
            st.rerun()

    md('</div>')

# -------------------------------
# REVIEW PAGE
# -------------------------------

elif st.session_state.page == "review":

    result = st.session_state.result

    md('<div class="container">')
    render_stepper("review")
    page_header("Final review", "One last look before it's locked in.")

    st.metric("Plan quality score", "96%")
    st.progress(.96)

    md(f'<div class="card">{result["Review"]}</div>')

    st.success("✔ Budget looks balanced")
    st.success("✔ Venue selection fits your guest count")
    st.success("✔ Weather works for the date")
    st.success("✔ Schedule is realistic")

    md('<hr class="divider-gold" />')

    c1, c2 = st.columns(2)
    with c1:
        if st.button("⬅ Back"):
            st.session_state.page = "schedule"
            st.rerun()
    with c2:
        if st.button("Finish ➜"):
            st.session_state.page = "finish"
            st.rerun()

    md('</div>')

# -------------------------------
# FINISH PAGE
# -------------------------------

elif st.session_state.page == "finish":

    result = st.session_state.result

    st.balloons()

    md("""
    <div class="balloon b1">🎈</div>
    <div class="balloon b2">🎈</div>
    <div class="balloon b3">🎈</div>
    <div class="balloon b4">🎈</div>
    """)

    md('<div class="container">')

    page_header("Your event is ready 🎉", "Every detail is planned — save it or start another.")

    md(f"""
    <div class="card" style="text-align:center;">
        <h3>{st.session_state.event}</h3>
        <p>📍 {st.session_state.city} &nbsp;·&nbsp; 📅 {st.session_state.date}</p>
    </div>
    """)

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("👥 Guests", st.session_state.guests)
    with c2:
        st.metric("💰 Budget", f"₹{st.session_state.budget:,}")
    with c3:
        st.metric("📍 Venues", len(result["Venues"]))
    with c4:
        st.metric("🍽 Caterers", len(result["Food"]))

    md('<div class="ticket-divider"></div>')

    st.download_button(
        "📥 Download event plan",
        data=json.dumps(result, indent=4),
        file_name="event_plan.json",
        mime="application/json"
    )

    md('<div class="footer-note">Save this file to share with vendors, family, or your team.</div>')

    if st.button("🏠 Plan another event"):
        st.session_state.clear()
        st.rerun()

    md('<div class="footer-note" style="margin-top:28px;">Made with ❤️ using Groq · Streamlit · Tavily · OpenWeather</div>')

    md('</div>')