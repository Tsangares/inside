
# Quickstart

To Install:

    pip install inside

To Include:

    from inside.isInside import isInside

Now use the funtion `isInside( array[(x0,y0),...] insideShape, array[(x0,y0),...] outsideShape )`.

# Description

This is a function that takes in two arrays of tuples. Will return `true` if the first polygon is completly inside of the second polygon, returns `false` otherwise.

There is also included a set of tests located in the file test.txt.
There is a parser called parse.py that can be run from command line.
It takes a url to test.txt as an input.
It can be installed using `pip install inside`
Once you have the inside packaege installed and you have the test.txt file in your working directory you can simply run `parse.py input.txt` like so:

    parse.py input.txt 
    Success true
    Success false
    Success false
    Success true
    Success false
    Success true
    Success false
    Success true
    Success false
    Success true
    Success false
    Success false
    Success true
    Success false
    Success true
    Success false
    Success false
    Success true
    Success false
    Success false
    Success true


# Example

    >>> from inside.isInside import isInside
    >>> isInside([(0,0),(1,0),(1,1),(0,1)],[(0,0),(.5,0),(.5,.5),(0,.5)])
    True
    >>> isInside([(0,0),(1,0),(1,1),(0,1)],[(0,0),(-.5,0),(-.5,-.5),(0,-.5)])
    False

