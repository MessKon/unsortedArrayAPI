import unittest
from app import app


class TestAssignmentEndpoint(unittest.TestCase):
    def setUp(self):
        # Set up the Flask test client
        self.app = app.test_client()
        self.app.testing = True

    def test_valid_input(self):
        # Test with valid input
        payload = {"data": [4, 23, 65, 67, 24, 12, 86]}
        response = self.app.post("/assignment", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("results", response.get_json())
        self.assertEqual(len(response.get_json()["results"]), 1)

    def test_no_input(self):
        # Test with no input
        response = self.app.post("/assignment", json={})
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.get_json())

    def test_missing_data_field(self):
        # Test with missing "data" field
        payload = {"numbers": [4, 5, 6]}
        response = self.app.post("/assignment", json=payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.get_json())

    def test_non_list_input(self):
        # Test with non-list input
        payload = {"data": "not a list"}
        response = self.app.post("/assignment", json=payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.get_json())

    def test_non_numeric_list(self):
        # Test with a list containing non-numeric values
        payload = {"data": [4, "a", 7]}
        response = self.app.post("/assignment", json=payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.get_json())

    def test_empty_list(self):
        # Test with an empty list
        payload = {"data": []}
        response = self.app.post("/assignment", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["results"], [])

    def test_valid_input_multiple_pairs(self):
        # Test with valid input containing multiple pairs with the same sum
        payload = {"data": [1, 9, 5, 5, 6, 4]}
        response = self.app.post("/assignment", json=payload)
        self.assertEqual(response.status_code, 200)
        result = response.get_json()["results"]
        self.assertTrue(any(res["sum"] == 10 for res in result))


if __name__ == "__main__":
    unittest.main()