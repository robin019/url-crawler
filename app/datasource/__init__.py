from app.persistence.sql import connection as pscon
import ijson
import abc
from settings import config
from datetime import datetime


class DataSource(metaclass=abc.ABCMeta):
    # Check unique constraint first and insert into two tables (malicious_url & malicious_url_detail)
    # Since the input URL may be extremely long, the unique constraint is set on md5(lower(url))
    url_parameterized_insert = f"""WITH ins0 AS(
INSERT INTO malicious_url (url) VALUES (%s) ON CONFLICT(md5(lower(url))) DO UPDATE SET url = %s RETURNING id)
INSERT INTO malicious_url_detail
    (url_id, source, source_id, verification_time) SELECT id, %s, %s, %s FROM ins0
    ON CONFLICT (url_id, source) DO UPDATE SET verification_time = %s;
    """

    @classmethod
    def insert(cls, values):
        batches = []
        for value in values:
            # remove the last character of url if it ends with /
            if value['url'][-1] == '/':
                value['url'] = value['url'][:-1]
            batches.append([value['url'],
                            value['url'],
                            value['source'],
                            '' if 'source_id' not in value else value['source_id'],
                            # since column source_id is optional
                            value['verification_time'],
                            value['verification_time']])
        with pscon.cursor() as cursor:
            cursor.executemany(cls.url_parameterized_insert, batches)
            pscon.commit()

    @staticmethod
    def get_datasource():
        return [PhishTank(), OpenPhish()]

    @abc.abstractmethod
    def execute(self):
        pass


class PhishTank(DataSource):
    def execute(self):
        # Load data downloaded from https://phishtank.com/
        with open(config.DATA_PHISHTANK) as phish_list_data:

            # Using ijson to parse objects from a stream of json to avoid large memory usage
            phish_list = ijson.items(phish_list_data, 'item')

            values = []
            for data in phish_list:
                values.append({
                    'url': data['url'],
                    'source': 'PhishTank',
                    'source_id': data['phish_id'],
                    'verification_time': data['verification_time'],
                })
                # Insert 1000 rows into database at a time
                if len(values) == 1000:
                    self.insert(values)
                    values.clear()
            self.insert(values)


class OpenPhish(DataSource):
    def execute(self):
        # Load data downloaded from https://openphish.com/phishing_feeds.html
        with open('./url_data/OpenPhish.txt') as file:
            line = file.readline()
            values = []
            while line and line != '':
                values.append({
                    'url': line[:-1],  # remove \n at the end of the string
                    'source': 'OpenPhish',
                    'verification_time': datetime.now()  # OpenPhish free licence does not offer verification time
                })
                # Insert 1000 rows into database at a time
                if len(values) == 1000:
                    self.insert(values)
                    values.clear()

                line = file.readline()
            self.insert(values)
