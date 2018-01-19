import unittest # Import the unittest module
import pyperclip
from contact import Contact #Importing the contact Class


class TestContact(unittest.TestCase):

   '''
   Test class that defines test cases for the contact class behaviours.

   Args:
       unittest.TestCase: TestCase class that helps in creating test cases
   '''

   def setUp(self):
       '''
       Set up method to run before each test cases.
       '''
       self.new_contact = Contact("evans","Mwenda","0705861793","test@user.com") # create contact object
   def test_init(self):
       '''
       test_init test case to test if the object is initialized properly
       '''
       self.assertEqual(self.new_contact.first_name,"evans")
       self.assertEqual(self.new_contact.last_name,"Mwenda")
       self.assertEqual(self.new_contact.number,"0705861793")
       self.assertEqual(self.new_contact.email,"test@user.com")



   def test_save_contact(self):
       '''
       test_save_contact test case to test if the object is saved onto
       the contact_list
       '''
       self.new_contact.save_contact() #saving the new contact
       self.assertEqual(len(Contact.contact_list),1)
# third test

# setup and class creation up here
# setup and class creation up here
   def tearDown(self):
       '''
       tearDown method that does clean up after each test case has run.
       '''
       Contact.contact_list = []

   def test_save_multiple_contact(self):
           '''
           test_save_multiple_contact to check if we save multiple contact_list
           objects to our contact_list
           '''
           self.new_contact.save_contact()
           test_contact=Contact("Test","user","0705861793","test@user.com")
           test_contact.save_contact()
           self.assertEqual(len(Contact.contact_list),2)

# foorth test
   def test_delete_contact(self):
            '''
            test_delete_contact to test if we can remove a contact from contact_list
            '''
            self.new_contact.save_contact()
            test_contact=Contact("Test","user","0705861793","test@user.com")
            test_contact.save_contact()
            self.new_contact.delete_contact()# Deleting a contact object
            self.assertEqual(len(Contact.contact_list),1)

            # fifth test
   def test_find_contact_by_number(self):
        '''
        test to check if we can find a contact by phone number and display information
        '''

        self.new_contact.save_contact()
        test_contact = Contact("Test","user","0705861793","test@user.com") # new contact
        test_contact.save_contact()

        found_contact = Contact.find_by_number("0705861793")

        self.assertEqual(found_contact.email,test_contact.email)

   def test_contact_exists(self):
        '''
        test to check if we can return a Boolean if we cannot find the
        contact
        '''
        self.new_contact.save_contact()
        test_contact=Contact("Test","user","0705861793","test@user.com")# add contact
        test_contact.save_contact()

        contact_exists=Contact.contact_exist("0705861793")


        self.assertTrue(contact_exists)

   def test_display_all_contacts(self):
        '''
        method that returns list the contact saved
        '''
        self.assertEqual(Contact.display_contacts(),Contact.contact_list)
   def test_copy_email(self):
        '''
        Test to confirm that we are copying the email address from a found contact
        '''

        self.new_contact.save_contact()
        Contact.copy_email("0705861793")

        self.assertEqual(self.new_contact.email,pyperclip.paste())
if __name__ ==  '__main__':
   unittest.main()
