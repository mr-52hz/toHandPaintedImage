"""
des: 将图片转换为手绘风格
author: mr_52hz
date: 2020-11-19
"""
from PIL import Image
import numpy as np
import os


def toHandPaintedImage(p):
    file_name, extension = os.path.splitext(r'%s' % p)
    hand_painted_image_file_name = file_name+'_handful'+extension
    a = np.asarray(Image.open(p).convert('L')).astype('float')

    depth = 10
    grad = np.gradient(a)
    grad_x, grad_y = grad
    grad_x = grad_x * depth / 100
    grad_y = grad_y * depth / 100
    A = np.sqrt(grad_x ** 2 + grad_y ** 2 + 1.)
    uint_x = grad_x / A
    uint_y = grad_y / A
    uint_z = 1./A

    vec_el = np.pi / 2.2
    vec_az = np.pi / 4
    dx = np.cos(vec_el) * np.cos(vec_az)
    dy = np.cos(vec_el) * np.sin(vec_az)
    dz = np.sin(vec_el)

    b = 255 * (dx * uint_x + dy * uint_y + dz * uint_z)
    b = b.clip(0, 255)

    im = Image.fromarray(b.astype('uint8'))
    im.save(hand_painted_image_file_name)
    print(hand_painted_image_file_name, ' OK!')


if __name__ == '__main__':
    p = input('please input your pic path')
    toHandPaintedImage(p)
