import dask.dataframe as dd

def read():

    database = 'sqlite:///registered_voters.sqlite'

    registered08 = dd.read_sql_table('ALL', database, index_col='index')
    registered08.columns = registered08.columns.str.lower()

    registered08['year'] = 2008
    registered08 = registered08.rename(columns={'voters':'Total Voters'}).drop('party', axis='columns')

    return registered08


if __name__ == '__main__':
    df = load()
    print('The DataFrame has')
    print(' {} rows'.format(len(df)))
    print(' {} columns'.format(df.columns.shape[0]))

