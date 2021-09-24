function prepareDataTableServerSideActionsRow(dt_language){
var dt_defaultContent = '<div class="btn-group btn-group-xs" role="group" aria-label="Basic example">'+
                        '<button type="button" class="btn btn-outline-info btn_view"><i class="far fa-eye"></i></button>'+
                        '<button type="button" class="btn btn-outline-success btn_edit"><i class="far fa-edit"></i></button>'+
                        '<button type="button" class="btn btn-outline-danger btn_delete"><i class="far fa-trash-alt"></i></button></div>'
var dt_dom = "<'card-header'<'row'<'col-sm-6 col-md-8'B><'col-sm-6 col-md-4'f>>>"+
             "<'card-body table-responsive p-1'tr>"+
             "<'card-footer clearfix'<'row'<'col-md'l><'col-md'i><'col-md'p>>>"

var t = $('#ref-table').DataTable({
        language: {
            url: dt_language,
        },
        processing: true,
        serverSide: true,
        columnDefs: [{
            targets: -1,
            data: null,
            width: 50,
            sortable: false,
            searchable: false,
            printable: false,
            defaultContent: dt_defaultContent,
        }],
        dom: dt_dom,
        buttons: [
            'create',
            'reload',
            {
                extend: 'print',
                text: '<div class="d-none d-md-block"><i class="fa fa-print"></i> Печать</div>'+
                      '<div class="d-md-none"><i class="fa fa-print"></i></div>',
            },
        ],
        lengthMenu: [
            [ 15, 25, 50, 100, -1 ],
            [ '15', '25', '50', '100', 'Все' ]
        ],
    });

    $('#ref-table tbody').on('click', 'button', function(){
		var baseUrl = $(this)[0].baseURI
		var data = t.row($(this).parents('tr')).data();
		if ($(this).hasClass('btn_view')) {
		    var nextUrl = baseUrl + data.id + '/view'
		}
		if ($(this).hasClass('btn_edit')) {
		    var nextUrl = baseUrl + data.id
		}
		if ($(this).hasClass('btn_delete')) {
		    var nextUrl = baseUrl + data.id	+ '/delete'
		}
		console.log(nextUrl)
		window.location = nextUrl
	});
}