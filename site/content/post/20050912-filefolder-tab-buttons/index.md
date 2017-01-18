+++
title = "Filefolder Tab Buttons"
date = "2005-09-12"
categories = ['Technology', 'Tutorials']
tags = []
arcs = ['Filefolder Tabs']
+++

To get started open photoshop and a new blank document. It is a good idea to make the document bigger than you need, you can always shrink images but you can't always enlarge them. Work big then scale down.

![]({{< localresource "pentagon.png" >}})

The first step is to get the general shape of the tab on the screen. It would be possible to draw a path in the shape of the tab, but the outline would be inconsistent and hard to make look good. Instead use the pentagon shape that is a preset of the pen tool. Press 'd' to reset your colours to black foreground and white background. Now click near the center of the document and drag outwards and down. Align the float side up, it helps to hold shift while dragging because it locks the shape so the line is horizontal.

![]({{< localresource "black-pentagon.png" >}})

The pentagon is defined with a vector mask in photoshop, right click on the layer in the layers palette and click rasterize. This discards the vector mask and creates a representation of the shape that can be editted. Now use the marquee selection tool to select the lower half of the image and fill it in with black. The edge of the pentagon will be slight grey so make sure you fill that with black as well.

![]({{< localresource "black-square-tab.png" >}})

By this point you should have a tab looking object that is made of straight lines and sharp angles. Real tabs are curved so these must be as well. To round the edges you will first blur the image slightly with gaussian blur. I would recommend using a radius of 5.5 to get a nice curvature but you may need to tailor that depending on the image size you are using.

![]({{< localresource "blurred-tab.png" >}})

Now that it has been blurred we can use levels command-l (ctrl-l) toconvert the blurriness to a nice smooth curve. It is important to note that this step requires the black blurred object to be on a white background. If you don't have a white background: add a new layer beneath the object layer and ensure it is filled with white. Now click on the object layer and press command-e (ctrl-e) to merge it with the layer beneath it.

![]({{< localresource "levels.png" >}})

Open the levels dialogue and bring the black and white markers close to each other. Note that if you bring them right together the line will look alittle jaggy, you want to keep them apart slightly to retain some of the blur and give the curve a smooth look

![]({{< localresource "smooth-tab.png" >}})

Final Thoughts

At this point you have the outline of a tab defined in black and white, you can use this image make selections and and the appropriate graphics. I just wanted the outline so I used the wand to select the black portion then I shrunk the selection by 2 pixels (select > modify > contract) and filled it with white.

![]({{< localresource "tab-outline.png">}})

This outline can be copied a few times and combined to give more tabs. You will need to set the layer blending mode to darken so the black shows through for each layer. You will also need to manually earse some of the lines to make it look realistic.

![]({{< localresource "tab-final.png" >}})

Whether you use the outline or use the black/white mask to make give them a different look, it is time to add the finishing touches. For my tabs I just added a slight gradient inside the tab, grey normally but orange on roll-over. I also have me setup to have the current tab forward, this is alittle tricky and should be left for another day. 



