
document.addEventListener('DOMContentLoaded', function(){
    document.querySelectorAll('#plus').forEach(function(plus){
        plus.onclick = function(){
            var counter_item = plus.previousElementSibling;
            var counterNr = parseInt(counter_item.innerHTML);
            counter_item.innerHTML = ++counterNr;
        }
    });

    document.querySelectorAll('#minus').forEach(function(minus){
        minus.onclick = function(){
            var counter_item = minus.nextElementSibling;
            var counterNr = parseInt(counter_item.innerHTML);
            if(counterNr != 0){
                counter_item.innerHTML = --counterNr;
            }
        }
    })
});