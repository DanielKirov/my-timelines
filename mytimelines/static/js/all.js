$(document).on('ready', function() {
    $("#pic").fileinput({
        maxFileCount: 50,
        allowedFileTypes: ["image"]
    });
});