#! /usr/bin/python
# -*- coding=utf-8 -*-

import urllib2,urllib,json





def post_request( url, timeout, paramsDict, urlencode=True):
    """post requester
    """
    try:
        if urlencode:
            reqParams = urllib.urlencode(paramsDict)
        else:
            reqParams = json.dumps(paramsDict, ensure_ascii=False)
        req = urllib2.Request(url, reqParams)
        res = urllib2.urlopen(req, timeout=timeout)
    except Exception as error:
        raise error
    return res.readlines()


if __name__ == "__main__":

    url = "http://yq01-kg-mario8-dy.yq01.baidu.com:8199/rawbases/auth/listPermissionByUser"
    timeout = 2
    paramDict =  {
                    'username': 'liqian11',
                    'param': '{"host":"","cred":"wenxiang","user":""}',
                 }
    resp =  post_request(url, timeout, paramDict)
    print resp
    response = json.loads(resp[0])
    print response
    auth = response['data']
    print auth

    rawbase_name = 'dy_knowledge1'
    if rawbase_name not in auth \
            or not ('read' in auth[rawbase_name]
                    or 'read_write' in auth[rawbase_name]):
        print '403', rawbase_name