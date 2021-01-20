import bottle
import csv
import json
import urllib.request
import urllib.parse
import os.path
import appcode


@bottle.route('/')
def index():
  return bottle.static_file("index.html", root=  ".")

@bottle.route('/eshan.js')
def staticjs():
  return bottle.static_file("eshan.js", root= ".")

@bottle.route('/piegraph')
def piegraph():
  piegraph = json.dumps(appcode.piegraph())
  return piegraph

@bottle.route('/linegraph')
def linegraph():
  linegraph = json.dumps(appcode.linegraph())
  return linegraph

bottle.run(host='0.0.0.0', port=8080, debug=True)
