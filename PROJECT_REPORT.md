# MINI INTERNET SIMULATOR
## B.Tech Computer Science Project Report

**Student Name:** ____________________  
**Roll Number:** ____________________  
**Department:** Computer Science and Engineering  
**College:** ____________________  
**Guide:** ____________________  
**Academic Year:** ____________________

## 1. Abstract
The Mini Internet Simulator is an educational web application developed using Python. It demonstrates a simplified client-server architecture in which a browser sends HTTP requests to a local Python server and receives HTML or JSON responses. The project includes a home page, a local name directory, service pages, a status dashboard, and JSON API endpoints. Names such as `library.mini` are resolved by the application to registered content. This is an application-level simulation of name resolution, not a replacement for the Domain Name System or the global internet.

## 2. Problem Statement
Beginners often learn networking concepts theoretically without seeing how a browser communicates with a server. This project provides a small, testable environment to observe requests, responses, routes, and name-to-content mapping.

## 3. Objectives
- Understand the client-server model.
- Demonstrate HTTP GET requests and status codes.
- Create pages served by a Python program.
- Simulate a small name directory.
- Provide a status page and JSON API.
- Test successful and unsuccessful requests.

## 4. Tools and Technologies
- Python 3
- Visual Studio Code
- HTML and CSS
- HTTP
- Python standard-library modules: `http.server`, `urllib.parse`, `datetime`, and `json`
- A web browser

## 5. System Design
The browser acts as the client. It sends an HTTP request to the Python server at `127.0.0.1:8000`. The request handler examines the URL path and query parameters, selects a page or API response, and returns an HTTP response. The local site dictionary maps names such as `library.mini` to sample page information.

## 6. Modules
1. Home page: provides project navigation.
2. Local directory: lists registered names.
3. Name resolver: looks up a submitted name in the local dictionary.
4. Service pages: serves home, library, news, and about content.
5. Status module: reports that the application is responding.
6. JSON API: returns registered sites and status in JSON format.
7. Error handling: returns a 404 response for unknown routes or names.

## 7. Algorithm
1. Start the Python server on the configured host and port.
2. Wait for an incoming HTTP request.
3. Parse the URL path and query parameters.
4. If the path is `/visit`, read the requested site name.
5. Search for that name in the local site directory.
6. If found, return the registered page; otherwise return a 404 response.
7. For `/directory`, `/status`, and API routes, return the corresponding response.
8. Continue until the user stops the server.

## 8. Testing Plan
| Test | Input | Expected result |
|---|---|---|
| Home page | `/` | Home page loads |
| Directory | `/directory` | Registered names appear |
| Known site | `/visit?site=library.mini` | Digital Library page loads |
| Unknown site | `/visit?site=unknown.mini` | 404 Site Not Found |
| Status | `/status` | Server status page loads |
| Sites API | `/api/sites` | JSON list of sites |
| Unknown route | `/does-not-exist` | 404 Page Not Found |

Record the actual result and screenshot for each test after running the program.

## 9. Results
The application is designed to serve multiple local pages and JSON endpoints from one Python server. Fill in this section with the actual test results and screenshots from your own run.

## 10. Limitations
- The `.mini` names work only inside the application's name directory.
- It does not implement real DNS, routing between networks, an ISP, or global internet access.
- The server is intended for local educational use, not production deployment.
- The status page reports application status, not the health of the whole internet connection.

## 11. Future Scope
- Store site records in SQLite.
- Add a simple administrator page to register new sites.
- Add user authentication for administrative actions.
- Add network measurements and request logging.
- Deploy behind a production-grade web server after appropriate security review.

## 12. Conclusion
The Mini Internet Simulator provides a practical introduction to web networking. It demonstrates how a client requests resources from a server, how HTTP responses are returned, and how an application can map friendly names to local content. It is a learning simulation rather than a complete internet implementation.

## 13. References
- Python documentation: https://docs.python.org/3/library/http.server.html
- Python in VS Code: https://code.visualstudio.com/docs/languages/python/
