import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Read in an image
# You can also read cutout2, 3, 4 etc. to see other examples
image = mpimg.imread('cutout1.jpg')

# Define a function to compute color histogram features  
# Pass the color_space flag as 3-letter all caps string
# like 'HSV' or 'LUV' etc.
# KEEP IN MIND IF YOU DECIDE TO USE THIS FUNCTION LATER
# IN YOUR PROJECT THAT IF YOU READ THE IMAGE WITH 
# cv2.imread() INSTEAD YOU START WITH BGR COLOR!
def bin_spatial(img, color_space='RGB', size=(32, 32)):
    # Convert image to new color space (if specified)
    convert_rgb_to = {'HSV': cv2.COLOR_RGB2HSV,
                      'BGR': cv2.COLOR_RGB2BGR,
                      'LUV': cv2.COLOR_RGB2BGR,
                      'HLS': cv2.COLOR_RGB2BGR,
                      'YUV': cv2.COLOR_RGB2YUV,
                      'YCrCb': cv2.COLOR_RGB2YCrCb
                     }
    if color_space in convert_rgb_to:
        new_img = cv2.cvtColor(img, convert_rgb_to[color_space])
    else:
        new_img = np.copy(img)
    # Use cv2.resize().ravel() to create the feature vector
    features = cv2.resize(new_img,size).ravel()
    #features = new_img.ravel()

    # Return the feature vector
    return features
    
feature_vec = bin_spatial(image, color_space='RGB', size=(32, 32))

# Plot features
plt.plot(feature_vec)
plt.title('Spatially Binned Features')