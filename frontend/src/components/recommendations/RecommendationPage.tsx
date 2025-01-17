import CardCarousel from "./RecommendationCarousel";
import { Typography } from "@mui/material";
import { CardType } from "../../types/Card";
import "./RecommendationPage.css";
import { useEffect, useState } from "react";
import axios from "axios";
import { getBackgroundImage } from "../../util/WeatherHelper";
import { WeatherData } from "../../types/Weather";
import { useSelection } from "../../context/SelectionContext";
import { mapRecommendationToCard } from "../../util/RecommendationHelper";

const RecommendationPage = () => {
  const [weather, setWeather] = useState<WeatherData | null>(null);
  const [recommendationContent, setRecommendationContent] = useState<CardType[]>([]);
  const { selections } = useSelection();

  const fetchWeather = async (): Promise<void> => {
    try {
      const response = await axios.get("/api/weather");
      setWeather(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  const fetchRecommendations = async (): Promise<void> => {
    try {
      const response = await axios.get(
        `/api/recommendations?energy_level=${selections.energy}&interest=${selections.activity}`
      );
      setRecommendationContent(mapRecommendationToCard(response.data.recommendations));
    } catch (error) {
      console.error(error);
    }
  };

  useEffect(() => {
    fetchWeather();
  }, []);

  useEffect(() => {
    fetchRecommendations();
  }, []);

  return (
    <div style={{ backgroundImage: `url(${getBackgroundImage(weather)})` }} className="recommendationPage">
      <div className="recommendationContent">
        <Typography
          variant="h4"
          sx={{
            color: "white",
            textAlign: "center",
            fontWeight: "bold",
            marginBottom: "20px",
            textShadow: "2px 2px 4px rgba(0, 0, 0, 0.5)",
            fontSize: "2.5rem", // Schriftgröße vergrößert
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
            fontSize: "1.2rem", // Schriftgröße für den Text vergrößert
            lineHeight: "1.8", // Optional: Zeilenabstand angepasst
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
