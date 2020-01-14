let api_url = document.location.href.split("/");
api_url = "/itinerary/details/" + api_url[api_url.length - 1];

$.get(api_url, (response) => {
    $("#itineraryName").html(response.name);
    $("#itineraryDate").val(response.date);

    for(const event of response.events){

        console.log(event);

    }
});