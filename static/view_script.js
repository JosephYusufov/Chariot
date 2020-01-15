let url_vector = document.location.href.split("/");
let id = url_vector[url_vector.length - 1];
let api_url = "/itinerary/details/" + id;

$("#delete").on("click", ()=>{
    $.get("/itinerary/delete/" + id);
    setTimeout(() => {
        window.location.replace("/welcome");
    }, 3000); // 3 seconds
});

$.get(api_url, (response) => {
    response = JSON.parse(response);
    // response.name = "hi there";
    // response.date = "2020/01/14";

    $("#itineraryName").html(response.name);
    $("#itineraryDate").html(response.date);
    // gives a list of string of addresses in order of event
    const destinations = [];
    let i = 1;
    for(const event of response.events){
        destinations.push(event.address);
        const html = `
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">${i}. ${event.name}</h5>
            <ul class="list-group list-group-flush">
              <li class="list-group-item">Address: ${event.address}</li>
              <li class="list-group-item">Start: ${event.time_start}</li>
              <li class="list-group-item">End: ${event.time_end}</li>
            </ul>
          </div>
        </div>
        `;
        $("#events").append($(html));
        i++;
    }

    // where the user starts the itinerary
    const startLocation = response.startPoint;


    // -- start here

    // -- end her
});