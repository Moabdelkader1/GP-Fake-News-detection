// Creating the context menu item 


var contextMenuItem = {
  id: "Fakes",
  title: "Detect Speech credibility",
  contexts: ["selection"]
};

chrome.contextMenus.create(contextMenuItem);

// Events when the context menu is clicked
chrome.contextMenus.onClicked.addListener(function(info,tab){
  // Get the URL of the current page
  chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
    var currentUrl = tabs[0].url;
    console.log(currentUrl);
    chrome.storage.sync.get('UrlOfSelectedData' , function(history){
      var url = history.UrlOfSelectedData || [];
      if (!Array.isArray(url)) {
        url = [url];
      }
      url.push(currentUrl)
    
      chrome.storage.sync.set({'UrlOfSelectedData': url})
    
    });})

// Define the data to send
var data = {text: info.selectionText};
//chrome.storage.sync.set({'SelectedData': data});
chrome.storage.sync.get('SelectedData' , function(history){
  var historySelected = history.SelectedData || [];
  if (!Array.isArray(historySelected)) {
    historySelected = [historySelected];
  }
  historySelected.push(data)

  chrome.storage.sync.set({'SelectedData': historySelected})




});


// Send the request using fetch
fetch('http://localhost:5000/predict', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(data)
})
.then(response => response.json())
.then(data => {
  
  // Listen for messages from the popup script
chrome.storage.sync.get('ResponseData' , function(history){
  var historyResult = history.ResponseData || [];
  if (!Array.isArray(historyResult)) {
    historyResult = [historyResult];
  }
  console.log(data.result) 
  historyResult.push(data.result)
  console.log(historyResult)
  chrome.storage.sync.set({'ResponseData': historyResult})
  chrome.storage.sync.set({'ResponseDataTemp': data.result})



});

var notif = {
  type: 'basic',
  iconUrl: 'assets/find48.png',
  title: data.result ,
  message: "this data is" +" "+ data.result 
};
chrome.notifications.create(notif,function(){

});






})
.catch(error => console.error(error));
}); 
