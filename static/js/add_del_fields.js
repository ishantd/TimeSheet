var table = 1;
var table_extended = 1;

$("#create").click(function(){
    markup = $('#input-row0').prop('outerHTML');
    markup = markup.replace('input-row0', 'input-row' + table.toString());
    markup = markup.replace('delete0', 'delete' + table.toString());
    markup = markup.replace('sel0', 'sel' + table.toString());
    $("#table-body tr:first").after(markup)
    table++;
});

function remove(delID) {
    var sr = delID.replace('delete', '');
    var deleteThis = '#input-row' + sr;
    if (sr!='0') {
        $(deleteThis).remove();
    }
    else {
        alert("Not allowed to delete all rows")
    }
}

$("#create_extended").click(function(){
    markup = $('#input-row0_extended').prop('outerHTML');
    markup = markup.replace('input-row0', 'input-row' + table_extended.toString());
    markup = markup.replace('delete0', 'delete' + table_extended.toString());
    markup = markup.replace('sel0', 'sel' + table_extended.toString());
    $("#table-body_extended tr:first").after(markup);
    table++;
});

function remove(delID) {
    var sr = delID.replace('delete', '');
    var deleteThis = '#input-row' + sr + '_extended';
    if (sr!='0') {
        $(deleteThis).remove();
    }
    else {
        alert("Not allowed to delete all rows")
    }
}