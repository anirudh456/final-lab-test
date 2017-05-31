
class Cmd():

    def __init__(self, cmd_name):
        self.name = cmd_name

    def __repr__(self):
        return self.name
    
    def __hash__(self):
        return hash(self.name)

    @staticmethod
    def is_cmd(cmd):
        return cmd in Cmd.cmds

    def __eq__(self, other):
        return isinstance(other, Cmd) and self.name == other.name


Cmd.show_users = Cmd('show_users')
Cmd.add_user = Cmd('add_user')
Cmd.del_user = Cmd('del_user')
Cmd.update_user = Cmd('update_user')

Cmd.cmds = [Cmd.show_users, 
            Cmd.add_user, 
            Cmd.del_user, 
            Cmd.update_user]
