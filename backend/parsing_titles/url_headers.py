from dataclasses import dataclass


@dataclass
class ForPars:
    anime_url = 'https://animego.org/search/all?q='
    manga_url = 'https://mangalib.me/search?type=manga&q='
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 OPR/108.0.0.0',
        'Content-Type': 'application/json'    
    }
    cookies = {
        'yandexuid': '4016679951677575930',
        'yabs-sid': '2388635041677575931',
        'yuidss': '4016679951677575930',
        'gdpr': '0',
        '_ym_uid': '1677575935202834095',
        'yandex_login': 'jooniG',
        'skid': '8723648561701014451',
        'amcuid': '9353222731703749175',
        'ymex': '2024496939.yrts.1709136939',
        'yashr': '1895955331709137422',
        '_ym_d': '1709218226',
        'yabs-vdrf': 'IVDDboG3LlRu17z9bT06ANN415y9b20FGV6W1MhbbD03tBPW1jB9b-07ems01X8vbT07Jfem1lZXb5W15z2O1bJPbAm1w6LK00',
        'my': 'YwA=',
        'i': 'RKjxccNMwsPrhazy4YYiYLACgC9KHRAoSigdZdPzyWAT6CBrh4VcBvuZbylfpjU05Ks/d2ycP3kWtXTChEScmH+1+T4=',
        'is_gdpr': '0',
        'is_gdpr_b': 'CLj5IhCS8wEoAg==',
        'Session_id': '3:1711640663.5.0.1677576022316:wuKlBQ:27.1.2:1|1404953483.-1.2.3:1677576022|3:10285195.330675.zAd73-cPu9P5SnrTbfT2AdNaDGk',
        'sessar': '1.1188.CiAYYhUxrEK5t6wfZf6ESmZC8cqFZrwk-qhCBbdPoycMPA.8490-uyUcIy3u_QTU0yelOr4mrGu_iN0MmXIt1t0nfI',
        'sessionid2': '3:1711640663.5.0.1677576022316:wuKlBQ:27.1.2:1|1404953483.-1.2.3:1677576022|3:10285195.330675.fakesign0000000000000000000',
        '_ym_isad': '2',
        'bh': 'EjkiQ2hyb21pdW0iO3Y9IjEyMiIsICJOb3QoQTpCcmFuZCI7dj0iMjQiLCAiT3BlcmEiO3Y9IjEwOCIaBSJ4ODYiIg8iMTA4LjAuNTA2Ny40MCIqAj8wMgIiIjoJIldpbmRvd3MiQggiMTAuMC4wIkoEIjY0IlJTIkNocm9taXVtIjt2PSIxMjIuMC42MjYxLjEyOSIsIk5vdChBOkJyYW5kIjt2PSIyNC4wLjAuMCIsIk9wZXJhIjt2PSIxMDguMC41MDY3LjQwIiI=',
        'bh': 'EjciQ2hyb21pdW0iO3Y9IjEyMiIsIk5vdChBOkJyYW5kIjt2PSIyNCIsIk9wZXJhIjt2PSIxMDgiGgUieDg2IiIPIjEwOC4wLjUwNjcuNDAiKgI/MDICIiI6CSJXaW5kb3dzIkIIIjEwLjAuMCJKBCI2NCJSUyJDaHJvbWl1bSI7dj0iMTIyLjAuNjI2MS4xMjkiLCJOb3QoQTpCcmFuZCI7dj0iMjQuMC4wLjAiLCJPcGVyYSI7dj0iMTA4LjAuNTA2Ny40MCIi',
        'ys': 'udn.cDrQodC10YDRkdC20LA%3D#wprid.1711740668298085-17204677078905543350-balancer-l7leveler-kubr-yp-sas-82-BAL#c_chck.963194251',
        'yp': '1712154811.hdrc.0#1715009009.p_cl.1683473008#1723392188.p_sw.1691856188#1723392190.p_undefined.1691856189#2027100669.pcs.1#4294967295.skin.s#1714992260.stltp.serp_bk-map_1_1683456260#1992936022.udn.cDpqb29uaUc%3D#1714756103.v_sum_b_onb.1%3A1706980102870#1725515008.szm.1%3A1920x1080%3A1918x922#1712425421.csc.1',
    }


all_components = ForPars()