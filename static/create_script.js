const orderOfEvents = [];

const tomorrow = new Date();
tomorrow.setDate(tomorrow.getDate() + 1);
document.getElementById("itineraryDate").min = tomorrow.toISOString().split('T')[0];

$("#create").on("click", (e) => {
    const itineraryName = $("#itineraryName").val();
    const itineraryDate = $("#itineraryDate").val();
    const timeStart = $("#timeStart").val();
    const timeEnd = $("#timeEnd").val();
    const startPoint = $("#startPoint").val();
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
    if(startPoint.length === 0){
        showMessage("Please set start location",true);
        return;
    }

   $.post("/itinerary/create", {
       name: itineraryName,
       itineraryDate: itineraryDate,
       events: orderOfEvents.join(","),
       timeStart,
       timeEnd,
       startPoint,
   }, (response) => {
       if(response.error !== undefined){
           // there is an error
           if(response.error === "location"){
               showMessage("Invalid location", true);
           }else if(response.error === "time"){
               showMessage("Make sure end time is after start time", true);
           }
       }else{
           showMessage("Successfully created! Redirecting...", false);
           setTimeout(() => {
               window.location.replace("/welcome");
           }, 3000); // 3 seconds

       }
   });
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
        `
            <div id="message" class="alert alert-${isError ? "danger" : "success"} alert-dismissible fade show w-100" role="alert">
              ${message}
              <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>`
    ));
};