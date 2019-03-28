from tensorflow.python import pywrap_tensorflow
import numpy as np

checkpoint_path = './model/Onet'	#
reader = pywrap_tensorflow.NewCheckpointReader(checkpoint_path)
var_to_shape_map = reader.get_variable_to_shape_map()

mtcnn = {}

for key in var_to_shape_map:
	sStr_2 = key.replace('mtcnn/', '')
	if not sStr_2 in mtcnn.keys():
		mtcnn[sStr_2] = reader.get_tensor(key)
	else:
		raise Exception("Same key in the same network!!!")

np.save('mtcnn.npy', mtcnn)