1. How the Web Works

The web works using a client–server model:

    Client → Browser (Chrome, Firefox)
    Server → Website backend

Flow:

    User enters URL
    Browser sends request
    Server processes it
    Server sends response
    Browser renders page
    
2. How Browser Communicates with Server

Communication happens using:

    HTTP (HyperText Transfer Protocol)

Steps:

    DNS resolves domain → IP
    Browser connects to server
    Sends HTTP request
    Server responds

DNS Lookup:

    browser uses DNS to convert a domain name into an IP address.

TCP/IP Connection:

    A reliable connection is established between the browser and server, usually using TCP.

Request & Response (HTTP/HTTPS):

    Request: The browser sends a request containing a method (e.g., GET to fetch, POST to submit), headers (meta-data), and sometimes a   body.
    Response: The server processes the request and sends back a response with a status code (e.g., 200 OK, 404 Not Found), headers, and requested data.
  
Rendering:

    Once the browser receives the HTML data, it renders the webpage, often triggering additional requests for images, scripts, or stylesheets.

State Management:

    Browsers use cookies to maintain session state with servers across different requests.

3. HTTP vs HTTPS

    Feature	        HTTP	          HTTPS
    Security	    Not secure	    Encrypted
    Encryption    None          	SSL/TLS
    Port          80              443

HTTPS protects:

    passwords
    cookies
    user data

4. HTTP Request vs Response

Request (Client → Server)

Example:

    GET /index.html HTTP/1.1
    Host: example.com
    User-Agent: Chrome
    
Response (Server → Client)

Example:

    HTTP/1.1 200 OK
    Content-Type: text/html

5. HTTP Headers

HTTP headers are key-value pairs of metadata sent between a client (like a browser) and a server during an HTTP request or response. They provide critical instructions on how content should be handled, covering security, caching, content type, and authentication, acting as the shipping label for web data.

Structure:

    It's case-insensitive (e.g., Content-Type: text/html).

Representation/Entity Headers:

    Describe the body's format, such as Content-Type or Content-Length.

Common Request Headers:

    User-Agent → browser info
    Cookie → session data
    Authorization → login info

Common Response Headers:

    Content-Type → data type
    Set-Cookie → create session
    Server → backend info

6. Cookies & Sessions

        Cookies are small text files stored on the client-side (browser) to store user data, while sessions store user data on the server-side, typically tracking users via a session ID stored in a cookie.

Cookies

    Stored in browser
    Sent with every request

Example:

    Cookie: sessionid=abc123

Sessions

    Stored on server
    Linked to cookie

=> Cookie = ID
=> Session = actual data

7. HTTP Methods

        Method	Purpose
        GET	Retrieve data
        POST	Send data
        PUT	Update data
        DELETE	Delete data
        PATCH	Partial update
   
9. Status Codes

        are 3-digit standardized server responses indicating the outcome of a client request

Key HTTP Status Code Categories:

    1xx (Informational): Request received, continuing process.
    2xx (Success): Request successfully received, understood, and accepted (e.g., 200 OK, 201 Created).
    3xx (Redirection): Further action needed, usually a URL change (e.g., 301 Moved Permanently).
    4xx (Client Error): The request contains bad syntax or cannot be fulfilled (e.g., 404 Not Found, 403 Forbidden).
    5xx (Server Error): The server failed to fulfill an apparently valid request (e.g., 500 Internal Server Error).

Common Status Codes:

    200 OK: Success.
    201 Created: Resource created (e.g., POST request).
    204 No Content: Request successful, no data returned.
    301 Moved Permanently: Resource moved, use new URL.
    304 Not Modified: Resource cached; use local copy.
    400 Bad Request: Server cannot process due to client error.
    401 Unauthorized: Authentication needed.
    403 Forbidden: Refused to authorize.
    404 Not Found: Resource not found.
    429 Too Many Requests: Rate limit exceeded.
    500 Internal Server Error: Generic server error.
    502 Bad Gateway: Invalid response from upstream server.
    503 Service Unavailable: Server overloaded or down.

9. Basic Authentication

Simple login method using:

    Authorization: Basic base64(username:password)

Weak because:

    easily decoded
    not secure without HTTPS

10. Developer Tools

Key Tabs:

    Network → see requests/responses
    Console → JavaScript
    Application → cookies, storage
