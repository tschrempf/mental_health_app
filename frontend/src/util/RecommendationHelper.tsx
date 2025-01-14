import { CardType } from "../types/Card";
import { RecommendationType } from "../types/Recommendation";

/**
 * Maps the backend given recommendations to the card type.
 * The recommendation is mapped to a card type with the title, text, image, video, and resource links.
 *
 * @param recommendations The recommendations given by the backend.
 * @returns The mapped recommendations as cards.
 * @public
 */
export const mapRecommendationToCard = (recommendations: RecommendationType[]): CardType[] => {
  return recommendations.map((recommendation) => {
    return {
      title: recommendation.activity,
      text: recommendation.description,
      imageUrl: recommendation.media.find((media) => isImage(media)) || "",
      videoUrl: recommendation.media.find((media) => isYoutubeVideo(media)) || "",
      resourceLinks: recommendation.media.filter((media) => !isImage(media) && !isYoutubeVideo(media)),
    } as CardType;
  });
};

/**
 * Checks if the given URL is an image.
 * The URL is checked if it is an image based on the image regex.
 * It accepts the following image formats: jpeg, png, gif, bmp, webp, tiff, ico, svg, avif, jpg.
 *
 * @param url The URL to check.
 * @returns True, if the URL is an image, false otherwise.
 */
const isImage = (url: string) => {
  const imageRegex = /\.(?:jpeg|png|gif|bmp|webp|tiff?|ico|svg|avif|jpg)(?:\?.*)?$/i;
  return imageRegex.test(url);
};

/**
 * Checks if the given URL is a YouTube video.
 * The URL is checked if it is a YouTube video wether it contains the word 'youtube'.
 *
 * @param url The URL to check.
 * @returns True, if it is a YouTube video, false otherwise.
 */
const isYoutubeVideo = (url: string) => {
  return url.includes("youtube");
};
