import unittest
import HtmlTestRunner
from test_youtube import Test_youtube
from test_luma import Test_Luma

# get all tests from SearchText and HomePageTest class
youtube_test = unittest.TestLoader().loadTestsFromTestCase(Test_youtube)
luma_test = unittest.TestLoader().loadTestsFromTestCase(Test_Luma)

# create a test suite combining search_text and home_page_test
test_suite = unittest.TestSuite([youtube_test, luma_test])

# run the suite
unittest.TextTestRunner(verbosity=2).run(test_suite)


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output = "./report"))


