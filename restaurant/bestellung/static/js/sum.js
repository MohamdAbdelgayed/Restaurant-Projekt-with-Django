$(document).ready(function(){
    var total;
    var sum = 0;
    $('.total').each(function(){
        total = parseFloat((this).innerHTML);
        sum+= total;
    });
     $('#summ').text(sum.toFixed(2)+' €')
});