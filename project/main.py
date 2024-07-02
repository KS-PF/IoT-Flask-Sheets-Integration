from flask import (
    Blueprint, render_template, request,
)
from datetime import datetime
import gspread

bp = Blueprint('main', __name__, url_prefix='/')  


#認証情報
credentials = {
#ダウンロードしたJsonファイルの情報を貼り付ける
}


@bp.route('/', methods=('GET', 'POST'))
def main():
    gc = gspread.service_account_from_dict(credentials)

    sh = gc.open('')#スプレッドシートの名前を入力する

    worksheet = sh.sheet1
    temp_list = worksheet.col_values(2)#2行目を全て取得
    date_list = worksheet.col_values(3)#3行目を全て取得
    msg_list = worksheet.col_values(4)#4行目を全て取得

    #タイトルの削除
    temp_list.pop(0)
    date_list.pop(0)
    msg_list.pop(0)

    toJapanese = {
        'Comfortable temperature':'過ごしやすい気温',
        'Beware of heat':'暑さに注意が必要',
        'Beware of cold':'寒さに注意が必要',
    }

    date_listS = [datetime.strptime(date, '%m/%d/%Y, %I:%M:%S %p') for date in date_list]

    data = []

    temp = request.args.get('temp', 'no')
    l = ['high', 'low', 'no']

    if temp not in l:
        temp = 'no'

    for i in range(len(temp_list)):
        if temp == 'no':
            row = [temp_list[i], date_listS[i], toJapanese[msg_list[i]],]
            data.append(row)

        elif temp == 'high':
            if int(temp_list[i]) >= 30:
                row = [temp_list[i], date_listS[i], toJapanese[msg_list[i]],]
                data.append(row)
        
        elif temp == 'low':
            if int(temp_list[i]) <= 10:
                row = [temp_list[i], date_listS[i], toJapanese[msg_list[i]],]
                data.append(row)

    return render_template('index.html', 
                data=data, 
                temp_list=temp_list, date_list=date_list, 
            )
