import streamlit as st
import requests


url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')


date = st.date_input("Date")
time = st.time_input("Time")
pickup_longitude = st.number_input("Pickup Longitude")
pickup_latitude = st.number_input("Pickup Latitude")
dropoff_longitude = st.number_input("Dropoff Longitude")
dropoff_latitude = st.number_input("Dropoff Latitude")
passenger_count = st.number_input("Passenger Count", min_value=1)

pickup_datetime = f"{date} {time}"

dict_API_keys = {
    'pickup_datetime': pickup_datetime,
    'pickup_longitude': pickup_longitude,
    'pickup_latitude': pickup_latitude,
    'dropoff_longitude': dropoff_longitude,
    'dropoff_latitude': dropoff_latitude,
    'passenger_count': passenger_count
}

if st.button('click me'):
    # print is visible in the server output, not in the page
    print('button clicked!')
    try:
        response = requests.get(url, params=dict_API_keys)
        prediction = response.json()['fare']
        st.success(f"Predicted Fare: ${prediction:.2f}")

    except requests.exceptions.RequestException as e:
        st.error("Failed to retrieve prediction from the API")

