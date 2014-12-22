import os
from bs4 import BeautifulSoup, SoupStrainer
from urllib.request import urlopen
import re
from lxml import html

from test import all_major_dict, get_links, majors

only_title = SoupStrainer('title')
only_td = SoupStrainer('td')

pattern1 = 'very semester'
#pattern15 = 'every semester'
pattern2 = 'very fall'
#pattern25 = 'every fall'
pattern26 = 'Every Fall'
pattern3 = 'all semester'
#pattern35 = 'fall semester'
pattern36 = 'Fall Semester'
pattern16 = 'only in the fall'
pattern4 = 'very spring'
#pattern45 = 'every spring'
pattern5 = 'pring semester'
#pattern55 = 'spring semester'
pattern56 = 'Spring Semester'
#pattern57 = 'Every year; Spring semester'
pattern6 = 'very year'
#pattern65 = 'every year'
pattern66= 'annually'
pattern67= 'yearly'
pattern68 = 'nce each year'
pattern69 = 'nce per year'
#pattern691 = 'once per year'
pattern7 = 'lternate years'
#pattern75 = 'alternate years'
pattern76 = 'every two years'
pattern77 = 'very other year'
#pattern78 = 'Every other year'
pattern8 = 'lternate fall semesters'
#pattern85 = 'alternate fall semesters'
pattern86 = 'Every other fall'
pattern87 = 'Alternate years, fall semester'
pattern88 = 'in the fall every two years'
pattern89 = 'Fall semester every other year'
pattern9 = 'lternate spring semesters'
#pattern95 = 'alternate spring semesters'
pattern96 = 'very other spring'
#pattern97 = 'every other spring'
pattern98 = 'Alternate years, spring semester'
pattern99 = 'Spring semester, every other year'
pattern10 = 'Even numbered fall semesters'
pattern105 = 'even-numbered fall semesters'
pattern106 = 'fall term of even-numbered years'
pattern11 = 'Even numbered spring semesters'
pattern115 = 'even-numbered spring semesters'
pattern116 = 'spring term of even-numbered years'
pattern12 = 'Odd numbered fall semesters'
pattern125 = 'odd-numbered fall semesters'
pattern126 = 'fall term of odd-numbered years'
pattern13 = 'Odd numbered spring semesters'
pattern135 = 'odd-numbered spring semesters'
pattern14 = 'very third year'
#pattern145 = 'every third year'
pattern146 = 'every three years'
pattern15 = 'Two years in every three'
pattern17 = 'Offered next in 2015'

#pattern_list = [pattern1, pattern2, pattern3, pattern36, pattern4, pattern5, pattern56, pattern6, pattern66, pattern67, pattern68, pattern69, pattern7, pattern76, pattern77, pattern8, pattern86, pattern87, pattern88, pattern89, pattern9, pattern96, pattern98, pattern99, pattern10, pattern105, pattern106, pattern11, pattern115, pattern116, pattern12, pattern125, pattern126, pattern13, pattern135, pattern14, pattern146, pattern15, pattern16, pattern17]

#freq_list = [('Every semester'),('every semester'),('Every fall'),('every fall'),('Fall semester'),('fall semester'),('Every spring'), ('every spring'),('Spring semester'),('spring semester'),('Every year; Spring semester'),('Every year'),('every year'),('Alternate years'),('alternate years'),('every two years'),('Alternate fall semesters'), ('alternate fall semesters'),('Alternate spring semesters'),('alternate spring semesters'),('Even numbered fall semesters'),('even-numbered fall semesters'),('Even numbered spring semesters'), ('even-numbered spring semesters'), ('Odd numbered fall semesters'), ('odd-numbered fall semesters'),('Odd numbered spring semesters'),('odd-numbered spring semesters'), ('Every third year'), ('every third year')]

#root = lxml.html.fromstring(html_data)
#links_lxml_res = root.cssselect("a.detailsViewLink")
#links_lxml = [link.get("href") for link in links_lxml_res]
#links_lxml = list(set(links_lxml))

