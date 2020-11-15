const DownloadYTFile = require('yt-dl-playlist')
 
const downloader = new DownloadYTFile({ 
  outputPath: process.cwd(),
  ffmpegPath: './ffmpeg/bin/ffmpeg.exe',
  maxParallelDownload: 10,
  fileNameGenerator: (videoTitle) => {
    return 'a-new-file-name.mp3'
  }
})
