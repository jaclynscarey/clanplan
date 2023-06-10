if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
        function(position) {
            var latitude = position.coords.latitude;
            var longitude = position.coords.longitude;

            // Use the latitude and longitude values
            console.log('Latitude:', latitude);
            console.log('Longitude:', longitude);
            
            // You can send them to your API or perform other operations
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