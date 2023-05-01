// Creating the context menu item 
chrome.runtime.onInstalled.addListener(() => {
  console.log("This is coming from the background script");

  var contextMenuItem = {
    id: "Fake",
    title: "Detect Speech credibility",
    contexts: ["selection"]
  };

  chrome.contextMenus.create(contextMenuItem);
});

// Events when the context menu is clicked
chrome.contextMenus.onClicked.addListener(function(info,tab){
  // Define the data to send
  var data = {text: info.selectionText};

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

  chrome.storage.sync.set({'ResponseData': data.result});
  var notif = {
    type: 'basic',
    iconUrl: 'assets/find48.png',
    title: data.result ,
    message: "This article is" +" "+ data.result 
  };
  chrome.notifications.create(notif,function(){

  });

 

})
  .catch(error => console.error(error));
}); 