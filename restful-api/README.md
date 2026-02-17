BASIC OF HTTP/HTTPS

1) Differences between HTTP and HTTPS

HTTP (HyperText Transfer Protocol) sends data in plain text, meaning traffic can be read or modified by anyone who can intercept the connection (e.g., on public Wi-Fi).

HTTPS is HTTP over TLS encryption, which adds:

* Confidentiality: content is encrypted (eavesdroppers can’t read it)

* Integrity: helps prevent tampering in transit

* Authentication: the server proves its identity via certificates

Proof from my inspection:

* URL uses HTTPS: https://www.stevewolf.co/
* Connection uses port 443: 34.160.37.117:443
* Response includes Strict-Transport-Security: max-age=86400 (HSTS), which enforces HTTPS.

2) Structure of an HTTP request and response (based on my capture)

HTTP Request (client → server)

General

* URL: https://www.stevewolf.co/
* (Typical) Method: GET
* (Typical) Path: /

Request structure

GET / HTTP/2
Host: www.stevewolf.co
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Encoding: gzip, deflate, br
Accept-Language: en-GB,en;q=0.9
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) ... Safari/605.1.15
Cookie: (session + security cookies...)
[blank line]
(optional body — usually empty for GET)


What these headers mean (examples)


* Accept tells the server what formats the browser can handle (HTML, XML, etc.).
* Accept-Encoding allows compressed responses (here includes br = Brotli).
* User-Agent identifies the browser.
* Cookie sends stored session/state info back to the server.


HTTP Response (server → client)

Summary

* Status: 200 (Success)
* Address: 34.160.37.117:443

Response structure

HTTP/2 200 OK
Content-Type: text/html; charset=UTF-8
Content-Encoding: br
Content-Length: 152360
Cache-Control: public,max-age=0,must-revalidate
Date: Mon, 16 Feb 2026 09:14:36 GMT
Server: Pepyaka
Set-Cookie: (cookies set by server)
Strict-Transport-Security: max-age=86400
[blank line]
<HTML body returned by server, starting with <!DOCTYPE html> ... >


Notes from my response headers

* Content-Type: text/html; charset=UTF-8 → the response body is HTML (matches the <!DOCTYPE html> I saw).
* Content-Encoding: br → the response was compressed with Brotli.
* x-cache: HIT and Age: 499659 → the response was served from cache.
* Set-Cookie → server updates/stores cookies in the browser.
* Strict-Transport-Security → browser should enforce HTTPS for that time period.

3) Common HTTP methods (at least 4)

1. GET — Retrieve data (no body required)
* Example: loading a webpage or GET /users

2. POST — Send data to create a  resource / submit form
* Example: POST /users to create a new user

3. PUT — Replace an entire resource
* Example: PUT /users/12 with a full updated user object

4. PATCH — Partially update a resource
* Example: PATCH /users/12 to update only the email address

5. DELETE — Remove a resource
* Example: DELETE /users/12


4) Common HTTP status codes (5)

* 200 OK — Request succeeded
Scenario: My request to https://www.stevewolf.co/ returned 200

* 201 Created — Resource created successfully
Scenario: After POST /users, a user is created

* 301 Moved Permanently — Permanent redirect
Scenario: http://... redirects to https://...

* 404 Not Found — Resource doesn’t exist
Scenario: requesting a page/endpoint that isn’t on the server

* 500 Internal Server Error — Server-side failure
Scenario: backend crashes or throws an unhandled exception

(Also: status codes are grouped by first digit: 2xx success, 3xx redirect, 4xx client error, 5xx server error.)

CURL

1. Consume data from an API using command line tools (curl)

Installing / checking curl

On macOS, curl is usually already installed. I verified it with:

curl --version
Expected output: shows the curl version and supported protocols (http/https, etc.).

Fetching data from an API (GET)

I used JSONPlaceholder to retrieve posts:
curl https://jsonplaceholder.typicode.com/posts

Result: returns a JSON array of posts. Each post contains fields like userId, id, title, and body.

Tip (optional, prettier output if you have jq installed):

curl -s https://jsonplaceholder.typicode.com/posts | jq .

Fetching only headers

To inspect only the response headers:
curl -I https://jsonplaceholder.typicode.com/posts

What you should see (example):

* A status line like HTTP/2 200 (or HTTP/1.1 200 OK)
* Headers such as content-type: application/json; charset=utf-8

This is useful for checking status codes, caching, content type, etc.

Making a POST request (send data)

Form-encoded (matches the project prompt)
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts

Expected result: JSONPlaceholder returns a simulated created object, typically including id: 101.

JSON body (common REST style)

curl -X POST \
  -H "Content-Type: application/json; charset=UTF-8" \
  -d '{"title":"foo","body":"bar","userId":1}' \
  https://jsonplaceholder.typicode.com/posts

Expected response (example):

{
  "title": "foo",
  "body": "bar",
  "userId": 1,
  "id": 101
}

JSONPlaceholder simulates creation (it doesn’t persist changes permanently).

Key curl options used (what they mean)

-I → fetch headers only
-X POST → choose HTTP method (here: POST)
-d → send data in the request body (commonly for POST/PUT/PATCH)
-H → add a request header (e.g., Content-Type)

Task 2: Consuming and processing data from an API using Python (requests)

Run

python3 main_02_requests.py

Output (example)

