import flask, pytest, json, config
from resources.v1.csvdata import CsvDataResource
from libs.csv_reader import read_csvfile

app = flask.Flask(__name__)

ASSETS_FOLDER = getattr(config, 'ASSETS_FOLDER', 'assets')
CSV_FILENAME = getattr(config, 'CSV_FILENAME', 'numbers.csv')

@pytest.yield_fixture
def client():
    """
    Fixture to return object for GET /v1/csvdata/<key> endpoint
    """
    with app.test_request_context():
        '''Returns a CsvData instance'''
        csv_client = CsvDataResource()
        yield csv_client

def test_csvdata(client):
    """
    Test data in all the records of the csv file
    """
    file_path = ASSETS_FOLDER + '/' + CSV_FILENAME

    try:
        for index, row in read_csvfile(file_path):
            response = client.get(row[0])
            assert response.status_code == 200
            assert response.content_type == 'application/json'
            assert json.loads(response.data) == {'status': True, 'data': {'key': str(row[0]), 'value': int(row[1])}}
    except:
        assert False

def test_incorrect_file():
    """
    Test if input incorrect filename will raises ValueError exception
    """
    file_path = "example.txt"
    with pytest.raises(IOError):
        with open(file_path):
            pass

def test_invalid_key(client):
    """
    Test with invalid key as GET parameter
    """
    key = 'example'
    response = client.get(key)
    assert response.status_code == 400
