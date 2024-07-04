import requests

# API endpoint and your API key
api_key = "6fd6fb85a557a160626a2c850795d2b9"
city_name = "jimma"
api_url = f"https://api.openweathermap.org/data/2.5/weather?&units=metric&q=jimma"

# Make the request to the API
response = requests.get(api_url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data from the response
    data = response.json()

    # Extract the relevant weather information
    weather_description = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]

    # Print the weather information
    print(f"Current weather in {city_name}: {weather_description}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
else:
    print(f"Error: {response.status_code} - {response.text}")