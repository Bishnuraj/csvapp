import logger, config, redis
from settings.redis_conn import redis_connection
from csv_reader import read_csvfile

ASSETS_FOLDER = getattr(config, 'ASSETS_FOLDER')
CSV_FILENAME = getattr(config, 'CSV_FILENAME')
INSERTION_LIMIT = 100

log = logger.getLogger(__name__)

class SyncCsvRedis():
    """
    Update CSV data from file system to redis
    """
    def sync_data(self):
        file_path = ASSETS_FOLDER + '/' + CSV_FILENAME
        log.info("Initiating to load csv file to redis db...")

        try:
            with redis_connection.pipeline() as pipe:
                pipe.multi()

                # set records into redis pipeline in chunks
                for index, row in read_csvfile(file_path):
                    pipe.setnx(str(row[0]).lower(), row[1])
                    if (index+1) % INSERTION_LIMIT == 0:
                        pipe.execute()
                        pipe.multi()

                pipe.execute()
        except redis.RedisError as e:
            log.error('Unable to connect to Redis DB: ' + str(e))
        except Exception as e:
            log.error('Unable to sync csv data to redis: ' + str(e))
