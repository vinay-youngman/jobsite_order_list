from __future__ import print_function

import psycopg2
import traceback
import json
from odoo import fields, models, api
import requests
from datetime import date
import logging
from urllib.request import urlopen
import time
import base64
from .jobsite_order_list import jobsite_order_list

_logger = logging.getLogger(__name__)


class JobsiteMarkerColorSync(models.TransientModel):
    _name = 'jobsite.marker.color.sync'

    def jobsite_marker_color_sync(self):
        jobsites = self.env['jobsite'].search([])

        _logger.info('Jobsite Marker Color Cron Started')
        for jobsite in jobsites:
            active_orders=jobsite['active_orders']
            closed_orders=jobsite['closed_orders']
            color = self.env['jobsite_order_list'].calculate_marker_color(jobsite)


            jobsite.write({'marker_color': color})
            self.env.cr.commit()
        _logger.info('Jobsite Marker Color Cron Ended')