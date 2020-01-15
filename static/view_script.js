let api_url = document.location.href.split("/");
api_url = "/itinerary/details/" + api_url[api_url.length - 1];

$.get(api_url, (response) => {
    response = JSON.parse(response);
    // response.name = "hi there";
    // response.date = "2020/01/14";

    $("#itineraryName").html(response.name);
    $("#itineraryDate").html(response.date);
    let i = 1;
    for(const event of response.events){
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
});