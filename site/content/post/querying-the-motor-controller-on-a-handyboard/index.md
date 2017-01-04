+++
title = "Querying the motor controller on a handyboard"
date = "2005-08-04T17:09:00Z"
tags = []
galleryprefix = ""
gallerythumbnailprefix = ""
+++

I have written a small library to query the status of the motors and it can be
downloaded below.

## On/Off and Direction

There are many built in functions in interactive c to set the motor speed and
direction; however, once it has been set there is no built in functionality to
query the status of the motors. It is a relatively easy process to get the
status by looking at the motor controller status byte 0x0e. The status byte (8
bits) uses the top 4 bits to turn the motors on and off and the bottom 4 bits
to set direction. So by looking at the byte: `poke( 0x0e )` we can see what
motors are set and which direction they are turning. By some simple bit
shifting and masking you can easily determine the state of any given motor.

## Getting Motor Speed

Getting the motor speed requires using the data that controlles the Pulse
Width Modulation (PWM) algorithms on the Handyboard. The speeds for motors 0 -
3 are, respectively, 0x22, 0x23, 0x24 and 0x25. By grabbing the value stored
at that memory location you can get the speed the motor is set to. The built
in functions let you control the speed using a range of 0 - 100 (in both
forward and backward directions) but a stock Handyboard only gives 7
graduations of control. The 7 speeds are denoted by the 7 following bit
patterns:

  * 0b00000000
  * 0b00010001
  * 0b01001001
  * 0b01010101
  * 0b01010111
  * 0b01110111
  * 0b01111111
  * 0b11111111

These two functions make up the library that I wrote for querying the motor
controller. Feel free to use it, abuse it and give it to your friends.

{{< gist vfilby 835575 >}}

