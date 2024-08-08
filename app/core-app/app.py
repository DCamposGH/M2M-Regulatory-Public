import streamlit as st
from home.login import check_password

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    # Request for login
    if not check_password():
        st.stop()
    st.session_state.logged_in = True
    st.rerun()
    # if st.button("Log in"):
    #     st.session_state.logged_in = True
    #     st.rerun()

def logout():
    if st.button("Log out"):
        # login()
        st.session_state.logged_in = False
        st.rerun()

login_page = st.Page(login, title="Log in", icon=":material/login:")
# login_page = st.Page("home/home.py", title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")

### My Code

# Home page
# login = st.Page("home/login.py", title="Home", icon=":material/home:")
# Home page
home = st.Page("home/home.py", title="Home", icon=":material/home:")
# Reports pages
dashboard = st.Page("reports/dashboard.py", title="Dashboard", icon=":material/dashboard:")
# Tools options / pages
risk_analyser = st.Page("tools/risk_analyser.py", title="Risk Analyser", icon=":material/bug_report:")
# Future planned enhancements
alerts = st.Page("enhancements/alerts.py", title="Alerts", icon=":material/precision_manufacturing:")
eligibility = st.Page("enhancements/eligiblity.py", title="Eligiblity", icon=":material/precision_manufacturing:")
risk_assess = st.Page("enhancements/risk_assess.py", title="Risk Assessment", icon=":material/precision_manufacturing:")
chatbot = st.Page("tools/chat.py", title="Chatbot", icon=":material/smart_toy:")

if st.session_state.logged_in:
    pg = st.navigation(
        {
            "Home": [home],
            "Reports": [dashboard],
            "Tools": [risk_analyser],
            "Enhancements": [alerts, eligibility, risk_assess, chatbot],
            "Logout": [logout_page]
        }
    )
else:
    pg = st.navigation([login_page])

pg.run()

