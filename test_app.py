import app

def test_handler():
    import dotenv, os
    dotenv.load_dotenv()
    options = {
        'server_hostname': os.environ.get('server_hostname'),
        'http_path': os.environ.get('http_path'),
        'access_token': os.environ.get('access_token')
    }
    data = app.handler(options, {})
    print(data)
    assert data is not None