from __future__ import unicode_literals

from frappe import _


def get_data():
	return {
		'heatmap': False,
		'fieldname': 'prestamo',
		'transactions': [
			{
				'label': _('Prestamos'),
				'items': ['Journal Entry']
			}
		]
	}