spring2015tree = html.fromstring(urlopen('http://www.macalester.edu/registrar/schedules/2015spring/class-schedule/').read())
fall2014tree = html.fromstring(urlopen('http://www.macalester.edu/registrar/schedules/2014fall/class-schedule/').read())
spring2014tree = html.fromstring(urlopen('http://www.macalester.edu/registrar/schedules/2014spring/class-schedule/').read())
fall2013tree = html.fromstring(urlopen('http://www.macalester.edu/registrar/schedules/2013fall/class-schedule/').read())
spring2013tree = html.fromstring(urlopen('http://www.macalester.edu/registrar/schedules/2013spring/class-schedule/').read())
fall2012tree = html.fromstring(urlopen('http://www.macalester.edu/registrar/schedules/2012fall/class-schedule/').read())
spring2012tree = html.fromstring(urlopen('http://www.macalester.edu/registrar/schedules/2012spring/class-schedule/').read())
fall2011tree = html.fromstring(urlopen('http://www.macalester.edu/registrar/schedules/2011fall/class-schedule/').read())

spring2015 = spring2015tree.xpath('.//table')[1].text_content()
fall2014 = fall2014tree.xpath('.//table')[1].text_content()
spring2014 = spring2014tree.xpath('.//table')[1].text_content()
fall2013 = fall2013tree.xpath('.//table')[1].text_content()
spring2013 = spring2013tree.xpath('.//table')[1].text_content()
fall2012 = fall2012tree.xpath('.//table')[1].text_content()
spring2012 = spring2012tree.xpath('.//table')[1].text_content()
fall2011 = fall2011tree.xpath('.//table')[1].text_content()


def nextSemester(url):
    next_sem = "No info"
    freq = "No info"
    
    pageHTML = html.fromstring(urlopen(url).read())
    soup = pageHTML.xpath('.//td[@class="block_content"]')[0].text_content()
    e = pageHTML.find('.//title')
    title = e.text_content()[0:4]+"\xa0"+e.text_content()[5:8]
    #title = "".join[(e.text_content()[0:4], "\xa0", e.text_content()[5:8])]    
    
    # title in spring2015:
    
    if pattern1 in soup:
        next_sem = 'Fall 2014'
        freq = 'Every semester'
    elif pattern2 in soup or pattern26 in soup or pattern3 in soup or pattern36 in soup or pattern16 in soup:
        if title in fall2013 or title in fall2012:
            next_sem = 'Fall 2015 (guess)'
        freq = 'Every fall'
    elif pattern4 in soup or pattern5 in soup or pattern56 in soup:
        next_sem = 'Spring 2016 (guess)'
        freq = 'Every spring'
    elif pattern6 in soup or pattern66 in soup or pattern67 in soup or pattern68 in soup or pattern69 in soup:
        if title in fall2013 or title in fall2012:
            next_sem = 'Fall 2015 (guess)'
        elif title in spring2014 or title in spring2013:
            next_sem = 'Spring 2015 (guess)'
        freq = 'Every year'  
    elif pattern7 in soup or pattern76 in soup or pattern77 in soup:      
        if title in spring2014:
            next_sem = 'Spring 2016'
        elif title in fall2013:
            next_sem = 'Fall 2015'   
        freq = 'Alternate years'
    elif pattern8 in soup or pattern86 in soup or pattern87 in soup or pattern88 in soup or pattern89 in soup:
        if title in fall2013:
            next_sem = 'Fall 2015'
        freq = 'Alternate fall semesters'
    elif pattern9 in soup or pattern96 in soup or pattern98 in soup or pattern99 in soup:
        if title in spring2014:
            next_sem = 'Spring 2016'
        freq = 'Alternate spring semesters'
    elif pattern10 in soup or pattern105 in soup or pattern106 in soup:
        if title in fall2012:
            next_sem = 'Fall 2016 (guess)'
        freq = 'Even numbered fall semesters'
    elif pattern11 in soup or pattern115 in soup or pattern116 in soup:
        next_sem = 'Spring 2016'
        freq = 'Even numbered spring semesters'
    elif pattern12 in soup or pattern125 in soup or pattern126 in soup:
        next_sem = 'Fall 2015'
        freq = 'Odd numbered fall semesters'
    elif pattern13 in soup or pattern135 in soup:
        if title in spring2013:
            next_sem = 'Spring 2017 (guess)'
        freq = 'Odd numbered spring semesters'
    elif pattern14 in soup or pattern146 in soup:
        if title in fall2012:
            next_sem = 'Fall 2015'    
        elif title in spring2013:
            next_sem = 'Spring 2016'
        elif title in fall2013:
            next_sem = 'Fall 2016'
        elif title in spring2014:
            next_sem = 'Spring 2017'
        freq = 'Every three years'
    #elif pattern15):
    #elif pattern16):
        #next_sem = 'Fall 2015'
        #freq = 'Only in the fall'
    elif pattern17 in soup:
        next_sem = 'Fall 2015'
        freq = 'Offered next in 2015'
    elif title in fall2011 and title in fall2013:
        next_sem = 'Fall 2015 (guess)'
    elif title in spring2012 and title in spring2014:
        next_sem = 'Spring 2016 (guess)'
    elif 'Tutorial' in e.text_content() or 'Independent Project' in e.text_content() or 'Internship' in e.text_content() or 'Preceptorship' in e.text_content() or 'Honors Independent' in e.text_content():
        if pattern4 in soup or pattern5 in soup or pattern56 in soup:
            next_sem = 'Spring 2015'
        else:
            next_sem = 'Fall 2014'    
    if title in fall2014:
        next_sem = 'Fall 2014'
    elif title in spring2015:
        next_sem = 'Spring 2015'    
    return next_sem, freq
                    
