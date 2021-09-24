$.fn.dataTable.ext.buttons.create = {
    className: 'btn-success buttons-create',
    text: function (dt) {
        return '<div class="d-none d-lg-block"><i class="fas fa-plus"></i> Создать</div>'+
               '<div class="d-lg-none"><i class="fas fa-plus"></i></div>';
    },
   action: function (e, dt, button, config) {
        window.location = window.location.href.replace(/\/+$/, "") + '/create';
   }
};