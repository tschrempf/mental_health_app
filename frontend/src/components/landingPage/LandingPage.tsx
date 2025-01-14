import "./LandingPage.css";
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { Typography, Button, TextField } from "@mui/material";

const LandingPage = () => {
  const [name, setName] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    window.scrollTo(0, 0);
  }, []);

  return (
    <div className="landing-page">
      <div className="content">
        <img src="/public/brightenUp.png" alt="Brighten" style={{ marginBottom: "-8%", marginTop: "-3%" }} />
        <Typography
          variant="h3"
          className="title"
          sx={{
            fontWeight: "bold",
            fontSize: { xs: "5vw", sm: "4vw", md: "3vw", lg: "2.6vw" },
            textAlign: "center",
            marginBottom: "3%",
            marginTop: "3%",
          }}
        >
          Tipps und Inspirationen <br />
          für deine mentale Gesundheit
        </Typography>
        <Typography
          variant="body1"
          sx={{
            marginBottom: "4%",
            fontSize: "1rem",
            color: "#666",
          }}
        >
          Abgestimmt auf deine Stimmung, Präferenzen und das lokale Wetter.
        </Typography>
        <TextField
          label="Dein Name (optional)"
          variant="outlined"
          fullWidth={true}
          className="name-input"
          value={name}
          autoComplete="off"
          onChange={(e) => setName(e.target.value)}
        />
        <Button
          variant="contained"
          sx={{
            backgroundColor: "#6B9AC4",
            color: "#fff",
            padding: { xs: "1rem 2rem", sm: "1rem 2.5rem", md: "1vh 3vw" },
            borderRadius: "0.6vw",
            fontSize: { xs: "1rem", sm: "1.2rem", md: "1.4vw" },
            transition: "background-color 0.3s ease",
            marginTop: "5%",
            marginBottom: "5%",
            "&:hover": {
              backgroundColor: "#2c387e",
            },
          }}
          onClick={() => navigate("/question1", { state: { name } })}
        >
          Weiter
        </Button>
        <Typography variant="caption" className="slogan1">
          Deine Angaben werden nicht gespeichert - jede Sitzung ist einzigartig!
        </Typography>
      </div>
    </div>
  );
};

export default LandingPage;
