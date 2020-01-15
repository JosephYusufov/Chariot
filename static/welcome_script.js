$.get("/itinerary/list", (response) => {
    response = JSON.parse(response);
    console.log(response);
    for(const itinerary of response.itinerary){
        const name = itinerary.name;
        const id = itinerary.id;
        const date = itinerary.date;

        $("#itinerary-container").append($(`
          <a href="/itinerary/${id}" class="list-group-item list-group-item-action">${name} -- ${date}</a>
        `))
    }
});