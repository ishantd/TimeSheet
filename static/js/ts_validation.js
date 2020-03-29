$(function(){
    $("#ts_form").validate({
        rules: {
            activity: {
               required: true
            },
            project: {
                required: true
            },
            total: {
                required: true,
                equalTo: 8
            },
            hours: {
                required: true,
                digits: true,
                max: 8
            }
        },
        messages: {
            activity: {
                required: 'Please enter the activity'
            },
            project: {
                required: 'Please select a project'
            },
            total: {
                equalTo: 'Total daily working hours should be 8'
            },
            hours: {
                digits: 'You can only enter digits',
                max: 'Number of working hours cannot exceed 8'
            }
        }
    });
});