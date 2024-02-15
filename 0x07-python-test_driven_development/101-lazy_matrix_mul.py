#!/usr/bin/python3
"""
Module 101-lazy_matrix_mul
Contains method to multiply matrix using numpy module (pip3 install numpy)
"""
import numpy as lazy


def lazy_matrix_mul(m_a, m_b):
    """Returns matrix multiplied"""
    return lazy.matmul(m_a, m_b)
