import math, numpy as np
def collision(car_pos, car_angle, CAR_WIDTH, CAR_HEIGHT, rectangle):
    # p2             p3
    #     |--------|
    #     |        |
    #     |--------|
    # p1             p4
    x1 = car_pos[0]
    y1 = car_pos[1]

    x2 = x1 - CAR_HEIGHT * math.cos(math.radians(90 - car_angle[0]))
    y2 = y1 + CAR_HEIGHT * math.sin(math.radians(90 - car_angle[0]))

    x3 = x2 + CAR_WIDTH * math.sin(math.radians(90 - car_angle[0]))
    y3 = y2 + CAR_WIDTH * math.cos(math.radians(90 - car_angle[0]))

    x4 = car_pos[0] + CAR_WIDTH * math.cos(math.radians(car_angle[0]))
    y4 = car_pos[1] + CAR_WIDTH * math.sin(math.radians(car_angle[0]))

    main_car_p1 = [x1,y1]
    main_car_p2 = [x2,y2]
    main_car_p3 = [x3,y3]
    main_car_p4 = [x4,y4]
    main_car =  [main_car_p1 , main_car_p2, main_car_p3, main_car_p4]

    rect_p1 = [rectangle.left, rectangle.bottom]
    rect_p2 = [rectangle.left, rectangle.top]
    rect_p3 = [rectangle.right, rectangle.top]
    rect_p4 = [rectangle.right, rectangle.bottom]

    rect = [rect_p1, rect_p2, rect_p3, rect_p4]
    is_car_points_inside_recatngle = is_point_inside_rectangle(rect, main_car_p1) or is_point_inside_rectangle(rect, main_car_p2) \
                                     or is_point_inside_rectangle(rect, main_car_p3) or is_point_inside_rectangle(rect, main_car_p4)

    is_recatngle_points_inside_car = is_point_inside_rectangle(main_car, rect_p1) or is_point_inside_rectangle(main_car, rect_p2) or\
                                     is_point_inside_rectangle(main_car, rect_p3) or is_point_inside_rectangle(main_car, rect_p4)


    return is_recatngle_points_inside_car or is_car_points_inside_recatngle
    # print("main_car: ",main_car)
    # print("rect",rect)


def is_point_inside_rectangle(rectangle_points, point):
    wn = 0  # Winding number

    for i in range(len(rectangle_points)):
        x1, y1 = rectangle_points[i]
        x2, y2 = rectangle_points[(i + 1) % len(rectangle_points)]

        # Check if the point is to the left of the line
        if y1 <= point[1]:
            if y2 > point[1] and (x2 - x1) * (point[1] - y1) - (point[0] - x1) * (y2 - y1) > 0:
                wn += 1
        else:
            if y2 <= point[1] and (x2 - x1) * (point[1] - y1) - (point[0] - x1) * (y2 - y1) < 0:
                wn -= 1

    if wn != 0:
        return True
    else:
        return False

