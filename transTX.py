from QcloudApi.qcloudapi import QcloudApi
import random
import json

def transTX(srcStr,srcL,tarL):
	with open("config.json","r") as confile:
		configJson=json.load(confile)
	module = 'tmt'


	action = 'TextTranslate'

	config = {
	    'Region' : 'gz',
	    'secretId' : configJson["secretId"],
	    'secretKey': configJson["secretKey"]
	}

	action_params = {
		'sourceText': srcStr,
	    'source': srcL,
	    'target': tarL
	}

	try:
	    service = QcloudApi(module, config)
	    service.generateUrl(action, action_params)
	    # print(service.generateUrl(action, action_params))
	    str_json=str(service.call(action, action_params), encoding = "utf-8")
	    # print(str_json)
	    datarturn=json.loads(str_json)
	    return datarturn['targetText']
	except Exception as e:
	    import traceback
	    print('traceback.format_exc():\n%s' % traceback.format_exc())