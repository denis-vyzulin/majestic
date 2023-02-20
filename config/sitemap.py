from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse


class StaticViewSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return ['majestic:home',
                'majestic:about',
                'majestic:vnkroe',
                'majestic:shevnash',
                'majestic:vngotizd',
                'majestic:cerkvysh',
                'majestic:price',
                'majestic:contacts',
                'majestic:qna',
                'majestic:privacy-policy',
                ]

    def location(self, item):
        return reverse(item)