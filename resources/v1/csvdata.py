from flask import make_response, jsonify
from flask_restful import Resource
from settings.redis_conn import redis_connection

import redis
from libs import logger
log = logger.getLogger(__name__)

class CsvDataResource(Resource):

    def get(self, key):
        """
        API Endpoint: GET /v1/csvdata/<key>
        """
        log.info("GET csv file record by Key: {}".format(key.encode('utf-8')))

        try:
            value = redis_connection.get(key.lower())
            if value is not None:
                # format value, if integer
                try:
                    data = {'key': key, 'value': int(value)}
                except ValueError:
                    data = {'key': key, 'value': value}
                return make_response(jsonify({'status':True,'data':data}), 200)
        except redis.RedisError as e:
            log.error('Unable to connect to Redis DB: ' + str(e))
        except Exception as e:
            log.warning('Redis connection error: ' + str(e))

        return make_response(jsonify({'status': False,'error': 'Invalid Key'}), 400)
