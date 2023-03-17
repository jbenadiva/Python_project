def surround_block(tag, text):
    """
    Surrounds the given text with the given html tag and returns the string.
    """

    html = "<" + tag + ">" + text + "</" + tag + ">"


    return html

def create_email_link(email_address):
    """
    Creates an email link with the given email_address.
    To cut down on spammers harvesting the email address from the webpage,
    displays the email address with [aT] instead of @.

    Example: Given the email address: lbrandon@wharton.upenn.edu
    Generates the email link: <a href="mailto:lbrandon@wharton.upenn.edu">lbrandon[aT]wharton.upenn.edu</a>

    Note: If, for some reason the email address does not contain @,
    use the email address as is and don't replace anything.
    """
    email_non_at = email_address.replace('@', '[aT]')
    email_link = "<a href=\"mailto:{}\">{}</a>".format(email_address,email_non_at)

    return email_link

def generate_email(lines):
    """Function that searches for '@' in the file and chooses that line for the email line. It will then check to see if the last 4 characters include a valid email (.edu, .com) If the email includes in digits, its in invalid email
    and returns an empty field"""
    for line in lines:
        if '@' in line:
            email_line = lines.index(line)

    email = lines[email_line]

    email = email.strip()
    email_length = len(email)
    email_suffix = ''
    for i in range(email_length-4, email_length):
        email_suffix += email[i]

    email_suffix = email_suffix.strip()
    valid_email_suffix = ['.edu','.com']
    if email_suffix not in valid_email_suffix:
        email = ''
    at_index = email.index('@')
    if email[at_index + 1].isupper():
        email = ""

    for char in email:
        if char.isdigit():
            email = ""
        else:
            continue

    return email

def generate_name(lines):
    """Takes the first line of the file as the name. If the first letter is upper, then strip the line and use it s the name. If not, it's an invalid name"""
    name_key = lines[0].strip()
    if name_key[0].isupper():
        name_key = lines[0].strip()
    else:
        name_key = "Invalid Name"

    return name_key

def generate_courses_list(lines):
    """Looks for the line that has a word "Courses" in it, and then makes that the line in the file talking about courses.
    Creates a list that is split after the word "courses" and then starts the list after that split.
    strips each string in the list of courses and removes the first item
    Splits the strings on a ',' and then only allows characters in the allowed_character lsit
    """
    for line in lines:
        if 'Courses' in line:
            course_line = lines.index(line)

    courses_key = lines[course_line].split('Courses')[1].strip()
    courses_key = courses_key.split(',')

    for i in range(len(courses_key)):
        courses_key[i] = courses_key[i].strip()

    allowed_characters = [' ','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                          't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                          'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5',
                          '6', '7', '8', '9', '0']

    for course in courses_key:
        index = courses_key.index(course)
        course_new = ""
        for char in course:
            if char in allowed_characters:
                course_new += char
        courses_key[index] = course_new

    for i in range(len(courses_key)):
        courses_key[i] = courses_key[i].strip()
    return courses_key

def generate_projects_list(lines):
    """looks for the line that has "Projects" in it and establishes that as the fist line of the projects section. Ends the section when we see ---------
    strips the content on each line and adds it to the list of projects"""


    for line in lines:
        if 'Projects' in line:
            project_line = lines.index(line)

    for line in lines:
        if "----------" in line:
            end_line = lines.index(line)

    project_value = []
    for line in range(project_line+1,end_line):
        if lines[line].strip():
            project_value.append(lines[line])
        else:
            continue

    # need to adjust this to check to see if there are characters in the line, if there is, then append to the list, for all lines in range(project_line+1, end_line)

    project_value = [project.strip().replace("\n", "") for project in project_value]

    return project_value

