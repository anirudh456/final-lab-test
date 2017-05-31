
import unittest
from unittest import TestCase
from runtime.objects.email.email import Email
from runtime.objects.name.name import Name
from runtime.objects.role.role import Role
from runtime.objects.user.user import User
from runtime.objects.session.session import Session
from runtime.datatypes.cmd.cmd import Cmd
from runtime.datatypes.instr.del_user.del_user_instr import DelUserInstr

class TestHarness(TestCase):
    def setUp(self):
        self.u1 = User(email=Email(val="joe@g.com"), 
                    name=Name(val="Joe Montana"), 
                    roles=[Role.admin])
        self.session = Session(user=self.u1, 
                               role=Role.admin,
                               key="123")


    def tearDown(self):
      self.em = None

    # The instruction is well formed.
    def test_correct_instr(self):
       instr = {'cmd': Cmd.del_user, 'session': self.session,
                'data': {'user': self.u1}}
       self.assertTrue(DelUserInstr.is_inst(instr))

    # The command is wrong
    def test_cmd_wrong(self):
       instr = {'cmd': "foo", 'session': self.session,
                'data': {'user': self.u1}}
       self.assertFalse(DelUserInstr.is_inst(instr))


    def test_session_missing(self):
       instr = {'cmd': Cmd.del_user, 
                'data': {'user': self.u1}}
       self.assertFalse(DelUserInstr.is_inst(instr))


    def test_cmd_missing(self):
       instr = {'session': self.session,
                'data': {'user': self.u1}}
       self.assertFalse(DelUserInstr.is_inst(instr))


    def test_data_missing(self):
       instr = {'cmd': Cmd.del_user, 'session': self.session}
       self.assertFalse(DelUserInstr.is_inst(instr))
