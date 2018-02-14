# *- coding:utf-8 *-
from QcloudApi.qcloudapi import QcloudApi
import random
import json
'''
module: 设置需要加载的模块
已有的模块列表：
cvm      对应   cvm.api.qcloud.com
cdb      对应   cdb.api.qcloud.com
lb       对应   lb.api.qcloud.com
trade    对应   trade.api.qcloud.com
sec      对应   csec.api.qcloud.com
image    对应   image.api.qcloud.com
monitor  对应   monitor.api.qcloud.com
cdn      对应   cdn.api.qcloud.com
'''
def transTX(srcStr,srcL,tarL):
	with open("config.json","r") as confile:
		configJson=json.load(confile)
	module = 'tmt'

	'''
	action: 对应接口的接口名，请参考产品 API 文档上对应接口的接口名
	'''
	action = 'TextTranslate'

	'''
	config: 云API的公共参数
	'''
	config = {
	    'Region' : 'gz',
	    'secretId' : configJson["secretId"],
	    'secretKey': configJson["secretKey"]
	}

	# 接口参数
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