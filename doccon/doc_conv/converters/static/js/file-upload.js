// document.getElementById('file-input').addEventListener("change", function () {
//     document.getElementById('filecount')
// });

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


        // for (var i = 0; i < files.length; i++) {
        //     output.classList.remove('quote-imgs-thumbs--hidden')
        //     var file = files[i];
        //
        //     var picReader = new FileReader();
        //     picReader.addEventListener("load", function (event) {
        //         var picFile = event.target;
        //         var div = document.createElement("div");
        //         div.innerHTML = "<img class='img-preview-thumb' src='" + picFile.result + "'" + "title='" + file.name + "'/>";
        //         output.insertBefore(div, null);
        //     });
        //     //Read the image
        //     picReader.readAsDataURL(file);
        // }
        if (!!files) {
            console.log("files YES");

            if (typeof(output) != 'undefined' && output != null) {
                output.classList.remove('quote-imgs-thumbs--hidden');
            }
            document.getElementById('uploadbutton').disabled = false;
        }

        if (typeof(output) != 'undefined' && output != null) {
            console.log("Output YES");
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

// document.getElementById('files').addEventListener('change', handleFileSelect, false);


// let nav_button_1 = document.getElementById('button-1')
// let nav_button_2 = document.getElementById('button-2')
// let nav_button_3 = document.getElementById('button-3')
// let nav_button_4 = document.getElementById('button-4')
// let nav_button_5 = document.getElementById('button-5')



// document.querySelector('.navbar-nav').addEventListener('click', function(event) {
//     event.preventDefault();

//     let active_btn = document.querySelector('.active')

//     if (!event.target.classList.contains('active')) {
//         active_btn.classList.remove('active')
//         event.target.classList.add('active')
//     }
// })
