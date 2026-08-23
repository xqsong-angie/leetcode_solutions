Imagine objects located on the canvas at a certain moment in time. You are given an array of integer pairs centers representing the coordinates of those objects. Each object has a collision box - a square area around its center with a side equal to 2. Two objects are supposed to collide if their collision boxes have at least one common point. Calculate the number of object pairs that collide.

The example of the object located in coordinates [1, 1] can be represented as following:

Where the green square is the collision box.

**Note**
Object collision boxes intersect if the distance in each coordinate between the object centers does not exceed 2.

If x1, y1 are coordinates of one object and x2, y2 are coordinates of the second object, then the collision condition for them can be written in the form |x[j] - x[i]| <= 2 and |y[j] - y[i]| <= 2