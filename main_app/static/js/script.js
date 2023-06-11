if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
        function(position) {
            const latitude = position.coords.latitude;
            const longitude = position.coords.longitude;
            // Get the event date from the HTML element
            const eventDate = document.getElementById('event-date').className;

            // Get the user's timezone
            const userTimezone = Intl.DateTimeFormat().resolvedOptions().timeZone;
            console.log('User Timezone:', userTimezone);
            
            // Use the latitude and longitude values
            console.log('Latitude:', latitude);
            console.log('Longitude:', longitude);

            // Make the AJAX request to the weather forecast API
            $.ajax({
                url: `https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,precipitation_probability_max&temperature_unit=fahrenheit&windspeed_unit=mph&precipitation_unit=inch&forecast_days=1&start_date=${eventDate}&end_date=${eventDate}&timezone=${userTimezone}`,
                method: 'GET',
                success: function(response) {
                    // Extract the relevant weather forecast data from the response
                    console.log('Weather forecast API response:', response);
                    const forecastData = response.daily;
                    console.log('Forecast Data: ', forecastData)
                    console.log('Precipitation Sum: ', forecastData.precipitation_sum)

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
        function(error) {
            // Handle error if location retrieval fails
            console.error('Error getting location:', error);
        }
    );
} else {
    // Geolocation is not supported by the browser
    console.error('Geolocation is not supported');
}