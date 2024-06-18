import unittest
from transform_image import transform_image_url

class TestTransformImageUrl(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ("rancher/fleet:v0.9.4", "sgccr.ccs.tencentyun.com/migrate/rancher-fleet:v0.9.4"),
            ("ubuntu:latest", "sgccr.ccs.tencentyun.com/migrate/ubuntu:latest"),
            ("gcr.io/kaniko-project/executor:v1.23.1-debug","sgccr.ccs.tencentyun.com/migrate/kaniko-project-executor:v1.23.1-debug"),
            ("http://mcr.microsoft.com/mssql/server:v0.1", "sgccr.ccs.tencentyun.com/migrate/mssql-server:v0.1"),
            ("https://mcr.microsoft.com/mssql/server:v0.1", "sgccr.ccs.tencentyun.com/migrate/mssql-server:v0.1"),
        ]

    def test_transform_image_url(self):
        for image_url, expected in self.test_cases:
            with self.subTest(image_url=image_url):
                self.assertEqual(transform_image_url(image_url), expected)

    def test_invalid_image_url(self):
        with self.assertRaises(ValueError):
            transform_image_url("invalid_image_url")

if __name__ == '__main__':
    unittest.main()
