from odoo import http
from odoo.http import request
from  datetime import date
import logging

class CoursesPage(http.Controller):
    @http.route(['/courses'], type='http', auth="public", website=True)
    def courses_page(self,**kw):
        return request.render("salim_website_odoo.offered_courses", {})
