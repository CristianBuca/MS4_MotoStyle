// Client Side Form Validation is done with the Jquery Validate Plugin

// Custom validator methods for the app's specifications

// Uses regex to exclude empty strings
$.validator.methods.notEmptyString = function( value, element ) {
    return this.optional( element) || /^(?!\s*$).+/.test( value );
};

// Calls the validate method on the add stock Form
$('.add-stock-form').validate({
    // Validation Rules
    rules: {
        name: {
            minlength: 5,
            maxlength: 254,
            required: true,
            notEmptyString: true,
        },
        description: {
            minlength: 10,
            required: true,
            notEmptyString: true,
        },
        price: {
            required: true,
            number: true,
        },
    }
});