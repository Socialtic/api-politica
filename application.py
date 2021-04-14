from app import application

appHost = '0.0.0.0'
appDebug = True

if __name__ == '__main__':
    application.run(host=appHost, debug=appDebug)
