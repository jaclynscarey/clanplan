let latitude;
let longitude;

let address = document.getElementById('location').innerText;
$.ajax({
    url: `http://api.positionstack.com/v1/forward?access_key=8a5d31dbe90b21bd5c1adc90f3d07997&query=${address}`,
    method: 'GET',
    success: function(response) {
        const locationData = response.data[0];
        console.log('Location Data:', locationData);

        latitude = locationData.latitude;
        longitude = locationData.longitude;
        console.log('Latitude:', latitude);
        console.log('Longitude:', longitude);

        // Get the event date from the HTML element
        const eventDate = document.getElementById('event-date').className;

        // Get the user's timezone
        const userTimezone = Intl.DateTimeFormat().resolvedOptions().timeZone;
        console.log('User Timezone:', userTimezone);

        if (latitude === undefined || longitude === undefined) {
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(
                    function(position) {
                        latitude = position.coords.latitude;
                        longitude = position.coords.longitude;
            
                        // Use the latitude and longitude values
                        console.log('Latitude:', latitude);
                        console.log('Longitude:', longitude);
                    },
                    function(error) {
                        // Handle error if location retrieval fails
                        console.error('Error getting location:', error);
                    }
                );
            };
        };

        // Make the AJAX request to the weather forecast API
        $.ajax({
            url: `https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,precipitation_probability_max&temperature_unit=fahrenheit&windspeed_unit=mph&precipitation_unit=inch&forecast_days=1&start_date=${eventDate}&end_date=${eventDate}&timezone=${userTimezone}`,
            method: 'GET',
            success: function(response) {
                // Extract the relevant weather forecast data from the response
                console.log('Weather forecast API response:', response);
                const forecastData = response.daily;

                // Update the weather-forecast element in the detail.html page with the forecast data
                const weatherForecastElement = document.getElementById('weather-forecast');
                weatherForecastElement.innerHTML = `
                    <span class="card-title">Weather Forecast</span>
                    <p>Max Temperature: ${forecastData.temperature_2m_max[0]} °F</p>
                    <p>Min Temperature: ${forecastData.temperature_2m_min[0]} °F</p>
                    <p>Precipitation Probability: ${forecastData.precipitation_probability_max[0]}%</p>
                    <p>Precipitation Total: ${forecastData.precipitation_sum[0]}"</p>
                `;
            },
            error: function(xhr, status, error) {
                console.error('AJAX request failed. Status:', status);
                console.error('Error:', error);
            }
        });
    },
    error: function(xhr, status, error) {
        console.error('AJAX request failed. Status:', status);
        console.error('Error:', error);
    }
});
