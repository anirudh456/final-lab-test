
import unittest
from runtime.objects.email.email import Email
from runtime.objects.name.name import Name
from runtime.objects.role.role import Role
from runtime.objects.user.user import User
from runtime.objects.session.session import Session
from runtime.components.guard.del_user.tests.harness import TestHarness
from runtime.datatypes.cmd.cmd import Cmd

class TestCheckAuth(TestHarness):

    def test_check_auth(self):
        print "test_check_auth"

        # replace the next line with your code
        self.assertTrue(True)
