#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle

def draw_spiral():
    screen = turtle.Screen()  # Create a screen object
    screen.bgcolor("white")  # Set background color to white

    t = turtle.Turtle()  # Create a turtle object
    t.speed(0)  # Set the speed to the fastest
    t.color("blue")  # Set pen color to blue

    angle = 59  # This angle will help in creating a nice spiral pattern
    length = 5  # Initial length of the line segment

    for _ in range(100):  # Draw 100 segments
        t.forward(length)
        t.left(angle)
        length += 2  # Increase the length for each segment

    screen.mainloop()  # Keep the window open

draw_spiral()


# In[ ]:




