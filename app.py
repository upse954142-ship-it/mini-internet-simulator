"""
Mini Internet Simulator - B.Tech beginner project
Run: python app.py
Open: http://127.0.0.1:8000
This educational demo uses Python's standard library only.
Do not expose this development server to the public internet.
"""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs
from datetime import datetime
import json

HOST = "127.0.0.1"
PORT = 8000

# A tiny, application-level name directory (not the global DNS system).
SITES = {
    "home.mini": {
        "title": "Mini Internet Home",
        "description": "Welcome to your own small internet-like network.",
        "content": "This page is hosted by your Python server."
    },
    "library.mini": {
        "title": "Digital Library",
        "description": "A sample library service on the Mini Internet.",
        "content": "Browse learning resources, notes, and project references."
    },
    "news.mini": {
        "title": "Mini News",
        "description": "A sample news service on the Mini Internet.",
        "content": "This is demonstration content served locally."
    },
    "about.mini": {
        "title": "About This Project",
        "description": "A student project demonstrating basic web networking.",
        "content": "Built with Python HTTP handling, HTML, and a local name directory."
    },
}

def page(title, body):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
:root {{ color-scheme: light; }}
body {{ margin:0; font-family:Arial,sans-serif; background:#f3f6fb; color:#172033; }}
header {{ background:#13294b; color:white; padding:22px max(20px, calc((100% - 960px)/2)); }}
main {{ max-width:960px; margin:28px auto; padding:0 18px; }}
.card {{ background:white; border:1px solid #dce4f0; border-radius:14px; padding:20px; margin:14px 0; box-shadow:0 4px 14px #15294b0b; }}
h1,h2 {{ margin-top:0; }}
a {{ color:#075fc7; }}
nav a {{ color:white; margin-right:14px; }}
input {{ padding:11px; width:min(440px,90%); border:1px solid #b8c6d9; border-radius:8px; }}
button {{ padding:11px 15px; border:0; border-radius:8px; background:#1769d2; color:white; cursor:pointer; }}
.pill {{ display:inline-block; background:#e4f7ec; color:#146c3a; padding:5px 9px; border-radius:20px; font-size:13px; }}
small, .muted {{ color:#65738a; }}
li {{ margin:8px 0; }}
footer {{ text-align:center; padding:25px; color:#65738a; }}
</style>
</head>
<body>
<header>
  <h1>🌐 Mini Internet Simulator</h1>
  <nav><a href="/">Home</a><a href="/directory">Directory</a><a href="/status">Network Status</a><a href="/about">About</a></nav>
</header>
<main>{body}</main>
<footer>Educational B.Tech project · Runs on your computer · No external packages required</footer>
</body></html>"""

class MiniInternetHandler(BaseHTTPRequestHandler):
    def send_html(self, html, status=200):
        data = html.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        self.wfile.write(data)

    def send_json(self, obj, status=200):
        data = json.dumps(obj, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        query = parse_qs(parsed.query)

        if path == "/":
            body = """
            <section class="card">
              <span class="pill">SERVER ONLINE</span>
              <h2>Welcome to your own Mini Internet</h2>
              <p>This project demonstrates how a browser requests a page from a Python HTTP server.</p>
              <form action="/visit" method="get">
                <label for="site"><b>Enter a local site name</b></label><br><br>
                <input id="site" name="site" placeholder="Try library.mini" required>
                <button type="submit">Visit site</button>
              </form>
              <p class="muted">Try: home.mini, library.mini, news.mini, about.mini</p>
            </section>
            <section class="card">
              <h2>What can you explore?</h2>
              <ul>
                <li><a href="/directory">Local name directory</a> — maps names to application routes.</li>
                <li><a href="/status">Network status</a> — checks whether the server is responding.</li>
                <li><a href="/api/sites">JSON API</a> — machine-readable list of registered sites.</li>
              </ul>
            </section>"""
            self.send_html(page("Mini Internet Home", body))

        elif path == "/visit":
            site = query.get("site", [""])[0].strip().lower()
            if site not in SITES:
                known = ", ".join(SITES.keys())
                body = f"""<section class="card"><h2>Site not found</h2>
                <p><b>{site or '(empty name)'}</b> is not registered in this Mini Internet.</p>
                <p>Registered names: {known}</p><p><a href="/">Try again</a></p></section>"""
                self.send_html(page("Site Not Found", body), 404)
            else:
                record = SITES[site]
                body = f"""<section class="card"><span class="pill">NAME RESOLVED</span>
                <h2>{record['title']}</h2><p>{record['description']}</p>
                <p>{record['content']}</p>
                <hr><p><b>Requested name:</b> {site}</p>
                <p><b>Resolved application route:</b> /visit?site={site}</p>
                <p><a href="/">Return home</a> · <a href="/directory">View directory</a></p></section>"""
                self.send_html(page(record["title"], body))

        elif path == "/directory":
            items = "".join(
                f"<li><b>{name}</b> — {record['description']} "
                f'<a href="/visit?site={name}">Open</a></li>'
                for name, record in SITES.items()
            )
            body = f"""<section class="card"><h2>Local Name Directory</h2>
            <p>This table is stored in the Python program. It is a small teaching model of name resolution, not a public DNS server.</p>
            <ul>{items}</ul></section>"""
            self.send_html(page("Local Directory", body))

        elif path == "/status":
            body = f"""<section class="card"><span class="pill">RESPONDING</span>
            <h2>Network Status</h2><ul>
            <li>HTTP server: Running</li><li>Host: {HOST}</li><li>Port: {PORT}</li>
            <li>Registered local sites: {len(SITES)}</li>
            <li>Server time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</li>
            </ul><p>This status means the local application is responding; it does not test your full internet connection.</p></section>"""
            self.send_html(page("Network Status", body))

        elif path == "/about":
            body = """<section class="card"><h2>About the Project</h2>
            <p><b>Objective:</b> demonstrate basic client-server communication and application-level name resolution.</p>
            <p><b>Tools:</b> Python standard library, HTTP, HTML, CSS, browser.</p>
            <p><b>Limitations:</b> names only work inside this application; this is not a real DNS server, ISP, router, or global internet.</p></section>"""
            self.send_html(page("About", body))

        elif path == "/api/sites":
            self.send_json({"project": "Mini Internet Simulator", "sites": SITES, "count": len(SITES)})

        elif path == "/api/status":
            self.send_json({
                "status": "online",
                "host": HOST,
                "port": PORT,
                "registered_sites": len(SITES),
                "checked_at": datetime.now().isoformat(timespec="seconds")
            })

        else:
            body = """<section class="card"><h2>404 — Page not found</h2>
            <p>The requested route does not exist in this Mini Internet.</p><p><a href="/">Return home</a></p></section>"""
            self.send_html(page("404 Not Found", body), 404)

    def log_message(self, format, *args):
        # Keep a simple request log in the terminal.
        print(f"[Mini Internet] {self.address_string()} - {format % args}")

def main():
    server = ThreadingHTTPServer((HOST, PORT), MiniInternetHandler)
    print("=" * 54)
    print("Mini Internet Simulator is running!")
    print(f"Open this address in your browser: http://{HOST}:{PORT}")
    print("Press Ctrl+C to stop the server.")
    print("=" * 54)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\\nStopping Mini Internet Simulator...")
    finally:
        server.server_close()
        print("Server stopped.")

if __name__ == "__main__":
    main()
