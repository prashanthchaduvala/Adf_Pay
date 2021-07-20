from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
class StaticViewSitemap(Sitemap):
    def items(self):
        return ['frontend:about', 'frontend:index', 'frontend:blog', 'frontend:news_event', 'frontend:services', 'frontend:contact', 'frontend:career', 'frontend:manage_team', 'frontend:apply-job', 'frontend:advisory_board']
    def location(self, item):
        return reverse(item)
