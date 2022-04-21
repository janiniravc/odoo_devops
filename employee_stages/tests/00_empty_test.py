from odoo.tests import Form
from odoo.addons.hr.tests.common import TestHrCommon

def test_empty():
    """
    PyTest tests are callables whose names start with "test"
    (by default)

    It looks for them in modules whose name starts with "test_" or ends with "_test"
    (by default)
    
    """
	_tz = 'Pacific/Apia'
	self.res_users_hr_officer.company_id.resource_calendar_id.tz = _tz
	Employee = self.env['hr.employee'].with_user(self.res_users_hr_officer)
	employee_form = Form(Employee)
	employee_form.name = 'Raoul Grosbedon'
	employee_form.work_email = 'raoul@example.com'
	employee = employee_form.save()
	self.assertEqual(employee.tz, _tz)
    pass


def empty_test():
    """
    My name doesn't start with "test", so I won't get run.
    (by default ;-)
    """
    pass
