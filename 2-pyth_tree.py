import turtle

def draw_tree(t, length, level):
    if level == 0:
        return

    t.forward(length)

    t.left(45)
    draw_tree(t, length * 0.8, level - 1)  
 
    t.right(90)
    draw_tree(t, length * 0.8, level - 1)  
  
    t.left(45)
    t.backward(length)

def main():

    screen = turtle.Screen()
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.left(90)  
    t.speed(0) 
    t.color("dark red") 

    t.penup()
    t.goto(0, -200)  
    t.pendown()


    level = int(input("Enter recursion level (default is 8): ") or 8) 

    length = 120 

    
    draw_tree(t, length, level)

    turtle.done()

if __name__ == "__main__":
    main()
