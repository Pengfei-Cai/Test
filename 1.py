#!usr/bin/pthon3
# -*- coding: UTF-8 -*-
import click
from PIL import Image
import os

@click.command()
@click.option('-h','--pheight', prompt='Height',default=1, help='Height of picture.')
@click.option('-w','--pwidth', prompt='Width',default=1, help='Width of picture.')
@click.option('-ip','--inpath', prompt='InPicture path',help=' Path of picture getting.')
@click.option('-pp','--outpath', prompt='OutPicture path',help='Path of picture saving.')
def imShr(pheight,pwidth,inpath,outpath):
    im = Image.open(inpath)
    img_resize = im.resize((int(pheight),int(pwidth)),Image.ANTIALIAS)  # 调整尺寸
    imgn =  'cp' + os.path.basename(inpath)
    opath = os.path.join(outpath,imgn)
    img_resize.save(opath)

if __name__ == '__main__':
    imShr()


    #测试语句
