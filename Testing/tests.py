import unittest
from activities import eat, nap

class ActivityTests(unittest.TestCase):
	
	def test_eat_healthy(self):
		self.assertEqual(
			eat("broccoli", is_healthy=True),
			"I am eating broccoli because its healthy"
		)

	def test_eat_unhealthy(self):
		self.assertEqual(
			eat("pizza", is_healthy=False),
			"I am eating pizza because YOLO!"
		)		


if __name__ == "__main__":
	unittest.main()