$('#new_image').change(function() {
    var file = $('#new_image')[0].files[0];
    $('#image_file').text(`Image will be set to: ${file.name}`);
});
$('#new_second_image').change(function() {
    var file = $('#new_second_image')[0].files[0];
    $('#second_image_file').text(`Image will be set to: ${file.name}`);
});
$('#new_third_image').change(function() {
    var file = $('#new_third_image')[0].files[0];
    $('#third_image_file').text(`Image will be set to: ${file.name}`);
});
$('#new_fourth_image').change(function() {
    var file = $('#new_fourth_image')[0].files[0];
    $('#fourth_image_file').text(`Image will be set to: ${file.name}`);
});
$('#new_fifth_image').change(function() {
    var file = $('#new_fifth_image')[0].files[0];
    $('#fifth_image_file').text(`Image will be set to: ${file.name}`);
});