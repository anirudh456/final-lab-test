
from runtime.objects.email.email import Email
from runtime.objects.name.name import Name
from runtime.objects.role.role import Role
from runtime.objects.user.user import User
from runtime.objects.session.session import Session
from runtime.emgrs.svem.tests.test_harness import TestHarness
from  runtime.utils.entitymgrs.volatile.volatile_entity_mgr_exception import VolatileEntityMgrException



class TestSession(TestHarness):
    TESTING = True

    def test_add_session(self):
        print "testing test_add_session"
        luke = User(name=Name(val="Luke Skywalker"),
                  email=Email(val="luke@space.org"),
                  roles=[Role.admin]);

        luke_session = Session(user=luke, key="1323", role=Role.admin)
        self.em.add_user(luke)
        self.em.add_session(luke_session)
        self.assertEquals(len(self.em.get_all(Session)), 1)

    def test_add_duplicate_session_fails(self):
        print "testing test_add_duplicate_session_fails"


        luke = User(name=Name(val="Luke Skywalker"),
                  email=Email(val="luke@space.org"),
                  roles=[Role.admin]);

        luke_session = Session(user=luke, key="1323", role=Role.admin)
        self.em.add_user(luke)
        self.em.add_session(luke_session)

        with self.assertRaises(VolatileEntityMgrException):
            self.em.add_session(luke_session)


        luke2 = User(name=Name(val="Luke Two Skywalker"),
                  email=Email(val="luke2@space.org"),
                  roles=[Role.admin]);

        self.em.add_user(luke2)
        luke2_session = Session(user=luke2, key="1323", role=Role.admin)

        with self.assertRaises(VolatileEntityMgrException):
            self.em.add_session(luke2_session)

    def test_delete_session(self):
        print "testing test_delete_session"
        luke = User(name=Name(val="Luke Skywalker"),
                  email=Email(val="luke@space.org"),
                  roles=[Role.admin]);

        luke_session = Session(user=luke, key="1323", role=Role.admin)
        self.em.add_user(luke)
        self.em.add_session(luke_session)

        self.assertEquals(len(self.em.get_all(Session)), 1)
        self.em.delete_session(luke_session)
        self.assertEquals(len(self.em.get_all(Session)), 0)

    def test_delete_session_fails(self):
        print "testing test_delete_session_fails"
        email=Email(val="luke@space.org")
        luke = User(name=Name(val="Luke Skywalker"),
                    email=email,
                    roles=[Role.admin]);

        luke_session = Session(user=luke, key="1323", role=Role.admin)
        #luke_session is not added so it can not be deleted
        with self.assertRaises(VolatileEntityMgrException):
            self.em.delete_session(luke_session)
        

    def test_update_session(self):
        # for debugging!
#        import pdb
 #       pdb.set_trace()

        print "testing test_update_session"
        luke = User(name=Name(val="Luke Skywalker"),
                  email=Email(val="luke@space.org"),
                  roles=[Role.admin]);

        luke_session = Session(user=luke, key="1323", role=Role.admin)
        self.em.add_user(luke)
        self.em.add_session(luke_session)

        self.assertEquals(len(self.em.get_all(Session)), 1)

        with self.assertRaises(Exception):
            self.em.update_session(luke_session, role=Role.user)
                                
        self.assertEquals(len(self.em.get_all(Session)), 1)

        self.assertEquals(self.em.get_all(Session)[0].get("role").get("val"), "admin")

    # We are trying updating luke's session key to be the same as
    # luke2's session key.  This should fail because the session key
    # is primary key of session. 

    def test_update_session_fails(self):
        print "testing test_update_session_fails"
        luke = User(name=Name(val="Luke Skywalker"),
                    email=Email(val="luke@space.org"),
                    roles=[Role.admin]);

        luke_session = Session(user=luke, key="1323", role=Role.admin)
        self.em.add_user(luke)
        self.em.add_session(luke_session)
        self.assertEquals(len(self.em.get_all(Session)), 1)

        luke2 = User(name=Name(val="Luke New Skywalker"),
                        email=Email(val="luke_new@space.org"),
                        roles=[Role.admin]);

        luke2_session = Session(user=luke2, key="4455", role=Role.admin)

        self.em.add_user(luke2)
        self.em.add_session(luke2_session)

        self.assertEquals(len(self.em.get_all(Session)), 2)

        with self.assertRaises(VolatileEntityMgrException):
            self.em.update_session(luke_session, key="4455")
        
