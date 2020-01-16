let url_vector = document.location.href.split("/");
let id = url_vector[url_vector.length - 1];
let api_url = "/itinerary/details/" + id;

$("#delete").on("click", ()=>{
    $.get("/itinerary/delete/" + id, () => {
        $("#errorContent").append($(`
            <div id="message" class="alert alert-success alert-dismissible fade show w-100" role="alert">
              Deleting!
              <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
        `));
        setTimeout(() => {
            window.location.replace("/welcome");
        }, 3000); // 3 seconds
    });
});

$.get(api_url, (response) => {
    response = JSON.parse(response);
    // response.name = "hi there";
    // response.date = "2020/01/14";
    document.title = response.name;

    $("#startLocation").html("Start address " + response.startPoint);
    $("#startTime").html("Start time: " + response.startTime);
    // gives a list of string of addresses in order of event
    const destinations = [];
    let i = 1;
    for(const event of response.events){
        const timeStart = new Date(event.time_start);
        const timeEnd = new Date(event.time_end);

        destinations.push(event.address);
        const html = `
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">${i}. ${event.name}</h5>
            <ul class="list-group list-group-flush">
              <li class="list-group-item">Address: ${event.address}</li>
              <li class="list-group-item">Start: ${timeStart.getHours()}:${timeStart.getMinutes()}</li>
              <li class="list-group-item">End: ${timeEnd.getHours()}:${timeEnd.getMinutes()}</li>
            </ul>
          </div>
        </div>
        `;
        $("#events").append($(html));
        i++;
    }
});
    // -- start here
  window.onload = function() {
      var x = document.getElementById("demo");
      
      function getLocation() {
          if (navigator.geolocation) {
              navigator.geolocation.getCurrentPosition(showPosition);
          } else { 
              x.innerHTML = "Geolocation is not supported by this browser.";
          }
      }
      
      function showPosition(position) {
          x.innerHTML = "Latitude: " + position.coords.latitude + 
              "<br>Longitude: " + position.coords.longitude;
      }
      
      L.mapquest.key = 'yNjXSwjvcoWeXAoUiJw9AZG6MiUvjX8f';
      
      var map = L.mapquest.map('map', {
          center: [37.7749, -122.4194],
          layers: L.mapquest.tileLayer('map'),
          zoom: 12
      });

      map.addControl(L.mapquest.control());

      L.mapquest.directions().route({
          start: '350 5th Ave, New York, NY 10118',
          end: 'One Liberty Plaza, New York, NY 10006'
      });
  
      /*
      const startP = response.StartPoint;
      
      for(const eventP of destinations){
        L.mapquest.directions().route({
          start: startP,
          end: eventP
        });
        startP = eventP;
      }*/
  }
    // -- end her