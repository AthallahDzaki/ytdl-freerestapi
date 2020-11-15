var Downloader = require("./downloader");
var dl = new Downloader();

dl.getMP3({videoId: "Vhd6Kc4TZls", name: "Cold Funk - Funkorama.mp3"}, function(err,res){
    if(err)
        throw err;
    else{
        console.log("Song "+ i + " was downloaded: " + res.file);
    }
});
