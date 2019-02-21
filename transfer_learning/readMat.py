import scipy.io
import os

cwd = os.getcwd()
mat = scipy.io.loadmat('cars_train_annos.mat')
classes = mat['annotations']['class']

for mytype in range(1,196):
    os.mkdir(cwd + '/cars_train/' + str(mytype))
    os.mkdir(cwd + '/cars_val/' + str(mytype))
    for index in range(0,9):
        if classes[0][index][0][0] == mytype:
            print(index,mytype)
            org = cwd + '/cars_train/' + '0000' + str(index+1) + '.jpg'
            dest = cwd + '/cars_train/' + str(mytype) + '/' + '0000' + str(index+1) + '.jpg'
            os.rename(org, dest)
    for index in range(10,99):
        if classes[0][index][0][0] == mytype:
            print(index,mytype)
            org = cwd + '/cars_train/' + '000' + str(index+1) + '.jpg'
            dest = cwd + '/cars_train/' + str(mytype) + '/' + '000' + str(index+1) + '.jpg'
            os.rename(org, dest)
    for index in range(100,999):
        if classes[0][index][0][0] == mytype:
            print(index,mytype)
            org = cwd + '/cars_train/' + '00' + str(index+1) + '.jpg'
            dest = cwd + '/cars_train/' + str(mytype) + '/' + '00' + str(index+1) + '.jpg'
            os.rename(org, dest)
    for index in range(1000,3999):
        if classes[0][index][0][0] == mytype:
            print(index,mytype)
            org = cwd + '/cars_train/' + '0' + str(index+1) + '.jpg'
            dest = cwd + '/cars_train/' + str(mytype) + '/' + '0' + str(index+1) + '.jpg'
            os.rename(org, dest)
    for index in range(4000,classes.size):
        if classes[0][index][0][0] == mytype:
            print(index,mytype)
            org = cwd + '/cars_train/' + '0' + str(index+1) + '.jpg'
            dest = cwd + '/cars_val/' + str(mytype) + '/' + '00' + str(index+1) + '.jpg'
            os.rename(org, dest)
