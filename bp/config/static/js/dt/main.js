function prepareDataTableServerSideActionsRow(dt_language){
var dt_defaultContent = '<div class="btn-group btn-group-xs" role="group" aria-label="Basic example">'+
                        '<button type="button" class="btn btn-outline-info btn_view"><i class="far fa-eye"></i></button>'+
                        '<button type="button" class="btn btn-outline-success btn_edit"><i class="far fa-edit"></i></button>'+
                        '<button type="button" class="btn btn-outline-danger btn_delete"><i class="far fa-trash-alt"></i></button></div>'
var dt_dom = "<'card-header'"+
                "<'row'"+
//                "<'d-flex justify-content-between'"+
                    "<'col-sm-12 col-md-6 header_left'B>"+
//                    "<'header_center'>"+
                    "<'col-sm-12 col-md-6 header_right pt-2'f>"+
                ">"+
             ">"+
             "<'card-body p-0't>"+
             "<'card-footer'"+
                "<'row'"+
//                "<'d-flex justify-content-between'"+
                    "<'col-lg-3 col-md-6 footer_left pt-2'l>"+
                    "<'col-lg-3 footer_center d-none d-lg-block'i>"+
                    "<'col-lg-6 col-md-6 footer_right'p>"+
                ">"+
             ">"
var table = $('#ref-table').DataTable({
        language: {
            url: dt_language,
        },
        processing: true,
        serverSide: true,
        columnDefs: [
            {
            targets: 0,
            visible: false,
            },
            {
            targets: -1,
            data: null,
            width: 85,
            sortable: false,
            searchable: false,
            printable: false,
            defaultContent: dt_defaultContent,},
//            {
//            targets: -2,
//            width: 85,
//            }
        ],
        dom: dt_dom,
        buttons: [
        ],
        initComplete: function(settings, json) {
            new $.fn.dataTable.Buttons( table, {
                name: 'but_top_left',
                buttons: [
                    'create',
                    'reload',
                    {
                        extend: 'print',
                        text: '<div class="d-none d-lg-block"><i class="fa fa-print"></i> Печать</div>'+
                              '<div class="d-lg-none"><i class="fa fa-print"></i></div>',
                        title: 'Титул',
                        messageTop: 'Заголовок',
                        messageBottom: 'Подвальчик',
                        exportOptions: {
                            columns: ':visible'
                        },
                        autoPrint: true
                    },
                ]});
            table.buttons('but_top_left', null).container()
            .addClass('mr-2').attr('style','margin: 2px 0;')
            .prependTo('.header_left');
        },
        lengthMenu: [
            [ 15, 25, 50, 100, -1 ],
            [ '15', '25', '50', '100', 'Все' ]
        ],
});

//$('#ref-table').css('display', 'block');
//table.columns.adjust().draw();

$('#ref-table tbody').on('click', 'button', function(){
    var baseUrl = $(this)[0].baseURI
    var data = table.row($(this).parents('tr')).data();
    var work = true;
    if ($(this).hasClass('btn_view')) {
        var nextUrl = baseUrl + data.id + '/view'
    }
    if ($(this).hasClass('btn_edit')) {
        var nextUrl = baseUrl + data.id
    }
    if ($(this).hasClass('btn_delete')) {
        var nextUrl = baseUrl + data.id	+ '/delete'
        work = false;
    }
    if (work == true) {
        console.log(nextUrl)
        window.location = nextUrl
    }
});
}

function prepareDataTableServerSideTreeActionsRow(dt_language){
var dt_defaultContent = '<div class="btn-group btn-group-xs" role="group" aria-label="Basic example">'+
                        '<button type="button" class="btn btn-outline-info btn_view"><i class="far fa-eye"></i></button>'+
                        '<button type="button" class="btn btn-outline-success btn_edit"><i class="far fa-edit"></i></button>'+
                        '<button type="button" class="btn btn-outline-danger btn_delete"><i class="far fa-trash-alt"></i></button></div>'
var dt_dom = "<'card-header'"+
                "<'d-flex justify-content-between'"+
                    "<'header_left'B>"+
//                    "<'header_center'>"+
                    "<'header_right pt-2'f>"+
                ">"+
             ">"+
             "<'card-body p-0't>"+
             "<'card-footer'"+
                "<'d-flex justify-content-between'"+
                    "<'footer_left pt-2'l>"+
                    "<'footer_center d-none d-xl-block'i>"+
                    "<'footer_right'p>"+
                ">"+
             ">"
var columns =[
//{
//    title: '',
//    target: 0,
//    className: 'treegrid-control',
//    data: function (item) {
//        if (item.children) {
//            return '<span>+</span>';
//        }
//        return '';
//    }
//},
{
    title: 'Name',
//    target: 1,
    data: function (item) {
        return item.name;
    }
},
]
var table = $('#ref-table').DataTable({
        language: {
            url: dt_language,
        },
        processing: true,
        serverSide: true,
        columns: columns,
//        columnDefs: [{
//            targets: -1,
//            data: null,
//            width: 50,
//            sortable: false,
//            searchable: false,
//            printable: false,
//            defaultContent: dt_defaultContent,
//        }],
        dom: dt_dom,
        buttons: [
        ],
        initComplete: function(settings, json) {
            new $.fn.dataTable.Buttons( table, {
                name: 'but_top_left',
                buttons: [
                    'create',
                    'reload',
                    {
                        extend: 'print',
                        text: '<div class="d-none d-lg-block"><i class="fa fa-print"></i> Печать</div>'+
                              '<div class="d-lg-none"><i class="fa fa-print"></i></div>',
                        title: 'Титул',
                        messageTop: 'Заголовок',
                        messageBottom: 'Подвальчик',
//                        exportOptions: {
//                            columns: ':visible'
//                        },
                        autoPrint: false
                    },
                ]});
            table.buttons('but_top_left', null).container()
            .addClass('mr-2').attr('style','margin: 2px 0;')
            .prependTo('.header_left');
        },
        lengthMenu: [
            [ 15, 25, 50, 100, -1 ],
            [ '15', '25', '50', '100', 'Все' ]
        ],
        treeGrid: {
            left: 10,
            expandIcon: '<span>+</span>',
            collapseIcon: '<span>-</span>',
        },
    });

    $('#ref-table tbody').on('click', 'button', function(){
		var baseUrl = $(this)[0].baseURI
		var data = table.row($(this).parents('tr')).data();
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