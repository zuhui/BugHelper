#!/usr/bin/python3
#coding:utf-8

from bottle import template

import GetBugDatas
import  time



def BuildHtmlEmailText():

    datas = GetBugDatas.GetDatasFromPostgreSQL();
    new_datas = []
    keyWords=['ID','Title','Status','name','adress']

    for data in  datas:
        new_datas.append(dict(zip(keyWords,data)))
        print(new_datas)


    template_demo ="""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>尚未关闭BUG</title>
    </head>
    <body>
    <p>大家好！请大家关注一下最新BUG状态，如已解决请及时更新BUG状态！点击<a href="http://192.168.18.105:35080/projects" >Redmine</a>跳转！</p>     
    %
        <table border="1">
            <tr>
                <th>BUG ID</th>
                <th>BUG Title</th>
                <th>创建时间</th>
                <th>当前状态</th>
                <th>当前所有人</th>
            </tr>
        % for data in items:
                <tr>
                    <td>{{data[0]}}</td>
                    <td>{{data[1]}}</td>
                    <td>{{data[2]}}</td>
                    <td>{{data[3]}}</td>
                    <td>{{data[4]}}</td>
                </tr>
        %end
        </table>
    
    </body>
    </html>
    """

    html = template(template_demo,items = datas)

    nowDate = time.strftime('%Y%m%d%H%M%S',time.localtime())

    print(nowDate)

    fileName = nowDate+'.html';

    with open("files/"+fileName,'wb') as f:

        f.write(html.encode('utf-8'))

'''
if __name__=="__main__":
    BuildHtmlEmailText();
'''



