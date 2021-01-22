from time import time as timestamp_unix_format
from json import loads as decode_json
from datetime import datetime
from requests import get


url = 'https://stats.uptimerobot.com/api/getMonitor/j8wEGcjZ7N?m=785845940'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.9 Safari/537.36'
}


def time_convert(timestamp_unix):
    return datetime.utcfromtimestamp(timestamp_unix).strftime('%d.%m.%Y %H:%M:%S')

def main():
    json_body = get(url, headers=headers)
    json_parsed = decode_json(json_body.text)
    return json_parsed

if __name__ == '__main__':
    body = main()
    print(
        'Name:',
        body['monitor']['name'],
        '\nTime response one:',
        str(body['monitor']['responseTimes'][0]['value'])+' ms',
        '\nTime response two:',
        str(body['monitor']['responseTimes'][1]['value'])+' ms',
        '\nTime response three:',
        str(body['monitor']['responseTimes'][2]['value'])+' ms',
        '\nAverage time:',
        str(round((body['monitor']['responseTimes'][0]['value']+body['monitor']['responseTimes'][1]['value']+body['monitor']['responseTimes'][2]['value'])/3))+' ms',
    )
    for el in body['monitor']['logs']:
        print(
            '*'*32,
            '\nAction:',
            el['label'],
            '\nDate:',
            el['date'],
            '\nDuration:',
            el['duration'],
            '\nStatus:',
            el['reason']['code']+' ('+el['reason']['detail']['short']+')',
        )
    print(
        '='*32,
        '\nStart:',
        time_convert(body['monitor']['createdAt']),
    )
    print(
        '='*32,
        '\nUpdated:',
        time_convert(int(timestamp_unix_format())),
    )
            
            
            
            
            
            
            
