Description

There are some objects placed on a number line. You are given their coordinates in ascending order as an array of integers objects. There are no two objects placed on the same coordinate.

Your task is to place a lamp on an integer coordinate on the same line so that it illuminates the maximal number of objects. The lamp placed at a coordinate c illuminates everything around it within a radius of radius, i.e. within a range [c - radius, c + radius] (inclusive). The lamp can be placed on any integer coordinate, even if there's an object on the coordinate.

Return the coordinate to place the lamp so that it illuminates