def populate():
    amst = add_major('American Studies')
    anth = add_major('Anthropology')
    #art = add_major ('Art and Art History')
    #asia = add_major('Asian Languages and Cultures')
    #biol = add_major('Biology')
    #chem = add_major('Chemistry')
    #chin = add_major('Chinese')
    #clas = add_major('Classics')
    #comp = add_major('Computer Science')
    #econ = add_major('Economics')
    #educ = add_major('Educational Studies')
    #engl = add_major('English')
    #envi = add_major('Environmental Studies')
    #fren = add_major('French and Francophone Studies')
    #geog = add_major('Geography')
    #geol = add_major('Geology')
    #germ = add_major('German Studies')
    #hisp = add_major('Hispanic and Latin American Studies')
    #hist = add_major('History')
    #intl = add_major('International Studies')
    #japa = add_major('Japanese')
    #lati = add_major('Latin American Studies')
    #ling = add_major('Linguistics')
    #math = add_major('Mathematics')
    #mcst = add_major('Media and Cultural Studies')
    #musi = add_major('Music')
    #neur = add_major('Neuroscience Studies')
    #phil = add_major('Philosophy')
    #phys = add_major('Physics and Astronomy')
    #poli = add_major('Political Science')
    #psyc = add_major('Psychology')
    #reli = add_major('Religious Studies')
    #russ = add_major('Russian')
    #soci = add_major('Sociology')
    thda = add_major('Theatre and Dance')
    wgss = add_major('Women\'s, Gender and Sexuality Studies')
    
    #major_list = [amst, anth, art, asia, biol, chem, chin, clas, comp, econ, educ, engl, envi, fren, geog, geol, germ, hisp, hist, intl, japa, lati, ling, math, mcst, musi, neur, phil, phys, poli, psyc, reli, russ, soci, thda, wgss]
        
    #major_list = [amst, anth, art, asia, biol, chem, chin, clas, comp, econ, educ, engl, envi, fren, geog, geol, germ, hisp, hist
    #major_list = [biol, chem, chin, clas, comp, econ, educ, engl, envi, fren, geog, geol, germ, hisp, hist, intl, japa, lati, ling, math, mcst, musi, neur, phil, phys, poli, psyc, reli, russ, soci, thda, wgss]
    
    major_list = [amst, anth, thda, wgss]
    
    #major_list = [amst]
    
    major_dict = all_major_dict() 
    
    for i in range(len(major_list)):
        major = major_list[i]        
        for class_ in major_dict.get(majors[i]):
            url = major_dict.get(majors[i]).get(class_)
            next_sem, frequency = nextSemester(url)
            add_class (major = major, 
                       class_name = class_, 
                       url = url, 
                       next_sem = next_sem,
                       frequency = frequency)
            
    for m in Major.objects.all():
        for c in Class.objects.filter(major = m):
            print ("- {0} - {1}".format(str(m), str(c)))

def add_class(major, class_name, url, next_sem, frequency):
    c = Class.objects.get_or_create(major = major, class_name = class_name, url = url, next_sem = next_sem, frequency = frequency)[0]
    return c

def add_major(major_name):
    m = Major.objects.get_or_create(major_name = major_name)[0]
    return m

if __name__ == '__main__':
    print ("Starting Class Selector population script...")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'class_selector_project.settings')
    from class_selector.models import Major, Class
    populate()