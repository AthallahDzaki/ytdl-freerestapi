from flask import Flask, request
from bs4 import BeautifulSoup as bs
from requests import get, post
import os, math, json, random, re, html_text


app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET','POST'])
def yta():
	if request.args.get('url'):
		if request.args.get('v2'):
			try:
				url = request.args.get('url').replace('[','').replace(']','')
				yta = post('https://www.y2mate.com/mates/en60/analyze/ajax',data={'url':url,'q_auto':'0','ajax':'1'}).json()
				yaha = bs(yta['result'], 'html.parser').findAll('td')
				filesize = yaha[len(yaha)-10].text
				id = re.findall('var k__id = "(.*?)"', yta['result'])
				thumb = bs(yta['result'], 'html.parser').find('img')['src']
				title = bs(yta['result'], 'html.parser').find('b').text
				dl_link = bs(post('https://www.y2mate.com/mates/en60/convert',data={'type':url.split('/')[2],'_id':id[0],'v_id':url.split('/')[3],'ajax':'1','token':'','ftype':'mp3','fquality':'128'}).json()['result'],'html.parser').find('a')['href']
				return {
					'status': 200,
					'title': title,
					'thumb': thumb,
					'filesize': filesize,
					'result': dl_link,
					'ext': 'mp3'
				}
			except Exception as e:
				print('Error : %s' % e)
				return {
					'status': False,
					'error': '[❗] Terjadi kesalahan mungkin link yang anda kirim tidak valid!'
				}
		else:
			try:
				url = request.args.get('url').replace('[','').replace(']','')
				yta = post('https://www.y2mate.com/mates/en60/analyze/ajax',data={'url':url,'q_auto':'0','ajax':'1'}).json()
				yaha = bs(yta['result'], 'html.parser').findAll('td')
				filesize = yaha[len(yaha)-10].text
				id = re.findall('var k__id = "(.*?)"', yta['result'])
				thumb = bs(yta['result'], 'html.parser').find('img')['src']
				title = bs(yta['result'], 'html.parser').find('b').text
				dl_link = bs(post('https://www.y2mate.com/mates/en60/convert',data={'type':url.split('/')[2],'_id':id[0],'v_id':url.split('/')[3],'ajax':'1','token':'','ftype':'mp3','fquality':'128'}).json()['result'],'html.parser').find('a')['href']
				return {
					'status': 200,
					'title': title,
					'thumb': thumb,
					'filesize': filesize,
					'result': dl_link,
					'ext': 'mp3'
				}
			except Exception as e:
				print('Error : %s' % e)
				return {
					'status': False,
					'error': '[❗] Terjadi kesalahan mungkin link yang anda kirim tidak valid!'
				}
	else:
		return {
			'status': False,
			'msg': '[!] Masukkan parameter url'
		}
@app.route('/debug', methods=['GET','POST'])
def download():
	self.vid =  request.args.get('vid'):
	
 	Generate="https://{}.y2mate.com/analyze/ajax"
        Convert="https://{}.y2mate.com/convert"
        Headers={
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.",
                "Referer": "https://y2mate.com/",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        }
        def __init__(self,vid:str,ftype:str="mp4",fquality:str="720p")->None:
                self.ftype=ftype
                self.fquality=fquality
                self.v_id=vid
                self._id,self.v_id=self._videourl()
                self._videourl(True)
        def _save(self,status:bool=True)-> bool:
                super().__init__(url=self.videolink,name=self.name,status=status)
                return True
        def _server(self,new:bool=True):
                if new:
                        self.Data_Gen={"url": "https://www.youtube.com/watch?v={self.v_id}","q_auto": 0,"ajax": "1"}
                if not new:
                        self.Data_Convert={"type":"youtube","_id":self._id,"v_id":self.v_id,"ajax":"1","ftype":self.ftype,"fquality":self.fquality}
                self.sub="mate"+str(choice(["{i:02d}" for i in range(1,12)]))
        def _videourl(self,new:bool=False)->list:
                if not new:
                        self._server()
                        gen=requests.post(self.Generate.format(self.sub), data=self.Data_Gen, headers=self.Headers).text
                        return re.findall("_id: '(.*?)'", gen)
                if new:
                        self._server(False)
                        res=requests.post(self.Convert.format(self.sub), data=self.Data_Convert, headers=self.Headers)
                        self.name='{randint(10000000,99999999)}.{self.ftype}'
			self.videolink=re.findall('<a href="(.*?)"',loads(res.text)['result'])[0]
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=int(os.environ.get('PORT','3000')),debug=True)
