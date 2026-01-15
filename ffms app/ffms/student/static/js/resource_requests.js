const data = {
  pending: [
    {
      title: "Projector for Lab 3",
      desc: "Required for final year presentations.",
      by: "Dr. Kim",
      date: "11 Jan 2026, 10:30 AM",
      status: "Pending"
    },
    {
      title: "White Board",
      desc: "Needed for lecture hall.",
      by: "Prof. Verma",
      date: "11 Jan 2026, 9:00 AM",
      status: "Pending"
    }
  ],
  approved: [
    {
      title: "New Computer Systems",
      desc: "Upgrade lab systems.",
      by: "Prof. Sharma",
      date: "10 Jan 2026, 4:15 PM",
      status: "Approved"
    }
  ],
  rejected: [
    {
      title: "Extra Furniture",
      desc: "Budget constraints.",
      by: "Dr. Mehta",
      date: "9 Jan 2026, 2:00 PM",
      status: "Rejected"
    }
  ]
};

let currentType = "pending";

/* ---------- LOAD REQUESTS ---------- */
function loadRequests(type) {
  currentType = type;

  document.getElementById("section-title").innerText =
    type.charAt(0).toUpperCase() + type.slice(1) + " Requests";

  const container = document.getElementById("request-list");
  container.innerHTML = "";

  data[type].forEach((req, index) => {
    container.innerHTML += `
      <div class="request-card">
        <h4>${req.title}</h4>
        <p>Requested by ${req.by}</p>

        <div class="request-actions">
          <button class="view"
            onclick="openModal(
              '${req.title}',
              '${req.desc}',
              '${req.by}',
              '${req.date}',
              '${req.status}'
            )">View</button>

          ${
            type === "pending"
              ? `
                <button class="approve" onclick="approveRequest(${index})">
                  Approve
                </button>
                <button class="reject" onclick="rejectRequest(${index})">
                  Reject
                </button>
              `
              : `<span class="status ${type}">
                   ${type === "approved" ? "✔ Approved" : "✖ Rejected"}
                 </span>`
          }
        </div>
      </div>
    `;
  });
}

/* ---------- APPROVE ---------- */
function approveRequest(index) {
  const req = data.pending.splice(index, 1)[0];
  req.status = "Approved";
  req.date = new Date().toLocaleString();
  data.approved.unshift(req);
  loadRequests("pending");
}

/* ---------- REJECT ---------- */
function rejectRequest(index) {
  const req = data.pending.splice(index, 1)[0];
  req.status = "Rejected";
  req.date = new Date().toLocaleString();
  data.rejected.unshift(req);
  loadRequests("pending");
}

/* ---------- MODAL ---------- */
function openModal(title, desc, by, date, status) {
  document.getElementById("modal-title").innerText = title;
  document.getElementById("modal-desc").innerText = desc;
  document.getElementById("modal-by").innerText = "Requested by: " + by;
  document.getElementById("modal-date").innerText = "Date: " + date;
  document.getElementById("modal-status").innerText = "Status: " + status;

  document.getElementById("requestModal").style.display = "block";
}

function closeModal() {
  document.getElementById("requestModal").style.display = "none";
}

/* ---------- FILTER BUTTON ACTIVE STATE ---------- */
document.querySelectorAll(".filter-btn").forEach(btn => {
  btn.addEventListener("click", () => {
    document.querySelectorAll(".filter-btn")
      .forEach(b => b.classList.remove("active"));

    btn.classList.add("active");
    loadRequests(btn.dataset.type);
  });
});

/* ---------- INITIAL LOAD ---------- */
loadRequests("pending");
