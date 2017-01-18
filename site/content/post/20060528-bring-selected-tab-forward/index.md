+++
title = "PHP Snippet: Bring Selected Tab Forward"
date = "2006-05-28"
tags = []
category = ['Tech']
arcs = ['Filefolder Tabs']
+++

When I first published my photoshop tutorial for creating quick filefolder style tab buttons, many people asked how I always made the selected tab appear to be in front of the others.

Unfortunately there is no easy way to accomplish this with straight html or css. The reason this is complex is because you are not only altering the selected tab, but the tabs on either side as well. You might be able to get away with this if you ditch the highlighting that I used and just have the tab outline.

To make the selected tab come first I used the following php snippet:


{{< highlight php >}}
<div id="links">
<?
  if( is_array( $primary_links ) ) {
    $classes = array();
    for( $i = sizeof( $primary_links ); $i >  0; $i-- ) {
        $classes[$i] = "";
    }
    $page = substr( $_SERVER['REQUEST_URI'], 1 );
    for( $i = sizeof( $primary_links ) ; $i >  0; $i-- ) {
      if( $primary_links["1-$i-active"] != "" ) {
        $primary_links["1-$i"] = $primary_links["1-$i-active"];
        if( $i == 1 ) {
          $classes[$i+1] .= "behind ";
          $classes[$i] .= "selected-first";
        } elseif( $i == sizeof( $primary_links ) ) {
          $classes[$i] .= "selected-last";
          $classes[$i-1] .= "before ";
        } else {
          $classes[$i+1] .= "behind ";
          $classes[$i] .= "selected ";
          $classes[$i-1] .= "before ";
        }
      } else {
        if( $i == sizeof( $primary_links ) ) {
          $classes[$i] .= "last ";
        }
        if( $i == 1 ) {
          $classes[$i] .= "first ";
        }
      }
    }
    print "<ul>";
    for( $i = sizeof( $primary_links ) + 1; $i >  0; $i-- ) {
      print "<li class=\"$classes[$i]\">" . $primary_links["1-$i"] . "</li>\n";
    }
    print "</ul>";
  } ?>
</div>
{{< /highlight >}}