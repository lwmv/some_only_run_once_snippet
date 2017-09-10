import lxml.html
from lxml.etree import HTMLParser

file_out = open('music_list.csv','w',encoding='utf_8_sig')
print('title,length,singer,album',file=file_out,flush=True)

tbody = lxml.html.parse('parse_music_list.txt', HTMLParser(encoding='gbk')).find('.//tbody')

for tr in tbody:
    song_title  = tr[1].find('.//b').get('title')
    song_length = tr[2].find('.//span').text
    song_singer = tr[3].find('.//div').get('title')
    song_album  = tr[4].find('.//a').get('title')
    print('"{0}","{1}","{2}","{3}"'.format(song_title,song_length,song_singer,song_album).replace('\xa0',' '),file=file_out)

file_out.close()



    

