import unittest
import requests


class TestAPI(unittest.TestCase):
    URL = "http://127.0.0.1:8088"
    data = {
        "name": "Testing",
        "acc_no": "Test",
        "balance": 100000
    }
    data1 = {
        'amount': -100000
    }
    def test_1_get_all_acc(self):
        resp = requests.get(self.URL)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.json()), 1)
        print("test 1 complete")

    def test_2_add_acc(self):
        resp = requests.get(self.URL + '/add', json=self.data)
        self.assertEqual(resp.status_code, 200)
        print("Test 2 complete")

    def test_3_deposit(self):
        resp = requests.get(self.URL + '/deposit/2', json=self.data1)
        self.assertEqual(resp.status_code, 200)
        print("Test 3 complete")

    def test_4_withdraw(self):
        resp = requests.get(self.URL + '/withdraw/3', json=self.data1)
        self.assertEqual(resp.status_code, 200)
        print("test 4 complete")


if __name__ == "__main__":
    tester = TestAPI()

    # tester.test_1_get_all_acc()
    # tester.test_2_add_acc()
    # tester.test_3_deposit()
    tester.test_4_withdraw()