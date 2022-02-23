# -*- coding: utf-8 -*-

from datetime import date
from odoo import models, fields, api


class EmployeeFormInherit(models.Model):
    _inherit = 'hr.employee'

    @api.model
    def create(self, vals):
        result = super(EmployeeFormInherit, self).create(vals)
        result.stages_history.sudo().create({'start_date': date.today(),
                                             'employee_id': result.id,
                                             'state': 'joined'})
        return result

    def start_grounding(self):
        self.state = 'grounding'
        self.stages_history.sudo().create({'start_date': date.today(),
                                           'employee_id': self.id,
                                           'state': 'grounding'})

    def set_as_employee(self):
        self.state = 'employment'
        stage_obj = self.stages_history.search([('employee_id', '=', self.id),
                                                ('state', '=', 'test_period')])
        if stage_obj:
            stage_obj.sudo().write({'end_date': date.today()})
        self.stages_history.sudo().create({'start_date': date.today(),
                                           'employee_id': self.id,
                                           'state': 'employment'})

    def start_notice_period(self):
        self.state = 'notice_period'
        stage_obj = self.stages_history.search([('employee_id', '=', self.id),
                                                ('state', '=', 'employment')])
        if stage_obj:
            stage_obj.sudo().write({'end_date': date.today()})
        self.stages_history.sudo().create({'start_date': date.today(),
                                           'employee_id': self.id,
                                           'state': 'notice_period'})

    def relived(self):
        self.state = 'relieved'
        self.active = False

    def start_test_period(self):
        self.state = 'test_period'

    def terminate(self):
        self.state = 'terminate'
        self.active = False

    state = fields.Selection([('joined', 'Slap On'),
                              ('grounding', 'Grounding'),
                              ('test_period', 'Test Period'),
                              ('employment', 'Employment'),
                              ('notice_period', 'Notice Period'),
                              ('relieved', 'Resigned'),
                              ('terminate', 'Terminated')])


class EmployeeStageHistory(models.Model):
    _name = 'hr.employee.status.history'
    _description = 'Status History'

    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    duration = fields.Integer(compute='get_duration', string='Duration(days)')

    def get_duration(self):
        self.duration = 0

    state = fields.Selection([('joined', 'Slap On'),
                              ('grounding', 'Grounding'),
                              ('test_period', 'Test Period'),
                              ('employment', 'Employment'),
                              ('notice_period', 'Notice Period'),
                              ('relieved', 'Resigned'),
                              ('terminate', 'Terminated')], string='Stage')
    employee_id = fields.Many2one('hr.employee', invisible=1)


class WizardEmployee(models.TransientModel):
    _name = 'wizard.employee.stage'

    def set_as_employee(self):
        return True

    related_user = fields.Many2one('res.users', string="Related User")
