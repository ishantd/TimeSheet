$(function(){
    $.validator.setDefaults({
        errorClass: "invalid-feedback",
        highlight: function(element) {
            $(element)
            .closest('.form-control')
            .addClass('is-invalid')
            .removeClass('is-valid');
        },
        unhighlight: function(element) {
            $(element)
            .closest('.form-control')
            .removeClass('is-invalid')
            .addClass('is-valid');
        }
    }),
    
    $.validator.addMethod('totalHours', function(value, element) {
        return parseInt(value)==8;
    },'The total number of working should be equal to 8');

    $("#dep_form").validate({  
        rules: {
            Process: {
                required: true,
                digits: true
            },
            Structure: {
                required: true,
                digits: true
            },
            Piping: {
                required: true,
                digits: true
            },
            Instrumentation: {
                required: true,
                digits: true
            },
            Electrical: {
                required: true,
                digits: true
            },
            Projects: {
                required: true,
                digits: true
            },
            Mechanical: {
                required: true,
                digits: true
            },
            Quality: {
                required: true,
                digits: true
            },
            Documentation: {
                required: true,
                digits: true
            },
            Planning: {
                required: true,
                digits: true
            },
        },
        messages: {
            Process: {
                required: "This field is required",
                digits: "You can only enter digits"
            },
            Structure: {
                required: "This field is required",
                digits: "You can only enter digits"
            },
            Piping: {
                required: "This field is required",
                digits: "You can only enter digits"
            },
            Instrumentation: {
                required: "This field is required",
                digits: "You can only enter digits"
            },
            Electrical: {
                required: "This field is required",
                digits: "You can only enter digits"
            },
            Projects: {
                required: "This field is required",
                digits: "You can only enter digits"
            },
            Mechanical: {
                required: "This field is required",
                digits: "You can only enter digits"
            },
            Quality: {
                required: "This field is required",
                digits: "You can only enter digits"
            },
            Documentation: {
                required: "This field is required",
                digits: "You can only enter digits"
            },
            Planning: {
                required: "This field is required",
                digits: "You can only enter digits"
            },
        },
        invalidHandler: function(event, validator) {
            // 'this' refers to the form
            var errors = validator.numberOfInvalids();
            if (errors) {
              alert(
                "Please Correct the errors and try again."
              )
            } else {
              $("div.error").hide();
            }
          },
        //   submitHandler: function(form) {
        //     $(form).ajaxSubmit();
        //  }
    });
});

