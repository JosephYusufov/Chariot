const orderOfEvents = [];

$("#create").on("click", (e) => {
    const itineraryName = $("#itineraryName").html();
    if(itineraryName.trim().length === 0){
        $(".container").prepend($(""));
        showError("Please enter a name for the itinerary");
    }

   $.post("/create-itinerary-create", {
        name: itineraryName,
        itineraryDate: $("#itineraryDate").val(),
        events: orderOfEvents,
   });
});

$(".dropdown-item").on("click", (e) => {
    const eventToAdd = e.target.innerHTML;
    orderOfEvents.push(eventToAdd);
    $(`<div>${eventToAdd}</div>`).insertBefore(".dropdown");
});

const showError = (errorMessage) => {
    console.log($("#error"));
    if($("#error").length !== 0){
        // error message is already showing, so just set text to it
        $("#error").remove();
    }
    $("#errorContainer").prepend($(
        `<div class="row">
            <div id="error" class="alert alert-danger alert-dismissible fade show" role="alert">
              ${errorMessage}
              <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
          </div>`
    ));
};