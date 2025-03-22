import pandas as pd
import numpy as np

dates = pd.date_range(start='2024-03-01', end='2024-03-31')


np.random.seed(42)
temperature = np.random.normal(loc=15, scale=5, size=len(dates))
wind_speed = np.random.normal(loc=20, scale=5, size=len(dates))
humidity = np.random.uniform(low=30, high=90, size=len(dates))
electricity_price = (
    50 + 0.5 * temperature - 0.3 * wind_speed + 0.2 * humidity +
    np.random.normal(0, 5, size=len(dates))
)

df = pd.DataFrame({
    'Date': dates,
    'Temperature (°C)': temperature.round(1),
    'Wind Speed (km/h)': wind_speed.round(1),
    'Humidity (%)': humidity.round(1),
    'Electricity Price (€/MWh)': electricity_price.round(2)
})

# Guardar como CSV
df.to_csv('weather_electricity.csv', index=False)
