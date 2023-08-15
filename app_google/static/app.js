function initMap(){

    // Map option

    var options = {
        center: { lat: {{ restaurants.0.lat }} , lng:{{ restaurants.0.lng }} },
        zoom: 10
   }

    //New Map
    map = new google.maps.Map(document.getElementById("map"),options)

    //listen for click on map location

    google.maps.event.addListener(map, "click", (event) => {
        //add Marker
        addMarker({location:event.latLng});
    })


    // Add marker
    {% for restaurant in restaurants %}
          var marker = new google.maps.Marker({
            position: {lat: {{ restaurant.lat }}, lng: {{ restaurant.lng }}},
            map: map,
            title: '{{ restaurant.name }}'
          });

        {% endfor %}


}

