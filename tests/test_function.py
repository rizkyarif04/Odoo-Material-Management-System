from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

class TestRegMaterial(TransactionCase):
    
    def setUp(self):
        super(TestRegMaterial, self).setUp()
        self.Material = self.env['material.register']
        self.record = self.Material.create({
            'code': 'M001',
            'name': 'Test Material',
            'type': 'fabric',
            'buy_price': 50.0,
            'supplier': 'PT. ASA',
        })

    def test_create(self):
        record = self.Model.create({
            'code': 'M001',
            'name': 'Test Material',
            'type': 'fabric',
            'buy_price': 50,
            'supplier': 'PT. ASA',
        })
        self.assertEqual(record.code, 'M001')
        self.assertEqual(record.name, 'Test Material')
        self.assertEqual(record.type, 'fabric')
        self.assertEqual(record.supplier, 'PT. ASA')
        with self.assertRaises(ValidationError):
            record._check_buy_price()
        
        # Update the buy_price to a valid value
        record.buy_price = 150.0
        self.assertEqual(record.buy_price, 150)

    def test_read(self):
        record = self.record
        self.assertEqual(record.code, 'M001')
        self.assertEqual(record.name, 'Test Material')
        self.assertEqual(record.type, 'fabric')
        self.assertEqual(record.buy_price, 150)
        self.assertEqual(record.supplier, 'PT. ASA')

    def test_update(self):
        record = self.record
        record.write({
            'code': 'M101',
            'name': 'Aluminum',
            'type': 'Cotton',
            'buy_price': 20000,
            'supplier': 'PT.NASA',
        })
        self.assertEqual(record.code, 'M101')
        self.assertEqual(record.name, 'Aluminum')
        self.assertEqual(record.type, 'Cotton')
        self.assertEqual(record.buy_price, 20000)
        self.assertEqual(record.supplier, 'PT.NASA')

    def test_delete(self):
        record = self.record
        record.unlink()
        self.assertFalse(record.exists())