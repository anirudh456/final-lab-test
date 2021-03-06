
import unittest
from runtime.objects.session.session import Session
from runtime.components.guard.del_user.tests.harness import TestHarness
from runtime.datatypes.cmd.cmd import Cmd

class TestDoPasses(TestHarness):

    def test_do_passes(self):
        print "test_do_passes"
        session = self.session
        instr = {'cmd': Cmd.del_user, 
                 'session': session, 
                 'data': {'user': self.d_user}}
        guard = self.component
        result = guard.do(instr)
        self.assertEqual(result, instr)
