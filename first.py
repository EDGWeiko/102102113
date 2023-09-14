import requests
import re
import pandas as pd
fin = []
result = pd.DataFrame()

for i in range(1,9):        #进行循环，遍历1~8页，共计8*42=316个视频
    headers = {
        'cookie':'buvid3=D9871DF6-0182-41A1-90E9-E29CEBB7486B148819infoc; LIVE_BUVID=AUTO9716390622274942; i-wanna-go-back=-1; dy_spec_agreed=1; buvid_fp_plain=undefined; buvid4=E4F99F79-D38D-7772-1504-36D850DFC56126916-022012117-lmSCu3UJG4vA%2FTj4GqHC7g%3D%3D; b_nut=100; rpdid=0z9Zw2XN99|DXLF9xln|3nv|3w1OV9i5; CURRENT_BLACKGAP=0; header_theme_version=CLOSE; nostalgia_conf=-1; hit-new-style-dyn=1; CURRENT_PID=c743ef00-ca3c-11ed-9fc5-d1323b0c18bf; FEED_LIVE_VERSION=V8; hit-dyn-v2=1; CURRENT_FNVAL=4048; _uuid=F642C575-6692-97F8-D3A6-B4D3AC4A5CBC53115infoc; fingerprint=891cbadcde040e541b9d28e4fbfe5478; buvid_fp=891cbadcde040e541b9d28e4fbfe5478; home_feed_column=5; browser_resolution=1536-715; bp_video_offset_145023955=839673983345360951; CURRENT_QUALITY=64; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTQ2MDQ0MzcsImlhdCI6MTY5NDM0NTIzNywicGx0IjotMX0.pE66B5Gk8NaWPsEvwVGfeiBo4TxGcKmNgERMmnRSgbw; bili_ticket_expires=1694604437; SESSDATA=bd0c1774%2C1709897330%2C6e20b%2A92CjDXcZPHBQ_MJwl2s9cHqTAqf3_FPSjL5CCtvSHv8uRT40kJNyATrAWWiba_aAHLJdgSVmgya0pEN3VEOHdReHNrYlBBWHdNanFGZWdNUl8wTWxBTGxWZ01BUTFXSVdFYXc3eWZvclNNVjhaMUQ4dVJaSEhjYU14dVE2M3g2TFdrM1l2SFRFdWhRIIEC; bili_jct=49ac6574d21f7ddc5deef86b99513d32; DedeUserID=1071519264; DedeUserID__ckMd5=0cc7d57275e1b217; bp_video_offset_1071519264=839690596279910433; b_lsid=6102FE8F3_18A7F2B9259; innersign=0; sid=7dutxo2r; PVID=3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    }            #对爬虫进行伪装
    page = i
    url = f'https://api.bilibili.com/x/web-interface/wbi/search/type?page={page}&page_size=42&keyword=核污水&search_type=video'
    data_bvid = requests.get(url=url, headers=headers)
    ABV = re.findall('BV..........', data_bvid.text)        #利用正则表达式提取data_bvid中的BV号
    fin = ABV+fin          #将提取到的BV号添加至列表fin
for bv in fin:
    df = pd.DataFrame({'bv': [bv]})
    result = pd.concat([result, df])
result.to_csv('all300_bv.csv', encoding='utf-8-sig',index=False)        #将fin转换为列表并储存到excel文件