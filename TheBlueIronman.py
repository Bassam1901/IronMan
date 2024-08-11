Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#importing turtle
import turtle
#defining coordinates
face_one = [[(-40, 120), (-70, 260), (-130, 230), (-170, 200), (-170, 100),
             (-160, 40), (-170, 10), (-150, -10), (-140, 10), (-40, -20),
             (0, -20)],
            [(0, -20), (40, -20), (140, 10), (150, -10), (170, 10), (160, 40),
             (170, 100), (170, 200), (130, 230), (70, 260), (40, 120),
             (0, 120)]]

face_two = [[(-40, -30), (-50, -40), (-100, -46), (-130, -40), (-176, 0),
             (-186, -30), (-186, -40), (-120, -170), (-110, -210), (-80, -230),
             (-64, -210), (0, -210)],
            [(0, -210), (64, -210), (80, -230), (110, -210), (120, -170),
             (186, -40), (186, -30), (176, 0), (130, -40), (100, -46),
             (50, -40), (40, -30), (0, -30)]]

face_three = [[(-60, -220), (-80, -240), (-110, -220), (-120, -250),
               (-90, -280), (-60, -260), (-30, -260), (-20, -250), (0, -250)],
              [(0, -250), (20, -250), (30, -260), (60, -260), (90, -280),
...                (120, -250), (110, -220), (80, -240), (60, -220), (0, -220)]]
... 
... #hiding pen,adding background color and setting screen scales up
... turtle.hideturtle()
... turtle.bgcolor("#03396c")
... turtle.setup(500, 600)
... 
... #defining starting points
... face_one_start = (0, 120)
... face_two_start = (0, -30)
... face_three_start = (0, -220)
... 
... #defining speed of drawing
... turtle.speed(1)
... 
... #adding the drawing function
... def draw_face(face_details_list, start_point):
...   turtle.penup()
...   turtle.goto(start_point)
...   turtle.pendown()
...   turtle.color("#4f5b66")
...   turtle.begin_fill()
...   #loop for working on every tuple in the list as (x,y)
...   for i in range(len(face_details_list[0])):
...     x, y = face_details_list[0][i]
...     turtle.goto(x, y)
... 
...   for i in range(len(face_details_list[1])):
...     x, y = face_details_list[1][i]
...     turtle.goto(x, y)
...   #important to fill every part alone
...   turtle.end_fill()
... 
... #Using the function
... draw_face(face_one, face_one_start)
... draw_face(face_two, face_two_start)
... draw_face(face_three, face_three_start)
... 
... #Author: Bassam Khaled <3
