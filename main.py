from app.datasource.basic import DataSource

if __name__ == '__main__':
    for source in DataSource.get_datasource():
        source.execute()