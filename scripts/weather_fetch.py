import requests

# Define the API endpoint and parameters
download_url = """https://api.open-meteo.com/v1/forecast?latitude=49.265&longitude=-123.242&
                daily=temperature_2m_max,temperature_2m_min,sunrise,sunset&hourly=temperature_2m,
                apparent_temperature,precipitation_probability,precipitation,rain,showers,snowfall,
                snow_depth&models=best_match&current=temperature_2m,relative_humidity_2m,
                apparent_temperature,precipitation,rain,showers,snowfall,cloud_cover,
                wind_speed_10m&timezone=America%2FLos_Angeles&format=csv"""

# Make the API call
response = requests.get(download_url, headers={}, stream=True)

if response.status_code == 200:  # successful request
    with open("data/raw/weather/weather_data.csv", "wb") as f:
        for chunk in response.iter_content(8192):
            if chunk:
                f.write(chunk)
    print("Downloaded successfully!")
else:
    print(f"Failed to download. Status code: {response.status_code}")
    print("Response content (first 500 chars):")
    print(response.text[:500])

