# Problem 94:
#     Almost Equilateral Triangles
#
# Description:
#     It is easily proved that no equilateral triangle exists with integral length sides and integral area.
#     However, the 'almost equilateral triangle' 5-5-6 has an area of 12 square units.
#
#     We shall define an 'almost equilateral triangle' to be a triangle
#       for which two sides are equal and the third differs by no more than one unit.
#
#     Find the sum of the perimeters of all 'almost equilateral triangles'
#       with integral side lengths and area and whose perimeters do not exceed one billion (1,000,000,000).

################################################################################
################################## UNFINISHED ##################################
################################################################################

from math import floor, sqrt


def heronian_area(a, b, c):
    """
    Returns the area of a triangle having side lengths a, b, c,
      using Heron's formula.

    Args:
        a (int): Natural number
        b (int): Natural number
        c (int): Natural number

    Returns:
        (float): Area of triangle having side lengths a, b, c

    Raises:
        AssertError: if incorrect args are given
    """
    assert type(a) == int and a > 0
    assert type(b) == int and b > 0
    assert type(c) == int and c > 0

    s = (a + b + c) / 2
    return sqrt(s * (s-a) * (s-b) * (s-c))


def main(p_limit):
    """
    Returns the sum of the perimeters of all Heronian "almost equilateral triangles" with perimeters below `p_limit`.

    NOTE:
        * A Heronian triangle is a triangle that has integral side lengths and area
        * An "almost equilateral triangle" is a triangle for which two side lengths are equal
            and the third differs from the former by no more than one unit.

    Args:
        p_limit (int): Natural number

    Returns:
        (int):
            Sum of perimeters of all "almost equilateral triangles"
              having integral side lengths and areas and perimeters not exceeding `p_limit`.

    Raises:
        AssertError: if incorrect args are given
    """
    assert type(p_limit) == int and p_limit > 0

    # Idea 0:
    #     Refer to these:
    #       * [https://en.wikipedia.org/wiki/Heronian_triangle]
    #       * [https://en.wikipedia.org/wiki/Heron%27s_formula]
    #
    #     Use Heron's formula for area of a triangle having side lengths a, b, c.
    #     Let perimeter be:
    #         p = a + b + c
    #     Let semi-perimeter be:
    #         s = p / 2
    #     Then area is:
    #         A = sqrt( s * (s-a) * (s-b) * (s-c) )

    # Idea 1:
    #     Check the claim that equilateral triangles cannot be Heronian, using Heron's formula.
    #
    #     Let `a` be the integral length of each side of an equilateral triangle.
    #     Then we have:
    #         p = a + a + a
    #           = 3*a
    #
    #         s = p / 2
    #           = (3/2)*a
    #
    #         A = sqrt( s * (s-a) * (s-b) * (s-c) )                 (Heron's formula)
    #           = sqrt( s * (s-a) * (s-a) * (s-a) )                 (all side lengths equal to `a`)
    #           = sqrt( s * (s-a)^3 )
    #           = sqrt( (3/2) * a * ((3/2)*a - a)^3 )               (substituting `s`)
    #           = sqrt( (3/2) * a * (a/2)^3 )
    #           = sqrt( (3/16) * a^4 )
    #           = a^2/4 * sqrt(3)
    #
    #     Given that `a` is integral, `A` cannot be integral due to sqrt(3) being irrational.

    triangles = []

    # No Heronian triangles having side lengths of 1 or 2, so start above
    a_max = floor((p_limit+1)/3) + 1
    for a in range(3, a_max):  # `a` is the duplicated side length
        for b in range(a-1, a+2, 2):  # `b` is the third side length
            p = 2*a + b
            if p >= p_limit:
                continue
            else:
                area = heronian_area(a, a, b)
                if area == floor(area):
                    triangles.append(tuple(sorted([a, a, b])))
                else:
                    continue

    for triangle in triangles:
        print(triangle)

    return 57


if __name__ == '__main__':
    perimeter_upper_limit = int(input('Enter a natural number: '))
    perimeter_sum = main(perimeter_upper_limit)
    print('Sum of perimeters of all Heronian "almost equilateral triangles" having perimeters < {}:'
          .format(perimeter_upper_limit))
    print('  {}'.format(perimeter_sum))
