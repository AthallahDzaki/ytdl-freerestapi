const readline = require('readline');
const ytdl = require('ytdl-core');
const ffmpeg = require('fluent-ffmpeg');
const anonfile = require('anonfile-lib');
const request = require('request');
const cheerio = require('cheerio');
const express = require("express");
const app = express();

app.get("/", async (req, response) => {
  let id = req.query.id;
    if(!id || id == undefined) 
        return response.send("{code:400,\nmessage:'Input ID of Video'}");
  let stream, info, infod
    try{ 
        stream = ytdl(id, {
          quality: 'highestaudio',
        })
      }
        catch(err) { 
        return response.send("{code:400,\nmessage:'"+err+"'}");
    };

    let start = Date.now();
    ffmpeg(stream)
    .audioBitrate(128)
    .save(`./output/${id}.mp3`)
    .on('progress', p => {
        console.log("Converting......")
    })
    .on('end', async () => {
        console.log(`\ndone, thanks - ${(Date.now() - start) / 1000}s`);
        await anonfile.upload(`./output/${id}.mp3`).then((info) => {
        infod = info.data.file.url.full;
      }).then(async () => {
      console.log(infod)
      await request({url:infod}, function (err, res, body) {
        if (err) throw err;
        let $ = cheerio.load(body);
        $('div.container').each((i, value) => {
            $('div.row').each((i, value) => {
                    $(value).find('a.btn').each((j, data) => {
			console.log($(data).attr('href'));
                        response.json("{'url':'"+$(data).attr('href')+"'}");
                 });
            });
        });
    });
        })
           const fs = require('fs')

            const path = './output/'+id+'.mp3'
            try {
              fs.unlinkSync(path);
	      console.log("File Removed")
            } catch(err) {
              console.error(err)
            }   
    });
});

const listener = app.listen(80, () => {
  console.log("Your app is listening on port " + listener.address().port);
});
