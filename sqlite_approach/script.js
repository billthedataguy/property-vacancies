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
  var records = [];
  
  for (var i = 0; i < localStorage.length; i++) {
    var key = localStorage.key(i);
    var recordLocal = localStorage.getItem(key);
    
    if (recordLocal != null) {
      try {
        var recordJSON = JSON.parse(recordLocal);
        records.push(recordJSON);
      } catch (e) {
        console.error("Error parsing JSON for key:", key, e);
      }
    }  
  }
  
  // Convert records to CSV
  var csv = convertToCSV(records);
  
  // Trigger download
  downloadCSV(csv);
}

function convertToCSV(records) {
  if (records.length === 0) return '';
  
  var headers = Object.keys(records[0]).join(',') + '\n';
  var rows = records.map(record => 
    Object.values(record).map(value => 
      `"${value}"`
    ).join(',')
  ).join('\n');
  
  return headers + rows;
}

function downloadCSV(csv) {
  var blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
  var link = document.createElement("a");
  if (link.download !== undefined) {
    var url = URL.createObjectURL(blob);
    link.setAttribute("href", url);
    link.setAttribute("download", "property_records.csv");
    link.style.visibility = 'hidden';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  }
}