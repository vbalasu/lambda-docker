def handler(event, context):
    import copy
    options = copy.deepcopy(event)
    if not 'query' in options:
        options['query'] = "SELECT 'hello world' message;"
    if not 'format' in options:
        options['format'] = 'csv'
    if not 'server_hostname' in options:
        raise Exception('server_hostname is not specified')
    if not 'http_path' in options:
        raise Exception('http_path is not specified')
    if not 'access_token' in options:
        raise Exception('access_token is not specified')
    data = run_sql(options)
    return data


def run_sql(options):
    from databricks import sql
    import os, json
    connection = sql.connect(
                            server_hostname = os.environ.get('server_hostname'),
                            http_path = os.environ.get('http_path'),
                            access_token = os.environ.get('access_token'))
    cursor = connection.cursor()
    cursor.execute(options['query'])
    rows = cursor.fetchall()
    if options['format'] == 'csv':
        import csv
        from io import StringIO
        # Create a file-like buffer to receive CSV data.
        buf = StringIO()
        # Create a CSV writer
        writer = csv.writer(buf)
        # Write the column names
        writer.writerow([i[0] for i in cursor.description])
        # Write the data rows
        writer.writerows(rows)
        # Get the value stored in the StringIO buffer
        data = buf.getvalue()
    else:
        data = json.dumps(rows)
    cursor.close()
    connection.close()
    return data
