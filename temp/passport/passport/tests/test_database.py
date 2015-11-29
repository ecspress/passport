"""Tests the module that handles in memory database"""

from passport.database_interface import Database
import unittest

class DatabaseTest(unittest.TestCase): # pylint: disable=too-many-public-methods
    """Contains tests for database module"""
    # {service:(tags, {user:blob, user2:blob}), ...}
    services = {"service1":("tag1", {"user1":"data1", "user2":"data2", "user6":"data6"}),
                "service2":("tag3, tag4", {"user3":"data3", "user2":"data2"}),
                "service3":("tag2, tag4", {"user4":"data4", "user5":"data5"}),
                "service4":("tag2, tag3", {"user3":"data3", "user5":"data5"}),
                "service5":("tag1, tag4, tag2", {"user1":"data1", "user4":"data4"}),
                "service6":("tag1, tag2, tag3, tag4", {"user6":"data6"}),
                "service7":("tag5", {})
               }

    def test_add_service(self):
        """Tests that adding services into database occurs correctly"""
        database = Database()

        count = 0
        self.assertEqual(len(database.services), count)

        tags = set()
        self.assertEqual(database.get_tags(), tags)

        for key, value in self.services.items():
            database.add_service(key, value[0])
            count += 1
            self.assertEqual(len(database.services), count)
            tags = tags | set(value[0].split(','))
            self.assertEqual(database.get_tags(), tags)

        self.assertEqual(count, len(self.services))

    def test_add_existing_service(self):
        """Tests that adding services into database fails if service is already present"""
        database = Database()
        for key, value in self.services.items():
            database.add_service(key, value[0])
            self.assertRaises(ValueError, database.add_service, key, value[0])

    def tast_remove_service(self):
        """Tests that removing services from database is done correctly"""
        database = Database()

        for key, value in self.services.items():
            database.add_service(key, value[0])

        count = len(self.services)
        for key in self.services.keys():
            database.remove_service(key)
            count -= 1
            self.assertEqual(len(database.services), count)
        self.assertEqual(len(database.services), 0)
        self.assertEqual(database.get_tags(), set())

    def test_remove_absent_service(self):
        """Tests that removing services from database fails if service is not in database"""
        database = Database()
        for key in self.services.keys():
            self.assertRaises(ValueError, database.remove_service, key)

    def tast_update_tag(self):
        """s"""
        pass

    def test_update_tag_absent_service(self):
        """Tests that updating tags of a services fails if the service is not in database"""
        database = Database()
        for key in self.services.keys():
            self.assertRaises(ValueError, database.update_service_tags, key, "")

    def tast_add_user(self):
        """s"""
        pass

    def tast_add_user_absent_service(self):
        """s"""
        pass

    def tast_add_existing_user(self):
        """s"""
        pass

    def tast_remove_user(self):
        """s"""
        pass

    def tast_remove_absent_user(self):
        """s"""
        pass

    def tast_remove_user_absent_service(self):
        """s"""
        pass

    def tast_update_user(self):
        """s"""
        pass

    def tast_update_absent_user(self):
        """s"""
        pass

    def tast_update_user_absent_service(self):
        """s"""
        pass

    def tast_get_users(self):
        """s"""
        pass

    def tast_service_users(self):
        """s"""
        pass

    def tast_absent_service_users(self):
        """s"""
        pass

    def tast_get_data(self):
        """s"""
        pass

    def tast_get_absent_user_data(self):
        """s"""
        pass

    def tast_get_data_absent_service(self):
        """s"""
        pass

    def tast_tag_search(self):
        """s"""
        pass

    def tast_user_search(self):
        """s"""
        pass

