import os
import sys
import configparser
from image import tweet2image
from imageflow import imageflow
from readtweet import readtweets
from queue import queue
import subprocess
from getkeys  import getkeys
from keyword_tweet_search import getkeyword
from flask import Flask
app = Flask(__name__)

@app.route('/starthere/<keyword>')

def main(keyword = ""):
  getkeyword(keyword)
  return keyword

if __name__ == '__main__':
  main()
