import React, { useState, useEffect } from "react";
import './Feedback.css';

const Feedback: React.FC = () => {
  const [email, setEmail] = useState("");
  const [feedback, setFeedback] = useState("");
  const [selectedStars, setSelectedStars] = useState(0);
  const [message, setMessage] = useState("");

  useEffect(() => {
    window.scrollTo(0, 0); // Scrollt die Seite beim Laden nach oben
  }, []);

  const handleStarClick = (index: number) => {
    setSelectedStars(index + 1); // Setzt die Sternebewertung
  };

  const handleSubmit = async () => {
    if (!feedback || selectedStars === 0) {
      setMessage("Bitte gib Feedback und eine Sternebewertung an.");
      return;
    }

    try {
      const response = await fetch("http://localhost:5000/api/feedback", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          email,
          feedback,
          stars: selectedStars,
        }),
      });

      if (response.ok) {
        setMessage("Vielen Dank für dein Feedback!");
        setEmail("");
        setFeedback("");
        setSelectedStars(0);
      } else {
        setMessage("Fehler beim Senden des Feedbacks. Bitte versuche es erneut.");
      }
    } catch (error) {
      console.error("Error submitting feedback:", error);
      setMessage("Es gab einen Fehler beim Senden deines Feedbacks.");
    }
  };

  return (
    <div className="feedback-container">
      <div>
        <h1 className="feedback-title">FEEDBACK</h1>
        <p className="feedback-description">
          Wir schätzen deine Meinung sehr! Teile uns mit, wie wir die BrightenUp-App noch verbessern können.
        </p>
      </div>

      <div className="feedback-stars">
        {Array(5).fill(0).map((_, index) => (
          <span
            key={index}
            className={`star ${index < selectedStars ? "selected" : ""}`}
            onClick={() => handleStarClick(index)}
            title={`${index + 1} Stern${index === 0 ? "" : "e"}`}
          >
            ★
          </span>
        ))}
      </div>

      <div className="feedback-form">
        <input
          type="email"
          placeholder="Deine E-Mail Adresse (optional)"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          className="feedback-input"
        />
        <textarea
          placeholder="Schreibe hier deine Anregungen und Wünsche."
          value={feedback}
          onChange={(e) => setFeedback(e.target.value)}
          className="feedback-textarea"
          rows={4}
        ></textarea>
      </div>

      {message && <p className="feedback-message">{message}</p>}

      <button className="feedback-button" onClick={handleSubmit}>
        Senden
      </button>
    </div>
  );
};

export default Feedback;
