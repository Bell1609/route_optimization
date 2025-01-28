# Route Optimization
# ![Route Optimization GIF](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExczZ1YnVuNm93aXpocGNtcTdtZTM3cmRmeWkzMXdwNW1ybGdydXQyNiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/2A29ghC2SEWYIYXGKt/giphy.gif)

An interactive Streamlit application for optimizing delivery routes efficiently.

## Overview

In an increasingly delivery-reliant world, route optimization differentiates mediocre delivery services from the best-in-class last mile carriers. Efficiently managing routes not only reduces operational costs but also enhances customer satisfaction through faster deliveries and optimized resource usage.

This application combines two powerful methods for route optimization:

- **Traveling Salesman Problem (TSP)**: A classic optimization problem that minimizes delivery distance and time in static environments.
- **OpenStreetMap Routing Services (OSRM)**: A real-time adaptable solution leveraging open-source map data for dynamic routing adjustments.

By integrating these methods, the application ensures both cost-effective and timely deliveries, adaptable to dynamic conditions like traffic and road closures.

## Features

- Static route optimization using TSP to minimize travel distance and time.
- Real-time route adjustments with OSRM for dynamic delivery scenarios.
- User-friendly interface powered by Streamlit.

## Demo

Try the live app here: [Route Optimization App](https://optimize-routes.streamlit.app/)

## Installation

1. Clone the repository:

    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit application:

    ```bash
    streamlit run main.py
    ```

## Usage

- Input delivery locations into the application.
- Select optimization criteria (e.g., minimize distance, adjust for traffic).
- View and download optimized routes for efficient deliveries.

## Technologies Used

- **Streamlit**: Interactive web application framework.
- **Python**: Core programming language.
- **OpenStreetMap (OSM)**: Open-source mapping data for routing.
- **TSP Algorithms**: Heuristic methods for solving static optimization problems.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## Credit & Licence & Citation
Copyright (c) 2025 Bell Tran.
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- OpenStreetMap contributors for providing open-source map data.
- The Streamlit community for making interactive applications accessible.

Feel free to contact us for any queries or suggestions!
