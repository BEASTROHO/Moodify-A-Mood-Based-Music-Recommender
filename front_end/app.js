document.getElementById("analyzeBtn").addEventListener("click", async () => {
  const input = document.getElementById("moodInput").value.trim();
  const resultDiv = document.getElementById("result");

  if (!input) {
    resultDiv.textContent = "Please enter some text.";
    return;
  }

  try {
    const response = await fetch("http://localhost:5000/analyze", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ text: input })
    });

    const data = await response.json();

    if (response.ok && data.mood) {
      resultDiv.textContent = `🎵 Detected Mood: ${data.mood}`;
    } else {
      resultDiv.textContent = `⚠️ Error: ${data.error || "Unexpected response"}`;
    }
  } catch (error) {
    resultDiv.textContent = `❌ Request failed: ${error.message}`;
  }
});
