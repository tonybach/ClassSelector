from bs4 import BeautifulSoup, SoupStrainer
from urllib.request import urlopen
import re
import collections

#majors = ['AMST', 'ANTH', 'ART', 'ASIA', 'BIOL', 'CHEM', 'CHIN', 'CLAS', 'COMP', 'ECON', 'EDUC', 'ENGL', 'ENVI', 'FREN', 'GEOG', 'GEOL', 'GERM', 'HISP', 'HIST', 'INTL', 'JAPA', 'LATI', 'LING', 'MATH', 'MCST', 'MUSI', 'NEUR', 'PHIL', 'PHYS', 'POLI', 'PSYC', 'RELI', 'RUSS', 'SOCI', 'THDA', 'WGSS']

#majors = ['BIOL', 'CHEM', 'CHIN', 'CLAS', 'COMP', 'ECON', 'EDUC', 'ENGL', 'ENVI', 'FREN', 'GEOG', 'GEOL', 'GERM', 'HISP', 'HIST', 'INTL', 'JAPA', 'LATI', 'LING', 'MATH', 'MCST', 'MUSI', 'NEUR', 'PHIL', 'PHYS', 'POLI', 'PSYC', 'RELI', 'RUSS', 'SOCI', 'THDA', 'WGSS']
majors = ['AMST', 'ANTH', 'THDA', 'WGSS']

#majors = ['AMST']

def get_links():
    html = urlopen('http://www.macalester.edu/registrar/schedules/2014fall/class-schedule/').read()
    soup = BeautifulSoup(html)
    soup.find(class_="more", href = "").decompose()
    soup.find(class_="more", href = "http://www.macalester.edu/academic/catalog/program/ped_m.html").decompose()
    more = soup.find_all(class_="more")
    links = []
    for link in more:
        links.append(link['href'])
    return links        

#link_list = ['http://www.macalester.edu/americanstudies/', 'http://www.macalester.edu/anthropology/', 'http://www.macalester.edu/art/', 'http://www.macalester.edu/academics/asian/', 'http://www.macalester.edu/academics/biology/', 'http://www.macalester.edu/academics/chemistry/', 'http://www.macalester.edu/academics/asian/', 'http://www.macalester.edu/academics/classics/', 'http://www.macalester.edu/academics/mscs/', 'http://www.macalester.edu/academics/economics/', 'http://www.macalester.edu/academics/education/', 'http://www.macalester.edu/academics/english/', 'http://www.macalester.edu/academics/environmentalstudies/', 'http://www.macalester.edu/academics/french/', 'http://www.macalester.edu/academics/geography/', 'http://www.macalester.edu/academics/geology/', 'http://www.macalester.edu/academics/german/', 'http://www.macalester.edu/academics/hispanicstudies/', 'http://www.macalester.edu/academics/history/']

def all_major_dict():
    #link_list = ['http://www.macalester.edu/americanstudies/']
    link_list = ['http://www.macalester.edu/americanstudies/', 'http://www.macalester.edu/anthropology/', 'http://www.macalester.edu/academics/theatreanddance/', 'http://www.macalester.edu/academics/wgss/']
    #link_list = ['http://www.macalester.edu/academics/biology/', 'http://www.macalester.edu/academics/chemistry/', 'http://www.macalester.edu/academics/asian/', 'http://www.macalester.edu/academics/classics/', 'http://www.macalester.edu/academics/mscs/','http://www.macalester.edu/academics/economics/', 'http://www.macalester.edu/academics/education/', 'http://www.macalester.edu/academics/english/', 'http://www.macalester.edu/academics/environmentalstudies/', 'http://www.macalester.edu/academics/french/', 'http://www.macalester.edu/academics/geography/', 'http://www.macalester.edu/academics/geology/', 'http://www.macalester.edu/academics/german/', 'http://www.macalester.edu/academics/hispanicstudies/', 'http://www.macalester.edu/academics/history/', 'http://www.macalester.edu/academics/internationalstudies/', 'http://www.macalester.edu/academics/asian/', 'http://www.macalester.edu/academics/las/', 'http://www.macalester.edu/academics/linguistics/', 'http://www.macalester.edu/academics/mscs/', 'http://www.macalester.edu/academics/mcs/', 'http://www.macalester.edu/academics/music/', 'http://www.macalester.edu/academics/neuroscience/', 'http://www.macalester.edu/academics/philosophy/', 'http://www.macalester.edu/academics/physics/', 'http://www.macalester.edu/academics/politicalscience/', 'http://www.macalester.edu/academics/psychology/', 'http://www.macalester.edu/academics/religiousstudies/', 'http://www.macalester.edu/academics/russian/', 'http://www.macalester.edu/academics/sociology/', 'http://www.macalester.edu/academics/theatreanddance/', 'http://www.macalester.edu/academics/wgss/']
    #link_list = get_links()
    name_link_dict = {}
    only_h3 = SoupStrainer('h3')
    only_a = SoupStrainer('a')
    for i in range(len(link_list)):
        soup = BeautifulSoup(urlopen(link_list[i] + "courses/").read(), parse_only = only_h3)        
        all_h3 = soup.find_all(text = re.compile(majors[i]))
        inside_dict = {}
        url = "".join(['http://catalog.macalester.edu/content.php?filter%5B27%5D=', majors[i], '&filter%5B29%5D=&filter%5Bcourse_type%5D=-1&filter%5Bkeyword%5D=&filter%5B32%5D=1&filter%5Bcpage%5D=1&cur_cat_oid=12&expand=&navoid=1086&search_database=Filter#acalog_template_course_filter'])
        soup2 = BeautifulSoup(urlopen(url).read(), parse_only = only_a)
        for h3 in all_h3:
            if '(' in h3 or ')' in h3: 
                h3 = h3.replace('(', '\(')
                h3 = h3.replace(')', '\)')
            pattern = re.compile(h3)
            if '"' in h3:
                pattern = re.compile (h3[40:])
            short_link = soup2.find('a', text = pattern)
            class_link = "".join(["http://catalog.macalester.edu/", short_link['href']])
            inside_dict.update ({h3:class_link})
        inside_dict = collections.OrderedDict(sorted(inside_dict.items(), key=lambda t: t[0]))
        name_link_dict.update ({majors[i]: inside_dict})
    return (name_link_dict)
