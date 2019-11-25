

let interval = 1000;



function generateImages(){
const path = require('path');
const fs = require('fs');
//joining path of directory 
const directoryPath = path.join(__dirname, 'test.MP4');
//passsing directoryPath and callback function
fs.readdir(directoryPath, function (err, files) {
    //handling error
    if (err) {
        return console.log('Unable to scan directory: ' + err);
    } 
    //listing all files using forEach
    files.forEach(function (file) {
        if (file.endsWith(".jpg")){
        // Do whatever you want to do with the file
        console.log(file); 
        }
    });
});
}

function sleep(ms) {
    return new Promise(resolve=>{
        setTimeout(resolve,ms)
    })
}

async function begin() {
while(true) {

    generateImages();

        await sleep(interval);
    }
}
begin();

