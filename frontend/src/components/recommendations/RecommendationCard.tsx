import React from "react";
import { CardType } from "../../types/Card";
import "./RecommendationCard.css";

const Card: React.FC<CardType> = ({ title, text, imageUrl, resourceLink, videoUrl, className }) => {
  return (
    <div className={`${className} card`} style={{ height: "400px", overflow: "hidden" }}>
      <h2 className="card-title">{title}</h2>
      <p className="card-text">{text}</p>
      {imageUrl && (
        <div className="media-container">
          <img src={imageUrl} alt={title} className="card-image" style={{ maxHeight: "100%" }} />
        </div>
      )}
      {resourceLink && (
        <div className="media-container">
          <a href={resourceLink} target="_blank" rel="noopener noreferrer" className="card-link">
            Weitere Infos
          </a>
        </div>
      )}
      {videoUrl && (
        <div className="media-container">
          <iframe
            src={videoUrl}
            allowFullScreen
            height="150"
            width="100%"
            title="YouTube video player"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
            referrerPolicy="strict-origin-when-cross-origin"
          ></iframe>
        </div>
      )}
    </div>
  );
};

export default Card;
