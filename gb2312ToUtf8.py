import os
import string
def gb2312ToUtf8(path):
    files = os.listdir(path)
    for filename in files:
        if os.path.isdir(filename):
            print "file folds:%s\n" % filename
            gbkToUtf8(filename)
            continue

        try:
            tokens = string.splitfields(filename, '.')
            if len(tokens) != 2 or tokens[1] != 'csv':
                #print tokens[1]
                continue
            else:
                print 'Encode Converting (GB2312 to UTF-8) : ', filename       
                utfFile=open(path+filename)
                tstr = utfFile.read().decode("gb2312")
                tstr = tstr.encode("UTF-8")
                utfFile.close()
                utfFile = open(path+filename, 'w')
                utfFile.write(tstr)
                utfFile.close()
                print "OK!"
        except:
            "error %s" %filename
gb2312ToUtf8("C:/Users/Administrator/Desktop/test/")
