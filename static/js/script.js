$(document).ready(function() {
    let position = 0;
    let c = 0
    const slidesToShow = 1;
    const slidesToScroll = 1;
    const container = $('.slider-container');
    const track = $('.slider-track');
    const item = $('.slider-item');
    const itemsCount = item.length;
    const itemWidth = container.width() / slidesToShow;
    const movePosition = slidesToScroll * itemWidth;
    let timerId = setInterval(() => Next(), 6000);
    item.each(function (index, item) {
        $(item).css ({
            minWidth: itemWidth,
        });
    });
    const setPosition = () => {
        track.css({
            transform: `translateX(${position}px)`
        });
    };
    const Prev = () => {
        position += movePosition * itemsCount; 
        setPosition();
    };
    const Next = () => {
        if (position <= (-(itemsCount - slidesToShow) * itemWidth)) {
            Prev();
          }
        position -= movePosition; 
        setPosition();
    };
});
