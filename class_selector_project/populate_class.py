import os
from bs4 import BeautifulSoup, SoupStrainer
from urllib.request import urlopen
import re

from test import all_major_dict, get_links, majors

only_title = SoupStrainer('title')
only_td = SoupStrainer('td')

pattern1 = re.compile ('very semester')
#pattern15 = re.compile ('every semester')
pattern2 = re.compile ('very fall')
#pattern25 = re.compile ('every fall')
pattern26 = re.compile ('Every Fall')
pattern3 = re.compile ('all semester')
#pattern35 = re.compile ('fall semester')
pattern36 = re.compile ('Fall Semester')
pattern16 = re.compile ('only in the fall')
pattern4 = re.compile ('very spring')
#pattern45 = re.compile ('every spring')
pattern5 = re.compile ('pring semester')
#pattern55 = re.compile ('spring semester')
pattern56 = re.compile ('Spring Semester')
#pattern57 = re.compile ('Every year; Spring semester')
pattern6 = re.compile ('very year')
#pattern65 = re.compile ('every year')
pattern66= re.compile ('annually')
pattern67= re.compile ('yearly')
pattern68 = re.compile ('nce each year')
pattern69 = re.compile ('nce per year')
#pattern691 = re.compile ('once per year')
pattern7 = re.compile ('lternate years')
#pattern75 = re.compile ('alternate years')
pattern76 = re.compile ('every two years')
pattern77 = re.compile ('very other year')
#pattern78 = re.compile ('Every other year')
pattern8 = re.compile ('lternate fall semesters')
#pattern85 = re.compile ('alternate fall semesters')
pattern86 = re.compile ('Every other fall')
pattern87 = re.compile ('Alternate years, fall semester')
pattern88 = re.compile ('in the fall every two years')
pattern89 = re.compile ('Fall semester every other year')
pattern9 = re.compile ('lternate spring semesters')
#pattern95 = re.compile ('alternate spring semesters')
pattern96 = re.compile ('very other spring')
#pattern97 = re.compile ('every other spring')
pattern98 = re.compile ('Alternate years, spring semester')
pattern99 = re.compile ('Spring semester, every other year')
pattern10 = re.compile ('Even numbered fall semesters')
pattern105 = re.compile ('even-numbered fall semesters')
pattern106 = re.compile ('fall term of even-numbered years')
pattern11 = re.compile ('Even numbered spring semesters')
pattern115 = re.compile ('even-numbered spring semesters')
pattern116 = re.compile ('spring term of even-numbered years')
pattern12 = re.compile ('Odd numbered fall semesters')
pattern125 = re.compile ('odd-numbered fall semesters')
pattern126 = re.compile ('fall term of odd-numbered years')
pattern13 = re.compile ('Odd numbered spring semesters')
pattern135 = re.compile ('odd-numbered spring semesters')
pattern14 = re.compile ('very third year')
#pattern145 = re.compile ('every third year')
pattern146 = re.compile ('every three years')
pattern15 = re.compile('Two years in every three')
pattern17 = re.compile ('Offered next in 2015')

#pattern_list = [pattern1, pattern2, pattern3, pattern36, pattern4, pattern5, pattern56, pattern6, pattern66, pattern67, pattern68, pattern69, pattern7, pattern76, pattern77, pattern8, pattern86, pattern87, pattern88, pattern89, pattern9, pattern96, pattern98, pattern99, pattern10, pattern105, pattern106, pattern11, pattern115, pattern116, pattern12, pattern125, pattern126, pattern13, pattern135, pattern14, pattern146, pattern15, pattern16, pattern17]

#freq_list = [('Every semester'),('every semester'),('Every fall'),('every fall'),('Fall semester'),('fall semester'),('Every spring'), ('every spring'),('Spring semester'),('spring semester'),('Every year; Spring semester'),('Every year'),('every year'),('Alternate years'),('alternate years'),('every two years'),('Alternate fall semesters'), ('alternate fall semesters'),('Alternate spring semesters'),('alternate spring semesters'),('Even numbered fall semesters'),('even-numbered fall semesters'),('Even numbered spring semesters'), ('even-numbered spring semesters'), ('Odd numbered fall semesters'), ('odd-numbered fall semesters'),('Odd numbered spring semesters'),('odd-numbered spring semesters'), ('Every third year'), ('every third year')]

