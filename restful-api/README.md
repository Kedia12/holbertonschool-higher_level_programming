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