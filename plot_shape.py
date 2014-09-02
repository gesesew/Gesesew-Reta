from pylab import *

from geom_formulae import *
#1  11111111111111111111111111111111111111111111111111111111111111
v_rectangle_area = np.vectorize(rectangle_area)
v_rectangle_perimeter = np.vectorize(rectangle_perimeter)

S = np.linspace(0, 30) # our side lengths
A = v_rectangle_area(S,8)  # the areas
P = v_rectangle_perimeter (S)  # the perimeters
plot(S, A, '-r', label="Area")
plot(S, P, ':b', label="Perimeter")
xlabel('side length')
ylabel('geo values')
title('rectangle geo Properties')
legend(loc='upper right')
show()
#2  2222222222222222222222222222222222222222222222222222222222222
v_trapezium_area = np.vectorize(trapezium_area)
#v_rectangle_perimeter = np.vectorize(rectangle_perimeter)

S = np.linspace(0, 30) # our side lengths
A = v_trapezium_area(S,8,20)  # the areas
#P = v_rectangle_perimeter (S)  # the perimeters
plot(S, A, '-r', label="Area")
#plot(S, P, ':b', label="Perimeter")
xlabel('side length')
ylabel('geo values')
title('trapezium geo Properties')
legend(loc='upper right')
show()
#3  3333333333333333333333333333333333333333333333333333333333333
v_circle_area = np.vectorize(circle_area)
#v_rectangle_perimeter = np.vectorize(rectangle_perimeter)

S = np.linspace(0, 30) # our side lengths
A = v_circle_area(S)  # the areas
#P = v_rectangle_perimeter (S)  # the perimeters
plot(S, A, '-r', label="Area")
#plot(S, P, ':b', label="Perimeter")
xlabel('side length')
ylabel('geo values')
title('circle geo Properties')
legend(loc='upper right')
show()
#4  4444444444444444444444444444444444444444444444444444444444444
v_isosceles_triangle_area = np.vectorize(isosceles_triangle_area)
#v_rectangle_perimeter = np.vectorize(rectangle_perimeter)

S = np.linspace(0, 30) # our side lengths
A = v_isosceles_triangle_area(S,8)  # the areas
#P = v_rectangle_perime_areater (S)  # the perimeters
plot(S, A, '-r', label="Area")
#plot(S, P, ':b', label="Perimeter")
xlabel('side length')
ylabel('geo values')
title('isosceles_triangle geo Properties')
legend(loc='upper right')
show()
#5  55555555555555555555555555555555555555555555555555555555555555
#v_regular_hexagon_perimeter = np.vectorize()
v_regular_hexagon_perimeter = np.vectorize(perimeter_regular_hexagon)

S = np.linspace(0, 100) # our side lengths
#A = v_isosceles_triangle_area(S,8)  # the areas
P = v_regular_hexagon_perimeter (S)  # the perimeters
#plot(S, A, '-r', label="Area")
plot(S, P, ':b', label="Perimeter")
xlabel('side length')
ylabel('geo values')
title('regular hexagon  geo Properties')
legend(loc='upper right')
show()
#6  66666666666666666666666666666666666666666666666666666666666666
v_cuboid_volume = np.vectorize(cuboid_volume)
#v_regular_hexagon_perimeter = np.vectorize()

S = np.linspace(0, 30) # our side lengths
#A = v_isosceles_triangle_area(S,8)  # the areas
V = v_cuboid_volume (S,50,60)  # the perimeters
#plot(S, A, '-r', label="Area")
plot(S, V, ':b', label="Perimeter")
xlabel('side length')
ylabel('geo values')
title('cuboid geo Properties')
legend(loc='upper right')
show()
#7  777777777777777777777777777777777777777777777777777777777777777

v_sphere_volume = np.vectorize(volume_sphere)
#v_sphere_volume = np.vectorize()


S = np.linspace(0, 30) # our side lengths
#A = v_isosceles_triangle_area(S,8)  # the areas
V = v_sphere_volume (S)  # the perimeters
#plot(S, A, '-r', label="Area")
plot(S, V, ':b', label="Perimeter")
xlabel('side length')
ylabel('geo values')
title('sphere geo Properties')
legend(loc='upper right')
show()
#8  8888888888888888888888888888888888888888888888888888888888888888

v_cube_volume = np.vectorize(cube_volume)
#v_rectangle_perimeter = np.vectorize(rectangle_perimeter)

S = np.linspace(0, 30) # our side lengths
V= v_cube_volume(S)  # the areas
#P = v_rectangle_perimeter (S)  # the perimeters
plot(S, V, '-r', label="volume")
#plot(S, P, ':b', label="Perimeter")
xlabel('side length')
ylabel('geo values')
title('cube geo Properties')
legend(loc='upper right')
show()
#9  999999999999999999999999999999999999999999999999999999999999999
v_cone_volume = np.vectorize(cone_volume)
#v_rectangle_perimeter = np.vectorize(rectangle_perimeter)

S = np.linspace(0, 30) # our side lengths
V= v_cone_volume(S,10)  # the areas
#P = v_rectangle_perimeter (S,10)  # the perimeters
plot(S, V, '-r', label="volume")
#plot(S, P, ':b', label="Perimeter")
xlabel('side length')
ylabel('geo values')
title('cone geo Properties')
legend(loc='upper right')
show()
#10  10101010101010101010101010101010101010101010101010101010101010

v_cylinder_volume = np.vectorize(cylinder_volume)
#v_rectangle_perimeter = np.vectorize(rectangle_perimeter)

S = np.linspace(0, 30) # our side lengths
V= v_cylinder_volume(S,10)  # the areas
#P = v_rectangle_perimeter (S,10)  # the perimeters
plot(S, V, '-r', label="volume")
#plot(S, P, ':b', label="Perimeter")
xlabel('side length')
ylabel('geo values')
title('cylinder geo Properties')
legend(loc='upper right')
show()






