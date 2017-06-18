#! /usr/bin/python
# -*- coding=utf-8 -*-

from flask import Flask,jsonify,request,abort,url_for
from flask_httpauth import HTTPBasicAuth,make_response





app = Flask(__name__)


"""
权限验证
"""
auth = HTTPBasicAuth()


"""
认证逻辑接口:
后台根据username查询得到其密码（下面的案例简单的模仿）
return 的密码需要与http Head中用户提供的密码所一致，不一致则flask框架调用
unauthorized()，认为鉴权失败。
"""
@auth.get_password
def get_password(username):
    if username == 'miguel':
        return 'python'
    return None


"""
故障处理接口：
当flask鉴权失败则会调用该函数。
"""
@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 403)






"""
模拟数据
"""
tasks = [
            {
                'id': 1,
                'title': u'Buy groceries',
                'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
                'done': False
            },
            {
                'id': 2,
                'title': u'Learn Python',
                'description': u'Need to find a good Python tutorial on the web',
                'done': False
            }
        ]

@app.route('/todo/api/tasks', methods=['GET'])
@auth.login_required
def get_tasks():
    # jsonify 可以将dict转换为json
    return jsonify({'tasks': tasks})



@app.route('/todo/api/success', methods=['GET'])
def send_success():
    success_msg = {'code':200, 'message':"success", 'data':{'msg':"data..."}}
    return jsonify(success_msg)

"""
解析URL中传递来的参数：
"""
@app.route('/todo/api/tasks/<int:task_id>', methods=['GET'])
@auth.login_required
def get_task(task_id):
    task = filter(lambda t:t['id'] == task_id, tasks)
    if len(task) == 0:
        not_found__msg = {'code': 404, 'message': "404 NOT FOUND", 'data': None}
        return jsonify(not_found__msg)

    return jsonify({'task': map(make_public_task, task)[0]})


"""
POST
创建
"""
@app.route('/todo/api/tasks', methods=['POST'])
def create_task():
    print request.json , type(request.json)
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
                'id': tasks[-1]['id'] + 1,
                'title': request.json['title'],
                'description': request.json.get('description', ""),
                'done': False
            }
    tasks.append(task)
    return jsonify({'task': map(make_public_task, tasks)}), 201


"""
PUT
更新
"""
@app.route('/todo/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    print request.json['done'],type(request.json['done'])
    task = filter(lambda t:t['id'] == task_id, tasks)
    print task, "\n"
    if len(task) == 0:
        abort(400)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': map(make_public_task, task)[0]})



"""
DELETE
删除
"""
@app.route('/todo/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = filter(lambda a: a['id'] == task_id, tasks)
    print task, "\n"
    if len(task) == 0:
        abort(400)
    tasks.remove(task[0])
    return jsonify({'result':True, 'tasks': map(make_public_task, tasks)})



"""
优化RS-WS
返回uri
"""
def make_public_task(task):
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['id'] = task['id']
            new_task['uri'] = url_for('get_task', task_id=task['id'], _external=True)
        else:
            new_task[field] = task[field]
    return new_task











if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8701, debug=True)


    # print tasks , type(tasks)
    # print tasks[0], type(tasks[0])
    # print tasks[0].__getitem__("id")
    # print tasks[0]["id"]
    # print tasks[-1]

    # print tasks, type(tasks)
    # map(make_public_task, tasks)