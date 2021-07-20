from api.models import *
from datetime import date, datetime
import calendar

def header():
    try:
        header_object = Header.objects.filter(action = 'Active')[0]
        header_logo = header_object.logo
        header_title = header_object.header_title
        header_description = header_object.header_description
        google_play_store_link = header_object.google_play_store_link
    except Exception as e:
        header_logo, header_title, header_description, google_play_store_link = '', '', '', ''
    return header_logo, header_title, header_description, google_play_store_link

def navmenu():
    navmenu_objects = NavigationMenu.objects.filter(action = 'Active')
    navmenu_list, count = [], 0
    for nav in navmenu_objects:
        navmenu_list.append([])
        navmenu_list[count].append(nav.nav_item)
        navmenu_list[count].append(nav.nav_link)
        count = count + 1
    return navmenu_list

def footer():
    try:
        footer_object = Footer.objects.filter(action = 'Active')[0]
        footer_logo = footer_object.logo
        footer_description = footer_object.footer_description
        google_play_store_link = footer_object.google_play_store_link
        facebook_page_link = footer_object.facebook_page_link
        twitter_page_link = footer_object.twitter_page_link
        pinterest_page_link = footer_object.pinterest_page_link
        linkedin_page_link = footer_object.linkedin_page_link
    except Exception as e:
        footer_logo, footer_description, google_play_store_link, facebook_page_link, twitter_page_link, pinterest_page_link, linkedin_page_link = '', '', '', '', '', '', ''
    return footer_logo, footer_description, google_play_store_link, facebook_page_link, twitter_page_link, pinterest_page_link, linkedin_page_link

def services_list():
    service_objects = Services.objects.filter(action = 'Active')
    services_dict = {}
    for service in service_objects:
        if service.category not in services_dict:
            services_dict[service.category] = []
            name = service.name.title()
            id = service.id
            services_dict[service.category].append([name, id])
        else:
            name = service.name
            id = service.id
            services_dict[service.category].append([name, id])
    return services_dict

def service_details(category, id):
    try:
        service_object = Services.objects.get(category=category, id = id)
        service_category = service_object.category
        service_name = service_object.name.title()
        service_image = service_object.image
        service_content = service_object.content
    except Exception as e:
        service_category, service_name, service_image, service_content = '', '', '', ''
    return service_category, service_name, service_image, service_content

def testimonials():
    testimonial_objects = Testimonials.objects.filter(action = 'Active')
    testimonials_list, count = [], 0
    for testimonial in testimonial_objects:
        testimonials_list.append([])
        testimonials_list[count].append(testimonial.photo)
        testimonials_list[count].append(testimonial.name)
        testimonials_list[count].append(testimonial.profession)
        testimonials_list[count].append(testimonial.comment)
        count = count + 1
    return testimonials_list

def partners():
    partner_objects = Partners.objects.filter(action = 'Active')
    partners_list = []
    for partner in partner_objects:
        partners_list.append(partner.logo)
    return partners_list

def about_us():
    try:
        aboutus_object = AboutUs.objects.filter(action = 'Active')[0]
        about_heading = aboutus_object.heading
        about_content = aboutus_object.content
        vision = aboutus_object.vision
        mission = aboutus_object.mission
    except Exception as e:
        about_heading, about_content, vision, mission = '', '', '', ''
    return about_heading, about_content, vision, mission

def contact_us():
    try:
        contactus_object = ContactUs.objects.filter(action = 'Active')[0]
        contact_email = contactus_object.email
        contact_phone_no = contactus_object.phone_no
        contact_address = contactus_object.address
    except Exception as e:
        contact_email, contact_phone_no, contact_address = '', '', ''
    return contact_email, contact_phone_no, contact_address

def manage_seo_content(pagename):
    try:
        seo_object = ManageSEOContent.objects.get(action = 'Active', page_name=pagename)
        seo_title = seo_object.title
        seo_description = seo_object.meta_description
    except Exception as e:
        seo_title, seo_description = '', ''
    return seo_title, seo_description

def manage_news_media():
    news_media_objects = ManageNewsMedia.objects.filter(action = 'Active').order_by('published_date')
    news_media_list, count, dual_count = [], -1, 0
    for news_media in news_media_objects:
        if dual_count % 2 == 0:
            news_media_list.append([])
            count = count + 1
        news_media_list[count].append(news_media.id)
        news_media_list[count].append('ADFPAY Neo Bank')
        news_media_list[count].append(news_media.topic)
        news_media_list[count].append(news_media.media_file)
        if len(news_media.content) > 160:
            news_media_list[count].append(news_media.content[0:160] + '...')
        else:
            news_media_list[count].append(news_media.content)
        news_media_list[count].append(news_media.published_date)
        dual_count = dual_count + 1
    return news_media_list

