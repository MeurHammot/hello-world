# -*- encoding: utf-8 -*-

import unittest
from chat import Chat

class TestUM(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.chat = Chat('Nice chat', 'Reni')

    def test_join(self):
        self.assertEqual(self.chat.join('Carl'), ['Reni', 'Carl'])

    def test_say(self):
        self.chat.join('Carl')
        self.assertEqual(self.chat.say('Reni'), ['Sam', 'Carl'])
    
    def test_leave(self):
        self.chat.join('Sam')
        self.assertEqual(self.chat.leave('Carl'), ['Reni', 'Sam'])


if __name__ == '__main__':
    unittest.main()