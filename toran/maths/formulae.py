#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# created_on: 2022-11-10 19:13

"""Formulae."""

__author__ = "Toran Sahu <toran.sahu@yahoo.com>"
__license__ = "Distributed under terms of the MIT license"


def ap(a: int, n: int, d: int) -> int:
    """Arithmatic Progression.

    :param a: First term
    :param n: Number of terms
    :param d: Common difference between the terms
    :return: Nth term
    """

    return a + (n - 1) * d


def sum_of_ap(a: int, n: int, d: int):
    """Sum of Arithmatic Progression sequence.

    :param a: First term
    :param n: Number of terms
    :param d: Common difference between the terms
    :return: Sum
    """

    return (n / 2) * (2 * a + (n - 1) * d)
