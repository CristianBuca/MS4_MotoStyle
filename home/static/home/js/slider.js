// Control for the card slider on index page
// Original code byPaul Phillips: https://codepen.io/pau1phi11ips/pen/rKyGzq
// Modified to fit this project's purpose

$('#infinite-carousel .control-right').on('click', () => {
    let $infinite_carousel_row = $('#infinite-carousel .row');
    let $col = $infinite_carousel_row.find('.col-12:first');
    $infinite_carousel_row.append($col[0].outerHTML);
    $col.remove();
    });

$('#infinite-carousel .control-left').on('click', () => {
    let $infinite_carousel_row = $('#infinite-carousel .row');
    let $col = $infinite_carousel_row.find('.col-12:last');
    $infinite_carousel_row.prepend($col[0].outerHTML);
    $col.remove();
});