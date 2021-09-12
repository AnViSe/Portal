function prepareDataTableServerSide(){
var t = $('#ref-table').DataTable({
        columnDefs: [{
            targets: -1,
            data: null,
            width: 50,
            sortable: false,
            searchable: false,
            printable: false,
            //visible: false,
            defaultContent: '<div class="btn-group btn-group-xs" role="group" aria-label="Basic example">'+
                              //'<button type="button" class="btn btn-outline-info btn_view"><i class="far fa-eye"></i></button>'+
                              '<button type="button" class="btn btn-outline-success btn_edit"><i class="far fa-edit"></i></button>'+
                              '<button type="button" class="btn btn-outline-danger btn_delete"><i class="far fa-trash-alt"></i></button></div>'
        }],
        dom: "<'card-header'<'row'<'col-sm-6 col-md-8'B><'col-sm-6 col-md-4'f>>>"+
             "<'card-body table-responsive p-1'tr>"+
             "<'card-footer clearfix'<'row'<'col-md'l><'col-md'i><'col-md'p>>>",
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



















(function ($, DataTable) {
    "use strict";

    var _buildParams = function (dt, action, onlyVisibles) {
        var params = dt.ajax.params();
        params.action = action;
        params._token = $('meta[name="csrf-token"]').attr('content');

        if (onlyVisibles) {
            params.visible_columns = _getVisibleColumns();
        } else {
            params.visible_columns = null;
        }

        return params;
    };

    var _getVisibleColumns = function () {

        var visible_columns = [];
        $.each(DataTable.settings[0].aoColumns, function (key, col) {
            if (col.bVisible) {
                visible_columns.push(col.name);
            }
        });

        return visible_columns;
    };

    var _downloadFromUrl = function (url, params) {
        var postUrl = url + '/export';
        var xhr = new XMLHttpRequest();
        xhr.open('POST', postUrl, true);
        xhr.responseType = 'arraybuffer';
        xhr.onload = function () {
            if (this.status === 200) {
                var filename = "";
                var disposition = xhr.getResponseHeader('Content-Disposition');
                if (disposition && disposition.indexOf('attachment') !== -1) {
                    var filenameRegex = /filename[^;=\n]*=((['"]).*?\2|[^;\n]*)/;
                    var matches = filenameRegex.exec(disposition);
                    if (matches != null && matches[1]) filename = matches[1].replace(/['"]/g, '');
                }
                var type = xhr.getResponseHeader('Content-Type');

                var blob = new Blob([this.response], {type: type});
                if (typeof window.navigator.msSaveBlob !== 'undefined') {
                    // IE workaround for "HTML7007: One or more blob URLs were revoked by closing the blob for which they were created. These URLs will no longer resolve as the data backing the URL has been freed."
                    window.navigator.msSaveBlob(blob, filename);
                } else {
                    var URL = window.URL || window.webkitURL;
                    var downloadUrl = URL.createObjectURL(blob);

                    if (filename) {
                        // use HTML5 a[download] attribute to specify filename
                        var a = document.createElement("a");
                        // safari doesn't support this yet
                        if (typeof a.download === 'undefined') {
                            window.location = downloadUrl;
                        } else {
                            a.href = downloadUrl;
                            a.download = filename;
                            document.body.appendChild(a);
                            a.click();
                        }
                    } else {
                        window.location = downloadUrl;
                    }

                    setTimeout(function () {
                        URL.revokeObjectURL(downloadUrl);
                    }, 100); // cleanup
                }
            }
        };
        xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
        xhr.send($.param(params));
    };

    var _buildUrl = function(dt, action) {
        var url = dt.ajax.url() || '';
        var params = dt.ajax.params();
        params.action = action;

        if (url.indexOf('?') > -1) {
            return url + '&' + $.param(params);
        }

        return url + '?' + $.param(params);
    };

    DataTable.ext.buttons.excel = {
        className: 'buttons-excel',

        text: function (dt) {
            return '<i class="fas fa-file-excel"></i> ' + dt.i18n('buttons.excel', 'Excel');
        },

        action: function (e, dt, button, config) {
            var url = _buildUrl(dt, 'excel');
            window.location = url;
        }
    };

    DataTable.ext.buttons.postExcel = {
        className: 'buttons-excel',

        text: function (dt) {
            return '<i class="fas fa-file-excel"></i> ' + dt.i18n('buttons.excel', 'Excel');
        },

        action: function (e, dt, button, config) {
            var url = dt.ajax.url() || window.location.href;
            var params = _buildParams(dt, 'excel');

            _downloadFromUrl(url, params);
        }
    };

    DataTable.ext.buttons.postExcelVisibleColumns = {
        className: 'buttons-excel',

        text: function (dt) {
            return '<i class="fas fa-file-excel"></i> ' + dt.i18n('buttons.excel', 'Excel (only visible columns)');
        },

        action: function (e, dt, button, config) {
            var url = dt.ajax.url() || window.location.href;
            var params = _buildParams(dt, 'excel', true);

            _downloadFromUrl(url, params);
        }
    };

    DataTable.ext.buttons.export = {
        extend: 'collection',

        className: 'buttons-export',

        text: function (dt) {
            return '<i class="fas fa-download"></i> ' + dt.i18n('buttons.export', 'Экспорт') + '&nbsp;<span class="caret"/>';
            // return '<i class="fas fa-download"></i> ';
            // return '<div class="d-none d-md-block"> Экспорт</div><div class="d-md-none"></div>';
        },

        buttons: ['csv', 'excel', 'pdf']
    };

    DataTable.ext.buttons.csv = {
        className: 'buttons-csv',

        text: function (dt) {
            return '<i class="fas fa-file-excel"></i> ' + dt.i18n('buttons.csv', 'CSV');
        },

        action: function (e, dt, button, config) {
            var url = _buildUrl(dt, 'csv');
            window.location = url;
        }
    };

    DataTable.ext.buttons.postCsvVisibleColumns = {
        className: 'buttons-csv',

        text: function (dt) {
            return '<i class="fas fa-file-excel"></i> ' + dt.i18n('buttons.csv', 'CSV (only visible columns)');
        },

        action: function (e, dt, button, config) {
            var url = dt.ajax.url() || window.location.href;
            var params = _buildParams(dt, 'csv', true);

            _downloadFromUrl(url, params);
        }
    };

    DataTable.ext.buttons.postCsv = {
        className: 'buttons-csv',

        text: function (dt) {
            return '<i class="fas fa-file-excel"></i> ' + dt.i18n('buttons.csv', 'CSV');
        },

        action: function (e, dt, button, config) {
            var url = dt.ajax.url() || window.location.href;
            var params = _buildParams(dt, 'csv');

            _downloadFromUrl(url, params);
        }
    };

    DataTable.ext.buttons.pdf = {
        className: 'buttons-pdf',

        text: function (dt) {
            return '<i class="fas fa-file-pdf"></i> ' + dt.i18n('buttons.pdf', 'PDF');
        },

        action: function (e, dt, button, config) {
            var url = _buildUrl(dt, 'pdf');
            window.location = url;
        }
    };

    DataTable.ext.buttons.postPdf = {
        className: 'buttons-pdf',

        text: function (dt) {
            return '<i class="fas fa-file-pdf"></i> ' + dt.i18n('buttons.pdf', 'PDF');
        },

        action: function (e, dt, button, config) {
            var url = dt.ajax.url() || window.location.href;
            var params = _buildParams(dt, 'pdf');

            _downloadFromUrl(url, params);
        }
    };

    DataTable.ext.buttons.print = {
        className: 'buttons-print',

        text: function (dt) {
            return '<div class="d-none d-md-block"><i class="fas fa-print"></i> Печать</div><div class="d-md-none"><i class="fas fa-print"></i></div>';
        },

        action: function (e, dt, button, config) {
            var url = _buildUrl(dt, 'print');
            window.location = url;
        }
    };

    DataTable.ext.buttons.reset = {
        className: 'buttons-reset',

        text: function (dt) {
            return '<i class="fas fa-undo"></i> ' + dt.i18n('buttons.reset', 'Сброс');
        },

        action: function (e, dt, button, config) {
            dt.search('');
            dt.columns().search('');
            dt.draw();
        }
    };

    DataTable.ext.buttons.reload = {
        className: 'buttons-reload',

        text: function (dt) {
            return '<div class="d-none d-md-block"><i class="fas fa-sync"></i> Обновить</div><div class="d-md-none"><i class="fas fa-sync"></i></div>';
        },

        action: function (e, dt, button, config) {
            dt.draw(false);
        }
    };

    DataTable.ext.buttons.create = {
        className: 'buttons-create',

        text: function (dt) {
            return '<div class="d-none d-md-block"><i class="fas fa-plus"></i> Создать</div><div class="d-md-none"><i class="fas fa-plus"></i></div>';
        },

        action: function (e, dt, button, config) {
            window.location = window.location.href.replace(/\/+$/, "") + '/create';
        }
    };

    if (typeof DataTable.ext.buttons.copyHtml5 !== 'undefined') {
        $.extend(DataTable.ext.buttons.copyHtml5, {
            text: function (dt) {
                return '<i class="fas fa-copy"></i> ' + dt.i18n('buttons.copy', 'Копировать');
            }
        });
    }

    if (typeof DataTable.ext.buttons.colvis !== 'undefined') {
        $.extend(DataTable.ext.buttons.colvis, {
            text: function (dt) {
                return '<i class="fas fa-eye"></i> ' + dt.i18n('buttons.colvis', 'Column visibility');
            }
        });
    }
})(jQuery, jQuery.fn.dataTable);