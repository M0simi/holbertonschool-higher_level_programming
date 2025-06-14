# 📡 Using curl with REST API

## ✅ Step 1: Check if `curl` is installed

```bash
curl --version

If not installed:

bash
Copy code
sudo apt update
sudo apt install curl
🌐 Step 2: Fetch a basic webpage
bash
Copy code
curl http://example.com
This returns the raw HTML of the page.

🔗 Step 3: Fetch JSON from a public API
bash
Copy code
curl https://jsonplaceholder.typicode.com/posts
This returns a list of posts in JSON format.

To make the output pretty (optional):

bash
Copy code
sudo apt install jq
curl https://jsonplaceholder.typicode.com/posts | jq
📄 Step 4: Get only the response headers
bash
Copy code
curl -I https://jsonplaceholder.typicode.com/posts
Example output:

python-repl
Copy code
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
...
📝 Step 5: Make a POST request
bash
Copy code
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
This sends data to the API and gets a response like:

json
Copy code
{
  "title": "foo",
  "body": "bar",
  "userId": "1",
  "id": 101
}
| Command                     | Description                         |                                     |
| --------------------------- | ----------------------------------- | ----------------------------------- |
| `curl URL`                  | Send a GET request (default method) |                                     |
| `curl -I URL`               | Fetch only the headers of response  |                                     |
| `curl -X POST -d "..." URL` | Send a POST request with data       |                                     |
| \`...                       | jq\`                                | Format and pretty-print JSON output |

---

## ✍️ Author
[Meshari - M0simi](https://github.com/M0simi)
