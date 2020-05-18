# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

from wolframclient.language.array import NumericArray
from wolframclient.serializers import export
from wolframclient.utils.api import numpy
from wolframclient.utils.tests import TestCase as BaseTestCase


class TestCase(BaseTestCase):
    def test_python_array(self):

        for array, numpy_type, wl_type in (
            ([True, False, True, False, True, False], numpy.int8, "Integer8"),
            ([1, 2, 3, 4, 5, 6], numpy.int8, "Integer8"),
            ([1, 2, 3, 4, 5, 6], numpy.int32, "Integer32"),
            ([1, 2, 3, 4, 5, 6], numpy.int64, "Integer64"),
            ([1.2, 2.3, 3, 4, 5, 6], numpy.float32, "Real32"),
            ([1.2, 2.3, 3, 4, 5, 6], numpy.float64, "Real64"),
        ):

            for shape in ((3, 2), None):

                arr = numpy.array(array, numpy_type)
                if shape:
                    arr = arr.reshape(shape)

                self.assertEqual(
                    export(arr, target_format="wxf"),
                    export(NumericArray(array, wl_type, shape=shape), target_format="wxf"),
                )