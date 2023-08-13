#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle

def draw_person():
    # Set up the screen and turtle
    screen = turtle.Screen()
    screen.bgcolor("white")
    
    person = turtle.Turtle()
    person.speed(5)
    person.width(3)
    
    # Draw the head
    person.penup()
    person.goto(0, -50)
    person.pendown()
    person.circle(50)
    
    # Draw the body
    person.penup()
    person.goto(0, 0)
    person.pendown()
    person.goto(0, -100)
    
    # Draw the left leg
    person.goto(0, -100)
    person.goto(-50, -150)
    
    # Draw the right leg
    person.goto(0, -100)
    person.goto(50, -150)
    
    # Draw the left arm
    person.goto(0, -50)
    person.goto(-50, -75)
    
    # Draw the right arm
    person.goto(0, -50)
    person.goto(50, -75)
    
    turtle.done()

draw_person()


# In[ ]:




