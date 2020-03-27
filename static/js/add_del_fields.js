var table = 1


$("#create").click(function(){
    markup = $('#input-row0').prop('outerHTML');
    // console.log(table)
    markup = markup.replace('input-row0', 'input-row' + table.toString())
    markup = markup.replace('delete0', 'delete' + table.toString())
    // console.log(markup)
    $("#table-body").append(markup)
    table++;
    // console.log(table)
})

function remove(delID) {
    var sr = delID.replace('delete', '')
    var deleteThis = '#input-row' + sr
    if (sr!='0') {
        $(deleteThis).remove()
    }
    
}