import unittest

from app import obtener_mensaje


class TestAplicacion(unittest.TestCase):

    def test_obtener_mensaje(self):
        self.assertEqual(
            obtener_mensaje(),
            "Hello World desde Jenkins y Docker!"
        )

    def test_mensaje_no_vacio(self):
        self.assertTrue(len(obtener_mensaje()) > 0)


if __name__ == "__main__":
    unittest.main()
