import unittest
from transform_image import transform_image_url

class TestTransformImageUrl(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ("rancher/fleet:v0.9.4", "registry.ap-southeast-1.aliyuncs.com/migrate-1/rancher-fleet:v0.9.4"),
            ("ubuntu:latest", "registry.ap-southeast-1.aliyuncs.com/migrate-1/ubuntu:latest"),
            ("gcr.io/kaniko-project/executor:v1.23.1-debug","registry.ap-southeast-1.aliyuncs.com/migrate-1/kaniko-project-executor:v1.23.1-debug"),
            ("http://mcr.microsoft.com/mssql/server:v0.1", "registry.ap-southeast-1.aliyuncs.com/migrate-1/mssql-server:v0.1"),
            ("https://mcr.microsoft.com/mssql/server:v0.1", "registry.ap-southeast-1.aliyuncs.com/migrate-1/mssql-server:v0.1"),
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
