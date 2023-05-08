from routes import *  # import routes of the web app and other necessary stuff

if __name__ == "__main__":  # run the blog app if this file is not imported
    app.run(debug=True,
            host="192.168.1.92")  # you can set port for server and when you like to connect to this server from your local network you must set host="ip_adress"
