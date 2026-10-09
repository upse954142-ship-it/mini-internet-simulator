"""Basic route tests for the Mini Internet Simulator."""
import unittest
from urllib.request import urlopen
from urllib.error import HTTPError
from threading import Thread
from http.server import ThreadingHTTPServer
import app

class MiniInternetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), app.MiniInternetHandler)
        cls.port = cls.server.server_address[1]
        cls.thread = Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.base = f"http://127.0.0.1:{cls.port}"

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join(timeout=2)

    def test_home(self):
        with urlopen(self.base + "/") as r:
            self.assertEqual(r.status, 200)
            self.assertIn(b"Mini Internet Simulator", r.read())

    def test_known_site(self):
        with urlopen(self.base + "/visit?site=library.mini") as r:
            self.assertEqual(r.status, 200)
            self.assertIn(b"Digital Library", r.read())

    def test_unknown_site_is_404(self):
        with self.assertRaises(HTTPError) as ctx:
            urlopen(self.base + "/visit?site=unknown.mini")
        self.assertEqual(ctx.exception.code, 404)

    def test_json_api(self):
        with urlopen(self.base + "/api/sites") as r:
            self.assertEqual(r.status, 200)
            self.assertIn(b"library.mini", r.read())

if __name__ == "__main__":
    unittest.main(verbosity=2)
