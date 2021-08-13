$(document).ready(function() {

    let position = 0;
    const slidesToShow = 3;
    const slidesToScroll = 2;
    const container = $('.slider-container');
    const track = $('.slider-track');
    const item = $('.slider-item');
    const btnPrev = $('.btn-prev');
    const btnNext = $('.btn-next');
    const itemWidth = container.width() / slidesToShow;

    item.each(function (index, item) {
        $(item).css ({
            minWidth: itemWidth,
        });
    });

    

});
