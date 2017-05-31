
import traceback
from runtime.exceptions.app.exception import AppException
from runtime.utils.type_utils.type_utils import check_pred
from runtime.datatypes.cmd.cmd import Cmd
from runtime.objects.session.session import Session
from runtime.objects.role.role import Role
from runtime.datatypes.instr.del_user.del_user_instr import DelUserInstr

class DelUser:

    @staticmethod 
    def do(obj, instr):
        print "del_user: %s" % instr

        DelUser.check_type(instr)
        DelUser.check_auth(obj, instr)
        DelUser.check_state(obj, instr)
        return instr

    @staticmethod
    def check_type(instr):
        # replace the next line with your code
        pass

    @staticmethod
    def check_auth(obj, instr):
        # replace the next line with your code
        pass

    @staticmethod
    def check_state(obj, instr):
        # replace the next line with your code
        pass
