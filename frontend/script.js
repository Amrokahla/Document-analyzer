const fileInput = document.getElementById("fileInput");
const uploadBtn = document.getElementById("uploadBtn");
const processBtn = document.getElementById("processBtn");
const preview = document.getElementById("preview");
const resultsContainer = document.getElementById("resultsContainer");

const filenameEl = document.getElementById("filename");
const docTypeEl = document.getElementById("docType");
const fieldsTableBody = document.querySelector("#fieldsTable tbody");
const ocrTextEl = document.getElementById("ocrText");

let uploadedFile = null;

// Upload button triggers hidden file input
uploadBtn.addEventListener("click", () => {
  fileInput.click();
});

// Handle file selection
fileInput.addEventListener("change", () => {
  uploadedFile = fileInput.files[0];
  if (uploadedFile) {
    const reader = new FileReader();
    reader.onload = (e) => {
      preview.src = e.target.result;
      preview.style.display = "block";
    };
    reader.readAsDataURL(uploadedFile);
    resultsContainer.style.display = "none"; // hide results until process
  }
});

// Process button: send file to backend
processBtn.addEventListener("click", async () => {
  if (!uploadedFile) {
    alert("Please select a file first!");
    return;
  }

  const formData = new FormData();
  formData.append("file", uploadedFile);

  try {
    const response = await fetch("http://127.0.0.1:8000/api/process-document", {
      method: "POST",
      body: formData,
    });

    if (!response.ok) throw new Error("Processing failed");

    const data = await response.json();

    // Fill results
    filenameEl.textContent = data.filename;
    docTypeEl.textContent = data.document_type;

    // Extracted fields table
    fieldsTableBody.innerHTML = "";
    const fields = data.extracted_data || {};
    if (Object.keys(fields).length === 0) {
      fieldsTableBody.innerHTML = "<tr><td colspan='2'>No extracted fields</td></tr>";
    } else {
      for (const [key, value] of Object.entries(fields)) {
        const row = document.createElement("tr");
        row.innerHTML = `<td>${key}</td><td>${value}</td>`;
        fieldsTableBody.appendChild(row);
      }
    }

    // OCR text
    ocrTextEl.textContent = data.extracted_text || "No OCR text";

    resultsContainer.style.display = "block"; // show results now

  } catch (error) {
    resultsContainer.style.display = "block";
    filenameEl.textContent = "";
    docTypeEl.textContent = "";
    fieldsTableBody.innerHTML = "<tr><td colspan='2'>Error fetching results</td></tr>";
    ocrTextEl.textContent = "❌ " + error.message;
  }
});
