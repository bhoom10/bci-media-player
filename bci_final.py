#loadmat

'''load 4 arrays
>x-train
>y-train
>x-test
>y-test: true labels


'''
import numpy as np
import scipy as sp
import scipy.io as scio 

#import matplotlib as mpl

#from wyrm import plot
#plot.beautify()
from wyrm.types import Data
from wyrm import processing as proc
#from wyrm.io import load_bcicomp3_ds2

#function to load data
def load_graz(filename):
   # load the training 
   data_mat = scio.loadmat('dataset_BCIcomp1.mat')
   data = data_mat['x_train'].astype('double')
   #print data.shape
   data = data.swapaxes(-3, -2)
   data = data.swapaxes(-1, -3)
   labels = data_mat['y_train'].astype('int').ravel()
   #print data.shape

   # convert into wyrm Data
   axes = [np.arange(i) for i in data.shape]
   axes[0] = labels
   axes[2] = [str(i) for i in range(data.shape[2])]
   names = ['Class', 'Time', 'Channel']
   units = ['#', 'ms', '#']
   dat_train = Data(data=data, axes=axes, names=names, units=units)
   dat_train.fs = 128
   dat_train.class_names = ['left', 'right']


   # load the test data
   #test_data_mat = loadmat(test_file)
   data = data_mat['x_test'].astype('double')
   data = data.swapaxes(-3, -2)
   data = data.swapaxes(-1, -3)

   # convert into wyrm Data
   axes = [np.arange(i) for i in data.shape]
   axes[2] = [str(i) for i in range(data.shape[2])]
   names = ['Class','Time', 'Channel']
   units = ['#','ms', '#']
   dat_test = Data(data=data, axes=axes, names=names, units=units)
   dat_test.fs = 128

   # map labels 2 -> 0
   dat_test.axes[0][dat_test.axes[0] == 2] = 0
   dat_train.axes[0][dat_train.axes[0] == 2] = 0

   return dat_train, dat_test


#function for preprocessing
def preprocess(dat,filt=None):
    	'''fs_n = dat.fs / 2
    	b, a = proc.signal.butter(5, [13 / fs_n], btype='low')
	dat = proc.lfilter(dat, b, a)
	b, a = proc.signal.butter(5, [8 / fs_n], btype='high')
	dat = proc.lfilter(dat, b, a)
	print dat'''
   

        dat = proc.subsample(dat, 64)
        #epo = proc.segment_dat(dat, MRK_DEF, SEG_IVAL)
	
        #fv = proc.jumping_means(epo, JUMPING_MEANS_IVALS)
        #fv = proc.create_feature_vectors(dat)

        if filt is None:
        	filt, pattern, _ = proc.calculate_csp(dat)
        	#plot_csp_pattern(pattern)
    	dat = proc.apply_csp(dat, filt)
    
   	dat = proc.variance(dat)
    	dat = proc.logarithm(dat)
    	return dat, filt


dat_train, dat_test=load_graz('dataset_BCIcomp1.mat')

labels=scio.loadmat('labels_data_set_iii.mat')
'''print type(labels)
print labels.shape'''
y_test=labels['y_test']
y_test[y_test == 2] = 0
print "true labels\n"
print y_test.swapaxes(1,0)

#dat_test=graz_data['x_test']
fv_train, filt = preprocess(dat_train)
fv_test, _ = preprocess(dat_test, filt)

cfy= proc.lda_train(fv_train)
result=proc.lda_apply(fv_test,cfy)
result = (np.sign(result) + 1) / 2

print "generated labels\n"
print result


#print y_test.shape
#print result.shape



sum=0.0
for i in range(len(result)):
	if result[i]==y_test[i]:
		sum=sum+1

print 'LDA Accuracy %.2f' % (sum/(len(result)))

