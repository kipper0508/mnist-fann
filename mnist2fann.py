import argparse
import struct
import numpy as np
import matplotlib.pyplot as plt

def readLabel(filepath):
    data = open(filepath, 'rb').read()
    #fmt of struct unpack, > means big endian, i means integer, well, ii mean 2 integers
    fmt = '>ii'
    offset = 0
    magic_number, label_number = struct.unpack_from(fmt, data, offset)
    print('label number is {}'.format(label_number))
    #slide over the 2 numbers above
    offset += struct.calcsize(fmt)
    #B means unsigned char
    fmt = '>B'
    labels = np.empty(label_number)
    for i in range(label_number):
        labels[i] = struct.unpack_from(fmt, data, offset)[0]
        offset += struct.calcsize(fmt)

    #print(labels)

    return labels.astype(int)

def readImage(filepath):
    data = open(filepath, 'rb').read()
    #fmt of struct unpack, > means big endian, i means integer, well, iiii mean 4 integers
    fmt = '>iiii'
    offset = 0
    magic_number, img_number, height, width = struct.unpack_from(fmt, data, offset)
    print('image number is {}, height is {} and width is {}'.format(img_number, height, width))
    #slide over the 2 numbers above
    offset += struct.calcsize(fmt)
    #28x28
    image_size = height * width
    #B means unsigned char
    fmt = '>{}B'.format(image_size)
        
    images = np.empty((img_number, height, width))
    flat_images=[]
    for i in range(img_number):
        images[i] = np.array(struct.unpack_from(fmt, data, offset)).reshape((height, width))
        flat_images.append(images[i].flatten().astype(int).tolist())
        offset += struct.calcsize(fmt)

    '''
    print(flat_images[1], len(flat_images[1]))
    plt.imshow(images[1])
    plt.show()
    '''

    return flat_images
    

def main():
    
    parser = argparse.ArgumentParser('python mnist2fann.py')
    parser.add_argument("-L","--label", default="")
    parser.add_argument("-I","--image", default="")
    parser.add_argument("-O","--output", default="a.data")

    args = parser.parse_args()

    labels = readLabel(args.label)
    images = readImage(args.image)

    f = open(args.output, "w")
    data_cnt = len(labels)
    f.write(str(data_cnt))
    f.write(" 784")
    f.write(" 10\n")
    for i in range(data_cnt):
        f.write(str(images[i][0]))
        for j in range(1,784):
            f.write(" "+str(images[i][j]))
        f.write('\n')
        output = [0] * 10
        output[labels[i]] = 1
        f.write(str(output[0]))
        for j in range(1,10):
            f.write(" "+str(output[j]))
        f.write('\n')
    f.close()


if __name__ == '__main__':
    main()