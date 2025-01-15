export interface FeedbackData {
    email_address: string;
    feedback_text: string;
    star_rating: number;
  }
  
  export const sendFeedback = async (feedbackData: FeedbackData): Promise<string> => {
    try {
      const response = await fetch("http://localhost:8000/feedback", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(feedbackData),
      });
  
      if (response.ok) {
        return "Feedback erfolgreich gesendet! Vielen Dank!";
      } else {
        return "Es gab einen Fehler beim Senden deines Feedbacks.";
      }
    } catch (error) {
      console.error("Fehler:", error);
      return "Es gab einen Fehler beim Senden deines Feedbacks.";
    }
  };
  