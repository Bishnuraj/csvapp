# Project bootstrap

from flask import Flask
from flask_restful import Api

import config
APP_HOST = getattr(config, 'APP_HOST', '127.0.0.1')
APP_PORT = getattr(config, 'APP_PORT', 8080)
APP_DEBUG = getattr(config, 'DEBUG', True)

from libs import logger
log = logger.getLogger(__name__)
log.info("Starting application...")

app = Flask(__name__)
api = Api(app, catch_all_404s=True)

from libs.sync_csv_redis import SyncCsvRedis
preprocessor = SyncCsvRedis()
preprocessor.sync_data()

log.info("Collecting resource endpoints...")
from resources.v1.csvdata import CsvDataResource
api.add_resource(CsvDataResource, '/v1/csvdata/<key>')

log.info("Binding to interface: %s:%d" % (APP_HOST, APP_PORT))
if __name__ == '__main__':
    app.run(debug=APP_DEBUG, host=APP_HOST, port=APP_PORT)
