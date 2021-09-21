window._buildUrl = function (dt, action) {
    let url = dt.ajax.url() || '';
    let params = dt.ajax.params();
    params.action = action;

    return url + '?' + $.param(params);
};

$.fn.dataTable.ext.buttons.create = {
    className: 'btn-success buttons-create',
    text: function (dt) {
        return '<div class="d-none d-md-block"><i class="fas fa-plus"></i> Создать</div>'+
               '<div class="d-md-none"><i class="fas fa-plus"></i></div>';
    },
   action: function (e, dt, button, config) {
        window.location = window.location.href.replace(/\/+$/, "") + '/create';
   }
};

$.fn.dataTable.ext.buttons.edit = {
    className: 'btn-info buttons-edit disabled',
    text: function (dt) {
        return '<div class="d-none d-md-block"><i class="far fa-edit"></i> Изменить</div>'+
               '<div class="d-md-none"><i class="far fa-edit"></i></div>';
    },
    action: function (e, dt, button, config) {
        if (dt.row('.selected').count() === 1) {
            var obj_id = dt.row('.selected').data().id;
            //console.log(obj_id);
            window.location = window.location.href.replace(/\/+$/, "") + '/' + obj_id;
        } else {
            console.log('No selected record');
        }
    },
    enabled: false,
};

$.fn.dataTable.ext.buttons.delete = {
    className: 'btn-danger buttons-delete disabled',
    text: function (dt) {
        return '<div class="d-none d-md-block"><i class="far fa-trash-alt"></i> Удалить</div>'+
               '<div class="d-md-none"><i class="far fa-trash-alt"></i></div>';
    },
    action: function (e, dt, button, config) {
         if (dt.row('.selected').count() === 1) {
            var obj_id = dt.row('.selected').data().id;
            //console.log(obj_id);
            window.location = window.location.href.replace(/\/+$/, "") + '/' + obj_id + '/delete';
         } else {
            console.log('No selected record');
        }
    },
    enabled: false,
};

$.fn.dataTable.ext.buttons.reload = {
//    name: 'reload',
    className: 'buttons-reload',
//    text: '<i class="fa fa-sync" data-toggle="tooltip" data-title="Reload"> Обновить</i>',
    text: '<div class="d-none d-md-block"><i class="fa fa-sync"></i> Обновить</div>'+
          '<div class="d-md-none"><i class="fa fa-sync"></i></div>',
    action: function (e, dt, button, config) {
        button.find('i').removeClass('fa-sync').addClass('fa-spinner fa-spin');
        button.attr('disabled', true);
        dt.on('xhr.reload', () => {
            button.find('i').addClass('fa-sync').removeClass('fa-spinner fa-spin');
            button.attr('disabled', false);
        });
        dt.draw(false);
    }
};

