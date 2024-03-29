'use strict'

document.querySelector('.navbar-nav').addEventListener('click', function(event) {
    console.log("CLicked")
    let active_btn = document.querySelector('.active')

    if (!event.target.classList.contains('active')) {
        active_btn.classList.remove('active')
        event.target.classList.add('active')
    }
})

function handleFileSelect(event) {
    //Check File API support
    if (window.File && window.FileList && window.FileReader) {
        console.log(window.File, window.FileList, window.FileReader);
        var files = event.target.files; //FileList object
        var output = document.getElementById("result");
        var filecount = document.getElementById('filecount');
        var filename = document.getElementById('filename')

        if (typeof(filecount) != 'undefined' && filecount != null) {
            console.log("filecount YES");
            document.getElementById('filecount').innerHTML = files.length + " files selected";
        }

        if (typeof(filename) != 'undefined' && filename != null) {
            console.log("filename YES");

            document.getElementById('filename').innerHTML = files[0].name;
        }

        if (!!files) {

            if (typeof(output) != 'undefined' && output != null) {
                output.classList.remove('quote-imgs-thumbs--hidden');
            }
            document.getElementById('uploadbutton').disabled = false;
        }

        if (typeof(output) != 'undefined' && output != null) {
            for (var i = 0; i < files.length; i++) {
                var img = document.createElement('img');
                img.src = URL.createObjectURL(event.target.files[i]);
                img.classList.add('img-preview-thumb');
                img.classList.add('remove');
                output.appendChild(img)
            }
        }

    } else {
        console.log("Your browser does not support File API");
    }
}

document.getElementById('files').addEventListener('change', handleFileSelect, false);