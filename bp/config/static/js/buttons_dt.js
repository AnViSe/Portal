$.fn.dataTable.ext.buttons.create = {
    className: 'btn-success buttons-create',
    text: function (dt) {
        return '<div class="d-none d-md-block"><i class="fas fa-plus"></i> Создать</div><div class="d-md-none"><i class="fas fa-plus"></i></div>';
    },
   action: function (e, dt, button, config) {
        window.location = window.location.href.replace(/\/+$/, "") + '/create';
   }
};
$.fn.dataTable.ext.buttons.edit = {
    className: 'btn-info buttons-edit disabled',
    text: function (dt) {
        return '<div class="d-none d-md-block"><i class="far fa-edit"></i> Изменить</div><div class="d-md-none"><i class="far fa-edit"></i></div>';
    },
   action: function (e, dt, button, config) {
        var obj_id = dt.row('.selected').data().id;
//        console.log(obj_id);
        window.location = window.location.href.replace(/\/+$/, "") + '/' + obj_id;
   }
};
$.fn.dataTable.ext.buttons.delete = {
    className: 'btn-danger buttons-delete disabled',
    text: function (dt) {
        return '<div class="d-none d-md-block"><i class="far fa-trash-alt"></i> Удалить</div><div class="d-md-none"><i class="far fa-trash-alt"></i></div>';
    },
   action: function (e, dt, button, config) {
        var obj_id = dt.row('.selected').data().id;
        console.log(obj_id);
//        window.location = window.location.href.replace(/\/+$/, "") + '/' + obj_id + '/delete';
   }
};

function prepareDataTableServerSideActionsTop(){
var dt_dom = "<'card-header'<'row'<'col-sm-6 col-md-8'B><'col-sm-6 col-md-4'f>>>"+
             "<'card-body table-responsive p-1'tr>"+
             "<'card-footer clearfix'<'row'<'col-md'l><'col-md'i><'col-md'p>>>"

var t = $('#ref-table').DataTable({
        dom: dt_dom,
        buttons: [
            'create',
            'edit',
            'delete',
            {
                extend: 'print',
                text: 'Печать',
            },
        ],
        language: {
            url: "/static/plugins/datatables/Russian.json"
        },
        lengthMenu: [
            [ 15, 25, 50, 100, -1 ],
            [ '15', '25', '50', '100', 'Все' ]
        ],
        select: {
            style: 'single'
        },
    });

t.on('select', function (e, dt, type, indexes) {
    if ( type === 'row' ) {
        var data = t.rows( indexes ).data().count();
        console.log('select' + data);
        //console.log(dt.find('.buttons-edit').class);
        for (var obj of document.getElementsByClassName('buttons-edit')) {
            obj.classList.toggle('disabled');
        }
        for (var obj of document.getElementsByClassName('buttons-delete')) {
            obj.classList.toggle('disabled');
        }
    }
});
t.on('deselect', function (e, dt, type, indexes) {
    if ( type === 'row' ) {
        var data = t.rows('.selected').data().count();
        console.log('deselect' + data);
        //console.log(dt.find('.buttons-edit').class);
        for (var obj of document.getElementsByClassName('buttons-edit')) {
            obj.classList.toggle('disabled');
        }
        for (var obj of document.getElementsByClassName('buttons-delete')) {
            obj.classList.toggle('disabled');
        }
    }
});
}

function prepareDataTableServerSideActionsRow(){
var dt_defaultContent = '<div class="btn-group btn-group-xs" role="group" aria-label="Basic example">'+
                        '<button type="button" class="btn btn-outline-info btn_view"><i class="far fa-eye"></i></button>'+
                        '<button type="button" class="btn btn-outline-success btn_edit"><i class="far fa-edit"></i></button>'+
                        '<button type="button" class="btn btn-outline-danger btn_delete"><i class="far fa-trash-alt"></i></button></div>'
var dt_dom = "<'card-header'<'row'<'col-sm-6 col-md-8'B><'col-sm-6 col-md-4'f>>>"+
             "<'card-body table-responsive p-1'tr>"+
             "<'card-footer clearfix'<'row'<'col-md'l><'col-md'i><'col-md'p>>>"

var t = $('#ref-table').DataTable({
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
            {
                extend: 'print',
                text: 'Печать',
                exportOptions: {
                    columns: 'searchable'
                },
                autoPrint: true,
            },
        ],
        language: {
            url: "/static/plugins/datatables/Russian.json",
        },
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

function prepareDataTableServerSide(){
var dt_defaultContent = '<div class="btn-group btn-group-xs" role="group" aria-label="Basic example">'+
                        '<button type="button" class="btn btn-outline-info btn_view"><i class="far fa-eye"></i></button>'+
                        '<button type="button" class="btn btn-outline-success btn_edit"><i class="far fa-edit"></i></button>'+
                        '<button type="button" class="btn btn-outline-danger btn_delete"><i class="far fa-trash-alt"></i></button></div>'
var dt_dom = "<'card-header'<'row'<'col-sm-6 col-md-8'B><'col-sm-6 col-md-4'f>>>"+
             "<'card-body table-responsive p-1'tr>"+
             "<'card-footer clearfix'<'row'<'col-md'l><'col-md'i><'col-md'p>>>"

var t = $('#ref-table').DataTable({
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
            {
                extend: 'create',
                //className: 'disabled',
            },
            {
                extend: 'edit',
                //className: 'disabled',
            },
            {
                extend: 'print',
                text: 'Печать',
                //exportOptions: {
                //    columns: 'searchable'
                //},
                autoPrint: false
            },
			//'selected',
			//'selectedSingle',
			//'selectAll',
			//'selectNone',
			//'selectRows',
			//'selectColumns',
			//'selectCells',
        ],
        language: {
            url: "{% static 'plugins/datatables/Russian.json' %}"
        },
        lengthMenu: [
            [ 15, 25, 50, 100, -1 ],
            [ '15', '25', '50', '100', 'Все' ]
        ],
        select: {
            style: 'single'
        },
    });

    $('#ref-table tbody').on('click', 'button', function(){
		var baseUrl = $(this)[0].baseURI
		var data = t.row($(this).parents('tr')).data();
		if ($(this).hasClass('btn_view')) {
		    var nextUrl = baseUrl + data.id + '/view'
		}
		if ($(this).hasClass('btn_edit')) {
		    var nextUrl = baseUrl + data.id + '/edit'
		}
		if ($(this).hasClass('btn_delete')) {
		    var nextUrl = baseUrl + data.id	+ '/delete'
		}
		console.log(nextUrl)
		//var c_u = $(this)[0].attributes.class
		//var c_u = $(this)[0].baseURI
		//console.log(c_u);
		//var data = t.row($(this).parents('tr')).data();
		//console.log(data.id);
		//window.location = c_u + data.id
	});

t.on('select', function (e, dt, type, indexes) {
    if ( type === 'row' ) {
        var data = t.rows( indexes ).data().count();
        console.log('select' + data);
        //console.log(dt.find('.buttons-edit').class);
        for (var obj of document.getElementsByClassName('buttons-edit')) {
            obj.classList.toggle('disabled');
        }
    }
});
t.on('deselect', function (e, dt, type, indexes) {
    if ( type === 'row' ) {
        var data = t.rows('.selected').data().count();
        console.log('deselect' + data);
        //console.log(dt.find('.buttons-edit').class);
        for (var obj of document.getElementsByClassName('buttons-edit')) {
            obj.classList.toggle('disabled');
        }
        // do something with the ID of the selected items
    }
});
t.ajax.reload(function(json){
    $('#ref-table tbody tr:eq(0)').click();
});
}
