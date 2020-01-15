let api_url = document.location.href.split("/");
api_url = "/itinerary/details/" + api_url[api_url.length - 1];

$.get(api_url, (response) => {
    response = JSON.parse(response);
    // response.name = "hi there";
    // response.date = "2020/01/14";

    $("#itineraryName").html(response.name);
    $("#itineraryDate").html(response.date);

    for(const event of response.events){
        console.log(event);
    }
});