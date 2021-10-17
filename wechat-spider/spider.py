import json
import yaml
import time
import html
import requests


def read_file(dir):
    with open(dir, 'r+', encoding='utf-8') as file:
        return file.read()


def write_file(dir, plain):
    with open(dir, 'w+', encoding='utf-8') as file:
        file.write(plain)


def parse(offset, keys):
    url = "https://mp.weixin.qq.com/mp/profile_ext"
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 "
        "Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat QBCore/3.43.901.400 "
        "QQBrowser/9.0.2524.400",
    }
    proxies = {
        'https': None,
        'http': None,
    }
    param = {
        'action': 'getmsg',
        '__biz': keys['__biz'],
        'f': 'json',
        'offset': offset,
        'count': '10',
        'is_ok': '1',
        'scene': '124',
        'uin': keys['uin'],
        'key': keys['key'],
        'pass_ticket': keys['pass_ticket'],
        'wxtoken': '',
        'appmsg_token': keys['appmsg_token'],
        'x5': '0',
        'f': 'json',
    }

    reponse = requests.get(url, headers=headers, params=param, proxies=proxies)
    reponse_dict = reponse.json()
    # print(reponse_dict)
    next_offset = reponse_dict['next_offset']
    can_msg_continue = reponse_dict['can_msg_continue']
    general_msg_list = reponse_dict['general_msg_list']
    data_list = json.loads(general_msg_list)['list']
    # print(data_list)
    for data in data_list:
        try:
            id = data['comm_msg_info']['id']
            title = data['app_msg_ext_info']['title']
            date = time.strftime('%Y-%m-%d', \
                    time.localtime(data['comm_msg_info']['datetime']),)
            url = data['app_msg_ext_info']['content_url'] \
                    .replace("\\","") \
                    .replace("http", "https")
            url = html.unescape(url)
            print(id,title, date, url)
            plain = requests.get(url, headers=headers, proxies=proxies).content
            data = dict(id=id,
                        title=title,
                        date=str(date),
                        url=url,
                        plain=plain.decode('utf-8'))
            write_file(f'data/{id}.json', json.dumps(data, ensure_ascii=False))
        except Exception as e:
            print(data['comm_msg_info']['id'], 'skipped.')
    if can_msg_continue == 1:
        return next_offset
    else:
        return -1


def main():
    config = yaml.load(read_file('config.yml'), Loader=yaml.FullLoader)
    offset = config['offset']
    for _ in range(int(config['page'])):
        print(f'=== offset {offset} ===')
        offset = parse(offset, config['keys'])
        if offset == -1:
            break
    print(f'=== offset {offset} ===')


main()