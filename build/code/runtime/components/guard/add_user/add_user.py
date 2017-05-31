
import traceback
from runtime.exceptions.app.exception import AppException
from runtime.utils.type_utils.type_utils import check_pred
from runtime.datatypes.cmd.cmd import Cmd
from runtime.objects.session.session import Session
from runtime.objects.role.role import Role
from runtime.datatypes.instr.add_user.add_user_instr import AddUserInstr

class AddUser:

    @staticmethod 
    def do(component, instr):
        print "add_user: %s" % instr

        AddUser.check_type(instr)
        AddUser.check_auth(component, instr)
        AddUser.check_state(component, instr)
        return instr

    @staticmethod
    def check_type(instr):
        # replace pass with your code 
        pass

    @staticmethod
    def check_auth(component, instr):
        # replace pass with your code 
        pass

    @staticmethod
    def check_state(component, instr):

        # replace pass with your code 
        pass
