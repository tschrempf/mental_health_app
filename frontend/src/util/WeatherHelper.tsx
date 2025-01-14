import { WeatherData } from "../types/Weather";

/**
 * Getter for the background image based on the weather data.
 * If the weather data is null, the unknown background image is returned.
 *
 * @param weatherData The weather data to get the background image for.
 * @returns The path to the background image.
 * @public
 */
export const getBackgroundImage = (weatherData: WeatherData | null) => {
  if (!weatherData) {
    return "/backgroundImages/unknown.png";
  }
  return `/backgroundImages/${weatherData.weather.toLowerCase()}.png`;
};
