# oauth
add the html files inside a file name it templates in same directory as the .py codes

Application Guide 
![icon-256x256](https://github.com/Ys01005/oauth/assets/93677795/1ee42b4c-7fa3-4753-ad6c-8005a9d7a2e7)

Running the OAuth Authentication Server:

1. Open your terminal or command prompt.

2. Navigate to the directory where the authentication server code file is located. Use the `cd` command followed by the directory path to navigate to the correct location. 

3. Make sure you have the necessary dependencies installed. If Flask is not installed, you can install it by running the following command:  pip install flask

4. Run the authentication server by executing the code file. Use the following command:
   Python3 auth.py
5. The authentication server will start running and listen for incoming requests on port 5000.

Running the Client Server:
1. Open another terminal or command prompt.

2. Navigate to the directory where the client server code file is located. Use the `cd` command followed by the directory path to navigate to the correct location. 

3. Make sure you have the necessary dependencies installed. If Flask is not installed, you can install it by running the following command:   pip install flask
   

4. Run the client server by executing the code file. Use the following command:  Python3 client.py

5. The client server will start running and listen for incoming requests 

Running the Resource Server

1. Open another terminal or command prompt.

2. Navigate to the directory where the resource server code file is located. Use the `cd` command followed by the directory path to navigate to the correct location.

3. Make sure you have the necessary dependencies installed for the resource server. If the resource server code uses Flask or any other specific libraries, ensure that they are installed.

4. Run the resource server by executing the code file. Use the following command: Python3 resource.py

5. The resource server will start running and listen for incoming requests.

Accessing the Application

1. Open a web browser of your choice.

2. In the browser's address bar, enter the URL where the client server is running. The URL typically consists of `http://localhost:5000` or `http://127.0.0.1:5000`.

3. On the login page, enter the required credentials (username and password) that are already saved in the auth.py code and submit the form.

4. If the credentials are valid, you will be redirected to a success page indicating a successful login. You will also receive an access token, which may be displayed on the success page or sent as a response in the network request.

5. Use the provided access token to access protected resources by making requests to the resource server. Depending on the application's implementation, you may need to include the access token as a header in your requests or follow a specific API endpoint structure.

6. If the access token expires, follow the token refreshing process provided in the application. This typically involves sending a request to a specific endpoint on the client server, providing the refresh token, and receiving a new access token in response.
![walking-code](https://github.com/Ys01005/oauth/assets/93677795/47ea75b5-e9f2-4ac4-b219-4273a0007b42)

