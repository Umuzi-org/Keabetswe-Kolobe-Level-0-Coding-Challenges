def area_of_triangle(side_1, side_2, side_3):
    semiperimeter = 0.5 * (side_1 + side_2 + side_3)

    return (semiperimeter * ((semiperimeter - side_1) * (semiperimeter - side_2) * (semiperimeter - side_3)))**0.5
