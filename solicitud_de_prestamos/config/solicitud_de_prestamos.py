from __future__ import unicode_literals
from frappe import _

def get_data():
    return [
      {
        "label":_("Solicitud de Prestamos"),
        "icon": "octicon octicon-calendar",
        "items": [
            {
              "type": "doctype",
              "name": "Solicitud de Capital",
              "label": _("Solicitud de Capital"),
              "description": _("Crear un nuevo prestamo"),
            }
          ]
      }
  ]