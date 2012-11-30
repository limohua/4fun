#/usr/bin/env python

try:
    f=open("/tmp/tmp","r")
    f.write("this is a tmp file for test, could you read it?")
except Exception as ex:
    print "read write error:%s" % ex


