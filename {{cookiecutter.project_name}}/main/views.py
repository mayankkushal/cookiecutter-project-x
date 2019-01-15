from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from keras.preprocessing import sequence
import tensorflow as tf
from keras.models import load_model
import pickle

from sklearn.externals import joblib

graph = tf.get_default_graph()

# load required files
def _load_model(filename=None):
    """
        Project specific -> returns the loaded model
    """
    if filename:
        return joblib.load(f'models/{{cookiecutter.model_name}}/{filename}')

# Model file name
model = _load_model()

class {{cookiecutter.model_view_name}}(APIView):
    def get(self, request, format=None):
        return Response({"details": "Welcome to {{cookiecutter.model_name}} analysis! Project-X"})

    def _predict(self):
        """
            Prediction logic goes here.
        """
        return prediction

    def _get_response(self):
        """
            Converts the prediction into a dict which can directly be passed
            as response.
            `Returns dict()`
        """
        prediction = self._predict()
        return {'score':prediction}


    def post(self, request, format=None):
        """
            `text`: text that needs to analyzed
        """
        self.text = request.data.get('text')
        if self.text: 
            return Response(self._get_response(), status=status.HTTP_201_CREATED)
        return Response({'details': "text not found"}, status=status.HTTP_400_BAD_REQUEST)