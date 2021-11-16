import json
from flask_restful import Resource
from Random.RandomObjects import RandomObjects
from Models.random_models import GenerateModel
from flask import send_file
from io import BytesIO


class CreateRandom(Resource):

    @classmethod
    def get(cls):
        try:
            random_data = RandomObjects().random_objects_main()
            data = {'values': json.dumps(random_data[0]), 'file_id': random_data[2], 'data': json.dumps(random_data[1])}
            if data:
                user = GenerateModel(**data)
                user.save_to_db()
                url = 'http://127.0.0.1//api/download/{}'.format(data['file_id'])
                return {"message": "User created successfully.", "file_path": url}, 201
            return {"message": "A user with that username already exists"}, 400
        except Exception as error:
            return {'message': str(error[:10])}, 500


class GetReport(Resource):

    @classmethod
    def get(cls, file_id: int):
        """
        :param file_id: Id Primary Key, For every Insert
        :return: a dict with Report of the file
        """
        try:
            data = GenerateModel.find_by_file_id(file_id)
            if not data:
                return {'message': 'file not found create first.'}, 404
            by_index_data = ['float', 'numbers', 'alphanumeric', 'alphabets']
            _report_value = json.loads(data.json()['values'])
            return dict(zip(by_index_data, _report_value)), 200, {'content-type': 'application/json'}

        except Exception as error:
            return {'message': str(error[:10])}, 500


class Download(Resource):

    @classmethod
    def get(cls, file_id: int):
        try:
            data = GenerateModel.get_file_data(file_id)
            if data is not None:
                data = json.loads(data)
                buffer = BytesIO()
                for i in data:
                    buffer.write(i.encode('utf-8'))
                buffer.seek(0)
                return send_file(buffer, as_attachment=True,
                                 download_name='{}.txt'.format(file_id),
                                 mimetype='text/csv')

            return {'Message': 'No Data For The Request',
                    'hint': 'generate random first:{}'.format(' /api/generate/')}, 404
        except Exception as error:
            return {'message': str(error[:10])}, 500
