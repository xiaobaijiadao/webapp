#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'wangxiao'

'''
JSON API definition
'''

import json, logging, inspect, functools

class APIError(Exception):
	'''
	the base APIError which contains error(required), data(optional) and message(optional).
	'''
	def __init__(self, error, data='', message=''):
		super(APIError, self).__init__(message)
		self.error = error
		self.data = data
		self.message = message

class APIValueError(APIError):
	'''
	Indicate the input value has error or invalid. The data specifies the error field of input form.
	表明输入数据有问题，data说明输入的错误字段
	'''
	def __init__(self, field, message=''):
		super(APIValueError,self).__init__('value: invalid',field, message)

class APIResourceNotFoundError(APIError):
	'''
	Indicate the resource was not found. The data specifies the resource name.
	表明找不到资源，data说明资源名字
	'''
	def __init__(self, field, message=''):
		super(APIResourceNotFoundError, self).__init__('value: notfound', field, message)

class APIPermissionError(APIError):
	'''
	Indicate the api has no permission
	接口没有权限
	'''
	def __init__(self, message=''):
		super(APIPermissionError, self).__init__('permission: forbidden', 'permission', message)
		
		

