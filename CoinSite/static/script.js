function showNetWorth(button, symbol) {
    var netWorth = button.nextElementSibling;
    var netWorthElement = document.getElementById(symbol + '-worth');

    // Fetch the real-time net worth
    fetchRealTimeNetWorth(symbol)
        .then(function (realTimeNetWorth) {
            netWorthElement.textContent = realTimeNetWorth + " $";
            netWorth.classList.toggle('hidden');
        })
        .catch(function (error) {
            console.log("Error fetching net worth:", error);
        });
}

function fetchRealTimeNetWorth(symbol) {
    return new Promise(function (resolve, reject) {
        var xhr = new XMLHttpRequest();
        xhr.open('GET', '/get_realtime_price?symbol=' + symbol, true);
        xhr.onload = function () {
            if (xhr.status === 200) {
                resolve(xhr.responseText);
            } else {
                reject(new Error("Request failed. Status: " + xhr.status));
            }
        };
        xhr.onerror = function () {
            reject(new Error("Request failed. Network error."));
        };
        xhr.send();
    });
}
