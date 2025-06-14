# 🌐 HTTP vs HTTPS and REST Basics

## 1. ✅ Difference Between HTTP and HTTPS

| Feature              | HTTP                          | HTTPS                                 |
|----------------------|-------------------------------|----------------------------------------|
| Encryption           | ❌ No encryption               | ✅ Uses SSL/TLS encryption              |
| Security             | ❌ Vulnerable to spying/editing| ✅ Secure and encrypted                 |
| Security Certificate | ❌ No certificate required     | ✅ Requires SSL certificate             |
| Usage                | Used for simple/internal sites| Used for sensitive sites (banking, e-commerce) |
| URL Prefix           | `http://`                     | `https://`                             |

## 2. 🧱 Structure of an HTTP Request and Response

### ✉️ Request Example:

GET /index.html HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0
Accept: text/html

shell
Copy
Edit

### 📩 Response:

HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1256

<html>...</html> ```

### ⚠️ Common HTTP Status Codes:
| Code | Name                  | When It Happens                          |
| ---- | --------------------- | ---------------------------------------- |
| 200  | OK                    | Everything is successful                 |
| 201  | Created               | A new resource has been created          |
| 400  | Bad Request           | The request was incorrect or malformed   |
| 401  | Unauthorized          | The user is not authenticated            |
| 404  | Not Found             | The resource doesn't exist on the server |
| 500  | Internal Server Error | The server had an unexpected error       |
