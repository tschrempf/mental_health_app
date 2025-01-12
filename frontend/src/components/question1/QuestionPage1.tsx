import React, { useEffect, useState } from "react";
import { Typography } from "@mui/material";
import { useNavigate } from "react-router-dom";
import LocationCityIcon from "@mui/icons-material/LocationCity";
import FitnessCenterIcon from "@mui/icons-material/FitnessCenter";
import SelfImprovementIcon from "@mui/icons-material/SelfImprovement";
import HomeIcon from "@mui/icons-material/Home";
import SpaIcon from "@mui/icons-material/Spa";
import { useSelection } from "../../context/SelectionContext";
import "./QuestionPage1.css";

const options = [
  { icon: <LocationCityIcon fontSize="inherit" />, label: "Outdoor", value: "Outdoor" },
  { icon: <FitnessCenterIcon fontSize="inherit" />, label: "Fitness", value: "Fitness" },
  { icon: <SelfImprovementIcon fontSize="inherit" />, label: "Yoga", value: "Yoga" },
  { icon: <HomeIcon fontSize="inherit" />, label: "Zuhause bleiben", value: "Home" },
  { icon: <SpaIcon fontSize="inherit" />, label: "Meditation", value: "Meditation" },
];

const QuestionPage1: React.FC = () => {
  const navigate = useNavigate();
  const { setSelection } = useSelection();
  const [value, setValue] = useState("");

  useEffect(() => {
    window.scrollTo(0, 0);
  }, []);

  const handleSelection = (value: string) => {
    console.log("Selected:", value);
    setValue(value);
    setSelection("activity", value);
    navigate("/question2"); // Korrigierter Pfad
  };

  return (
    <div className="question1-page">
      <div className="transparent-box" />
      <div className="content">
        <Typography variant="h4" className="title">
          Worauf hast du heute Lust?
        </Typography>

        <div className="icon-grid">
          {options.map((option, index) => (
            <div key={index} className="icon-box" onClick={() => handleSelection(option.value)}>
              <div className="icon">{option.icon}</div>
              <Typography className="icon-label">{option.label}</Typography>
            </div>
          ))}
        </div>

        <Typography variant="caption" className="slogan">
          Deine Angaben werden nicht gespeichert – jede Sitzung ist einzigartig!
        </Typography>
      </div>
    </div>
  );
};

export default QuestionPage1;
