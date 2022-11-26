import streamlit as st
from pyresparser import ResumeParser
from pdfminer3.layout import LAParams, LTTextBox
from pdfminer3.pdfpage import PDFPage
from pdfminer3.pdfinterp import PDFResourceManager
from pdfminer3.pdfinterp import PDFPageInterpreter
from pdfminer3.converter import TextConverter
import io
import json 





# these method allo as to read cv

def pdf_reader(file):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(
        resource_manager, fake_file_handle, laparams=LAParams())
    page_interpreter = PDFPageInterpreter(resource_manager, converter)
    with open(file, 'rb') as fh:
        for page in PDFPage.get_pages(fh,
                                      caching=True,
                                      check_extractable=True):
            page_interpreter.process_page(page)
            print(page)
        text = fake_file_handle.getvalue()

    # close open handles
    converter.close()
    fake_file_handle.close()
    return text




def run(file):
    print(file)
    pdf_file = open('C:/Users/21620/OneDrive/Bureau/Projects/RestApi/restapistage/apistage/'+file, "rb")
    data = pdf_file.read()
    pdf_file.close()
    save_image_path = 'C:/Users/21620/OneDrive/Bureau/Projects/RestApi/restapistage/apistage/CV/' + file
    with open(save_image_path, "wb") as f:
        f.write(data)
    resume_data = ResumeParser(save_image_path).get_extracted_data()
    if resume_data:
        # Get the whole resume data
        resume_text = pdf_reader(save_image_path)
        try:
            name = resume_data['name']
            Email = resume_data['email']
            Contact = resume_data['mobile_number']
            no_of_pages = resume_data['no_of_pages']
            skills = resume_data['skills']
        except:
            pass
        cand_level = ''
        if resume_data['no_of_pages'] == 1:
            cand_level = "Fresher"

        elif resume_data['no_of_pages'] == 2:
            cand_level = "Intermediate"

        elif resume_data['no_of_pages'] >= 3:
            cand_level = "Experienced"

        # recommendation
        ds_keyword = ['tensorflow', 'keras', 'pytorch',
                      'machine learning', 'deep Learning', 'flask', 'streamlit']
        web_keyword = ['react', 'django', 'node jS', 'react js', 'php', 'laravel', 'magento', 'wordpress',
                       'javascript', 'angular js', 'c#', 'flask']
        android_keyword = ['android', 'android development',
                           'flutter', 'kotlin', 'xml', 'kivy']
        ios_keyword = ['ios', 'ios development',
                       'swift', 'cocoa', 'cocoa touch', 'xcode']
        uiux_keyword = ['ux', 'adobe xd', 'figma', 'zeplin', 'balsamiq', 'ui', 'prototyping', 'wireframes', 'storyframes', 'adobe photoshop', 'photoshop', 'editing', 'adobe illustrator',
                        'illustrator', 'adobe after effects', 'after effects', 'adobe premier pro', 'premier pro', 'adobe indesign', 'indesign', 'wireframe', 'solid', 'grasp', 'user research', 'user experience']

        recommended_skills = []
        reco_field = ''
        rec_course = ''
        # Courses recommendation
        for i in resume_data['skills']:
            # Data science recommendation
            if i.lower() in ds_keyword:
                print(i.lower())
                reco_field = 'Data Science'
                st.success(
                    "** Our analysis says you are looking for Data Science Jobs.**")
                recommended_skills = ['Data Visualization', 'Predictive Analysis', 'Statistical Modeling', 'Data Mining', 'Clustering & Classification', 'Data Analytics',
                                      'Quantitative Analysis', 'Web Scraping', 'ML Algorithms', 'Keras', 'Pytorch', 'Probability', 'Scikit-learn', 'Tensorflow', "Flask", 'Streamlit']
                # recommended_keywords = st_tags(label='### Recommended skills for you.',
                # text='Recommended skills generated from System',value=recommended_skills,key = '2')
                # st.markdown('''<h4 style='text-align: left; color: #1ed760;'>Adding this skills to resume will boost🚀 the chances of getting a Job💼</h4>''',unsafe_allow_html=True)
                # rec_course = course_recommender(ds_course)
                break

            # Web development recommendation
            elif i.lower() in web_keyword:
                print(i.lower())
                reco_field = 'Web Development'
                st.success(
                    "** Our analysis says you are looking for Web Development Jobs **")
                recommended_skills = ['React', 'Django', 'Node JS', 'React JS', 'php', 'laravel',
                                      'Magento', 'wordpress', 'Javascript', 'Angular JS', 'c#', 'Flask', 'SDK']
                # recommended_keywords = st_tags(label='### Recommended skills for you.',
                # text='Recommended skills generated from System',value=recommended_skills,key = '3')
                # st.markdown('''<h4 style='text-align: left; color: #1ed760;'>Adding this skills to resume will boost🚀 the chances of getting a Job💼</h4>''',unsafe_allow_html=True)
                # rec_course = course_recommender(web_course)
                break

            # Android App Development
            elif i.lower() in android_keyword:
                print(i.lower())
                reco_field = 'Android Development'
                st.success(
                    "** Our analysis says you are looking for Android App Development Jobs **")
                recommended_skills = ['Android', 'Android development', 'Flutter',
                                      'Kotlin', 'XML', 'Java', 'Kivy', 'GIT', 'SDK', 'SQLite']
                # recommended_keywords = st_tags(label='### Recommended skills for you.',
                # text='Recommended skills generated from System',value=recommended_skills,key = '4')
                # st.markdown('''<h4 style='text-align: left; color: #1ed760;'>Adding this skills to resume will boost🚀 the chances of getting a Job💼</h4>''',unsafe_allow_html=True)
                # rec_course = course_recommender(android_course)
                break

            # IOS App Development
            elif i.lower() in ios_keyword:
                print(i.lower())
                reco_field = 'IOS Development'
                st.success(
                    "** Our analysis says you are looking for IOS App Development Jobs **")
                recommended_skills = ['IOS', 'IOS Development', 'Swift', 'Cocoa', 'Cocoa Touch', 'Xcode',
                                      'Objective-C', 'SQLite', 'Plist', 'StoreKit', "UI-Kit", 'AV Foundation', 'Auto-Layout']
                # recommended_keywords = st_tags(label='### Recommended skills for you.',
                # text='Recommended skills generated from System',value=recommended_skills,key = '5')
                # st.markdown('''<h4 style='text-align: left; color: #1ed760;'>Adding this skills to resume will boost🚀 the chances of getting a Job💼</h4>''',unsafe_allow_html=True)
                # rec_course = course_recommender(ios_course)
                break

            # Ui-UX Recommendation
            elif i.lower() in uiux_keyword:
                print(i.lower())
                reco_field = 'UI-UX Development'
                st.success(
                    "** Our analysis says you are looking for UI-UX Development Jobs **")
                recommended_skills = ['UI', 'User Experience', 'Adobe XD', 'Figma', 'Zeplin', 'Balsamiq', 'Prototyping', 'Wireframes', 'Storyframes',
                                      'Adobe Photoshop', 'Editing', 'Illustrator', 'After Effects', 'Premier Pro', 'Indesign', 'Wireframe', 'Solid', 'Grasp', 'User Research']
                # recommended_keywords = st_tags(label='### Recommended skills for you.',
                # text='Recommended skills generated from System',value=recommended_skills,key = '6')
                # st.markdown('''<h4 style='text-align: left; color: #1ed760;'>Adding this skills to resume will boost🚀 the chances of getting a Job💼</h4>''',unsafe_allow_html=True)
                # rec_course = course_recommender(uiux_course)
                break

                #

        # Resume writing recommendation

        resume_score = 0
        if 'Objective' in resume_text:
            resume_score = resume_score+20

        if 'Declaration' in resume_text:
            resume_score = resume_score + 20

        if 'Hobbies' or 'Interests' in resume_text:
            resume_score = resume_score + 20

        if 'Achievements' in resume_text:
            resume_score = resume_score + 20

        if 'Projects' in resume_text:
            resume_score = resume_score + 20

        score = 0
        for percent_complete in range(resume_score):
            score += 1

    else:
        return "No Result"
    print(resume_data)
    return json.dumps({"name": name, "email": Email, "Contact": Contact, "no_of_pages": no_of_pages, "cand_level": cand_level, "score": score, "Recommanded_Skills": recommended_skills, "skills": skills})
