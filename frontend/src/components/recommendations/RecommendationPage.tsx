import CardCarousel from "./RecommendationCarousel";
import { Typography } from "@mui/material";
import { CardType } from "../../types/Card";
import "./RecommendationPage.css";

const RecommendationPage = () => {
  const recommendationContent: CardType[] = [
    {
      title: "Spaziergang im Park",
      text: "Ein Spaziergang im Park kann wahre Wunder bewirken. Die frische Luft und die Natur können dir helfen, dich zu entspannen und neue Energie zu tanken.",
      imageUrl: "https://images.unsplash.com/photo-1606785883223-6f4b2f3d3d4b",
    },
    {
      title: "Yoga",
      text: "Yoga ist eine großartige Möglichkeit",
      videoUrl: "https://www.youtube.com/embed/v7SN-d4qXx0?si=pDzmpr5Vei4bCVs5",
    },
    {
      title: "Spaziergang im Park",
      text: "Ein Spaziergang im Park kann wahre Wunder bewirken. Die frische Luft und die Natur können dir helfen, dich zu entspannen und neue Energie zu tanken.",
      imageUrl: "https://images.unsplash.com/photo-1606785883223-6f4b2f3d3d4b",
    },
    {
      title: "Yoga",
      text: "Yoga ist eine großartige Möglichkeit",
      videoUrl: "https://www.youtube.com/embed/v7SN-d4qXx0?si=pDzmpr5Vei4bCVs5",
    },
    {
      title: "Spaziergang im Park",
      text: "Ein Spaziergang im Park kann wahre Wunder bewirken. Die frische Luft und die Natur können dir helfen, dich zu entspannen und neue Energie zu tanken.",
      imageUrl: "https://images.unsplash.com/photo-1606785883223-6f4b2f3d3d4b",
    },
    {
      title: "Yoga",
      text: "Yoga ist eine großartige Möglichkeit",
      videoUrl: "https://www.youtube.com/embed/v7SN-d4qXx0?si=pDzmpr5Vei4bCVs5",
    },
  ];

  return (
    <div className="recommendationPage">
      <div className="recommendationContent">
        <Typography
          variant="h4"
          sx={{
            color: "white",
            textAlign: "center",
            fontWeight: "bold",
            marginBottom: "20px",
            textShadow: "2px 2px 4px rgba(0, 0, 0, 0.5)",
          }}
        >
          Unsere Vorschläge für dich
        </Typography>
        <Typography
          variant="body1"
          sx={{
            color: "white",
            textAlign: "center",
            marginBottom: "30px",
            maxWidth: "600px",
            margin: "0 auto",
            textShadow: "1px 1px 1px rgba(0, 0, 0, 0.5)",
          }}
        >
          Unsere Empfehlungen basieren auf dem aktuellen Wetter und sollen dir helfen, Aktivitäten zu finden, die dir
          guttun – sowohl für deinen Körper als auch für deine Seele. Natürlich gibt es noch viele andere Dinge, die dir
          helfen können, dich wohlzufühlen. Sieh unsere Vorschläge als kleine Inspiration. Deine mentale Gesundheit ist
          wichtig, und das Wetter kann deine Stimmung stark beeinflussen. Egal ob Sonnenschein, Regen oder Schnee – mit
          den richtigen Aktivitäten kannst du das Beste aus jedem Tag herausholen und dich dabei besser fühlen.
        </Typography>
        <div className="carousel-bottom">
          <CardCarousel cards={recommendationContent} />
        </div>
      </div>
    </div>
  );
};

export default RecommendationPage;
