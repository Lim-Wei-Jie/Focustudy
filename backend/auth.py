from flask import Flask, url_for, session, render_template, redirect, request, jsonify
from authlib.integrations.flask_client import OAuth
import os
 
app = Flask(__name__)



if __name__ == '__main__':
  app.run(port=5000, debug=True)