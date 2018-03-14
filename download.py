

import sys
import glob

import queue
import threading
import urllib
import os
import re





def down(url,n,title):
    print ('item '+str(n)+' start ')
    filename=url.split('/')[-1].split('.')[0]
    urllib.request.urlretrieve(url, title+'/'+title+filename + '.jpg')
    print ('item '+str(n)+' finish ')


def worker():
    while True:
        i = q.get()
        url=i[0]
        n=i[1]
        down(url,n,title)
        q.task_done()

def open_allfile(path, filetype):
    data = []
    read_files = glob.glob(path + '*' + filetype)
    for i in read_files:
        with open(i, 'rb') as infile:
            data.append(infile.read())
    return data


def get_filename(path,filetype):
    import os
    name=[]
    for root,dirs,files in os.walk(path):
        for i in files:
            if filetype in i:
                name.append(i.replace(filetype,''))
    return name


def mkdir(path):

    # 判断路径是否存在
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)

        print (path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print (path + ' 目录已存在')
        return False



if __name__=="__main__":

    num_worker_threads=5
    path1 = 'urltxt'
    filetype2 = '.txt'
    data1 = open_allfile(path1, filetype2)
    name2 = get_filename(path1, filetype2)

    for title in name2 :
        mkdir(title)
        f=open('urltxt/'+ title+'.txt')
        l=f.readlines()
        q = queue.Queue()
        for i in range(num_worker_threads):
            t = threading.Thread(target=worker)
            t.daemon = True
            t.start()

        for i in range(0,len(l)):
            q.put((l[i],i))

        q.join()