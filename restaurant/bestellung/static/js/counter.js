var productId;
var action;

document.addEventListener('DOMContentLoaded', function(){

    document.querySelectorAll('#plus').forEach(function(plus){
         plus.onclick = function(){
            var counter_item = plus.previousElementSibling;
            var counterNr = parseInt(counter_item.innerHTML);
            counter_item.innerHTML = ++counterNr;
            productId = this.dataset.product;
            action = this.dataset.action;
            updateUserOrder(productId,action);
        }
    });

    document.querySelectorAll('#minus').forEach(function(minus){
        minus.onclick = function(){
            var counter_item = minus.nextElementSibling;
            var counterNr = parseInt(counter_item.innerHTML);
            if(counterNr != 0){
                counter_item.innerHTML = --counterNr;
                productId = this.dataset.product;
                action = this.dataset.action;
                updateUserOrder(productId,action);
            }
        }
    })
});

function updateUserOrder(productId,action){
    var url = '/bestellung/einkaufskorb/';
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'productId':productId, 'action':action})
    })
    .then((response) => {
        return response.json()
    })
    .then((data) => {
        console.log('data:', data);
    })
}