// Control for the card slider on index page
// Credit to Paul Phillips: https://codepen.io/pau1phi11ips/pen/rKyGzq

$('.toggle-all').on('click', function() {
    $('#infinite_carousel .row').toggleClass('flex-nowrap');
    $('#infinite_carousel .control').toggleClass('d-none');
});

$('#infinite_carousel .fa-chevron-right').on('click', () => {
    let $infinite_carousel_row = $('#infinite_carousel .row');
    let $col = $infinite_carousel_row.find('.col-12:first');
    $infinite_carousel_row.append($col[0].outerHTML);
    $col.remove();
    });

$('#infinite_carousel .fa-chevron-left').on('click', () => {
    let $infinite_carousel_row = $('#infinite_carousel .row');
    let $col = $infinite_carousel_row.find('.col-12:last');
    $infinite_carousel_row.prepend($col[0].outerHTML);
    $col.remove();
});