const express = require('express');
const fetch = require('node-fetch')
const app = express();

app.get("/", async (req, res) => {
    let id = req.query.id;
    if(!id || id == undefined) 
        return response.send("{code:400,\nmessage:'Input ID of Video'}");
    if(id.includes("youtube")){
	urls = id;
	var r, rx = /^.*(?:(?:youtu\.be\/|v\/|vi\/|u\/\w\/|embed\/)|(?:(?:watch)?\?v(?:i)?=|\&v(?:i)?=))([^#\&\?]*).*/;

    	r = urls.match(rx);
	id = r[1]
    }
    const response = await fetch('http://128.199.136.3/?id='+id);
    const json = await response.json();
    res.send(json);
});

const listener = app.listen(process.env.PORT, () => {
  console.log("Your app is listening on port " + listener.address().port);
});
