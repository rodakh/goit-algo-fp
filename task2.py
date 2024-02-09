import turtle
import math


def draw_pythagoras_tree(t, branch_length, depth):
    if depth == 0:
        return
    else:
        t.forward(branch_length)
        t.left(45)

        draw_pythagoras_tree(t, branch_length / math.sqrt(2), depth - 1)

        t.right(90)

        draw_pythagoras_tree(t, branch_length / math.sqrt(2), depth - 1)

        t.left(45)
        t.backward(branch_length)


def main():
    window = turtle.Screen()
    window.title("Pythagoras Tree Fractal")

    t = turtle.Turtle()
    t.speed("fastest")

    t.left(90)
    t.penup()
    t.goto(0, -200)
    t.pendown()

    depth = int(input("Enter the recursion depth (e.g., 5): "))
    draw_pythagoras_tree(t, 100, depth)

    window.mainloop()


if __name__ == "__main__":
    main()
