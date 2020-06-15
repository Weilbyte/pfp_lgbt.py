import unittest
import pfp_lgbt 

class IconTestCase(unittest.TestCase):
    def setUp(self):
        self.client = pfp_lgbt.Client()
        self.flag = pfp_lgbt.Flag('pride')

class Icon(IconTestCase):
    def test_icon_pride(self):
        url = self.client.icon(self.flag)
        assert url == 'https://api.pfp.lgbt/v3/icon/pride', 'Pride icon link does not match'
    def test_icon_bytes(self):
        byte = self.client.iconBytes(self.flag)
        assert byte == b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x01\xf4\x00\x00\x01,\x08\x02\x00\x00\x00\xba\xd9\xd6\x9f\x00\x00\x04^IDATx\x9c\xec\xd6\xc1\t\x02A\x14\x04\xd1\x1d\xd9<L\xc6\x98\xccA\xf0d\x92\x1e\raMb\xe0C\xf1^\x04}*\xfa\xfc\x1e\x00\xd4\xdc\xa6\x07\x00\xb0\x9f\xb8\x03\x04\x89;@\x90\xb8\x03\x04\x89;@\x90\xb8\x03\x04\x89;@\x90\xb8\x03\x04\x89;@\x90\xb8\x03\x04\x89;@\x90\xb8\x03\x04\x89;@\x90\xb8\x03\x04\x89;@\x90\xb8\x03\x04\x89;@\x90\xb8\x03\x04\x89;@\x90\xb8\x03\x04\x89;@\x90\xb8\x03\x04\x89;@\x90\xb8\x03\x04\x89;@\x90\xb8\x03\x04\x89;@\x90\xb8\x03\x04\x89;@\x90\xb8\x03\x04\x89;@\x90\xb8\x03\x04\x89;@\x90\xb8\x03\x04\x89;@\x90\xb8\x03\x04\x89;@\x90\xb8\x03\x04\x89;@\x90\xb8\x03\x04\x89;@\x90\xb8\x03\x04\x89;@\x90\xb8\x03\x04\x89;@\x90\xb8\x03\x04\x89;@\x90\xb8\x03\x04\x89;@\x90\xb8\x03\x04\xad\xeb==\x01\x80\xdd<w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08Z\xd7oz\x02\x00\xbby\xee\x00A\xe2\x0e\x10$\xee\x00A\xe2\x0e\x10$\xee\x00A\xe2\x0e\x10$\xee\x00A\xe2\x0e\x10$\xee\x00A\xe2\x0e\x10$\xee\x00A\xe2\x0e\x10$\xee\x00A\xe2\x0e\x10$\xee\x00A\xe2\x0e\x10$\xee\x00A\xe2\x0e\x10$\xee\x00A\xe2\x0e\x10$\xee\x00A\xe2\x0e\x10$\xee\x00A\xe2\x0e\x10$\xee\x00A\xe2\x0e\x10$\xee\x00A\xe2\x0e\x10$\xee\x00A\xe2\x0e\x10$\xee\x00A\xe2\x0e\x10$\xee\x00A\xe2\x0e\x10$\xee\x00A\xe2\x0e\x10$\xee\x00A\xe2\x0e\x10$\xee\x00A\xe2\x0e\x10$\xee\x00A\xe2\x0e\x10$\xee\x00A\xe2\x0e\x10$\xee\x00A\xe2\x0e\x10$\xee\x00A\xe2\x0e\x10$\xee\x00A\xe2\x0e\x10t\xae\xcf}z\x03\x00\x9by\xee\x00A\xe2\x0e\x10$\xee\x00A\xe2\x0e\x10$\xee\x00A\xe2\x0e\x10$\xee\x00A\xe2\x0e\x10$\xee\x00A\xe2\x0e\x10$\xee\x00A\xe2\x0e\x10$\xee\x00A\xe2\x0e\x10$\xee\x00A\xe2\x0e\x10$\xee\x00A\xe2\x0e\x10$\xee\x00A\xe2\x0e\x10$\xee\x00A\xe2\x0e\x10$\xee\x00A\xe2\x0e\x10$\xee\x00A\xe2\x0e\x10$\xee\x00A\xe2\x0e\x10$\xee\x00A\xe2\x0e\x10$\xee\x00A\xe2\x0e\x10$\xee\x00A\xe2\x0e\x10$\xee\x00A\xe2\x0e\x10$\xee\x00A\xe2\x0e\x10$\xee\x00A\xe2\x0e\x10$\xee\x00A\xe2\x0e\x10$\xee\x00A\xe2\x0e\x10$\xee\x00A\xe2\x0e\x10$\xee\x00A\xe2\x0e\x10$\xee\x00A\xe2\x0e\x10\xb4\x8e\xc75\xbd\x01\x80\xcd<w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08Z\xcf\xe35\xbd\x01\x80\xcd<w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\x12w\x80 q\x07\x08\xfa\x07\x00\x00\xff\xff\xa5\x0b\t\xada\xee\x08\xdb\x00\x00\x00\x00IEND\xaeB`\x82', 'Pride icon bytes do not match'