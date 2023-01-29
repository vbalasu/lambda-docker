def handler(event, context):
    try:
        query = event['query']
    except KeyError:
        query = "SELECT 'hello world' message;"
    try:
        format = event['format']
    except KeyError:
        format = 'csv'
    data = run_sql(query, format)
    return data


def run_sql(query="SELECT * from range(10)", format='csv'):
    from databricks import sql
    import os, json
    connection = sql.connect(
                            server_hostname = "adb-2548836972759138.18.azuredatabricks.net",
                            http_path = "/sql/1.0/warehouses/9fb2ea023126d1f4",
                            access_token = os.environ['DATABRICKS_TOKEN'])
    cursor = connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    if format == 'csv':
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
