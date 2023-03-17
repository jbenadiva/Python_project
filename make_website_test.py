import unittest

from make_website import *

class MakeWebsite_Test(unittest.TestCase):

    def test_surround_block(self):
        # test text with surrounding h1 tags
        self.assertEqual("<h1>Eagles</h1>", surround_block('h1', 'Eagles'))

        # test text with surrounding h2 tags
        self.assertEqual("<h2>Red Sox</h2>", surround_block('h2', 'Red Sox'))

        # test text with surrounding p tags
        self.assertEqual('<p>Lorem ipsum dolor sit amet, consectetur ' +
                         'adipiscing elit. Sed ac felis sit amet ante porta ' +
                         'hendrerit at at urna.</p>',
                         surround_block('p', 'Lorem ipsum dolor sit amet, consectetur ' +
                                        'adipiscing elit. Sed ac felis sit amet ante porta ' +
                                        'hendrerit at at urna.'))

    def test_create_email_link(self):

        # test email with @ sign
        self.assertEqual(
            '<a href="mailto:lbrandon@wharton.upenn.edu">lbrandon[aT]wharton.upenn.edu</a>',
            create_email_link('lbrandon@wharton.upenn.edu')
        )

        # test email with @ sign
        self.assertEqual(
            '<a href="mailto:krakowsky@outlook.com">krakowsky[aT]outlook.com</a>',
            create_email_link('krakowsky@outlook.com')
        )

        # test email without @ sign
        self.assertEqual(
            '<a href="mailto:lbrandon.at.seas.upenn.edu">lbrandon.at.seas.upenn.edu</a>',
            create_email_link('lbrandon.at.seas.upenn.edu')
        )

    def test_generate_email(self):

        f = open('TestResumes/resume_wrong_email/resume.txt', "r")
        lines = f.readlines()
        self.assertEqual("", generate_email(lines))
        f.close()
        f = open('TestResumes/resume_bad_name_lowercase/resume.txt', "r")
        lines = f.readlines()
        self.assertEqual("lbrandon@wharton.upenn.edu", generate_email(lines))
        f.close()
        f = open('TestResumes/resume_template_email_w_whitespace/resume.txt', "r")
        lines = f.readlines()
        self.assertEqual("lbrandon@wharton.upenn.edu", generate_email(lines))
        f.close()

    def test_generate_name(self):
        f = open('TestResumes/resume_bad_name_lowercase/resume.txt', "r")
        lines = f.readlines()
        self.assertEqual("Invalid Name", generate_name(lines))
        f.close()
        f = open('TestResumes/resume_courses_w_whitespace/resume.txt', "r")
        lines = f.readlines()
        self.assertEqual("Brandon (courses w/ whitespace)", generate_name(lines))
        f.close()
        f = open('TestResumes/resume_courses_weird_punc/resume.txt', "r")
        lines = f.readlines()
        self.assertEqual("Brandon (courses weird punctuation)", generate_name(lines))
        f.close()

    def test_generate_courses_list(self):
        f = open('TestResumes/resume_courses_weird_punc/resume.txt', "r")
        lines = f.readlines()
        self.assertEqual(['Programming Languages and Techniques', 'Biomedical image analysis', 'Software Engineering'], generate_courses_list(lines))
        f.close()
        f = open('TestResumes/resume_courses_w_whitespace/resume.txt', "r")
        lines = f.readlines()
        self.assertEqual(['Programming Languages and Techniques', 'Biomedical image analysis', 'Pottery'], generate_courses_list(lines))
        f.close()
        f = open('TestResumes/resume_projects_with_blanks/resume.txt', "r")
        lines = f.readlines()
        self.assertEqual(['Programming Languages and Techniques', 'Biomedical image analysis', 'Software Engineering'], generate_courses_list(lines))
        f.close()

    def test_generate_projects_list(self):
        f = open('TestResumes/resume_projects_w_whitespace/resume.txt', "r")
        lines = f.readlines()
        self.assertEqual(['CancerDetector.com, New Jersey, USA - Project manager, codified the assessment and mapped it to the CancerDetector ontology. Member of the UI design team, designed the portfolio builder UI and category search pages UI. Reviewed existing rank order and developed new search rank order approach.', 'Biomedical Imaging - Developed a semi-automatic image mosaic program based on SIFT algorithm (using Matlab)'],
                         generate_projects_list(lines))
        f.close()
        f = open('TestResumes/resume_projects_with_blanks/resume.txt', "r")
        lines = f.readlines()
        self.assertEqual(['CancerDetector.com, New Jersey, USA - Project manager, codified the assessment and mapped it to the CancerDetector ontology. Member of the UI design team, designed the portfolio builder UI and category search pages UI. Reviewed existing rank order and developed new search rank order approach.', 'Biomedical Imaging - Developed a semi-automatic image mosaic program based on SIFT algorithm (using Matlab)'],
                         generate_projects_list(lines))
        f.close()





if __name__ == '__main__':
    unittest.main()
