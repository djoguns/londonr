import numpy as np

from circle import circle_area

from cube import volume_cube

from cuboid import volume_cuboid


area_of_circle = circle_area(6)
print(f'\nArea of the circle is {area_of_circle} cm sq.')

volume_of_cube = volume_cube(6)
print(f'\nVolume of the cube is {volume_of_cube} cm cb.')

volume_of_cuboid = volume_cuboid(6, 2, 9)
print(f'\nVolume of the cuboid is {volume_of_cuboid} cm cb.')