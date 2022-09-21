#!/usr/bin/python3
"""

This module contains a function that multiplies 2 matrices

"""


def matrix_mul(m_a, m_b):
    """This function multiplies two matrices

    Args:
        m_a (list of lists of int/float): Matrix to be multiplied
        m_b (list of lists of int/float): Matrix to be multiplied

    Raises:
        TypeError: If m_a or m_b is not a list
        TypeError: If m_a or m_b is not a list of lists
        TypeError: If one element of list of lists is not int/float
        TypeError: If row of m_a or m_b are not the same size
        ValueError: If m_a or m_b is empty
        ValueError: If m_a and m_b cannot be multiplied

    Returns:
        A new list which is the outcome of the multiplication

    """
    
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    for x in m_a:
        if type(x) is not list:
            raise TypeError("m_a must be a list of lists")
    for x in m_b:
        if type(x) is not list:
            raise TypeError("m_b must be a list of lists")
    if len(m_a) < 1:
        raise ValueError("m_a can't be empty")
    if len(m_b) < 1:
        raise ValueError("m_b can't be empty")
    arowlen = len(m_a[0])
    if arowlen < 1:
        raise ValueError("m_a can't be empty")
    browlen = len(m_b[0])
    if browlen < 1:
        raise ValueError("m_b can't be empty")
    for row in m_a:
        if len(row) != arowlen:
            raise TypeError("each row of m_a must should be of the same size")
        for col in row:
            if type(col) is not float and type(col) is not int:
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if len(row) != browlen:
            raise TypeError("each row of m_b must should be of the same size")
        for col in row:
            if type(col) is not float and type(col) is not int:
                raise TypeError("m_b should contain only integers or floats")
    if arowlen != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    newmatrix = []
    for x in range(len(m_a)):
        newrow = []
        for y in range(browlen):
            sum = 0
            for z in range(arowlen):
                sum += m_a[x][z] * m_b[z][y]
            newrow.append(sum)
        newmatrix.append(newrow)
    return newmatrix
