import React, { useEffect, useState } from "react";
import { Typography } from "@mui/material";
import { useNavigate, useLocation } from "react-router-dom"; // <-- useLocation hinzufügen
import SentimentVerySatisfiedIcon from "@mui/icons-material/SentimentVerySatisfied";
import SentimentSatisfiedIcon from "@mui/icons-material/SentimentSatisfied";
import SentimentNeutralIcon from "@mui/icons-material/SentimentNeutral";
import SentimentDissatisfiedIcon from "@mui/icons-material/SentimentDissatisfied";
import SentimentVeryDissatisfiedIcon from "@mui/icons-material/SentimentVeryDissatisfied";
import { useSelection } from "../../context/SelectionContext";
import "./QuestionPage2.css";

const QuestionPage2: React.FC = () => {
  const navigate = useNavigate();
  const location = useLocation(); // <-- Hinzufügen
  const { setSelection } = useSelection();
  const [value, setValue] = useState("");

  // Den Namen aus dem Zustand abrufen (falls vorhanden)
  const name = location.state?.name || "";

  useEffect(() => {
    window.scrollTo(0, 0);
  }, []);

  const handleSelection = (value: string) => {
    console.log("Energy:", value);
    setValue(value);
    setSelection("energy", value);
    navigate(`/recommendation`, { state: { name } }); // Name weitergeben
  };

  const energyOptions = [
    {
      label: "Gut und\nvoller Energie",
      icon: <SentimentVerySatisfiedIcon className="icon" />,
      hoverColor: "#4caf50",
      value: "very-energetic",
    },
    {
      label: "Gut, aber\netwas müde",
      icon: <SentimentSatisfiedIcon className="icon" />,
      hoverColor: "#ffeb3b",
      value: "good",
    },
    {
      label: "Neutral und\nmoderate Energie",
      icon: <SentimentNeutralIcon className="icon" />,
      hoverColor: "#795548",
      value: "neutral",
    },
    {
      label: "Schlecht, aber\nnoch etwas Energie",
      icon: <SentimentDissatisfiedIcon className="icon" />,
      hoverColor: "#9e9e9e",
      value: "low",
    },
    {
      label: "Schlecht und\nsehr erschöpft",
      icon: <SentimentVeryDissatisfiedIcon className="icon" />,
      hoverColor: "red",
      value: "very-low",
    },
  ];

  return (
    <div className="question2-page">
      <div className="content">
        <Typography variant="h4" className="title">
          Wie fühlst du dich heute{name ? `, ${name}` : ""}?
        </Typography>

        <div className="energy-options">
          {energyOptions.map((option, index) => (
            <div
              key={index}
              className="energy-option"
              onClick={() => handleSelection(option.value)}
              style={{
                "--hover-color": option.hoverColor,
                cursor: "pointer",
              } as React.CSSProperties}
            >
              <div className="icon">{option.icon}</div>
              <Typography
                className="option-label"
                style={{
                  whiteSpace: "pre-wrap",
                  textAlign: "center",
                }}
              >
                {option.label}
              </Typography>
            </div>
          ))}
        </div>

        <Typography className="slogan">
          Deine Angaben werden nicht gespeichert – jede Sitzung ist einzigartig!
        </Typography>
      </div>
    </div>
  );
};

export default QuestionPage2;
