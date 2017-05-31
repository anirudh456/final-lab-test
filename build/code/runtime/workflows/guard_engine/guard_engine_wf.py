
from runtime.components.guard.guard import Guard
from runtime.components.engine.engine import Guard
from runtime.emgrs.svem.svem import EntityMgr
from runtime.components import guard
from runtime.components import engine

class GuardSysWf():
  
  def __init__(self):
     em      = EntityMgr()
     guard   = Guard(em)
     engine  = Engine(em)

     # set up routes in the guard
     guard.add_command_handler(Cmd.add_user, guard.add_user.add_user.AddUser.do)
     guard.add_command_handler(Cmd.del_user, guard.del_user.del_user.DelUser.do)
     guard.add_command_handler(Cmd.show_users, guard.show_users.show_users.ShowUsers.do)

     # set up routes in the engine
     engine.add_command_handler(Cmd.add_user, engine.add_user.add_user.AddUser.do)
     engine.add_command_handler(Cmd.del_user, engine.del_user.del_user.DelUser.do)
     engine.add_command_handler(Cmd.show_users, engine.show_users.show_users.ShowUsers.do)
   
     self.em = em
     self.guard = guard
     self.engine = engine

  def run(instr):
    result = None
    try:
      # action same as instr
      action = self.guard.do(instr)
      result = self.sys.do(action)
    except Exception as e:
      result = e
    finally:
      return result
