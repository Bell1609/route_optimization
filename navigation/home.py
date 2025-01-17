import streamlit as st

def home_page():
    st.divider()
    st.markdown(
        "<h3 style='text-align: center; color: black;'>🛣️Route Optimization🛣️</h1>",
        unsafe_allow_html=True)
    with open('./clock.time', 'r') as f:
        last_updated_on = f.readlines()[0]
    st.caption(last_updated_on)
    st.markdown('') 
    st.image('img/trip.jpg', use_container_width=True)  
    st.markdown('')  
    st.markdown('**Overview**')
    
    # First paragraph of overview
    st.markdown(
        '<div style="text-align: justify;">In an increasingly delivery-reliant world, route optimization differentiates mediocre delivery services from the best-in-class last mile carriers. Efficiently managing routes not only reduces operational costs but also enhances customer satisfaction through faster deliveries and optimized resource usage.</div>',
        unsafe_allow_html=True)
    st.markdown('') 
    
    # Explanation of methods used for route optimization
    st.markdown(
        '<div style="text-align: justify;">To achieve optimal routing, I will employ two methods:</div>',
        unsafe_allow_html=True)
    
    # The Traveling Salesman Problem
    st.markdown(
        '<div style="text-align: justify;"><b>➖The Traveling Salesman Problem (TSP):</b> The TSP is one of the most well-known optimization problems in computer science. The goal is to find the shortest possible route that visits each location exactly once and then returns to the starting point, forming a cycle. The primary challenge is to explore all potential paths and identify the one with the minimum distance or time. In delivery route optimization, TSP helps reduce fuel consumption, vehicle wear, and delivery time by ensuring that each stop is made in the most efficient sequence.</div>',
        unsafe_allow_html=True)
    
    # Details of the Traveling Salesman Problem
    st.markdown(
        '<div style="text-align: justify;">TSP is a classic NP-hard problem, meaning there is no known polynomial-time solution for large numbers of locations. However, approximation algorithms, like greedy algorithms, genetic algorithms, or simulated annealing, are used to find near-optimal solutions in a reasonable time frame. While TSP guarantees a theoretically optimal solution, in practice, heuristic or approximation methods are often used to handle larger datasets.</div>',
        unsafe_allow_html=True)
    
    st.markdown('') 
    
    # OpenStreetMap Routing Services (OSRM)
    st.markdown(
        '<div style="text-align: justify;"><b>➖OpenStreetMap Routing Services (OSRM):</b> OSRM leverages OpenStreetMap (OSM) data, which is an open-source map of the world, to calculate optimal routes in real-time. OSM data includes streets, points of interest, geographical features, and more, all of which can be used by routing algorithms to compute the best route for a specific journey. In the context of delivery, this method can dynamically adjust the route based on real-time factors like traffic, road closures, accidents, and weather conditions.</div>',
        unsafe_allow_html=True)
    
    # Details of OpenStreetMap Routing Services (OSRM)
    st.markdown(
        '<div style="text-align: justify;">Unlike TSP, which focuses on static route optimization, OSRM provides real-time adaptability. OSRM algorithms, such as Dijkstra’s or A*, utilize a vast network of roads and intersections to calculate the shortest path between two or more points. It accounts for time-varying conditions such as road closures, congestion, or accidents, making it ideal for dynamic last-mile delivery routing. By using OSM and real-time data, OSRM can suggest the most efficient route under current conditions, ensuring that deliveries are made as quickly as possible.</div>',
        unsafe_allow_html=True)
    
    st.markdown('') 
    
    # Conclusion combining both methods
    st.markdown(
        '<div style="text-align: justify;">By combining these two methods—TSP for static route optimization and OSRM for real-time adjustments we can build a robust system capable of efficiently managing last-mile delivery logistics, ensuring that deliveries are both cost-effective and timely. TSP offers the advantage of minimizing distance and time in a static environment, while OSRM ensures that routes remain optimal under constantly changing traffic conditions, road closures, and other dynamic factors.</div>',
        unsafe_allow_html=True)

    st.divider()  
