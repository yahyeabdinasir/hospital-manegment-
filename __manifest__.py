
{
    'name': 'hospital manegment ',
    'version': '1.0.0',
    'summary': 'hospital manegment system',
    'sequence': -100,
    'category': 'Tools',
    'description': 'hospiatal system for learning',
    'author': "yahye farah ",
    'depends': ['mail', 'product' ],
    'data': [
        "security/ir.model.access.csv",
        'data/patient_tag_data.xml',
        'data/patient_Sequance.xml',
        'data/mail_template.xml',
        'data/hospital.patient_tag.csv',
        'wizard/cancell_appointment.xml',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/female_patient.xml',
        'views/appointment_views.xml',
        'views/patient_tag_viws.xml',
        'views/odoo_plyaground.xml',
        'views/res_config_settings_views.xml',
        'views/operation_view.xml',
        'report/report_patient_details.xml',
        'report/report.xml',
        'report/apppointment_details.xml',
        'report/appointment_rep.xml',




    ],
    'installable': True,
    'application': True,
    'demo': [],
    'license': 'LGPL-3'
}