def generate_html(txt_input_file, html_output_file):
    """

    Loads given txt_input_file,
    gets the name, email address, list of projects, and list of courses,
    then writes the info to the given html_output_file.

    # Hint(s):
    # call function(s) to load given txt_input_file
    # call function(s) to get name
    # call function(s) to get email address
    # call function(s) to get list of projects
    # call function(s) to get list of courses
    # call function(s) to write the name, email address, list of projects, and list of courses to the given html_output_file
    """
    resume = {}

    f = open(txt_input_file, "r")
    lines = f.readlines()

    email = generate_email(lines)

    student_name = 'Student name'
    name_key = generate_name(lines)

    courses = "Courses"
    courses_key = generate_courses_list(lines)

    projects = "Projects"
    project_value = generate_projects_list(lines)

    resume = {'Email': email, student_name: name_key, courses: courses_key, projects: project_value}

    f.close()

    #the biggest problem here is padding...need to figure out how to add 10px to the padding of the entire page
    with open(html_output_file, 'w') as f:
        f.write('<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">\n')
        f.write('<head>\n')
        f.write('\t<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>\n')
        f.write('\t<title>My Resume</title>\n')
        f.write('\t<style type="text/css">\n')
        f.write('\t\t* { margin: 0; padding: 0; }\n')
        f.write('\t\tbody { font: 16px Helvetica, Sans-Serif; line-height: 24px; }\n')
        f.write('\t\t.clear { clear: both; }\n')
        f.write('\t\t#page-wrap { width: 800px; margin: 40px auto 60px; }\n')
        f.write('\t\t#pic { float: right; margin: -30px 0 0 0; }\n')
        f.write(
            '\t\th1 { margin: 0 0 16px 0; padding: 0 0 16px 0; font-size: 42px; font-weight: bold; letter-spacing: -2px; border-bottom: 1px solid #999; }\n')
        f.write('\t\th2 { font-size: 20px; margin: 0 0 6px 0; position: relative; }\n')
        f.write(
            '\t\th2 span { position: absolute; bottom: 0; right: 0; font-style: italic; font-family: Georgia, Serif; font-size: 16px; color: #999; font-weight: normal; }\n')
        f.write('\t\tp { margin: 0 0 16px 0; }\n')
        f.write('\t\ta { color: #999; text-decoration: none; border-bottom: 1px dotted #999; }\n')
        f.write('\t\ta:hover { border-bottom-style: solid; color: black; }\n')
        f.write('\t\tul { margin: 0 0 32px 17px; }\n')
        f.write('\t\t#objective { width: 500px; float: left; }\n')
        f.write('\t\t#objective p { font-family: Georgia, Serif; font-style: italic; color: #666; }\n')
        f.write(
            '\t\tdt { font-style: italic; font-weight: bold; font-size: 18px; text-align: right; padding: 0 26px 0 0; width: 150px; float: left; height: 100px; border-right: 1px solid #999;  }\n')
        f.write('\t\tdd { width: 600px; float: right; }\n')
        f.write('\t\tdd.clear { float: none; margin: 0; height: 15px; }\n')
        f.write('\t\thtml, body {padding: 20px;}\n')
        f.write('\t</style>\n')
        f.write('</head>\n')
        f.write('<body>\n')
        f.write(f"<html><head><title>{resume['Student name']} - My Resume</title></head><body>")
        f.write('<div>\n')
        f.write(f"<h1>{resume['Student name']}</h1>")
        f.write(f"<p>Email: {create_email_link(resume['Email'])}</p>")
        f.write('</div>\n')
        f.write('<div>\n')
        f.write(f"<h2>Projects</h2>")
        f.write("<ul>")
        for project in resume["Projects"]:
            f.write(f"<li>{project}</li>")
        f.write("</ul>")
        f.write('</div>\n')
        f.write('<div>\n')
        f.write(f"<h3>Courses</h3>")
        course_list = ''
        for i, course in enumerate(resume['Courses']):
            course_list += course
            if i < len(resume['Courses']) - 1:
                course_list += ', '
        f.write(f"<span>{course_list}</span>")
        f.write('</div>\n')
        f.write('</body>\n')
        f.write('</html>')
    return resume

def main():

    # DO NOT REMOVE OR UPDATE THIS CODE
    # generate resume.html file from provided sample resume.txt
    resume = generate_html('resume.txt', 'resume.html')

    # DO NOT REMOVE OR UPDATE THIS CODE.
    # Uncomment each call to the generate_html function when you’re ready
    # to test how your program handles each additional test resume.txt file
    generate_html('TestResumes/resume_bad_name_lowercase/resume.txt', 'TestResumes/resume_bad_name_lowercase/resume.html')
    generate_html('TestResumes/resume_courses_w_whitespace/resume.txt', 'TestResumes/resume_courses_w_whitespace/resume.html')
    generate_html('TestResumes/resume_courses_weird_punc/resume.txt', 'TestResumes/resume_courses_weird_punc/resume.html')
    generate_html('TestResumes/resume_projects_w_whitespace/resume.txt', 'TestResumes/resume_projects_w_whitespace/resume.html')
    generate_html('TestResumes/resume_projects_with_blanks/resume.txt', 'TestResumes/resume_projects_with_blanks/resume.html')
    generate_html('TestResumes/resume_template_email_w_whitespace/resume.txt', 'TestResumes/resume_template_email_w_whitespace/resume.html')
    generate_html('TestResumes/resume_wrong_email/resume.txt', 'TestResumes/resume_wrong_email/resume.html')

    # If you want to test additional resume files, call the generate_html function with the given .txt file
    # and desired name of output .html file

if __name__ == '__main__':
    main()