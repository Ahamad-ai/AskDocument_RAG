document.addEventListener("DOMContentLoaded", () => {
    const uploadForm = document.getElementById("upload-form");
    const queryForm = document.getElementById("query-form");
    const uploadStatus = document.getElementById("upload-status");
    const answerOutput = document.getElementById("answer-output");
    const contextOutput = document.getElementById("context-output");

    uploadForm.addEventListener("submit", async (event) => {
        event.preventDefault();
        uploadStatus.innerText = "⏳ Uploading and embedding documents...";

        const formData = new FormData(uploadForm);

        try {
            const response = await fetch("/upload/", {
                method: "POST",
                body: formData
            });
            const result = await response.json();
            if (response.ok) {
                uploadStatus.innerText = result.message;
            } else {
                uploadStatus.innerText = `❌ Error: ${result.error}`;
            }
        } catch (err) {
            uploadStatus.innerText = `❌ Request failed: ${err.message}`;
        }
    });

    queryForm.addEventListener("submit", async (event) => {
        event.preventDefault();
        answerOutput.innerText = "Thinking...";
        contextOutput.innerHTML = "";

        const formData = new FormData(queryForm);
        try {
            const response = await fetch("/query/", {
                method: "POST",
                body: formData
            });
            const result = await response.json();
            if (response.ok) {
            const raw = result.answer || "No response received.";
            const html = marked.parse(raw);
            answerOutput.innerHTML = html;

                if (result.context && result.context.length > 0) {
                    result.context.forEach((text) => {
                        const p = document.createElement("p");
                        p.innerText = text;
                        contextOutput.appendChild(p);
                        contextOutput.appendChild(document.createElement("hr"));
                    });
                } else {
                    contextOutput.innerHTML = "<em>No matching content found.</em>";
                }
            } else {
                answerOutput.innerText = `❌ Error: ${result.error}`;
            }
        } catch (err) {
            answerOutput.innerText = `❌ Request failed: ${err.message}`;
        }
    });
});