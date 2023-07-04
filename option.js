

document.addEventListener("DOMContentLoaded", function () {
    chrome.storage.sync.get(['SelectedData', 'ResponseData', 'UrlOfSelectedData'], function (history) {
        var selectedDataa = history.SelectedData || [];
        var responseDataa = history.ResponseData || [];
        var UrlDataa = history.UrlOfSelectedData || [];
        //console.log(responseDataa);
        // Populate the history list on the HTML page
        var historyList = document.getElementById("history-list");

        // Iterate over selectedData and responseDate arrays
        for (var i = 0; i < selectedDataa.length; i++) {
            if (i == 0) {
                var historyentered = document.getElementById("historyentered");
                historyentered.style.display = "none";
            }
            var listItem = document.createElement("li");
            listItem.style.width = "1450px"; // Set the width to 1450 pixels
            listItem.style.height = "15px"; // Set the height to 15 pixels
            var responseData = responseDataa[i];
            var selectedData = selectedDataa[i].text;
            var CurrentUrl = UrlDataa[i];
            //console.log(responseData);

            // Create left and right spans for the row
            var leftSpan = document.createElement("span");
            leftSpan.className = "speech";
            //leftSpan.textContent = selectedData;
            leftSpan.style.overflow = "hidden"; // Hide any overflowing content
            leftSpan.style.textOverflow = "ellipsis"; // Truncate the text with ellipsis
            leftSpan.style.whiteSpace = "nowrap"; // Prevent line breaks
            leftSpan.style.display = "flex";
            leftSpan.style.alignItems = "center"; // Center vertically
            leftSpan.style.justifyContent = "center"; // Center horizontall
            // Create an anchor element as a child of the leftSpan
            var linkElement = document.createElement("a");
            linkElement.href = CurrentUrl; // Set the href to the currentUrl
            linkElement.textContent = selectedData; // Set the text content
            linkElement.style.textDecoration = "none";

            leftSpan.appendChild(linkElement);



            var rightSpan = document.createElement("span");
            rightSpan.className = "credibility";
            rightSpan.style.fontSize = "16px"; // Set the font size to a larger value
            rightSpan.style.fontWeight = "bold"; // Make the text bold
            rightSpan.style.display = "flex"; // Use flexbox for centering
            rightSpan.style.alignItems = "center"; // Center vertically
            rightSpan.style.justifyContent = "center"; // Center horizontall
            rightSpan.textContent = responseData;

            // Check if responseData contains "fake" or "authentic" and set inline styles
            if (responseData.includes("Fake")) {
                rightSpan.style.color = "red";
            } else if (responseData.includes("Authentic")) {
                rightSpan.style.color = "green";
            }

            // Append left and right spans to the list item
            listItem.appendChild(leftSpan);
            listItem.appendChild(rightSpan);
            historyList.appendChild(listItem);

        }

    });
    var HistoryButton = document.getElementById("clearHistory");
    HistoryButton.addEventListener('click', function () {
        chrome.storage.sync.set({ 'SelectedData': [] });
        chrome.storage.sync.set({ 'ResponseData': [] });
        chrome.storage.sync.set({ 'UrlOfSelectedData': [] });
        location.reload();
        var historyentered = document.getElementById("historyentered");
        historyentered.style.display = "Block";
    })
});
