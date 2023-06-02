// document.getElementById('file-input').addEventListener("change", function () {
//     document.getElementById('filecount')
// });


document.getElementById('uploadbutton').addEventListener('click', function(event) {
    console.log("convert button clicked");
})


document.querySelector('.navbar-nav').addEventListener('click', function(event) {
    event.preventDefault();
    console.log("CLicked")
    let active_btn = document.querySelector('.active')

    if (!event.target.classList.contains('active')) {
        active_btn.classList.remove('active')
        event.target.classList.add('active')
    }
})

function deleteFolder() {
    // Get the folder name from the button.
    var folderName = this.getAttribute('data-folder-name');
    console.log("dedkjfkadsj");
    // Make a POST request to the delete_folder view.
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/delete_folder', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({
      folder_name: folderName
    }));
  
    // Handle the response.
    xhr.onload = function() {
      if (xhr.status === 200) {
        // The folder was deleted successfully.
        alert('Folder deleted successfully.');
      } else {
        // An error occurred.
        alert('Error deleting folder.');
      }
    };
  }

// deleteF.addEventListener('click', function(event) {
//     event.preventDefault();
//     console.log("Delete Button clicked");
// })


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