function prepareDataTableServerSideActionsTop(){
var dt_dom = "<'card-header'<'row'<'col-sm-6 col-md-8'B><'col-sm-6 col-md-4'f>>>"+
             "<'card-body table-responsive p-1'tr>"+
             "<'card-footer clearfix'<'row'<'col-md'l><'col-md'i><'col-md'p>>>"

var t = $('#ref-table').DataTable({
        processing: true,
        serverSide: true,
//        columnDefs: [{
//            targets: -1,
//            data: null,
//            visible: false,
//            searchable: false,
//        }],
//        dom: dt_dom,
//        buttons: [
//            'create',
//            'edit',
//            'delete',
//            {
//                extend: 'print',
//                text: '<div class="d-none d-md-block"><i class="fa fa-print"></i> Печать</div>'+
//                      '<div class="d-md-none"><i class="fa fa-print"></i></div>',
//                exportOptions: {
//                    columns: 'visible'
//                },
//            },
//            'reload',
//        ],
        language: {
            url: "/static/plugins/datatables/Russian.json"
        },
        lengthMenu: [
            [ 15, 25, 50, 100, -1 ],
            [ '15', '25', '50', '100', 'Все' ]
        ],
        select: {
            style: 'single',
            items: 'row',
            info: false,
        },
});

t.on( 'select deselect', function () {
		var selectedRows = t.rows( { selected: true } ).count();
		t.button(1).enable( selectedRows === 1 );
		t.button(2).enable( selectedRows > 0 );
});


//t.on('select', function (e, dt, type, indexes) {
//    if ( type === 'row' ) {
        //var data = t.rows( indexes ).data().count();
        //console.log('select' + data);
        //console.log(dt.find('.buttons-edit').class);
//        for (var obj of document.getElementsByClassName('buttons-edit')) {
//            obj.classList.toggle('disabled');
//        }
//        for (var obj of document.getElementsByClassName('buttons-delete')) {
//            obj.classList.toggle('disabled');
//        }
//    }
//});

//t.on('deselect', function (e, dt, type, indexes) {
//    if ( type === 'row' ) {
        //var data = t.rows('.selected').data().count();
        //console.log('deselect' + data);
        //console.log(dt.find('.buttons-edit').class);
//        for (var obj of document.getElementsByClassName('buttons-edit')) {
//            obj.classList.toggle('disabled');
//        }
//        for (var obj of document.getElementsByClassName('buttons-delete')) {
//            obj.classList.toggle('disabled');
//        }
//    }
//});
new $.fn.dataTable.Buttons( t, {
    buttons: [
        {
            text: 'Button 1',
            action: function ( e, dt, node, conf ) {
                console.log( 'Button 1 clicked on' );
            }
        },
        {
            text: 'Button 2',
            action: function ( e, dt, node, conf ) {
                console.log( 'Button 2 clicked on' );
            }
        }
    ]
});
t.buttons().container().prependTo(t.table().container());
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
            'reload',
            {
                extend: 'print',
                text: '<div class="d-none d-md-block"><i class="fa fa-print"></i> Печать</div>'+
                      '<div class="d-md-none"><i class="fa fa-print"></i></div>',
            },
        ],
        language: {
            url: '/static/plugins/datatables/Russian.json',
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

//t.buttons().container().prependTo(t.table().container());
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

function prepareDataTableServerSideActionsTop1(dt_language){
var dt_dom =
//             "<'card-header'"+
//                "<'d-flex justify-content-between'"+
//                    "<'header_left'B>"+
//                    "<'header_center'>"+
//                    "<'header_right'f>"+
//                ">"+
//             ">"+
             "<'card-body table-responsive p-1't>"+
             "<'card-footer clearfix'"+
                "<'d-flex justify-content-between'"+
//                "<"+
//                    "<'col-md'l><'col-md'i><'col-md'p>"+
                    "<'footer_left'l>"+
                    "<'footer_center'p>"+
                    "<'footer_right'>"+
                ">"+
             ">"
var dt_dom1 = "<'card-header'<'row'<'col-sm-6 col-md-8'B><'col-sm-6 col-md-4'f>>>"+
             "<'card-body table-responsive p-1'tr>"+
             "<'card-footer clearfix'<'row'<'col-md'l><'col-md'i><'col-md'p>>>"
var table = $('#ref-table').DataTable({
        language: {
            url: dt_language,
        },
		buttons: [
//			'copy', 'csv', 'excel', 'pdf', 'print',
		],
        initComplete: function(settings, json) {
            new $.fn.dataTable.Buttons( table, {
                name: 'qqq',
                buttons: [
                    'create',
                    'edit',
                    'delete',
                ]});

//            table.buttons('qqq', null).container().addClass('mr-2')
//                .prependTo($('.col-sm-6:eq(0)', table.table().container()));
//            table.buttons('qqq', null).container().appendTo(table.table().container());
            table.buttons('qqq', null).container().addClass('mr-2').attr('style','margin: 2px 0;')
            .prependTo('.header_left');
        },
        processing: true,
        serverSide: true,
        dom: dt_dom,
//        dom: 'T<"clear">lfrtip',
//        dom: 'Bt',
        lengthMenu: [
            [ 15, 25, 50, 100, -1 ],
            [ '15', '25', '50', '100', 'Все' ]
        ],
        select: {
            style: 'single',
            items: 'row',
            info: false,
        },
});
//new $.fn.dataTable.Buttons( table, {
//    buttons: [
//        'create',
//        'edit',
//        'delete',
//    ]
//});
//table.buttons().container().prependTo(table.table().container());
//table.buttons().container().appendTo('#cccc');
new $.fn.dataTable.Buttons( table, {
    name: 'but1',
    buttons: [
        'create',
        'edit',
        'delete',
    ]
});
new $.fn.dataTable.Buttons( table, {
    name: 'but2',
    buttons: [
        'reload',
    ]
});
//table.buttons('but1', null).container().appendTo('#cccc');
//table.buttons('but1', null).container().appendTo('#cccc');
//table.buttons('but2', null).container().appendTo('#bbbb');
//table.buttons('but2', null).container().appendTo('.dataTables_info');
//table.buttons('but2', null).container().appendTo(table.table().container());
}
