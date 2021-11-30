# -*- coding: utf-8 -*-
{
    "name": "Automatic Partner Reference and Accounts",
    "version": "14.1.0.2",
    'license': 'LGPL-3',
    'author': 'pragma',
    'website': 'https://www.fletscher.de',
    "summary": """
    Automatically create the partner reference, the debitor and the creditor account from a sequence when a customer or vendor is being created.
    """,
    "description": """
Automatic Partner Reference and Accounts
========================================
Automatically create the partner reference, the debitor and the creditor account from a sequence when a customer or vendor is being created.

The partner referemce can be configured in the sequence "Partner Reference".
    """,
    "category": "Base",
    "depends": [
        "base",
        "sale",
        "purchase",
        "account",
    ],
    "data": [
        "data/sequencer.xml"
    ],
    "installable": True,
    "auto_install": False,
}
