"use client";
import { useState } from "react";

export default function SchedulePage() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState<string[]>([]);
  const [confirmation, setConfirmation] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  const vehicleId = 101;

  const sendMessage = async () => {
    if (!input.trim()) return;

    const text = input;
    setMessages((prev) => [...prev, text]);
    setInput("");
    setLoading(true);

    try {
      const res = await fetch("http://localhost:8000/chat/schedule", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          message: text,
          vehicle_id: vehicleId
        })
      });

      const data = await res.json();
      setConfirmation(data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const startListening = () => {
    const SpeechRecognition =
      (window as any).SpeechRecognition ||
      (window as any).webkitSpeechRecognition;

    if (!SpeechRecognition) {
      alert("Voice input not supported");
      return;
    }

    const recognition = new SpeechRecognition();
    recognition.lang = "en-US";
    recognition.start();

    recognition.onresult = (e: any) => {
      setInput(e.results[0][0].transcript);
    };
  };

  return (
    <div className="page">
      <div className="card">
        <header>
          <h1>Service Scheduling</h1>
          <p>AI Assistant</p>
        </header>

        <section className="chat">
          <div className="message bot">
            Please tell me your preferred date and time.
          </div>

          {messages.map((m, i) => (
            <div key={i} className="message user">{m}</div>
          ))}

          {loading && (
            <div className="message bot">Processing…</div>
          )}
        </section>

        <footer>
          <input
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="e.g. Tomorrow at 3 PM"
            onKeyDown={(e) => e.key === "Enter" && sendMessage()}
          />

          <button className="mic" onClick={startListening}>🎙</button>
          <button onClick={sendMessage}>Send</button>
        </footer>

        {confirmation && (
          <div className="confirmation">
            <strong>Appointment Confirmed</strong>
            <div>{confirmation.service_center}</div>
            <div>{confirmation.date} · {confirmation.time}</div>
          </div>
        )}
      </div>
    </div>
  );
}
