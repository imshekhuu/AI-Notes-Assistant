function sendData(action) {
    const notes = document.getElementById("notes").value;

    if (!notes.trim()) {
        alert("Paste notes first.");
        return;
    }

    fetch("/process", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            notes: notes,
            action: action
        })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("result").textContent = data.result;
        document.getElementById("output").style.display = "block";
    })
    .catch(err => {
        console.error(err);
        alert("Server error");
    });
}
