# from MSG_Template.text.user_conn import *
# from MSG_Template.text.key_conn import *
from linebot.models import *
from twstock import *
import twstock

def text_get_stock_info(key):
    stock = realtime.get(key)
    name = stock['info']['name']
    price = stock['realtime']['latest_trade_price']
    trade_volume = stock['realtime']['trade_volume']
    best_bid_price = stock['realtime']['best_bid_price'][0]
    best_ask_price = stock['realtime']['best_ask_price'][0]
    P_open = stock['realtime']['open']
    P_high = stock['realtime']['high']
    P_low = stock['realtime']['low']
    return TextMessage(text = f'股票名字: {name}\n最近成交價: {price}\n成交量: {trade_volume}\n開盤價: {P_open}\n最高價: {P_high}\n最低價: {P_low}')
    

# return TextMessage(text=f'{name} : 股價為 {price}')
    

# {'timestamp': 1610087400.0,
# 'info':
#     {'code': '2330',
#     'channel': '2330.tw',
#     'name': '台積電',
#     'fullname': '台灣積體電路製造股份有限公司',
#     'time': '2021-01-08 14:30:00'},

# 'realtime':
#     {'latest_trade_price': '580.0000',
#     'trade_volume': '7685',
#     'accumulate_trade_volume': '58882',
#     'best_bid_price': ['579.0000', '578.0000', '577.0000', '576.0000', '575.0000'],
#     'best_bid_volume': ['326', '341', '349', '431', '751'],
#     'best_ask_price': ['580.0000', '581.0000', '582.0000', '583.0000', '584.0000'],
#     'best_ask_volume': ['3340', '325', '451', '219', '151'],
#     'open': '580.0000',
#     'high': '580.0000',
#     'low': '571.0000'},
#     'success': True}