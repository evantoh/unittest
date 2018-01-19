import unittest
import pyperclip

class Contact:
    contact_list = [] #class variable tha belongs to entire class and can be accessed by all instances of the class

    def __init__(self,first_name,last_name,number,email):#instance variables & cannot be changed

        self.first_name= first_name
        self.last_name= last_name
        self.number=number
        self.email=email

        contact_list = [] # Empty contact list
 # Init method up here
    def save_contact(self):

        '''
        save_contact method saves contact objects into contact_list
        '''

        Contact.contact_list.append(self)

    def delete_contact(self):
        '''
        delete_contact method delates a saved contact from contact_list
        '''
        Contact.contact_list.remove(self)
    @classmethod
    def find_by_number(cls,number):
        '''
        Method that takes in a number and returns a contact that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            Contact of person that matches the number.
        '''
        for contact in cls.contact_list:
            if contact.number == number:
                return contact

    @classmethod
    def contact_exist(cls,number):
        '''
        method that checks if  contact exists in contact contact_list

            Args:
                number: Phone number to search if it exists
            Returns :
                Boolean: True or false depending if the contact exists
        '''
        for contact in cls.contact_list:
            if contact.number == number:
                return True


        return False
    @classmethod
    def display_contacts(cls):
            '''
            method that returns the contact contact_list
            '''
            return cls.contact_list
    @classmethod
    def copy_email(cls,number):
        contact_found = Contact.find_by_number(number)
        pyperclip.copy(contact_found.email)
