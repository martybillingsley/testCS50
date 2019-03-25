# Fractals
A *fractal* is a curve or geometric figure, each part of which has the same statistical character as the whole. In other words, it looks the same at any magnification. Fractals are useful in modeling structures (such as eroded coastlines or snowflakes) in which similar patterns recur at progressively smaller scales, and in describing partly random or chaotic phenomena such as crystal growth, fluid turbulence, and galaxy formation.

In drawing a fractal on the screen, there must be some point at which the program stops drawing. A Python turtle, after all, can't move forward less than one pixel or turn less than one degree.

### Start with drawing a simple tree. 
A tree is made of a trunk and branches. Write a `drawTree()` function that draws a simple tree. The turtle must end up where it started, facing the way it was when it started.

![Simple tree](https://raw.githubusercontent.com/martybillingsley/images/master/tree1.png) 
{% spoiler "Turtle Reference" %}
forward (distance)
backward (distance)
right (degrees)
left (degrees)
{% endspoiler %}

{% spoiler "Algorithm" %}
Go forward<br>
Turn right<br>
Go forward<br>
Go backward the same number of steps<br>
Turn left the same number of degrees that you turned right<br>
Turn left<br>
Go forward<br>
Go backward the same number of steps<br>
Turn right the same number of degrees that you turned left<br>
Go backward the same number of steps as the first forward<br>
{% endspoiler %}

{% spoiler "Code" %}
`def drawTree():`<br>
 &nbsp;&nbsp; `forward(100)`<br>
 &nbsp;&nbsp; `left(30)`<br>
 &nbsp;&nbsp; `forward(100)`<br>
 &nbsp;&nbsp; `backward(100)`<br>
 &nbsp;&nbsp; `right(30)`<br>
 &nbsp;&nbsp; `right(30)`<br>
 &nbsp;&nbsp; `forward(100)`<br>
 &nbsp;&nbsp; `backward(100)`<br>
  &nbsp;&nbsp;`left(30)`<br>
 &nbsp;&nbsp; `backward(100)`
{% endspoiler %}

{% next  %}

### Add an argument to the `drawTree()` function that specifies the size of the tree
Try it out with the following commands:
`drawTree(100)`
and
`drawTree(50)`

{% spoiler "Details" %}
In each `forward` and `backward` command, use the argument variable instead of a number
{% endspoiler %}

{% spoiler "Code" %}
`def drawTree(size):`<br>
 &nbsp;&nbsp; `forward(size)`<br>
 &nbsp;&nbsp; `left(30)`<br>
 &nbsp;&nbsp; `forward(size)`<br>
 &nbsp;&nbsp; `backward(size)`<br>
 &nbsp;&nbsp; `right(30)`<br>
 &nbsp;&nbsp; `right(30)`<br>
 &nbsp;&nbsp; `forward(size)`<br>
 &nbsp;&nbsp; `backward(size)`<br>
 &nbsp;&nbsp; `left(30)`<br>
 &nbsp;&nbsp; `backward(size)`
{% endspoiler %}

{% next  %}
### At the end of each branch, draw another tree 3/4 the size of the original
`drawTree(50, 6)` should draw a tree like this:<br>
![Tree](https://raw.githubusercontent.com/martybillingsley/images/master/tree3.png) <br>
<br>Note: think about when to stop!

{% spoiler "Algorithm" %}
Draw the trunk<br>
Turn and draw a branch<br>
Draw a tree on the end of that branch<br>
Go backward to the trunk<br>
Turn left and draw another branch<br>
Draw a tree on the end of that branch<br>
Go backward to the trunk<br>
Turn right and go backward down the trunk<br>
{% endspoiler %}

{% spoiler "Problems?" %}
Does your tree look like this?<br>
![Tree gone wrong](https://raw.githubusercontent.com/martybillingsley/images/master/tree2.png) <br>
Add another argument to the `drawTree()` function to indicate the depth of the tree.<br>
Every time you draw another tree, make it smaller **and** reduce the depth by one.
{% endspoiler %}

{% spoiler "Code" %}
`def drawTree(size, depth):`<br>
 &nbsp;&nbsp; `if depth > 0:`<br>
 &nbsp;&nbsp;&nbsp;&nbsp; `forward(size)`<br>
 &nbsp;&nbsp;&nbsp;&nbsp; `left(30)`<br>
 &nbsp;&nbsp;&nbsp;&nbsp; `forward(size)`<br>
 &nbsp;&nbsp;&nbsp;&nbsp; `drawTree(size*0.75, depth-1)`<br>
 &nbsp;&nbsp;&nbsp;&nbsp; `backward(size)`<br>
 &nbsp;&nbsp;&nbsp;&nbsp; `right(30)`<br>
 &nbsp;&nbsp;&nbsp;&nbsp; `right(30)`<br>
 &nbsp;&nbsp;&nbsp;&nbsp; `forward(size)`<br>
 &nbsp;&nbsp;&nbsp;&nbsp; `drawTree(size*0.75, depth-1)`<br>
 &nbsp;&nbsp;&nbsp;&nbsp; `backward(size)`<br>
 &nbsp;&nbsp;&nbsp;&nbsp; `left(30)`<br>
 &nbsp;&nbsp;&nbsp;&nbsp; `backward(size)`
{% endspoiler %}
