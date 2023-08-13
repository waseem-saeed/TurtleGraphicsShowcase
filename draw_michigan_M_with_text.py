#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle

def draw_michigan_M_with_text():
    screen = turtle.Screen()
    screen.bgcolor("white")
    
    m_turtle = turtle.Turtle()
    m_turtle.speed(5)
    m_turtle.width(5)
    m_turtle.color("blue")
    
    # Starting position
    m_turtle.penup()
    m_turtle.goto(-70, 0)
    m_turtle.pendown()

    # Draw the M
    m_turtle.goto(-70, 100)  # Left vertical
    m_turtle.goto(0, 50)     # Middle slant
    m_turtle.goto(70, 100)   # Right vertical
    m_turtle.goto(70, 0)     # Right bottom horizontal
    m_turtle.goto(-70, 0)    # Left bottom horizontal

    # Write "University of Michigan" below the M
    m_turtle.penup()
    m_turtle.goto(-90, -40)
    m_turtle.pendown()
    m_turtle.write("University of Michigan", font=("Arial", 16, "normal"))

    turtle.done()

draw_michigan_M_with_text()


# In[ ]:




