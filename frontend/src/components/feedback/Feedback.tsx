import React, { useState } from "react";
import "./Feedback.css";

const FeedbackPage: React.FC = () => {
  const [email, setEmail] = useState("");
  const [feedbackText, setFeedbackText] = useState("");
  const [rating, setRating] = useState(0);
  const [message, setMessage] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    const feedbackData = {
      email_address: email,
      feedback_text: feedbackText,
      star_rating: rating,
    };

    try {
      const response = await fetch("http://127.0.0.1:5000/feedback", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(feedbackData),
      });

      if (response.ok) {
        setMessage("Feedback erfolgreich gesendet! Vielen Dank!");
        // Felder zurücksetzen
        setEmail("");
        setFeedbackText("");
        setRating(0);
      } else {
        const errorData = await response.json();
        setMessage(`Fehler: ${errorData.error || "Unbekannter Fehler"}`);
      }
    } catch (error) {
      console.error("Fehler beim Senden des Feedbacks:", error);
      setMessage("Es gab einen Fehler beim Senden deines Feedbacks.");
    }
  };

  return (
    <div className="feedback-page">
      <div className="feedback-container">
        <h1 className="feedback-title">FEEDBACK</h1>
        <p className="feedback-description">
          Wir schätzen deine Meinung sehr! Teile uns mit, wie wir die BrightenUp-App noch verbessern können.
        </p>
        <form className="feedback-form" onSubmit={handleSubmit}>
          <div className="feedback-stars">
            {[1, 2, 3, 4, 5].map((star) => (
              <span
                key={star}
                className={`star ${rating >= star ? "selected" : ""}`}
                onClick={() => setRating(star)}
              >
                ★
              </span>
            ))}
          </div>
          <input
            type="email"
            className="feedback-input"
            placeholder="Deine E-Mail Adresse (optional)"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
          <textarea
            className="feedback-textarea"
            placeholder="Schreibe hier deine Anregungen und Wünsche."
            value={feedbackText}
            onChange={(e) => setFeedbackText(e.target.value)}
          />
          <button type="submit" className="feedback-button">
            Senden
          </button>
        </form>
        {message && <p className="feedback-message">{message}</p>}
      </div>
    </div>
  );
};

export default FeedbackPage;
