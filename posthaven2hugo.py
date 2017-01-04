#!/usr/bin/env python
import os
import re
import json
import urllib
import html2text
from collections import OrderedDict
from lxml import html
from lxml import etree

posthaven_dir = "./posthaven-posts"
hugo_output = "./site/content/post/"
#image_output = "./site/static/img/" Not used since I switched to subdir posts


# Taken from http://stackoverflow.com/a/600612/119527
def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        # if exc.errno == errno.EEXIST and os.path.isdir(path):
        #     pass
        # else: raise
        pass
        

def handle_youtube_links( root_element ):
    youtube_iframes = root_element.xpath( "//iframe[contains(@src, 'youtube')]")
    for iframe in youtube_iframes:
        src = iframe.get('src')
        m = re.search( "embed/(?P<id>[A-Za-z0-9_-]+)", src )
        #print src, m.group("id")
        iframe.tail = "{{{{< youtube {0} >}}}}".format( m.group("id") )
        iframe.drop_tree()
        
def handle_gists( root_element ):
    gists = root_element.xpath( "//script[contains( @src, 'gist.github')]")
    for gist in gists:
        src = gist.get('src')
        m = re.search( "/(?P<id>[0-9]+)\.js", src)
        print src, m.group("id")
        gist.tail = "{{{{< gist vfilby {0} >}}}}".format( m.group("id") )
        gist.drop_tree()
        
def download_and_relink_images( root_element, post_path ):
    # Each "image" in posthaven is a gallery even if it is a single image.  
    # So we look at each gallery individually, if it is a single we'll treat it
    # as a single image and if there is more than one we'll treat it as a gallery
    print "post_path:", post_path
    cars = root_element.xpath( "//div[@class='posthaven-gallery-car']")
    print " > Found {0} galleries...".format( len(cars) )
    for car in cars:
        print " > Gallery ", car
        cdr = car.getnext()
        
        #print "car", etree.tostring( car )
        #print "cdr", etree.tostring( cdr )

        car_images = car.xpath( ".//*[@data-orig-src]/@data-orig-src" )
        cdr_images = cdr.xpath( ".//*[@data-orig-src]/@data-orig-src" )
        
        # If there is only one then cdr is empty, otherwise the head image
        # is duplicated in car and cdr.
        
        images = list(OrderedDict.fromkeys(car_images + cdr_images))
        print " > ", images
        
        # Fetch the images
        for image in images:
            image_filename = os.path.basename( image )
            image_dest = os.path.join( post_path, image_filename )
            print " > Retrieving asset", image
            print "    -> {0}".format( image_dest )
            #urllib.urlretrieve( image, image_dest )
        
        if len( images ) == 1:
            #single image
            print " > converting single image..."
            image_filename = os.path.basename( image )
            print " > image_filename: ", image_filename
            web_abs_path = os.path.join( "/", post_path[post_path.index('post'):], image_filename )
            print " > web_abs_path: ", web_abs_path
            
            img_element = car.xpath( ".//img[@class='posthaven-gallery-image']")[0]
            img_element.attrib['src'] = web_abs_path
            
            # Since we modified the car, keep it.
            cdr.drop_tree()
            
        if len( images) > 1:
            #gallery 
            print " > converting gallery..."
            gallery_content = "{{< gallery >}}\n"
            for image in images:
                image_filename = os.path.basename( image )
                gallery_content += """{{{{% galleryimage file="{0}" title="{1}" caption="{2}"%}}}}\n""".format( image_filename, "", "" )
            gallery_content += "{{< /gallery >}}"
            
            cdr.tail = gallery_content
        
            # Trash the posthaven gallery html
            cdr.drop_tree()
            car.drop_tree()
        
def main():
    for filename in os.listdir(posthaven_dir):
        filepath = os.path.join( posthaven_dir, filename )
        post_path = os.path.join( hugo_output, filename )
        target_filepath = os.path.join( post_path, "index.md" )

        mkdir_p( post_path )

        print "Parsing ", filepath
        tree = html.parse( filepath )

        # Extract post metadata
        title = tree.xpath('//meta[@property="og:title"]/@content' )[0]
        date = tree.xpath('//div[@class="actual-date posthaven-timezone-string"]')[0].get("data-posthaven-date-utc-iso8601")
        tags = tree.xpath('//section[@class="tag-list"]/ul/li/a/text()')
        
        # Handle assets and special posthave widgets
        handle_youtube_links( tree )
        handle_gists( tree )
        download_and_relink_images( tree, post_path )
        image_assets = tree.xpath('//meta[@property="og:image"]/@content')
        #print image_assets
        
        # Convert HTML to markdown
        content = etree.tostring( tree.xpath('//div[@class="post-body"]')[0], pretty_print=True )
        #print content
        markdown_content = html2text.html2text(content)
        
        # Short codes are urlencoded, we need to undo that so they function as expected
        markdown_content = markdown_content.replace( "{{&lt;", "{{<" )
        markdown_content =  markdown_content.replace( "&gt;}}", ">}}" )
        #print markdown_content
        
        # Originally just a dumped json object, but hugo didn't playwell with unformated json
        frontmatter = """+++
title = "{0}"
date = "{1}"
tags = {2}
galleryprefix = ""
gallerythumbnailprefix = "t190_"
+++\n""".format( title.replace('"','\\"'), date, tags )
        
        print "Writing", target_filepath

        target = open( target_filepath, "w" )
        target_content = frontmatter + "\n" + markdown_content
        target.write( target_content.encode( "ascii", "ignore" ) )
        target.close()
        
# instagram mostly works but is a little broken.
# only run galleria when there is a gallery on the page

if __name__ == '__main__':
    main()
    