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

    $("#ts_form").validate({  
        rules: {
            activity: {
               required: true
            },
            activity_extended: {
                required: true
             },
            project: {
                required: true
            },
            project_extended: {
                required: true
            },
            total: {
                required: true,
                totalHours: true
            },
            hours: {
                digits: true,
                max: 8
            },
            hours_extended: {
                digits: true,
                max: 8
            },
            total_extended: {
                required: true,
                totalHours: true
            },
        },
        messages: {
            activity: {
                required: 'Please enter the activity'
            },
            project: {
                required: 'Please select a project'
            },
            hours: {
                digits: 'You can only enter digits',
                max: 'Number of working hours cannot exceed 8'
            },
            activity_extended: {
                required: 'Please enter the activity'
            },
            project_extended: {
                required: 'Please select a project'
            },
            hours_extended: {
                digits: 'You can only enter digits',
                max: 'Number of working hours cannot exceed 8'
            }
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

$("#create").click(function() {
    $('input[name="hours"]').rules('add', {
        digits: true,
        max: 8,
        messages: {
            digits: "You can only enter digits",
            max: 'Number of working hours cannot exceed 8'
        }
    });
    $('input[name="activity"]').rules('add', {
        required: true,
        messages: {
            required: "This field is required"
        }
    });
})