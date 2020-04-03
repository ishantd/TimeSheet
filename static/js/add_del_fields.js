var table = 1

$("#create").click(function(){
    markup = $('#input-row0').prop('outerHTML');
    markup = markup.replace('input-row0', 'input-row' + table.toString())
    markup = markup.replace('delete0', 'delete' + table.toString())
    markup = markup.replace('sel0', 'sel' + table.toString())
    $("#table-body tr:first").after(markup)
    table++;
    console.log(table)
    console.log("TEST2")
})

function remove(delID) {
    var sr = delID.replace('delete', '')
    var deleteThis = '#input-row' + sr
    if (sr!='0') {
        $(deleteThis).remove()
    }
    else {
        alert("Not allowed to delete all rows")
    }
}