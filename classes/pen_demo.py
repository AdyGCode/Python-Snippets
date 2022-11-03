from pen import Pen


def demo():
    my_empty_pen = Pen()
    my_red_pen = Pen("Staedtler", "red", "roller ball")

    print(my_empty_pen)
    print(my_red_pen)

    my_empty_pen.ink_colour = "blue"
    print(my_empty_pen)

    my_empty_pen.name = "Lamy"
    print(my_empty_pen)

    my_empty_pen.pen_type = "fountain"
    print(my_empty_pen)


if __name__ == "__main__":
    demo()
