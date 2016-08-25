import matplotlib
matplotlib.use('Agg')
from dataObj.image import cifarObj
from tf.fista import FISTA
#from plot.roc import makeRocCurve
import numpy as np
import pdb

trainImageLists =  "/home/slundquist/mountData/datasets/cifar/images/train.txt"
#testImageLists = "/home/slundquist/mountData/datasets/cifar/images/test.txt"
randImageSeed = None
#Get object from which tensorflow will pull data from
trainDataObj = cifarObj(trainImageLists, resizeMethod="pad", shuffle=True, seed=randImageSeed)
#testDataObj = cifarObj(testImageLists, resizeMethod="pad")

#FISTA params
params = {
    #Base output directory
    'outDir':          "/home/slundquist/mountData/tfSparseCode/",
    #Inner run directory
    'runDir':          "/fista_cifar_nf256/",
    'tfDir':           "/tfout",
    #Save parameters
    'ckptDir':         "/checkpoints/",
    'saveFile':        "/save-model",
    'savePeriod':      100, #In terms of displayPeriod
    #output plots directory
    'plotDir':         "plots/",
    'plotPeriod':      100, #With respect to displayPeriod
    #Progress step
    'progress':        100,
    #Controls how often to write out to tensorboard
    'writeStep':       10,
    #Flag for loading weights from checkpoint
    'load':            False,
    'loadFile':        "/home/slundquist/mountData/tfLCA/saved/cifar_nf128.ckpt",
    #Device to run on
    'device':          '/gpu:0',
    #####FISTA PARAMS######
    'numIterations':   10,
    'displayPeriod':   1000,
    #Batch size
    'batchSize':       8,
    #Learning rate for optimizer
    'learningRateA':   .15,
    'learningRateW':   1,
    #Lambda in energy function
    'thresh':          .001,
    #Number of features in V1
    'numV':            256,
    #Stride of V1
    'VStrideY':        2,
    'VStrideX':        2,
    #Patch size
    'patchSizeY':      12,
    'patchSizeX':      12,
}

#Allocate tensorflow object
tfObj = FISTA(params, trainDataObj)
print "Done init"

tfObj.runModel()
print "Done run"

tfObj.closeSess()

