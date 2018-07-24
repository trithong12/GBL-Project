// $(document).ready(function() {
//     $("#listProductTable").dataTable().fnDestroy();
//     $('#listProductTable').dataTable( {
//     "processing": true,
//     "serverSide": true,
//     "ajax": {
//         "url": "/api/gbl/product/",
//         "type": "GET"
//     },
//     "columns": [
//         { "data": "product_id" },
//         { "data": "product_name" },
//         { "data": "product_category" },
//         { "data": "product_price" },
//         { "data": "product_description" },
//         {
//             "data": null,
//             "defaultContent": '<button type="button" class="btn btn-info">Edit</button>' + '&nbsp;&nbsp' +
//             '<button type="button" class="btn btn-danger">Delete</button>'
//         }
//     ]
//     } );
// } );



let id = 0;

$(function() {
    $('#listProductTable tbody').on('click', 'button', function () {
        let data = table.row($(this).parents('tr')).data();
        let class_name = $(this).attr('class');
        if (class_name == 'btn btn-info') {
            // EDIT button
            alert('yes');
            $('#product_id').val(data['product_id']);
            $('#product_name').val(data['product_name']);
            $('#product_category').val(data['product_category']);
            $('#product_price').val(data['product_price']);
            $('#product_description').val(data['product_description']);
            $('#type').val('edit');
            $('#modal_title').text('EDIT');
            $("#myModal").modal();
        } else {
            // DELETE button
            $('#modal_title').text('DELETE');
            $("#confirm").modal();
        }
    
        id = data['product_id'];
    
    });
})

$('form').on('submit', function (e) {
    e.preventDefault();
    let $this = $(this);
    let type = $('#type').val();
    let method = '';
    let url = '/api/gbl/product/';
    if (type == 'new') {
        // new
        method = 'POST';
    } else {
        // edit
        url = url + id + '/';
        method = 'PUT';
    }

    $.ajax({
        url: url,
        method: method,
        data: $this.serialize()
    }).success(function (data, textStatus, jqXHR) {
        location.reload();
    }).error(function (jqXHR, textStatus, errorThrown) {
        console.log(jqXHR)
    });
});

$('#confirm').on('click', '#delete', function (e) {
    $.ajax({
        url: '/api/gbl/product/' + id + '/',
        method: 'DELETE'
    }).success(function (data, textStatus, jqXHR) {
        location.reload();
    }).error(function (jqXHR, textStatus, errorThrown) {
        console.log(jqXHR)
    });
});


$('#new').on('click', function (e) {
    $('#product_id').val('');
    $('#product_name').val('');
    $('#product_category').val('');
    $('#product_price').val('');
    $('#product_description').val('');
    $('#type').val('new');
    $('#modal_title').text('NEW');
    $("#myModal").modal();
});