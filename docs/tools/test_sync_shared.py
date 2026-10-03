# Pruebas de sync_shared.py sobre una copia temporal de dist/ (no toca el proyecto).
# Uso: python docs/tools/test_sync_shared.py
import subprocess, sys, tempfile, unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
SCRIPT = TOOLS / 'sync_shared.py'

INDEX = '''<!doctype html>
<html lang="en">
<head>
  <!-- shared:assets -->
  <link rel="stylesheet" href="assets/css/main.css">
  <!-- /shared:assets -->
</head>
<body>
  <!-- shared:header -->
  <header>
    <a class="site-nav__sublink" href="./" aria-current="page">Home Version 01</a>
    <a class="site-nav__sublink" href="about-us.html">About Us</a>
  </header>
  <!-- /shared:header -->
  <main>home</main>
  <!-- shared:footer -->
  <footer>
    <a class="offcanvas__sublink" href="./" aria-current="page">Home Version 01</a>
    <a class="offcanvas__sublink" href="about-us.html">About Us</a>
  </footer>
  <!-- /shared:footer -->
</body>
</html>
'''

PAGE = '''<!doctype html>
<html lang="en">
<head>
  <!-- shared:assets -->
  <!-- /shared:assets -->
</head>
<body>
  <!-- shared:header -->
  <!-- /shared:header -->
  <main>about</main>
  <!-- shared:footer -->
  <!-- /shared:footer -->
</body>
</html>
'''

def run(dist, *args):
    return subprocess.run([sys.executable, str(SCRIPT), '--dist', str(dist), *args], capture_output=True, text=True)

class SyncSharedTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dist = Path(self.tmp.name)
        (self.dist / 'index.html').write_text(INDEX, encoding='utf-8')
        (self.dist / 'about-us.html').write_text(PAGE, encoding='utf-8')

    def tearDown(self):
        self.tmp.cleanup()

    def test_copies_blocks_and_marks_current_page(self):
        result = run(self.dist)
        self.assertEqual(result.returncode, 0, result.stderr)
        about = (self.dist / 'about-us.html').read_text(encoding='utf-8')
        self.assertIn('assets/css/main.css', about)
        self.assertIn('<main>about</main>', about)
        # el enlace a la propia página queda marcado, en el header y en el off-canvas
        self.assertIn('<a class="site-nav__sublink" href="about-us.html" aria-current="page">', about)
        self.assertIn('<a class="offcanvas__sublink" href="about-us.html" aria-current="page">', about)
        # y la marca de la home no se copia
        self.assertNotIn('href="./" aria-current="page"', about)

    def test_source_is_not_modified(self):
        run(self.dist)
        self.assertEqual((self.dist / 'index.html').read_text(encoding='utf-8'), INDEX)

    def test_check_reports_stale_pages_and_is_idempotent(self):
        self.assertEqual(run(self.dist, '--check').returncode, 1)
        run(self.dist)
        self.assertEqual(run(self.dist, '--check').returncode, 0)

    def test_missing_marker_fails(self):
        (self.dist / 'broken.html').write_text('<html><body></body></html>', encoding='utf-8')
        result = run(self.dist)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('shared:assets', result.stderr)

if __name__ == '__main__':
    unittest.main()
