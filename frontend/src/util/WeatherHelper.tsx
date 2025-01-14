import { WeatherData } from "../types/Weather";

export const getBackgroundImage = (weatherData: WeatherData | null) => {
  if (!weatherData) {
    return "public/backgroundImages/unknown.png";
  }
  return `public/backgroundImages/${weatherData.weather.toLowerCase()}.png`;
};
