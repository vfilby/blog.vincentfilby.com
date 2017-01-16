(function($) {
	"use strict";

	$(document).ready(function() {
		BackgroundCheck.init({
			targets: '.fn-item',
			images: '.post-holder'
		});

		var $bgobj = $("#ph-me"); // assigning the object

		$(window).scroll(function() {
			if ($(window).width() > 1130) {

				var yPos = -($(window).scrollTop() / 5) - 150;

				// Put together our final background position
				var coords = '50% ' + yPos + 'px';

				// Move the background
				$bgobj.css({
					backgroundPosition: coords
				});
			}
		});
	});
}(jQuery));
