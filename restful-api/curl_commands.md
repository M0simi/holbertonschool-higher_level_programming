# 📡 curl Commands Practice

This document contains examples of using `curl` to interact with HTTP APIs, including GET, POST, and header-only requests.

---

## ✅ Check curl version

```bash
curl --version
🔍 Purpose:
Displays your installed curl version and supported protocols.

🌍 Fetch a Web Page (GET request)
curl http://example.com
🔍 Purpose:
Retrieves the content of a basic web page. Useful for testing HTTP access.

📦 GET Request from a Public API
curl https://jsonplaceholder.typicode.com/posts
🔍 Purpose:
Sends a GET request to the JSONPlaceholder fake API and returns a list of posts in JSON format.

📄 Fetch Only Headers
curl -I https://jsonplaceholder.typicode.com/posts
🔍 Purpose:
Sends a HEAD request and retrieves only the headers of the response (e.g. status, content-type, etc.) without the body.

📝 Send a POST Request
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
🔍 Purpose:
Sends data to the server using POST method. The server will respond with a mock new post (with ID 101).

🧹 (Optional) Format the Output Using jq
curl https://jsonplaceholder.typicode.com/posts | jq
🔍 Purpose:
Pipes the JSON response into jq for cleaner formatting and readability. You must have jq installed.

🧠 Summary of curl Flags
| Flag | Description                                   |
|------|-----------------------------------------------|
| -X   | Specifies the request method (e.g. POST, PUT) |
| -d   | Sends data in the body of the request         |
| -I   | Retrieves only headers                        |
| jq   | Formats JSON output (optional)                |
