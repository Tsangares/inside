
# Quickstart

To Install:

    pip install inside

To Include:

   from inside.isInside import isInside

Now use the funtion `isInside`.

# Description

This is a function that takes in two arrays of tuples. Will return `true` if the first polygon is completly inside of the second polygon, returns `false` otherwise.

There is also included a set of tests.

# Example

    >>> from inside.isInside import isInside
    >>> isInside([(0,0),(1,0),(1,1),(0,1)],[(0,0),(.5,0),(.5,.5),(0,.5)])
    True
    >>> isInside([(0,0),(1,0),(1,1),(0,1)],[(0,0),(-.5,0),(-.5,-.5),(0,-.5)])
    False

