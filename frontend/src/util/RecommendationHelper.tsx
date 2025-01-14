import { CardType } from "../types/Card";
import { RecommendationType } from "../types/Recommendation";

export const mapRecommendationToCard = (recommendation: RecommendationType[]): CardType[] => {
  return recommendation.map((recommendation) => {
    return {
      title: recommendation.activity,
      text: recommendation.description,
      imageUrl: recommendation.media.find((media) => isImage(media)) || "",
      videoUrl: recommendation.media.find((media) => isYoutubeVideo(media)) || "",
      resourceLinks: recommendation.media.filter((media) => !isImage(media) && !isYoutubeVideo(media)),
    } as CardType;
  });
};

const isImage = (url: string) => {
  const imageRegex = /\.(?:jpeg|png|gif|bmp|webp|tiff?|ico|svg|avif|jpg)(?:\?.*)?$/i;
  return imageRegex.test(url);
};

const isYoutubeVideo = (url: string) => {
  return url.includes("youtube");
};
