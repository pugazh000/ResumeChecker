document.getElementById("resumeForm").addEventListener("submit", function(event) {
    event.preventDefault();
    let formData = new FormData();
    formData.append("resume", document.getElementById("resume").files[0]);
    formData.append("job_role", document.getElementById("jobRole").value);

    fetch("https://your-api-id.execute-api.region.amazonaws.com/dev/upload", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerText = 
            `Match Score: ${data.match_score}%\n` +
            `Matched Skills: ${data.matched_skills.join(", ")}\n` +
            `Missing Skills: ${data.missing_skills.join(", ")}`;
    })
    .catch(error => console.error("Error:", error));
});
