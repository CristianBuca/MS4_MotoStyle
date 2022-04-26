// Client Side Form Validation is done with the Jquery Validate Plugin

// Custom validator methods for the app's specifications

// Uses Regex to define email format
$.validator.methods.email = function( value, element ) {
    return this.optional( element ) || /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test( value );
};

// Uses regex to exclude empty strings
$.validator.methods.notEmptyString = function( value, element ) {
    return this.optional( element) || /^(?!\s*$).+/.test( value );
};

// Calls the validate method on the add stock Form
$('#signup_form').validate({
    // Validation Rules
    rules: {
        email: {
            required: true,
            notEmptyString: true,
            email: true,
        },
        email2: {
            required: true,
            notEmptyString: true,
            email: true,
            equalTo: '#id_email',
        },
        username: {
            required: true,
            minlength: 4,
            notEmptyString: true,
        },
        password: {
            required: true,
        },
        password2: {
            required: true,
            equalTo: '#id_password1',
        }
    },
    // Custom messages for custom validator method
    messages: {
        email2: {
            notEmptyString: "No empty strings please.",
            equalTo: "Email addresses do not match",
        }, 
        username: {
            notEmptyString: "No empty strings please.",
        },
        password2: {
            equalTo: "Passwords do not match",
        }
    },
});