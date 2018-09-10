import csv

def read_csvfile(file_path):
    """
    Generator function to read CSV file and process
    """
    with open(file_path) as csvdata:
        csvReader = csv.reader(csvdata)
        next(csvReader)

        for index, row in enumerate(csvReader):
            yield index, row
