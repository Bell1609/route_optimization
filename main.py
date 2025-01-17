import streamlit as st
import hydralit_components as hc

from navigation.home import home_page
from navigation.tsp_optimizer import main
from navigation.osrm_optimizer import trip_optimizer
from navigation.contact import contact_page

# Set page configuration and title
st.set_page_config(
    page_title='Route Optimization',
    page_icon="img/logo_page.png",
)

# Navigation Tabs
HOME = 'Home'
TSP = 'TSP Optimizer'
OSRM = 'OSRM Optimizer'
CONTACT = 'Contact'

tabs = [HOME, TSP, OSRM, CONTACT]

option_data = [
    {'icon': "🏠", 'label': HOME},
    {'icon': "🌍", 'label': TSP},
    {'icon': "🛠️", 'label': OSRM},
    {'icon': "👋", 'label': CONTACT},
]

over_theme = {'txc_inactive': 'black', 'menu_background': '#D6E5FA', 'txc_active': 'white', 'option_active': '#749BC2'}

# Create a Hydralit Tabs widget
chosen_tab = hc.option_bar(
    option_definition=option_data,
    title='',
    key='PrimaryOptionx',
    override_theme=over_theme,
    horizontal_orientation=True
)

# Welcome message
st.success("Welcome to the Route Optimization application! This platform is designed to help you efficiently plan and optimize routes for your deliveries. "
           "Thank you for using the app, and I'm excited to assist you in making your trips faster, more cost-effective, and optimized! 🥰")

# Display the page based on selected tab
if chosen_tab == HOME:
    home_page()
elif chosen_tab == TSP:
    main()
elif chosen_tab == OSRM:
    trip_optimizer()
elif chosen_tab == CONTACT:
    contact_page()

# Footer
footer = """<footer style="text-align: center;">Bell Tran © 2025</footer>"""
for _ in range(4):
    st.markdown('#')
st.markdown(footer, unsafe_allow_html=True)

