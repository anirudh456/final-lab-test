
from runtime.objects.email.email import Email
from runtime.objects.name.name import Name
from runtime.objects.role.role import Role
from runtime.objects.user.user import User
from runtime.emgrs.svem.tests.test_harness import TestHarness
from  runtime.utils.entitymgrs.volatile.volatile_entity_mgr_exception import VolatileEntityMgrException



class TestUser(TestHarness):
    TESTING = True

    def test_add_user(self):
        print "testing test_add_user"
        luke = User(name=Name(val="Luke Skywalker"),
                  email=Email(val="luke@space.org"),
                  roles=[]);
        self.em.add_user(luke)
        self.assertEquals(len(self.em.get_all(User)), 1)

    def test_add_user_fails(self):
        print "testing test_add_user_fails"
        email=Email(val="luke@space.org")
        luke = User(name=Name(val="Luke Skywalker"),
                    email=email,
                    roles=[]);
        self.em.add_user(luke)

        luke2 = User(name=Name(val="Luke Two Skywalker"),
                    email=email,
                    roles=[]);

        with self.assertRaises(VolatileEntityMgrException):
            self.em.add_user(luke2)
        

    def test_delete_user(self):
        print "testing test_delete_user"
        luke = User(name=Name(val="Luke Skywalker"),
                  email=Email(val="luke@space.org"),
                  roles=[]);
        self.em.add_user(luke)
        self.assertEquals(len(self.em.get_all(User)), 1)
        self.em.delete_user(luke)
        self.assertEquals(len(self.em.get_all(User)), 0)

    def test_delete_user_fails(self):
        print "testing test_delete_user_fails"
        email=Email(val="luke@space.org")
        luke = User(name=Name(val="Luke Skywalker"),
                    email=email,
                    roles=[]);
        #user luke is not added
        with self.assertRaises(VolatileEntityMgrException):
            self.em.delete_user(luke)
        

    def test_update_user(self):
        print "testing test_update_user"
        luke = User(name=Name(val="Luke Skywalker"),
                  email=Email(val="luke@space.org"),
                  roles=[]);
        self.em.add_user(luke)
        self.assertEquals(len(self.em.get_all(User)), 1)
        self.em.update_user(luke,
                            email=Email(val="newluke@space.org"),
                            name=Name(val="Luke New Skywalker"))
                                
        self.assertEquals(len(self.em.get_all(User)), 1)
        self.assertEquals(self.em.get_all(User)[0].get("name").get("val"),
                              "Luke New Skywalker")

        self.assertEquals(self.em.get_all(User)[0].get("email").get("val"), 
                        "newluke@space.org")


    def test_update_user_fails(self):
        print "testing test_update_user_fails"
        luke = User(name=Name(val="Luke Skywalker"),
                    email=Email(val="luke@space.org"),
                    roles=[]);

        self.em.add_user(luke)
        self.assertEquals(len(self.em.get_all(User)), 1)

        luke2 = User(name=Name(val="Luke New Skywalker"),
                        email=Email(val="luke_new@space.org"),
                        roles=[]);
        self.em.add_user(luke2)
        self.assertEquals(len(self.em.get_all(User)), 2)

        with self.assertRaises(VolatileEntityMgrException):
            self.em.update_user(luke, email=Email(val="luke_new@space.org"))
        