spring2015 = BeautifulSoup(urlopen('http://www.macalester.edu/registrar/schedules/2015spring/class-schedule/').read(), parse_only = only_td)
fall2014 = BeautifulSoup(urlopen('http://www.macalester.edu/registrar/schedules/2014fall/class-schedule/').read(), parse_only = only_td)
spring2014 = BeautifulSoup(urlopen('http://www.macalester.edu/registrar/schedules/2014spring/class-schedule/').read(), parse_only = only_td)
fall2013 = BeautifulSoup(urlopen('http://www.macalester.edu/registrar/schedules/2013fall/class-schedule/').read(), parse_only = only_td)
spring2013 = BeautifulSoup(urlopen('http://www.macalester.edu/registrar/schedules/2013spring/class-schedule/').read(), parse_only = only_td)
fall2012 = BeautifulSoup(urlopen('http://www.macalester.edu/registrar/schedules/2012fall/class-schedule/').read(), parse_only = only_td)
spring2012 = BeautifulSoup(urlopen('http://www.macalester.edu/registrar/schedules/2012spring/class-schedule/').read(), parse_only = only_td)
fall2011 = BeautifulSoup(urlopen('http://www.macalester.edu/registrar/schedules/2011fall/class-schedule/').read(), parse_only = only_td)


#def get_frequency():
    #link_list = get_links()
    #for i in range(len(link_list)):
        #soup = BeautifulSoup(urlopen(link_list[i] + "/courses/").read())
        #frequency = soup.find_all('p', text = re.compile('Frequency'))
        #for freq in frequency:
            #freq_text = freq.get_text().lstrip('Frequency:').rstrip('.')
            #if 'Offered' in freq_text:
                #freq_text = freq_text.lstrip('Offered')
            #freq_text = freq_text.lstrip("  ")
            #if freq_text not in freq_list:
                #print(freq_text)

#get_frequency()

#def get_frequency(url):
    #frequency = "No info"
    #soup = BeautifulSoup(urlopen(url).read())
    #for pattern in pattern_list:
        #if soup.find(text = pattern):
            #frequency = pattern.pattern
    #return frequency

#only_p = SoupStrainer('p')


def nextSemester(url):
    next_sem = "No info"
    freq = "No info"
    
    #titleSoup = BeautifulSoup(urlopen(url).read(), parse_only = only_title)
    #title = re.compile ("".join([titleSoup.get_text()[0:4], "\xa0", titleSoup.get_text()[5:8]]))
    #soup = BeautifulSoup(urlopen(url).read(), parse_only = only_td)
    
    soup = BeautifulSoup(urlopen(url).read())
    title = re.compile("".join([soup.title.get_text()[0:4], "\xa0", soup.title.get_text()[5:8]]))
    
    if soup.find(text = pattern1):
        next_sem = 'Fall 2014'
        freq = 'Every semester'
    elif soup.find(text = pattern2) or soup.find(text = pattern26) or soup.find(text = pattern3) or soup.find(text = pattern36) or soup.find(text = pattern16):
        if fall2013.find(text = title) or fall2012.find(text = title):
            next_sem = 'Fall 2015 (guess)'
        freq = 'Every fall'
    elif soup.find(text = pattern4) or soup.find(text = pattern5) or soup.find(text = pattern56):
        next_sem = 'Spring 2016 (guess)'
        freq = 'Every spring'
    elif soup.find(text = pattern6) or soup.find(text = pattern66) or soup.find(text = pattern67) or soup.find(text = pattern68) or soup.find(text = pattern69):
        if fall2013.find(text = title) or fall2012.find(text = title):
            next_sem = 'Fall 2015 (guess)'
        elif spring2014.find(text = title) or spring2013.find(text = title):
            next_sem = 'Spring 2015 (guess)'
        freq = 'Every year'  
    elif soup.find(text = pattern7) or soup.find(text = pattern76) or soup.find(text = pattern77):      
        if spring2014.find(text = title):
            next_sem = 'Spring 2016'
        elif fall2013.find(text = title):
            next_sem = 'Fall 2015'   
        freq = 'Alternate years'
    elif soup.find (text = pattern8) or soup.find(text = pattern86) or soup.find(text = pattern87) or soup.find(text = pattern88) or soup.find(text = pattern89):
        if fall2013.find(text = title):
            next_sem = 'Fall 2015'
        freq = 'Alternate fall semesters'
    elif soup.find(text = pattern9) or soup.find(text = pattern96) or soup.find(text = pattern98) or soup.find(text = pattern99):
        if spring2014.find(text = title):
            next_sem = 'Spring 2016'
        freq = 'Alternate spring semesters'
    elif soup.find(text = pattern10) or soup.find(text = pattern105) or soup.find(text = pattern106):
        if fall2012.find(text = title):
            next_sem = 'Fall 2016 (guess)'
        freq = 'Even numbered fall semesters'
    elif soup.find(text = pattern11) or soup.find(text = pattern115) or soup.find(text = pattern116):
        next_sem = 'Spring 2016'
        freq = 'Even numbered spring semesters'
    elif soup.find(text = pattern12) or soup.find(text = pattern125) or soup.find(text = pattern126):
        next_sem = 'Fall 2015'
        freq = 'Odd numbered fall semesters'
    elif soup.find(text = pattern13) or soup.find(text = pattern135):
        if spring2013.find(text = title):
            next_sem = 'Spring 2017 (guess)'
        freq = 'Odd numbered spring semesters'
    elif soup.find(text = pattern14) or soup.find(text = pattern146):
        if fall2012.find(text = title):
            next_sem = 'Fall 2015'    
        elif spring2013.find(text = title):
            next_sem = 'Spring 2016'
        elif fall2013.find(text = title):
            next_sem = 'Fall 2016'
        elif spring2014.find(text = title):
            next_sem = 'Spring 2017'
        freq = 'Every three years'
    #elif soup.find(text = pattern15):
    #elif soup.find(text = pattern16):
        #next_sem = 'Fall 2015'
        #freq = 'Only in the fall'
    elif soup.find(text = pattern17):
        next_sem = 'Fall 2015'
        freq = 'Offered next in 2015'
    elif fall2011.find(text = title) and fall2013.find(text = title):
        next_sem = 'Fall 2015 (guess)'
    elif spring2012.find(text = title) and spring2014.find(text = title):
        next_sem = 'Spring 2016 (guess)'
    elif soup.find('title', text = re.compile('Tutorial')) or soup.find('title', text = re.compile('Independent Project')) or soup.find('title', text = re.compile('Internship')) or soup.find('title', text = re.compile('Preceptorship')) or soup.find('title', text = re.compile('Honors Independent')):
        if soup.find(text = pattern4) or soup.find(text = pattern5) or soup.find(text = pattern56):
            next_sem = 'Spring 2015'
        else:
            next_sem = 'Fall 2014'    
    if fall2014.find(text = title):
        next_sem = 'Fall 2014'
    elif spring2015.find(text = title):
        next_sem = 'Spring 2015'    
    return [next_sem, freq]
                    
