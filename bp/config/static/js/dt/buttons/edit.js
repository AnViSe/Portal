$.fn.dataTable.ext.buttons.edit = {
    className: 'btn-info buttons-edit disabled',
    text: function (dt) {
        return '<div class="d-none d-md-block"><i class="far fa-edit"></i> Изменить</div>'+
               '<div class="d-md-none"><i class="far fa-edit"></i></div>';
    },
    action: function (e, dt, button, config) {
        if (dt.row('.selected').count() === 1) {
            var obj_id = dt.row('.selected').data().id;
            window.location = window.location.href.replace(/\/+$/, "") + '/' + obj_id;
        } else {
            console.log('No selected record');
        }
    },
    enabled: false,
};