# Object-removal
 Remove object from image with inpainting
 when the dataset is unbalanced and traditional augumentation can't fix the balance issue
 for example a dataset that contain 1000 sample of A and 100 sample of B, and the image that contain the object B are also contain the object A so augumentate the object 
 B will also augument the object A 
 the solution here is to remove the object A from the images
 
 I have used random 100 image from Pascal Voc dataset 
 annotation used are Pascal Voc format 
 
 the folder data contains "in" for input and "out" 
 I have removed object with the name "person" from the dataset 
 
 ** note that some times if the object is large you will have a destorted image and if there is a small object inside the big object both will be unrecognized 
 
 See this [example](https://github.com/MustafaAlahmid/Object-removal/blob/main/example.ipynb)
 
 Before:
 
 
 After:
 
 ![After removing the object 'bottle' image ](https://raw.githubusercontent.com/MustafaAlahmid/Object-removal/main/a.jpg?token=GHSAT0AAAAAAB7YFSS6V6S6P4CJGIVV5MXUZAIVBOA)

 
 
 
