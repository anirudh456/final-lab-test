
import unittest
from runtime.objects.session.session import Session
from runtime.components.guard.show_users.tests.harness import TestHarness
from runtime.datatypes.cmd.cmd import Cmd

class TestNoSession(TestHarness):

    def test_no_session(self):
        print "test_no_session"
        # delete session from entity manager setup in the TestHarness
        self.component.em.delete_session(self.session)
        session = self.session
        instr = {'cmd': Cmd.show_users, 'session': session}
        guard = self.component
        with self.assertRaises(Exception):
            guard.do(instr)
