# -*- coding=utf-8 -*-
from __future__ import unicode_literals
from flask import Flask, jsonify, request, abort, url_for, json
from flask_restplus import Api, Resource, fields


app = Flask(__name__)
api = Api(app, version='1.0', title='Sample API', description='A sample API',)

ns = api.namespace('Task', description='Task API : falsk-restplus demo')




# 模拟数据
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

# task_model = api.model('Task' , {
#     'id': fields.Integer(readOnly=True, description='The task unique identifier'),
#     'title': fields.String(readOnly=True, description='The task Title'),
#     'description': fields.String(readOnly=True, description='The task description'),
#     'task': fields.String(readOnly=True, description='The task details')
# })

task_model = api.model('Task', {
    'task': fields.String(required=True, description='The task details')
})


@ns.route('/hello')                   #  Create a URL route to this resource
class HelloWorld(Resource):            #  Create a RESTful resource
    def get(self):                     #  Create GET endpoint
        return {'hello': 'world'}


@ns.route('/todo/api/tasks')
class TaskList(Resource):
    """ ts """
    def get(self):
        return {'tasks': tasks}


@ns.route('/todo/api/tasks/<int:task_id>', endpoint='get_by_task_id')
@ns.param('task_id', 'An task ID')
class Task(Resource):
    """
    test
    """
    @ns.marshal_with(task_model)
    def get(self, task_id):
        task = filter(lambda t: t['id'] == task_id, tasks)
        if len(task) == 0:
            not_found__msg = {'code': 404, 'message': "404 NOT FOUND", 'data': None}
            return jsonify(not_found__msg)
        print '----', task , jsonify({'task': task})
        # print '----', jsonify({'task': map(make_public_task, task)[0]})
        # return jsonify({'task': map(make_public_task, task)[0]})
        return {'task': task}


@ns.route('/todo/api/success')
class SuccessMsg(Resource):
    def get(self):
        success_msg = {'code': 200, 'message': "success", 'data': {'msg': "data..."}}
        return jsonify(success_msg)


def make_public_task(task):
    """
    优化RS-WS
    返回uri
    :param task:
    :return:
    """
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['id'] = task['id']
            new_task['uri'] = url_for('get_by_task_id', task_id=task['id'], _external=True)
        else:
            new_task[field] = task[field]
    return new_task


ns2 = api.namespace('Swagger', description='Swagger API : generate swagger json for task api')


@ns2.route('/api/')
class SwaggerJson(Resource):
    """ swagget json """
    def get(self):
        return jsonify(api.__schema__)


if __name__ == '__main__':
    app.run(debug=True)                #  Start a development server
