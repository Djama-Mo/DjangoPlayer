$(document).ready(function () {

    $('.updateButton').on('click', function () {

        var item_id = $(this).attr('itemid');
        var like_status = document.getElementById(item_id)

        req = $.ajax({
            url: 'add-favourite/' + item_id,
            type: 'GET',
            data: {'id': item_id}
        });

        req.done(function (data) {
            $('#updateButton' + item_id).data(like_status.innerHTML = data.id)
        });
    });
});