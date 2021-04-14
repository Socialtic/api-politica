from app import app

appHost = 'localhost'
appPort = 8080
appDebug = True

if __name__ == '__main__':
    app.run(host=appHost, port=appPort, debug=appDebug)
