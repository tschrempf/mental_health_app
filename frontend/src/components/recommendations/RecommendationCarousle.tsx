import RecommendationCard from "./RecommendationCard";
import { CardType } from "../../types/Card.d";
import ArrowBackIosNewRoundedIcon from "@mui/icons-material/ArrowBackIosNewRounded";
import ArrowForwardIosRoundedIcon from "@mui/icons-material/ArrowForwardIosRounded";
import { useState } from "react";

import "./RecommendationCarousel.css";

interface CardCarouselProps {
  cards: CardType[];
}

const CardCarousel = ({ cards }: CardCarouselProps) => {
  // save state of current slide
  const [slide, setSlide] = useState(1);

  // function to move to next slide
  const nextSlide = () => {
    if (slide === cards.length - 1) {
      setSlide(0);
      return;
    }
    setSlide(slide + 1);
  };

  // function to move to previous slide
  const prevSlide = () => {
    if (slide === 0) {
      setSlide(cards.length - 1);
      return;
    }
    setSlide(slide - 1);
  };

  // function to select a slide based on the index
  const selectVisibleSlide = (index: number) => {
    setSlide(index);
  };

  // function to decide if the card should be visible based on the index
  const getSlideClassName = (currentIndex: number): string => {
    if (slide === currentIndex || slide === currentIndex - 1 || slide === currentIndex + 1) {
      return "slide";
    } else {
      return "hidden-slide";
    }
  };

  // function to decide if the indicator should be active or inactive based on the index
  const getIndicatorClassName = (currentIndex: number): string => {
    const indicatorClassNames = ["indicator"];
    if (slide !== currentIndex) {
      indicatorClassNames.push("indicator-inactive");
    }
    return indicatorClassNames.join(" ") as string;
  };

  // render the carousel
  return (
    <div className="carousel">
      <ArrowBackIosNewRoundedIcon className="carousel-arrow arrow-left" onClick={prevSlide} />
      {cards.map((card, index) => (
        <RecommendationCard
          title={card.title}
          text={card.text}
          imageUrl={card?.imageUrl}
          resourceLink={card?.resourceLink}
          videoUrl={card?.videoUrl}
          className={getSlideClassName(index)} // decide dynamically if the card should be visible based on the index
        />
      ))}
      <ArrowForwardIosRoundedIcon className="carousel-arrow arrow-right" onClick={nextSlide} />
      <span className="indicators">
        {cards.map((_, index) => (
          <button className={getIndicatorClassName(index)} key={index} onClick={() => selectVisibleSlide(index)} />
        ))}
      </span>
    </div>
  );
};

export default CardCarousel;
