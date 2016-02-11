# Copyright (c) 2015 The Jackson Laboratory
#
# This software was developed by Gary Churchill's Lab at The Jackson
# Laboratory (see http://research.jax.org/faculty/churchill).
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software.  If not, see <http://www.gnu.org/licenses/>.

from flask import Flask, url_for, redirect, render_template, g
from flask import request, render_template

from qtl_viewer.views import general
from qtl_viewer.views import api
from qtl_viewer.utils import data_utils
from qtl_viewer.utils import search_utils

import h5py

app = Flask(__name__)
app.config.from_object('config')
app.register_blueprint(general.mod)
app.register_blueprint(api.mod)

class Config:
    pass

CONF = Config()

print 'we are here'

HDF_DATA = None
R_DATA = None

#@app.errorhandler(404)
#def not_found(error):
#    return render_template('general/404.html'), 404


@app.errorhandler(404)
def handle_404(e):
    path = request.path

    # go through each blueprint to find the prefix that matches the path
    # can't use request.blueprint since the routing didn't match anything
    for bp_name, bp in app.blueprints.items():

        if bp.url_prefix and path.startswith(bp.url_prefix):
            # get the 404 handler registered by the blueprint
            handler = app.error_handler_spec.get(bp_name, {}).get(404)

            if handler is not None:
                # if a handler was found, return it's response
                return handler(e)

    # return a default response
    return render_template('general/404.html'), 404



@app.before_request
def load_request():
    """
    Make sure the web and api portion have access to g.WWW
    """
    g.WWW = app.config['WWW']
    g.CONF = CONF




@app.before_first_request
def initialize():
    print 'Initializing'

    CONF.URL_BASE = app.config['URL_BASE']
    CONF.URL_STATIC = app.config['URL_BASE_STATIC']
    #CONF.URL_CHROMOSOME = app.config['URL_CHROMOSOME']
    #CONF.DATA_MATRIX = app.config['DATA_MATRIX']
    #CONF.DATA_RDATA = app.config['DATA_RDATA']

    CONF.DATA_CHROMOSOMES = app.config['DATA_CHROMOSOMES']




    HDF_FILENAME = app.config['DATA_HDF5']

    #R_DATA = ro.r['load'](CONF.DATA_RDATA)



    search_utils.DATABASE = app.config['SEARCH_DB']
    data_utils.HDF5_FILENAME = app.config['DATA_HDF5']
    data_utils.init()

    if 'DEFAULT_DATASET' in app.config:
        CONF.DEFAULT_DATASET = app.config['DEFAULT_DATASET']
    else:
        datasets = data_utils.get_datasets()
        CONF.DEFAULT_DATASET = datasets.keys()[0]

    print data_utils.HDF5_FILENAME
    print CONF.DEFAULT_DATASET

    print str(app.config)




