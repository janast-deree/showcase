$(document).ready(function () {
    /**
     * Filter pieces by name, category and artist, with ajax. Render response in #pieces div
     */
    $("form#filter-pieces").submit(function (event) {
        let formData = {
            csrfmiddlewaretoken: $('[name=csrfmiddlewaretoken]').val(),
            name: $("#name-filter").val(),
            category: $("#category-filter").val(),
            artist: $("#artist-filter").val(),
        };

        $.ajax({
            method: 'POST',
            url: 'filter_pieces',
            data: formData,
            success: function(response) {
                $("#pieces").html(response);
            }
        });

        event.preventDefault();
    });

    /**
     * when a category is selected enable artist selection with only the relevant artists visible
     */
    $("#category-filter").change(function () {
        const category_id = $(this).val();
        let artist_filter = $("#artist-filter");
        artist_filter.val('Artist');
        if (category_id > 0) {
            artist_filter.children("option:not(:first-child)").each(function( index ) {
                if ($(this).attr('category') === category_id) {
                    $(this).show();
                }
                else {
                    $(this).hide();
                }
            });
            artist_filter.removeAttr('disabled');
        }
        else {
            artist_filter.attr('disabled', '');
        }
    });
});