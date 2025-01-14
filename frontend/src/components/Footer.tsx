import { Box, Typography, Link, IconButton } from "@mui/material";
import { Link as RouterLink } from "react-router-dom";
import InstagramIcon from "@mui/icons-material/Instagram";
import LinkedInIcon from "@mui/icons-material/LinkedIn";
import YouTubeIcon from "@mui/icons-material/YouTube";

const Footer = () => {
  return (
    <Box
      sx={{
        backgroundColor: "#FFFFFF",
        color: "#666",
        padding: "1.25rem 0",
        width: "100%",
        display: "flex",
        flexDirection: { xs: "column", md: "row" }, // Responsive layout
        justifyContent: "space-between",
        alignItems: { xs: "center", md: "center" },
        fontFamily: "Arial, sans-serif",
      }}
    >
      {/* Copyright-Text */}
      <Typography
        variant="body1"
        sx={{
          marginLeft: { xs: "0", md: "1.25rem" },
          marginBottom: { xs: "0.625rem", md: "0" },
          textAlign: { xs: "center", md: "left" },
          fontFamily: "Arial, sans-serif",
        }}
      >
        © 2025 BrightenUp
      </Typography>

      {/* Navigation */}
      <Box
        sx={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          gap: "0.5rem",
          flexWrap: { xs: "wrap", md: "nowrap" },
          marginBottom: { xs: "0.625rem", md: "0" },
        }}
      >
        <Link component={RouterLink} to="/" color="#666" underline="hover" sx={{ fontFamily: "Arial, sans-serif" }}>
          Startseite
        </Link>
        <Typography variant="body1" sx={{ color: "#2c387e", fontSize: "1rem" }}>
          •
        </Typography>
        <Link color="#666" underline="hover" sx={{ fontFamily: "Arial, sans-serif" }}>
          Über uns
        </Link>
        <Typography variant="body1" sx={{ color: "#2c387e", fontSize: "1rem" }}>
          •
        </Typography>
        <Link color="#666" underline="hover" sx={{ fontFamily: "Arial, sans-serif" }}>
          Impressum
        </Link>
      </Box>

      {/* Social Media Icons */}
      <Box
        sx={{
          display: "flex",
          gap: "0.5rem",
          justifyContent: { xs: "center", md: "flex-end" },
          marginRight: { xs: "0", md: "1.25rem" },
        }}
      >
        <IconButton
          component="a"
          href="https://www.instagram.com"
          target="_blank"
          rel="noopener noreferrer"
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
          <InstagramIcon fontSize="large" />
        </IconButton>
        <IconButton
          component="a"
          href="https://www.linkedin.com"
          target="_blank"
          rel="noopener noreferrer"
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
          <LinkedInIcon fontSize="large" />
        </IconButton>
        <IconButton
          component="a"
          href="https://www.youtube.com"
          target="_blank"
          rel="noopener noreferrer"
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
          <YouTubeIcon fontSize="large" />
        </IconButton>
      </Box>
    </Box>
  );
};

export default Footer;
