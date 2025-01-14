import { AppBar, Toolbar, IconButton, Box } from "@mui/material";
import { Link as RouterLink } from "react-router-dom";
import HomeIcon from "@mui/icons-material/Home";
import FeedbackIcon from "@mui/icons-material/Feedback";

const Header = () => {
  return (
    <AppBar
      position="sticky"
      sx={{
        backgroundColor: "#FFFFFF",
        color: "#6B9AC4",
        boxShadow: "none",
        borderBottom: "1px solid #6B9AC4",
      }}
    >
      <Toolbar>
        {/* Spacer to center content */}
        <Box sx={{ flexGrow: 1 }} />

        {/* Home-Button */}
        <IconButton
          component={RouterLink}
          to="/"
          aria-label="home"
          sx={{
            backgroundColor: "#6B9AC4",
            color: "#FFFFFF",
            padding: "0.40625rem",
            borderRadius: "0.3125rem",
            marginRight: "0.625rem",
            transition: "background-color 0.3s ease",
            "&:hover": {
              backgroundColor: "#2c387e",
              color: "#EEEEEE",
            },
          }}
        >
          <HomeIcon
            fontSize="large"
            sx={{
              transition: "color 0.3s ease",
            }}
          />
        </IconButton>

        {/* Feedback-Button as Icon */}
        <IconButton
          component={RouterLink}
          to="/feedback"
          aria-label="feedback"
          sx={{
            backgroundColor: "#6B9AC4",
            color: "#FFFFFF",
            padding: "0.40625rem",
            borderRadius: "0.3125rem",
            transition: "background-color 0.3s ease",
            "&:hover": {
              backgroundColor: "#2c387e",
              color: "#EEEEEE",
            },
          }}
        >
          <FeedbackIcon
            fontSize="large"
            sx={{
              transition: "color 0.3s ease",
            }}
          />
        </IconButton>
      </Toolbar>
    </AppBar>
  );
};

export default Header;
