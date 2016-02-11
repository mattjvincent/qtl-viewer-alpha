from qtl_viewer.application import app
app.run(host='0.0.0.0', port=app.config['PORT'], threaded=True)
