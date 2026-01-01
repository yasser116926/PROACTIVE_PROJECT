// app.js
import { login, authHeaders } from "./auth.js";

/* =========================
   NEWS LOADER
========================= */

async function loadNews() {
  const response = await fetch("http://127.0.0.1:8000/api/news/", {
    headers: authHeaders(),
  });

  if (!response.ok) {
    console.error("Failed to load news");
    return;
  }

  const news = await response.json();

  const container = document.getElementById("news-container");
  if (!container) return;

  container.innerHTML = "";

  news.forEach((item) => {
    const div = document.createElement("div");
    div.innerHTML = `
      <h3>${item.title}</h3>
      <p>${item.description}</p>
    `;
    container.appendChild(div);
  });
}

document.addEventListener("DOMContentLoaded", loadNews);

/* =========================
   STUDENT UI STATE
========================= */

function updateStudentBorder(studentId, state) {
  const studentEl = document.querySelector(
    `.student-card[data-student-id="${studentId}"]`
  );
  if (!studentEl) return;

  studentEl.classList.remove(
    "student-muted",
    "student-speaking",
    "student-disconnected"
  );

  if (state === "muted") {
    studentEl.classList.add("student-muted");
  } else if (state === "speaking") {
    studentEl.classList.add("student-speaking");
  } else if (state === "disconnected") {
    studentEl.classList.add("student-disconnected");
  }
}

/*
  IMPORTANT:
  Call updateStudentBorder() from:
  - mic mute logic
  - mic unmute logic
  - student disconnect events
*/
