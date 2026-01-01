let TOKEN = null;

async function login(username, password) {
  const response = await fetch("http://127.0.0.1:8000/api/token/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password }),
  });
  const data = await response.json();
  TOKEN = data.access;
}

function authHeaders() {
  return TOKEN ? { Authorization: `Bearer ${TOKEN}` } : {};
}
export { login, authHeaders };
// auth.js
// auth.js
