DEBUG = True
SECRET_KEY='pheno-db-secret-key-is-ou812'
MONGODB_SETTINGS = {'db': "phenodb", 'alias':'default', "host":'mongodb://localhost:27017'}
WWW={}

SEARCH_DB='data/search.db'

COMPRESS_DEBUG=True
COMPRESS_MIMETYPES=['text/tab-separated-values', 'text/html', 'text/css', 'text/xml', 'application/json', 'application/javascript']



HOST='0.0.0.0'
URL_HOST='127.0.0.1'
PORT=8082

URL_BASE='http://' + URL_HOST + ':' + str(PORT)
URL_BASE_STATIC=URL_BASE+'/static'


DATA = {}
DATA_CHROMOSOMES='../data/chromosomes.json'
DATA_HDF5='data/data_2sets.h5'
#DATA_HDF5='data/new_data.h5'
DATA_HDF5='data/btbr.h5'


####

WWW['APP_HEADER']='QTL Viewer'

WWW['DATASET_TEXT'] = 'Select a dataset'
WWW['DATASET_DEFAULT'] = None

# MATRIX PORTLET
WWW['MATRIX_HEADER'] = 'QTL Matrix Plot'
WWW['MATRIX_DATA_TAB_TEXT'] = 'Data Matrix'
WWW['MATRIX_LIST_TAB_TEXT'] = 'Data Matrix'
WWW['LOD_THRESHOLD_SLIDER_TEXT'] = 'LOD Score Threshold'
WWW['LOD_THRESHOLD_SLIDER_DEFAULT'] = 7
WWW['LOD_THRESHOLD_SLIDER_MIN'] = 1
WWW['LOD_THRESHOLD_SLIDER_MAX'] = 100
WWW['MATRIX_X_AXIS_TEXT'] = 'Marker Position'
WWW['MATRIX_Y_AXIS_TEXT'] = 'Gene Position'

# SEARCH PORTLET
WWW['SEARCH_HEADER'] = 'Gene Search'
WWW['SEARCH_SEARCH_TAB_TEXT'] = 'Gene Search'
WWW['SEARCH_HISTORY_TAB_TEXT'] = 'History'
WWW['SEARCH_BUTTON_FIND_TEXT'] = 'Find'

# LOD PORTLET
WWW['LOD_HEADER'] = 'LOD Score Plot'
WWW['LOD_X_AXIS_TEXT'] = 'Chromosome'
WWW['LOD_Y_AXIS_TEXT'] = 'LOD Score'

# EFFECT PORTLET
WWW['EFFECT_HEADER'] = 'Effect Plot'
WWW['EFFECT_X_AXIS_TEXT'] = 'Position (Mb)'
WWW['EFFECT_Y_AXIS_TEXT'] = 'Effect'

# FACTORIAL VIEWER PORTLET
WWW['FACT_HEADER'] = 'Factorial Viewer'
WWW['FACT_FACT_ORDER_HEADER'] = 'Factor Header'
WWW['FACT_FACT_ORDER_TEXT'] = 'Please select the order you would like the factors to be displayed'
WWW['FACT_BUTTON_PLOT_TEXT'] = 'Plot'



