$(document).ready(function() {
    alert('yes');
    $('#example').dataTable( {
        "processing": true,
        "ajax": {
            "processing": true,
            "url": "{% url 'listProducts_ajax_url' %}",
            "dataSrc": ""
        },       
        "columns": [
                { "data": "product_id" },
                { "data": "product_category.product_category_name" },
        ]
    } );
} );