def news_media_detail(objectId):
    try:
        news_media_object = ManageNewsMedia.objects.get(id = objectId)
        news_media_topic = news_media_object.topic
        news_media_media_file = news_media_object.media_file
        news_media_contents = news_media_object.content
        news_media_published_date = news_media_object.published_date
    except Exception as e:
        news_media_topic, news_media_media_file, news_media_contents, news_media_published_date = '', '', '', ''
    return news_media_topic, news_media_media_file, news_media_contents, news_media_published_date

def blog_objects():
    blog_objects = PublishBlogs.objects.filter(action = 'Active').order_by('published_date')
    blog_list, count, dual_count = [], -1, 0
    for blog in blog_objects:
        if dual_count % 2 == 0:
            blog_list.append([])
            count = count + 1
        blog_list[count].append(blog.id)
        blog_list[count].append(blog.publisher_name)
        blog_list[count].append(blog.topic)
        blog_list[count].append(blog.image)
        if len(blog.content) > 160:
            blog_list[count].append(blog.content[0:160] + '...')
        else:
            blog_list[count].append(blog.content)
        blog_list[count].append(blog.published_date)
        dual_count = dual_count + 1
    return blog_list


#newsandmedia

def news_objects():

    news_objects = ManageNewsMedia.objects.filter(action = 'Active').order_by('published_date')
    news_list, count, dual_count = [], -1, 0
    for news in news_objects:
        if dual_count % 2 == 0:
            news_list.append([])
            count = count + 1
        news_list[count].append(news.id)
        news_list[count].append(news.topic)
        news_list[count].append(news.media_file)
        news_list[count].append(news.publisher_name)
        news_list[count].append(news.published_date)
        if len(news.content) > 160:
            news_list[count].append(news.content[0:160] + '...')
        else:
            news_list[count].append(news.content)
        dual_count = dual_count + 1
    return news_list
def news_details( objectId):
    try:
        news_object = ManageNewsMedia.objects.get(id = objectId)
        news_publisher_name = news_object.publisher_name
        news_topic = news_object.topic
        news_image = news_object.media_file
        news_contents = news_object.content
        news_published_date = news_object.published_date
    except Exception as e:
        news_publisher_name, news_topic, news_image, news_contents, news_published_date = '', '', '', '', ''
    return news_publisher_name, news_topic, news_image, news_contents, news_published_date

def blog_details(objectId):
    try:
        blog_object = PublishBlogs.objects.get(id = objectId)
        blog_publisher_name = blog_object.publisher_name
        blog_topic = blog_object.topic
        blog_image = blog_object.image
        blog_contents = blog_object.content
        blog_published_date = blog_object.published_date
    except Exception as e:
        blog_publisher_name, blog_topic, blog_image, blog_contents, blog_published_date = '', '', '', '', ''
    return blog_publisher_name, blog_topic, blog_image, blog_contents, blog_published_date
    


def footer_content(objectType):
    modelClass = globals()[objectType]
    try:
        model_object = modelClass.objects.filter(action = 'Active')[0]
        page_content = model_object.content
    except Exception as e:
        page_content = ''
    return page_content

def manage_team_members():
    team_objects = ManagementTeam.objects.filter(action = 'Active')
    team_list, count = [], 0
    for team in team_objects:
        team_list.append([])
        team_list[count].append(team.name)
        team_list[count].append(team.designation)
        team_list[count].append(team.image)
        team_list[count].append(team.content)
        count = count + 1
    return team_list

def advisory_board_members():
    team_objects = AdvisoryBoard.objects.filter(action = 'Active')
    team_list, count = [], 0
    for team in team_objects:
        team_list.append([])
        team_list[count].append(team.name)
        team_list[count].append(team.designation)
        team_list[count].append(team.image)
        team_list[count].append(team.content)
        count = count + 1
    return team_list

def get_list_of_blogs(month, year):
    blog_objects = PublishBlogs.objects.filter(published_date__year=year, published_date__month=month)
    blog_list, count = [], 0
    for blog in blog_objects:
        blog_list.append([])
        blog_list[count].append(blog.id)
        blog_list[count].append(blog.topic)
        count = count + 1
    return blog_list

def blog_archive_date_dict():
    now_year = date.today().year
    now_month = date.today().month
    now_month_name = calendar.month_name[now_month]
    start_year = 2020
    start_month = 11
    blog_dict = {}
    for year in range(start_year, now_year + 1):
        blog_dict[year] = {}
        for month in range(1, 13):
            if year == start_year and month >= start_month and month <= now_month:
                blog_dict[year][calendar.month_name[month]] = get_list_of_blogs(month, year)
            elif year != start_year and year == now_year and month <= now_month:
                blog_dict[year][calendar.month_name[month]] = get_list_of_blogs(month, year)
            elif year != start_year and year != now_year:
                blog_dict[year][calendar.month_name[month]] = get_list_of_blogs(month, year)
    return blog_dict

def blog_archive():
    blog_dict = blog_archive_date_dict()
    return blog_dict
