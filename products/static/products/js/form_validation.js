// Client Side Form Validation is done with the Jquery Validate Plugin

// Custom validator methods for the app's specifications

// Uses regex to exclude empty strings
$.validator.methods.notEmptyString = function( value, element ) {
    return this.optional( element ) || /^(?!\s*$).+/.test( value );
};

// Calls the validate method on the add stock form
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
        rating: {
            range: [0, 5]
        }
    },
    // Custom messages for custom validator method
    messages: {
        name: {
            notEmptyString: 'No empty strings please.',
        }, 
        description: {
            notEmptyString: 'No empty strings please.',
        },      
    },
});

// Calls the validate method on the edit stock form
$('.edit-product-form').validate({
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
        rating: {
            range: [0, 5]
        },
    },
    // Custom messages for custom validator method
    messages: {
        name: {
            notEmptyString: 'No empty strings please.',
        }, 
        description: {
            notEmptyString: 'No empty strings please.',
        },      
    },
});

// Calls the validate method on the review form
$('#reviewModal').find('form').validate({
    // Validation Rules
    rules: {
        comment: {
            notEmptyString: true,
        }
    },
    messages: {
        comment: {
            notEmptyString: 'No empty strings please.',
        },
    },
})