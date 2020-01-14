$.get("/itinerary/list", (response) => {
    for(const itinerary of response.itineraries){
        const name = itinerary.name;
        const id = itinerary.id;
        const date = itinerary.date;

        $("#itinerary-container").append($(`
          <a href="/itinerary/view" class="list-group-item list-group-item-action">${name} -- ${date}</a>
        `))
    }
});