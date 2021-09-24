$.fn.dataTable.ext.buttons.reload = {
//    name: 'reload',
    className: 'buttons-reload',
//    text: '<i class="fa fa-sync" data-toggle="tooltip" data-title="Reload"> Обновить</i>',
    text: '<div class="d-none d-lg-block"><i class="fa fa-sync"></i> Обновить</div>'+
          '<div class="d-lg-none"><i class="fa fa-sync"></i></div>',
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