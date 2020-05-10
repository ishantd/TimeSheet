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
    $.validator.addMethod('positive', function(value, element) {
        return parseInt(value)>=0;
    },'You cannot enter a negative value.');

    $("#new-project-form").validate({  
        rules: {
            project_type: {
                required: true,
            },
            project_id: {
                required: true,
                digits: true,
                minlength: 5,
                maxlength: 5,
                positive: true
            },
            name: {
                required: true,
            },
            controlled_manhours: {
                required: true,
                // digits: true,
                positive: true
            }
        },
        messages: {
            project_id: {
                digits: "Only digits are allowed",
                minlength: "Project ID should only have 5 digits",
                maxlength: "Project ID should only have 5 digits"
            },
            controlled_manhours: {
                digits: "Only digits are allowed",
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

