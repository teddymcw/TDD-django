from selenium import webdriver, Keys
import unittest
import time

class NewVisitorTest(unittest.TestCase): # 

    def setUp(self): #
        self.browser = webdriver.Firefox() 
        self.browser.implicitly_wait(3)

    def tearDown(self): 
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table') 
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):

        # Edith has heard about a cool new online to-do app. 
        # She goes to check out its homepage self.browser.get('http://localhost:8000')
        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)


        # She is invited to enter a to-do item straight away
        # There is still a text box inviting her to add another item. She # enters "Use peacock feathers to make a fly" (Edith is very
        # methodical)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER) 
        inputbox.send_keys('Use peacock feathers to make a fly')
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly') 


        # The page updates again, and now shows both items on her list
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows]) 
        self.assertIn('2: Use peacock feathers to make a fly' ,
                       [row.text for row in rows] 
                     )
        # Edith wonders whether the site will remember her list. Then she sees 
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.
        self.fail('Finish the test!')


        # self.assertTrue(
        #     any(row.text == '1: Buy peacock feathers' for row in rows),
        #     "New to-do item did not appear in table -- its text was:\n%s" % (
        #     table.text,
        #     )
        # )
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows]) #rewriting statement above

        # There is still a text box inviting her to add another item. 
        # She enters "Use peacock feathers to make a fly" (Edith is very methodical)
        self.fail('Finish the test!')

        # When she hits enter, the page updates, and now the page lists # "1: Buy peacock feathers" as an item in a to-do list table inputbox.send_keys(Keys.ENTER)
        
        time.sleep(10)
        table = self.browser.find_element_by_id('id_list_table')

        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows), "New to-do item did not appear in table"
            )

if __name__ == '__main__': #
    unittest.main()