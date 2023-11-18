function initMap()
      {
        var options = {
          zoom: 12,
          center: { lat: 46.7715124, lng:23.6213963 },
        };
        var map = new google.maps.Map(document.getElementById('map'), options);
        var marker = new google.maps.Marker({
          position: { lat: 46.7821964, lng: 23.614196 },
          map: map,
        });
        var marker2 = new google.maps.Marker({
          position: { lat: 46.7576976, lng: 23.6088566 },
          map: map,
        });
      }