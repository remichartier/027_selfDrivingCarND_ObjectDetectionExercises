# 027_selfDrivingCarND_ObjectDetectionExercises
Udacity course quizz/practice on Object Detection course

- 001_drawBoundingBoxesManual : Manual draw and overlay bounding boxes on image using cv2.rectangle()
- 002_TemplateMatching : Test Template Matching with .matchTemplate() and cv2.minMaxLoc()
- 003_BuildHistogramColorsConcatenatedRGBVector : Build Concatenated RGB Vector containing Color Histogram for an image, useful for next project coming on.
- 004_ExploreColorSpaces : RGB/HSU 3D Visualisation of strees, cars and others.
- 005_SpatialBinningOfColorBuildFeatureVector : write a function that allows you to convert any test image into a feature vector that you can feed your classifier. Takes an image, a color space conversion, and the resolution you would like to convert it to, and returns a feature vector.
- 006_ObjectDetectionDataExploration : function that takes in these two lists and returns a dictionary with the keys "n_cars", "n_notcars", "image_shape", and "data_type"
- 007_scikitImageHogFeatureFunction : Define a function to return HOG features and visualization. Features will always be the first element of the return. Image data will be returned as the second element if visualize= True. Otherwise there is no second return element
- 008_CombineAndNormalizeFeaturesUseStandardScaler : Provided the feature scaling steps for you, need to provide the feature vectors. Write a function that takes in a list of image filenames, reads them one by one, then applies a color conversion (if necessary) and uses bin_spatial() and color_hist() to generate feature vectors.
