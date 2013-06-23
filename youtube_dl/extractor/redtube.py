import re

from .common import InfoExtractor


class RedTubeIE(InfoExtractor):
    _VALID_URL = r'(?:http://)?(?:www\.)?redtube\.com/(?P<id>[0-9]+)'

    def _real_extract(self,url):
        mobj = re.match(self._VALID_URL, url)

        video_id = mobj.group('id')
        video_extension = 'mp4'        
        webpage = self._download_webpage(url, video_id)

        self.report_extraction(video_id)

        video_url = self._html_search_regex(r'<source src="(.+?)" type="video/mp4">',
            webpage, u'video URL')

        video_title = self._html_search_regex('<h1 class="videoTitle slidePanelMovable">(.+?)</h1>',
            webpage, u'title')

        return [{
            'id':       video_id,
            'url':      video_url,
            'ext':      video_extension,
            'title':    video_title,
        }]
