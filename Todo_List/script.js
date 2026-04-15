const BASE_URL = "http://127.0.0.1:8000";

function getToken() {
    return localStorage.getItem("token");
}

function setToken(token) {
    localStorage.setItem("token", token);
}

function logout() {
    localStorage.removeItem("token");
    location.reload();
}

function showApp() {
    document.getElementById("auth-section").style.display = "none";
    document.getElementById("app-section").style.display = "block";
    loadUser();
}

// 🔐 LOGIN
async function login() {
    const formData = new URLSearchParams();
    formData.append("username", document.getElementById("login-username").value);
    formData.append("password", document.getElementById("login-password").value);

    const res = await fetch(`${BASE_URL}/auth/token`, {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: formData
    });

    const data = await res.json();

    if (!data.access_token) {
        alert("Login failed");
        return;
    }

    setToken(data.access_token);
    showApp();
    loadTodos();
}

// 📝 REGISTER
async function register() {
    const body = {
        email: reg("email"),
        username: reg("username"),
        name: reg("name"),
        phone_number: reg("phone"),
        password: reg("password"),
        role: reg("role")
    };

    await fetch(`${BASE_URL}/auth/create_user`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(body)
    });

    alert("User created! Now login.");
}

function reg(id) {
    return document.getElementById(`reg-${id}`).value;
}

// 👤 LOAD USER INFO
async function loadUser() {
    const res = await fetch(`${BASE_URL}/user/details`, {
        headers: { Authorization: `Bearer ${getToken()}` }
    });

    const user = await res.json();
    document.getElementById("user-info").innerText =
        `Welcome ${user.name} (${user.username})`;
}

// 📋 LOAD TODOS
async function loadTodos() {
    const res = await fetch(`${BASE_URL}/`, {
        headers: { Authorization: `Bearer ${getToken()}` }
    });

    const todos = await res.json();
    const table = document.getElementById("todo-list");
    table.innerHTML = "";

    todos.forEach(todo => {
        table.innerHTML += `
            <tr>
                <td>${todo.title}</td>
                <td>${todo.description}</td>
                <td>${todo.priority}</td>
                <td>${todo.status ? "✅" : "❌"}</td>
                <td>
                    <button onclick="deleteTodo(${todo.id})">Delete</button>
                </td>
            </tr>
        `;
    });
}

// ➕ CREATE TODO
async function createTodo() {
    const body = {
        title: val("title"),
        description: val("description"),
        priority: parseInt(val("priority")),
        status: document.getElementById("status").checked
    };

    await fetch(`${BASE_URL}/todos/create`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${getToken()}`
        },
        body: JSON.stringify(body)
    });

    loadTodos();
}

function val(id) {
    return document.getElementById(id).value;
}

// ❌ DELETE
async function deleteTodo(id) {
    await fetch(`${BASE_URL}/todos/delete/${id}`, {
        method: "DELETE",
        headers: {
            Authorization: `Bearer ${getToken()}`
        }
    });

    loadTodos();
}