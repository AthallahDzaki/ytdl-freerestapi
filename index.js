const express = require('express')
const app = express()
const readline = require('readline');
const ytdl = require('ytdl-core');
const ffmpeg = require('fluent-ffmpeg');
const anonfile = require('anonfile-lib');
const request = require('request');
const cheerio = require('cheerio');

app.get('/', function (req, res) {
    let id = req.query.id;
    if(!id || id == undefined) 
        return res.send("{code:400,\nmessage:"Input ID of Video"}");
    let stream = ytdl(id, {
    quality: 'highestaudio',
    });

    let start = Date.now();
    ffmpeg(stream)
    .audioBitrate(128)
    .save(`./output/${id}.mp3`)
    .on('progress', p => {
        readline.cursorTo(process.stdout, 0);
        process.stdout.write(`${p.targetSize}kb downloaded`);
    })
    .on('end', () => {
        console.log(`\ndone, thanks - ${(Date.now() - start) / 1000}s`);
    });
    let info;
    anonfile.upload(`./output/${id}.mp3`).then((info) => {
        info = info.data.file.url;
    });
    request(info, function (err, res, body) {
        if (err && res.statusCode !== 200) throw err;
        let $ = cheerio.load(body);
        $('div.container').each((i, value) => {
            $('div.row').each((i, value) => {
                    $(value).find('a.btn').each((j, data) => {
                        res.json($(data).attr('href')+",\n'Author':'./RootCracker.sh'");
                 });
            });
        });
    });
    const fs = require('fs')

    const path = './output/'+id+'.mp3'

    try {
        fs.unlinkSync(path).then(console.log("File Removed");
    } catch(err) {
        console.error(err)
    }
})

app.listen(3000)
