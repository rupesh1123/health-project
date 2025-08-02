function setGoal() {
  const goal = document.getElementById("goalInput").value;

  if (!goal.trim()) {
    document.getElementById("response").innerText = "Please enter a goal.";
    return;
  }

  fetch("http://127.0.0.1:5000/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: goal })  // send as 'message' for chatbot
  })
    .then(res => res.json())
    .then(data => {
      document.getElementById("response").innerText = data.response;
    })
    .catch(error => {
      console.error("Error:", error);
      document.getElementById("response").innerText = "Server error.";
    });
}
