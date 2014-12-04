# HTMLParser.py
# encoding utf-8
# read open.163.com course page video download links and write to file
# run with python3 cli, depends thirdparty lib: BeautifulSoup4 https://pypi.python.org/pypi/beautifulsoup4/4.3.2
# input:　update line 22 value; output: console log, a new file in pwd

import socket
import urllib.request
from bs4 import BeautifulSoup
import os
import re
import codecs

if __name__=="__main__":

      print('connect...')

      # timeout in seconds
      socket.setdefaulttimeout(20)

      # main page url of some course
      url = u'http://v.163.com/special/Khan/probability.html'

      user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0'
      headers = { 'User-Agent' : user_agent,
                  'Accept'     : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                  'Connection' : 'close'}

      req = urllib.request.Request(url, headers = headers)

      content = urllib.request.urlopen(req).read().decode('gb18030')

      print('parse...')

      # root = ET.fromstring(content)
      # root.findall("//table[@id='list2']/tbody/tr") # use xpath

      soup = BeautifulSoup(content)

      '''
        <td class="u-ctitle">
           [第1集]
            <a href="http://v.163.com/movie/2011/3/B/Q/M82IF3HFQ_M831V1DBQ.html">基本概率</a>
                <img src="http://img1.cache.netease.com/v/2011/1414.png" class="isyy">
        </td>

        <td class="u-cdown">
            <a class="downbtn" href="http://mov.bn.netease.com/mobilev/2012/8/1/E/S87AFUK1E.mp4"
                id="M831V1DBQ" target="_blank"></a>
        </td>
      '''
      count = 0;
      pwd = os.path.dirname(os.path.abspath(__file__))

      p = re.compile(r'\w+\.*\w*$')
      result = re.search(p, url).group(0)

      file = codecs.open(pwd + '/' + result + '.txt', 'a', 'utf-8')
      # title soup.title.string
      file.write('# ' + soup.title.string + '\n')

      for tag in soup.find_all('table', id='list2'):

          for tr in tag.children:

              if tr.name == 'tr':
                  title_str = ''
                  link_str = ''

                  for td in tr.find_all('td'):
                      try:
                          if 'u-ctitle'in td['class']:
                                title_str = td.contents[0].string  + td.contents[1].contents[0].string
                                title_str = title_str.replace('\n', '').replace('\r', '').replace(' ', '')

                          elif 'u-cdown' in td['class']:
                                link_str = td.contents[1]['href'];

                          if title_str and link_str:
                                count = count + 1
                                link_str = link_str + '        ' + title_str
                                link_str = link_str.replace('\n', '').replace('\r', '')
                                file.write(link_str + '\n')
                                print(link_str)
                      except:
                            pass

      file.close();
      print('row: ' + str(count) + ' done!')
