let latitude;
let longitude;

// Function to handle weather forecast retrieval
async function getWeatherForecast(latitude, longitude) {
    // Get the event date from the HTML element
    const eventDate = document.getElementById('event-date').className;

    // Get the user's timezone
    const userTimezone = Intl.DateTimeFormat().resolvedOptions().timeZone;
    console.log('User Timezone:', userTimezone);

    try {
        // Make the fetch request to the weather forecast API
        const response = await fetch(`https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,precipitation_probability_max&temperature_unit=fahrenheit&windspeed_unit=mph&precipitation_unit=inch&forecast_days=1&start_date=${eventDate}&end_date=${eventDate}&timezone=${userTimezone}`);
        
        if (!response.ok) {
        throw new Error('Weather forecast API request failed');
    }

    const data = await response.json();
    console.log('Weather forecast API response:', data.daily);
    const forecastData = data.daily;

    // Update the weather-forecast element in the detail.html page with the forecast data
    const weatherForecastElement = document.getElementById('weather-forecast');
    weatherForecastElement.innerHTML = `
        <p class="card-text">Max Temperature: ${forecastData.temperature_2m_max[0]} °F</p>
        <p class="card-text">Min Temperature: ${forecastData.temperature_2m_min[0]} °F</p>
        <p class="card-text">Precipitation Probability: ${forecastData.precipitation_probability_max[0]}%</p>
        <p class="card-text">Precipitation Total: ${forecastData.precipitation_sum[0]}"</p>
    `;
    } catch (error) {
        console.error('Fetch request failed. Error:', error);
    }
}

async function getAddressLocation(address) {
    // Replace all spaces in address with +
    const formattedAddress = address.trim().replace(/ /g, '+');
    console.log('Formatted Address:', formattedAddress);

    try {
        const response = await fetch(`https://geocode.maps.co/search?q=${formattedAddress}`);
        
        if (!response.ok) {
        throw new Error('Geolocation API request failed');
        }

        const data = await response.json();
        const locationData = data[0];
        console.log('Location Data:', locationData);

        if (locationData === undefined) {
            // Use browser's geolocation
            const position = await getCurrentPosition();
            latitude = position.coords.latitude;
            longitude = position.coords.longitude;

            console.log('Browser Latitude Inside Address Fetch:', latitude);
            console.log('Browser Longitude Inside Address Fetch:', longitude);
        } else {
            latitude = locationData.lat;
            longitude = locationData.lon;
            console.log('Address Latitude:', latitude);
            console.log('Address Longitude:', longitude);
        }

        // Call the function to fetch weather forecast
        getWeatherForecast(latitude, longitude);
    } catch (error) {
        console.error('Fetch request failed. Error:', error);
    }
}

function getCurrentPosition() {
    return new Promise((resolve, reject) => {
        navigator.geolocation.getCurrentPosition(resolve, reject);
    });
}

// Check if address is available
const address = document.getElementById('location').innerText;

if (address) {
    getAddressLocation(address);
} else {
    // Fallback to browser's geolocation
    if (navigator.geolocation) {
        getCurrentPosition()
        .then(position => {
            latitude = position.coords.latitude;
            longitude = position.coords.longitude;

            console.log('Browser Latitude:', latitude);
            console.log('Browser Longitude:', longitude);

            // Call the function to fetch weather forecast
            getWeatherForecast(latitude, longitude);
        })
        .catch(error => {
            console.error('Error getting location:', error);
        });
    } else {
        latitude = 40.782864;
        longitude = -73.965355;
        console.log('Central Park Latitude:', latitude);
        console.log('Central Park Longitude:', longitude);
    }
}