def populate():
    amst = add_major('American Studies')
    anth = add_major('Anthropology')
    art = add_major ('Art and Art History')
    asia = add_major('Asian Languages and Cultures')
    biol = add_major('Biology')
    chem = add_major('Chemistry')
    chin = add_major('Chinese')
    clas = add_major('Classics')
    comp = add_major('Computer Science')
    econ = add_major('Economics')
    educ = add_major('Educational Studies')
    engl = add_major('English')
    envi = add_major('Environmental Studies')
    fren = add_major('French and Francophone Studies')
    geog = add_major('Geography')
    geol = add_major('Geology')
    germ = add_major('German Studies')
    hisp = add_major('Hispanic and Latin American Studies')
    hist = add_major('History')
    intl = add_major('International Studies')
    japa = add_major('Japanese')
    lati = add_major('Latin American Studies')
    ling = add_major('Linguistics')
    math = add_major('Mathematics')
    mcst = add_major('Media and Cultural Studies')
    musi = add_major('Music')
    neur = add_major('Neuroscience Studies')
    phil = add_major('Philosophy')
    phys = add_major('Physics and Astronomy')
    poli = add_major('Political Science')
    psyc = add_major('Psychology')
    reli = add_major('Religious Studies')
    russ = add_major('Russian')
    soci = add_major('Sociology')
    thda = add_major('Theatre and Dance')
    wgss = add_major('Women\'s, Gender and Sexuality Studies')
    
    major_list = [amst, anth, art, asia, biol, chem, chin, clas, comp, econ, educ, engl, envi, fren, geog, geol, germ, hisp, hist, intl, japa, lati, ling, math, mcst, musi, neur, phil, phys, poli, psyc, reli, russ, soci, thda, wgss]
        
    #major_list = [amst, anth, art, asia, biol, chem, chin, clas, comp, econ, educ, engl, envi, fren, geog, geol, germ, hisp, hist
    #major_list = [biol, chem, chin, clas, comp, econ, educ, engl, envi, fren, geog, geol, germ, hisp, hist, intl, japa, lati, ling, math, mcst, musi, neur, phil, phys, poli, psyc, reli, russ, soci, thda, wgss]
    
    # major_list = [amst, anth, thda, wgss]
    
    # major_list = [amst]
    
    major_dict = all_major_dict() 
    
    for i in range(len(major_list)):
        major = major_list[i]        
        for class_ in major_dict.get(majors[i]):
            url = major_dict.get(majors[i]).get(class_)
            next_sem_and_freq = nextSemester(url)
            next_sem = next_sem_and_freq[0]
            frequency = next_sem_and_freq[1]
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