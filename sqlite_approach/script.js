// This is the onclick function that runs when the user clicks the ADD TO DATABASE button

function processData() {

  var propertyId = document.querySelector("#propertyId").value;
  var videoTourUrl = document.querySelector("#videoTourUrl").value;
  var picsUrl = document.querySelector("#picsUrl").value;  
  var vacancyStatus = document.querySelector("#vacancyStatus").value;
  var resultsDiv = document.querySelector("#resultsDiv");

  const now = new Date().toLocaleDateString(); 
   
  // Write the results to the div 

  var recordString = "(" + propertyId  + ", " + videoTourUrl  + ", " + picsUrl  + ", " + vacancyStatus + ")";

  var recordObject = {
      "propertyId": propertyId, 
      "videoTourUrl": videoTourUrl, 
      "picsUrl": picsUrl,
      "vacancyStatus": vacancyStatus  
  };
    
  var recordJSON = JSON.stringify(recordObject);

  // store record in localstorage
  localStorage.setItem(now + "_" + propertyId, recordJSON);

  // resultsDiv.innerHTML += "<br>Record as string: " + recordString;

  // resultsDiv.innerHTML += "<br>Record as object: " + recordObject + " (see in console)";
  // console.log(recordObject);

  // resultsDiv.innerHTML += "<br>Record as JSON: " + recordJSON;
  
}

function reportData() {

  var resultsDiv = document.querySelector("#resultsDiv");
  var recordLocalStored;
  
  for (var i=0; i<=localStorage.length; i++) {

    console.log(localStorage.length);

    recordLocalStored = localStorage.getItem(localStorage.key(i));
    
    if (recordLocalStored != null) {

      resultsDiv.innerHTML += "<br>" + recordLocalStored;

    }  

  }  
  
}

function wipeData() {

  localStorage.clear();
  location.reload();
  
}

function saveData() {

  var recordLocal;
  
  for (var i=0; i<=localStorage.length; i++) {

    recordLocal = localStorage.getItem(localStorage.key(i));
    
    if (recordLocal != null) {

      console.log("RECORD #: " + localStorage.key(i) + " " + recordLocal);
      
    }  
  
  }
}