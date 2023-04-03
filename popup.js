chrome.storage.sync.get('ResponseData',function(Temp){
    console.log(Temp.ResponseData);
    document.querySelector('.title').textContent = Temp.ResponseData;

});

// Send a message to the background script
 /*chrome.runtime.sendMessage({ type: "sendToBackground", data: "Send the Result of prediction" }, function(response) {
    if (response.type === "responseFromBackground") {
      console.log(response.data); // output the message to the console
      document.querySelector('.title').textContent = response.data;
    }
  });*/
