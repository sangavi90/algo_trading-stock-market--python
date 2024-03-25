from django.shortcuts import render
from django.http import JsonResponse,response
#from rest_framework.generics import APIView
from rest_framework.views import APIView
from rest_framework.response import Response

from SmartApi import SmartConnect,SmartWebSocket #or from SmartApi.smartConnect import SmartConnect
import pyotp
from logzero import logger
from django.conf import settings
from angelproject.settings import *
import requests
from rest_framework import status
import http.client
import mimetypes
import http.client
import json
import pandas
import http.client
import json
import pyotp
import time
import uuid 
import logging