Status Code: 200
sunt aut facere repellat provident occaecati excepturi optio reprehenderit
qui est esse
ea molestias quasi exercitationem repellat qui ipsa sit aut
...

CSV generated

After running, a file named posts.csv is created.

head posts.csv

Output:

id,title,body
1,sunt aut facere repellat provident occaecati excepturi optio reprehenderit,"quia et suscipit
suscipit recusandae consequuntur expedita et cum
reprehenderit molestiae ut ut quas totam
nostrum rerum est autem sunt rem eveniet architecto"
2,qui est esse,"est rerum tempore vitae
sequi sint nihil reprehenderit dolor beatae ea dolores neque
...

Task 3: Simple API using http.server

Run the server

python3 task_03_http_server.py

Server output:

Serving on http://localhost:8000

Test endpoints

curl http://localhost:8000/

Hello, this is a simple API!

curl http://localhost:8000/status

OK

curl http://localhost:8000/data

{"name": "John", "age": 30, "city": "New York"}

curl http://localhost:8000/info

{"version": "1.0", "description": "A simple API built with http.server"}

404 handling

curl -i http://localhost:8000/doesnotexist

Output (excerpt):

HTTP/1.0 404 Not Found
Content-Type: text/plain; charset=utf-8

Endpoint not found

Task 4: Simple API using Flask

Run the server

flask --app task_04_flask.py run

Test endpoints

Root

curl http://127.0.0.1:5000/

Welcome to the Flask API!

Status

curl http://127.0.0.1:5000/status

OK

Data (usernames list)

Before adding users:

curl http://127.0.0.1:5000/data

[]

Add user (POST)

curl -i -X POST http://127.0.0.1:5000/add_user \
  -H "Content-Type: application/json" \
  -d '{"username":"alice","name":"Alice","age":25,"city":"San Francisco"}'

Output (excerpt):

HTTP/1.1 201 CREATED
{"message":"User added","user":{"age":25,"city":"San Francisco","name":"Alice","username":"alice"}}

Get user

curl http://127.0.0.1:5000/users/alice

{"age":25,"city":"San Francisco","name":"Alice","username":"alice"}

Error handling

Missing username (400)

curl -i -X POST http://127.0.0.1:5000/add_user \
  -H "Content-Type: application/json" \
  -d '{"name":"NoUsername"}'

HTTP/1.1 400 BAD REQUEST
{"error":"Username is required"}

Duplicate username (409)

curl -i -X POST http://127.0.0.1:5000/add_user \
  -H "Content-Type: application/json" \
  -d '{"username":"alice","name":"Alice","age":25,"city":"San Francisco"}'

HTTP/1.1 409 CONFLICT
{"error":"Username already exists"}

Invalid JSON (400)

curl -i -X POST http://127.0.0.1:5000/add_user \
  -H "Content-Type: application/json" \
  -d 'not-json'

HTTP/1.1 400 BAD REQUEST
{"error":"Invalid JSON"}

User not found (404)

curl -i http://127.0.0.1:5000/users/doesnotexist
HTTP/1.1 404 NOT FOUND
{"error":"User not found"}

Task 5: API Security and Authentication Techniques

This task focuses on securing a Flask API using Basic Authentication and JWT (JSON Web Tokens), and introducing role-based access control (RBAC).

Concepts covered

* Authentication vs Authorization
    * Authentication: confirms who you are (e.g., username/password, token).
    * Authorization: confirms what you’re allowed to do (e.g., admin-only access).
* Basic Auth: uses an Authorization: Basic ... header (username/password).
* JWT Auth: uses a signed token (Authorization: Bearer <token>) to access protected routes.
* RBAC: restricts routes based on the user role stored in the token (e.g., admin vs user).

Dependencies

Install required libraries:

python3 -m pip install Flask-HTTPAuth Flask-JWT-Extended

API Endpoints (expected behavior)

1) Basic Authentication Protected Route
* URL: /basic-protected
* Method: GET
* Auth: Basic
* Success response: Basic Auth: Access Granted
* Failure response: 401 Unauthorized

Test:

curl -i http://127.0.0.1:5000/basic-protected

With credentials:

curl -i -u user1:password http://127.0.0.1:5000/basic-protected

2) JWT Login (Token Generation)

* URL: /login
* Method: POST
* Body: JSON { "username": "...", "password": "..." }
* Success response: JSON containing access_token
* Failure response: 401 Unauthorized

Test:

curl -i -X POST http://127.0.0.1:5000/login \
  -H "Content-Type: application/json" \
  -d '{"username":"user1","password":"password"}'

3) JWT Protected Route

* URL: /jwt-protected
* Method: GET
* Auth: Bearer token
* Success response: JWT Auth: Access Granted
* Failure response: 401 Unauthorized

Test (replace <TOKEN>):

curl -i http://127.0.0.1:5000/jwt-protected \
  -H "Authorization: Bearer <TOKEN>"

4) Admin-only Route (RBAC)

* URL: /admin-only
* Method: GET
* Auth: JWT + role check
* Admin success response: Admin Access: Granted
* Non-admin response: 403 Forbidden with JSON:

{"error":"Admin access required"}

Test:

curl -i http://127.0.0.1:5000/admin-only \
  -H "Authorization: Bearer <TOKEN>"

Notes on error handling (important for checker)

All authentication failures (missing/invalid/expired/malformed JWT) should return:

* HTTP 401 with a consistent JSON error message.

Files

* task_05_basic_security.py — implementation of Basic Auth + JWT + RBAC.