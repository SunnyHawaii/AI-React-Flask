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
      npm