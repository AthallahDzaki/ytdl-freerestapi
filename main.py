import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET','POST'])
def yta():
	if request.args.get('url'):
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


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=int(os.environ.get('PORT','3000')),debug=True)
