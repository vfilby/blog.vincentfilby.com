+++
title = "Bias FX on an iPad with ToneLab LE"
date = "2017-01-10"
tags = ['Music', 'Bias FX', 'Guitar']
arcs = ['Bias FX']
description = "Setting up an electric guitar rig with only an iPad, Bias FX and a Vox Tonelab LE" 
+++
It's been awhile since I kept my guitar amps out and ready for use.  Digital sound modelling is pretty good so they sit stowed away in storage and I have been contemplating getting rid of them for years.  

I used main stage for awhile in conjunction with a midi capable floor board but more recently I have been playing with [Bias FX by Postive Grid](https://www.positivegrid.com/bias-fx/), an iPad app that does everything I need and it sounds pretty good.

### Wiring

To make this all work I use:

* **Apogee Jam 96k** I have an old One as well but it draws too much power from USB to work properly.  
* **A Vox ToneLab LE** This has been a gem for me over the years.  It is a multi effects pedal in and of itself but it also has midi in/out so you can use it to control other systems.  The bonus is that it has an expression pedal *with* a toggle switch like a wah.  That gives you the ability to use the expression effect without leaving preset mode.  In FX mode you have effectively 6 switches to play with (the expression toggle will always be one of these).
* **x-eMu** USB → Midi cable
* A decent powered speaker--I use a Bose SoundLink III--but anything should do.  If you try to use the iPad's speakers you are going to lose a lot of the sound quality that Bias FX provides.

The trick is to use the USB 3.0 camera adapter and connect it to a small USB hub.  From there you can plug in both the Jam and the USB Midi cable (yes the Jam can use lightning directly, but USB is better for sharing).  By using the USB 3.0 adapter you can also supply power from a lightning cable to keep the iPad alive longer.

![]( {{< localresource "asset.jpg" >}})

### Configuring Midi

The Vox ToneLab LE has two modes: 1) preset mode where you select preconfigured sounds, and 2) FX mode where you can control various parts of the current preset.  Preset mode works out of the box and controls Bias FX in exactly the way you'd expect by switching presets and banks.  FX mode also works but you have to configure the global or preset midi settings. 

The most obvious way to setup midi in Bias FX is through the settings, but that only lets you configure global settings and only certain functions like toggling effects or system things like Tap Temp or Tuner.  The more useful and less obvious way is to press and hold on the thing you want to set.  For example, press and hold on the light of an effect (or the switch) and it will pop up a window that lets you set or learn the midi.  This also works with expression based pedals like volume or wah  (and it works with dials).

Couple things you'll need to do: configure one generic preset on the ToneLab (I set the switch under the expression pedal to control toggling modulation and control as a tap tempo with the rest at defaults).  Write this preset into as many presets as you use in Bias, that way you'll have consistent midi control regardless of the preset.

### Conclusion

Overall I like the setup, it is very versatile easy to setup/pack and very portable. So far I have switched entirely from using Mainstage to using Bias FX for my day to day playing.

The floorboard & midi integration makes this just as usable as my previous amp/effect configuration.

### Sounds

{{< clyp s20cdyaa >}}

{{< clyp wuxp5ljo >}}

{{< clyp 3dsl15sn >}}
