# Fractals
A *fractal* is a curve or geometric figure, each part of which has the same statistical character as the whole. In other words, it looks the same at any magnification. Fractals are useful in modeling structures (such as eroded coastlines or snowflakes) in which similar patterns recur at progressively smaller scales, and in describing partly random or chaotic phenomena such as crystal growth, fluid turbulence, and galaxy formation.

In drawing a fractal on the screen, there must be some point at which the program stops drawing. A Python turtle, after all, can't move forward less than one pixel or turn less than one degree.

Start with drawing a simple tree. 
A tree is made of a trunk and branches. Write a <drawTree()> function that draws a simple tree. The turtle must end up where it started, facing the way it was when it started.

![Simple tree](https://raw.githubusercontent.com/martybillingsley/images/master/tree1.png) 
{% spoiler "Turtle Reference" %}
forward (distance)
backward (distance)
right (degrees)
left (degrees)
{% endspoiler %}

{% spoiler "Algorithm" %}
Go forward a certain number of steps
Turn right a certain number of degrees
Go forward the same number of steps
Go backward the same number of steps
Turn left the same number of degrees
Turn left the same number of degrees
Go forward the same number of steps
Go backward the same number of steps
Turn right the same number of degrees
Go backward the same number of steps
{% endspoiler %}

{% spoiler "Code" %}
forward(100)
left(30)
forward(100)
backward(100)
right(30)
right(30)
forward(100)
backward(100)
left(30)
backward(100)
{% endspoiler %}

{% next "Step 2" %}

Add an argument to the drawTree() function that specifies the size of the tree
