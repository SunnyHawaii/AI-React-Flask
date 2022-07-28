from flask import Flask, request, jsonify, make_response
from flask_restplus import Api, Resource, fields
import joblib
import numpy as np
import sys

flask_app = Flask(__name__)
app = Api(app = flask_app,
		  version = "1.0",
		  title = "Iris React-Flask App",
		  description = "Predict results using a trained model")

name_space = app.namespace('prediction', description='Prediction APIs')

model = app.model('Prediction params',
				  {'sepalLength': fields.Float(required = True,
				  							   description="Sepal Length",
    					  				 	   help="Sepal Length cannot be blank"),
				  'sepalWidth': fields.Float(required = True,
				  							   description="Sepal Width",
    					  				 	   help="Sepal Width cannot be blank"),
				  'petalLength': fields.Float(required = True,
				  							description="Petal Length",
    					  				 	help="Petal Length cannot be blank"),
				  'petalWidth': fields.Float(required = True,
				  							description="Petal Width",
    					  				 	help="Petal Width cannot be blank")})

classifier = joblib.load('cl