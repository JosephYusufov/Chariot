const orderOfEvents = [];

const tomorrow = new Date();
tomorrow.setDate(tomorrow.getDate() + 1);
document.getElementById("itineraryDate").min = tomorrow.toISOString().split('T')[0];

$("#create").on("click", (e) => {
    const itineraryName = $("#itineraryName").val();
    const itineraryDate = $("#itineraryDate").val();
    const timeStart = $("#timeStart").val();
    const timeEnd = $("#timeEnd").val();
    if(itineraryName.trim().length === 0){
        console.log(itineraryName);
        showMessage("Please enter a name for the itinerary", true);
        return;
    }
    if(itineraryDate.length === 0){
        showMessage("Please enter a date for the itinerary", true);
        return;
    }
    if(timeStart.length === 0){
        showMessage("Please set start time",true);
        return;
    }

    if(timeEnd.length === 0){
        showMessage("Please set end time",true);
        return;
    }

   $.post("/create-itinerary-create", {
       name: itineraryName,
       itineraryDate: itineraryDate,
       events: orderOfEvents,
       timeStart,
       timeEnd,

   }, () => showMessage("Successfully created!"));
});

$(".dropdown-item").on("click", (e) => {
    const eventToAdd = e.target.innerHTML;
    orderOfEvents.push(eventToAdd);
    $(`<div>${eventToAdd}</div>`).insertBefore(".dropdown");
});

const showMessage = (message, isError) => {
    console.log($("#error"));
    if($("#message").length !== 0){
        // error message is already showing, so just set text to it
        $("#message").remove();
    }
    $("#errorContainer").prepend($(
        `<div class="row">
            <div id="message" class="alert alert-${isError ? "danger" : "success"} alert-dismissible fade show" role="alert">
              ${message}
              <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
          </div>`
    ));
};