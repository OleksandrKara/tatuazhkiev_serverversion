# -*- coding: utf-8 -*-
# ����������� ������� �����
from django.contrib.sitemaps import Sitemap
# ����������� ������ � ������� 
#from fotos.models import Foto

'''class SitemapXML(Sitemap):
    # ������� ���������� �������� (��. http://www.sitemaps.org/) 
    changefreq = 'weekly'
    # ��������� ������������ �������� (��. http://www.sitemaps.org/)
    priority = 0.5

    def items(self):
        # �������� �� ��������� ������ �� ������ ��� ������� ����������
        # ��������� ���� sitemap
        return Foto.objects.filter(date__lte='2055-01-01').order_by('id')
		#date__lte='2055-01-01'

    def lastmod(self, obj):
        # ����� ���������� ���� ������� ����������� � ��������� lastmod
        # (��. http://www.sitemaps.org/)
        return obj.date

    def location(self, obj):
        # ����� ���������� URL ������� ����������� � ��������� loc
        # (��. http://www.sitemaps.org/)
        return "/media/%s" % obj.image_location'''
		
class FlatpageSitemap(Sitemap): 
    def items(self): 
        from django.contrib.sites.models import Site 
        return FlatPage.all().filter('sites = ', 
Site.objects.get_current().key()) 