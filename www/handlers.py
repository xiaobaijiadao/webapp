#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'WangXiao'

#' url handlers '
import re, time, json, logging, hashlib, base64, asyncio
from coroweb import get,post
from models import User, Comment, Blog, next_id


#编写用于测试的URL处理函数
@get('/')
async def index(request):
	users = await User.findAll() 
	res = {
		'__template__' : 'test.html',
		'users' : users
	}
	return res
    	

@get('/greeting')
async def handler_url_greeting(*,name,request):
    body='<h1>Awesome: /greeting %s</h1>'%name
    return body