# AI-React-Flask
This is a comprehensive template for building a React application with a Flask machine learning server. Originally cloned from 'https://github.com/kb22/ML-React-App-Template'.

## Tech Stack
- Backend
  - Flask
- Frontend
  - React

### How to Use
A detailed guide for using this repository can be found here: https://towardsdatascience.com/create-a-complete-machine-learning-web-application-using-react-and-flask-859340bddb33

# Setup Procedures
Use Create-react-app to start with a basic React app. Load Bootstrap for responsive website creation across multiple screen sizes. Add a form with dropdowns and Predict and Reset Prediction buttons in the App.js file. The form's state is updated on pressing the Predict button and the data is sent to the Flask backend. The App.css file is used to apply stylings.

The Flask app has a POST endpoint '/prediction' that accepts input values as json, converts it into an array, uses the classifier stored in the classifier.joblib to make a prediction, and returns the prediction result as json.

Clone the repository and undertake the following steps in two different terminals:

- In the first terminal, navigate to the ui folder using 'cd ui' and perform the following sequence:

    ```bash
      $ npm install
    ```

Install serve globally, build our application and finally run the UI using serve on port 3000.

    ```bash
      npm install -g serve
      npm run build
      serve -s build -l 3000
    ```

The UI should now be accessible at localhost:3000. However, the Flask service needs to be initiated separately.

- In the second terminal, navigate to the service folder using 'cd service' and perform the following sequence to create a virtual environment and run the Flask app:

    ```bash
      pipenv install -r requirements.txt
      pipenv shell
      flask run
    ```

This will initiate the Flask service on 127.0.0.1:5000. You can now access the backend via localhost.

The app uses a DecisionTreeClassifier on the iris dataset which requires 4 features — Sepal Length, Sepal Width, Petal Length and Petal Width. The model is pickled to classifier.joblib using joblib.dump(). To use the trained model for prediction on new data, the line 'classifier = joblib.load(‘classifier.joblib’)' is added to app.py.