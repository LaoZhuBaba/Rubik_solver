#!/usr/bin/python
# -*- coding: utf-8 -*-
from display import mf
from rubik_class import Rubik as rc
from data_def import CLOCKWISE, ANTICLOCKWISE, X_LEFT

def solve_layer1_edges():
    mf.message( "Top centre piece appears to be: %d with colour: %s" % ( rc.relative_cube[ 8 ], rc.COLOUR_DESCRIPTIONS[ rc.get_colour( 8 ) ] ) )
    mf.message( "The top seems to be centred with colour: %s" %  ( rc.COLOUR_DESCRIPTIONS[ rc.get_colour( 8 ) ] ) )
    good_edges = rc.get_edges_of_colour( 8, rc.get_colour( 8 ) )
    for e in good_edges:
        mf.message( "This edge piece seems to have the right colour %d" % ( e ) )
    count = 0
    if ( len( good_edges ) != 0 ):
        mf.message( "It looks like at least one edge of the right colour is present on top" )
        while ( rc.get_colour( 5 ) != rc.get_colour( 8 ) ):
            rc.rotate_cube( X_LEFT )
        mf.message( "We should have a good coloured edge at position 5" )
        while ( rc.get_colour( 19 ) != rc.get_colour( 26 ) ):
            rc.rotate_horizontal_middle( X_LEFT )
        mf.message( "And now the edge at position 5 should match on both colours" )
    else:
        mf.message( "It looks like no edges of the right colour are present on top" )

    # Reaching here means that if there are edge squares of the correct colour on top
    # then one should be at the top front.
    # We should now rotate the horizontal middle so that the top front edge matches
    # the correct centre colour at front as well as top.
    # MARK #1
    mf.message( "Reached MARK #1. len(good_edges) = %d." % ( len(good_edges) )  )
    count = 0
    while ( ( len( rc.get_edges_of_colour( 8, rc.get_colour( 8 ) ) ) ) < 4 ):
        mf.message( "Length of good_edges is: %d" % ( len( good_edges ) ) )
        if ( count > 40 ):
            mf.message( "count is too high.  Breaking from loop" )
            break
        count += 1
        while ( rc.get_colour( 8 ) == rc.get_colour( 3 ) ):
            mf.message( "while loop 2" )
            rc.rotate_cube( X_LEFT )
        mf.message( "Square 3 should not be the right colour" )
        # At this point we should have a top right edge of the wrong colour which can be swapped out
        while ( rc.get_colour( 46 ) == rc.get_colour( 8 ) ):
            if ( rc.get_colour( 32 ) == rc.get_colour( 35 ) ):
                rc.rotate_edge( 35, CLOCKWISE )
                rc.rotate_edge( 35, CLOCKWISE )
                break
            else:
                rc.rotate_top_2_layers( CLOCKWISE )
        while ( rc.get_colour( 48 ) == rc.get_colour( 8 ) ):
            if ( rc.get_colour( 41 ) == rc.get_colour( 44 ) ):
                rc.rotate_edge( 44, CLOCKWISE )
                rc.rotate_edge( 44, CLOCKWISE )
                break
            else:
                rc.rotate_top_2_layers( CLOCKWISE )

        while ( rc.get_colour( 50 ) == rc.get_colour( 8 ) ):
            if ( rc.get_colour( 14 ) == rc.get_colour( 17 ) ):
                rc.rotate_edge( 17, CLOCKWISE )
                rc.rotate_edge( 17, CLOCKWISE )
                break
            else:
                rc.rotate_top_2_layers( CLOCKWISE )

        while ( rc.get_colour( 52 ) == rc.get_colour( 8 ) ):
            if ( rc.get_colour( 23 ) == rc.get_colour( 26 ) ):
                rc.rotate_edge( 26, CLOCKWISE )
                rc.rotate_edge( 26, CLOCKWISE )
                break
            else:
                rc.rotate_top_2_layers( CLOCKWISE )
        if ( rc.get_colour( 21 ) == rc.get_colour( 8 ) ):
            mf.message( "matched at 21" )
            # The next if section ensures that piece we are putting into the top layer also matches on its other edge
            if ( rc.get_colour( 34 ) != rc.get_colour( 35 ) ):
                rc.rotate_edge( 35, ANTICLOCKWISE )
                rc.rotate_edge( 53, ANTICLOCKWISE )
                rc.rotate_edge( 35, CLOCKWISE )
            else:
                rc.rotate_edge( 35, CLOCKWISE )
            continue
        elif ( rc.get_colour( 43 ) == rc.get_colour( 8 ) ):
            mf.message( "matched at 43" )
            # The next if section ensures that piece we are putting into the top layer also matches on its other edge
            if ( rc.get_colour( 30 ) != rc.get_colour( 35 ) ):
                rc.rotate_edge( 35, CLOCKWISE )
                rc.rotate_edge( 53, CLOCKWISE )
                rc.rotate_edge( 35, ANTICLOCKWISE )
            else:
                rc.rotate_edge( 35, ANTICLOCKWISE )
        elif ( rc.get_colour( 23 ) == rc.get_colour( 8 ) ):
            mf.message( "matched at 23" )
            rc.rotate_edge( 26, ANTICLOCKWISE )
            rc.rotate_edge( 35, ANTICLOCKWISE )
            rc.rotate_edge( 26, CLOCKWISE )
            rc.rotate_edge( 35, CLOCKWISE )
        elif ( rc.get_colour( 25 ) == rc.get_colour( 8 ) ):
            mf.message( "matched at 25" )
            rc.rotate_edge( 17, CLOCKWISE )
            rc.rotate_edge( 53, CLOCKWISE )
            rc.rotate_edge( 17, ANTICLOCKWISE )
        elif ( rc.get_colour( 39 ) == rc.get_colour( 8 ) ):
            mf.message( "matched at 39" )
            rc.rotate_edge( 17, ANTICLOCKWISE )
            rc.rotate_edge( 53, ANTICLOCKWISE )
            rc.rotate_edge( 17, CLOCKWISE )
        elif ( rc.get_colour( 12 ) == rc.get_colour( 8 ) ):
            mf.message( "matched at 12" )
            rc.rotate_edge( 26, ANTICLOCKWISE )
            rc.rotate_edge( 53, CLOCKWISE )
            rc.rotate_edge( 26, CLOCKWISE )
        elif ( rc.get_colour( 16 ) == rc.get_colour( 8 ) ):
            mf.message( "matched at 16" )
            rc.rotate_edge( 44, CLOCKWISE )
            rc.rotate_edge( 53, CLOCKWISE )
            rc.rotate_edge( 44, ANTICLOCKWISE )
        elif ( rc.get_colour( 34 ) == rc.get_colour( 8 ) ):
            mf.message( "matched at 34" )
            rc.rotate_edge( 26, CLOCKWISE )
            rc.rotate_edge( 53, CLOCKWISE )
            rc.rotate_edge( 26, ANTICLOCKWISE )
        elif ( rc.get_colour( 30 ) == rc.get_colour( 8 ) ):
            mf.message( "matched at 30" )
            rc.rotate_edge( 44, ANTICLOCKWISE )
            rc.rotate_edge( 53, ANTICLOCKWISE )
            rc.rotate_edge( 44, CLOCKWISE )
        elif ( rc.get_colour( 19 ) == rc.get_colour( 8 ) ):
            mf.message( "matched at 19" )
            rc.rotate_edge( 26, CLOCKWISE )
            rc.rotate_edge( 35, ANTICLOCKWISE )
            rc.rotate_edge( 53, CLOCKWISE )
            rc.rotate_edge( 35, CLOCKWISE )
            rc.rotate_edge( 26, ANTICLOCKWISE )
        elif ( rc.get_colour( 37 ) == rc.get_colour( 8 ) ):
            mf.message( "matched at 37" )
            rc.rotate_edge( 44, ANTICLOCKWISE )
            rc.rotate_edge( 35, CLOCKWISE )
            rc.rotate_edge( 53, ANTICLOCKWISE )
            rc.rotate_edge( 35, ANTICLOCKWISE )
            rc.rotate_edge( 44, CLOCKWISE )
        elif ( rc.get_colour( 28 ) == rc.get_colour( 8 ) ):
            mf.message( "matched at 35" )
            rc.rotate_edge( 35, ANTICLOCKWISE )
            rc.rotate_edge( 26, CLOCKWISE )
            rc.rotate_edge( 53, ANTICLOCKWISE )
            rc.rotate_edge( 26, ANTICLOCKWISE )
            rc.rotate_edge( 35, CLOCKWISE )
        elif ( rc.get_colour( 10 ) == rc.get_colour( 8 ) ):
            mf.message( "matched at 10" )
            rc.rotate_edge( 17, CLOCKWISE )
            rc.rotate_edge( 26, ANTICLOCKWISE )
            rc.rotate_edge( 53, CLOCKWISE )
            rc.rotate_edge( 26, CLOCKWISE )
            rc.rotate_edge( 17, ANTICLOCKWISE )
        else:
            rc.rotate_edge( 53, CLOCKWISE )
            continue

    mf.message( "Reached MARK #2. len(good_edges) = %d." % ( len(good_edges) )  )
####
def solve_layer1_corners():
    count1 = 0
    flipflopflap = 0
    while( True ):
       count1 += 1
       mf.message( "Press a key.  Outer while" )
       if ( count1 > 4 ):
           mf.message( "Too many iterations on outer loop.  Exiting" )
           break
       top_colour = rc.get_colour( 8 )
       count2 = 0
       while ( not (
                       ( rc.get_colour( 6 ) == top_colour ) and ( rc.get_colour( 11 ) == rc.get_colour( 17 ) ) and
                       ( rc.get_colour( 4 ) == top_colour ) and ( rc.get_colour( 27 ) == rc.get_colour( 35 ) ) and
                       ( rc.get_colour( 0 ) == top_colour ) and ( rc.get_colour( 9 ) == rc.get_colour( 17 ) ) and
                       ( rc.get_colour( 2 ) == top_colour ) and ( rc.get_colour( 29 ) == rc.get_colour( 35 ) )
                    )
           ):
           count2 += 1
           if ( count2 > 50 ):
               mf.message( "Too many iterations.  Exiting" )
               break
           if ( rc.get_colour( 22 ) == top_colour ):
           # Front bottom right colour matches the top colour
               mf.message( "found the right colour at 22" )
               if ( rc.get_colour( 33 ) == rc.get_colour( 35 ) ):
                   # And it is a perfect match for the front top right corner.
                   mf.message( "found a match at 22" )
                   rc.rotate_edge( 26, CLOCKWISE )
                   rc.rotate_edge( 53, CLOCKWISE )
                   rc.rotate_edge( 26, ANTICLOCKWISE )
                   mf.message( "here 1" )
                   continue
               elif ( rc.get_colour( 33 ) == rc.get_colour( 26 ) ):
                   # And it is a perfect match for the front top left corner
                   mf.message( "matches on the other side so moving to top" )
                   rc.rotate_edge( 53, ANTICLOCKWISE )
                   rc.rotate_edge( 17, CLOCKWISE )
                   rc.rotate_edge( 53, CLOCKWISE )
                   rc.rotate_edge( 17, ANTICLOCKWISE )
                   mf.message( "here 2" )
                   continue
           if ( rc.get_colour( 24 ) == top_colour ):
           # Front bottom left colour matches the top colour
               mf.message( "found the right colour at 24" )
               if ( rc.get_colour( 13 ) == rc.get_colour( 17 ) ):
                   # And it is a perfect match for the front top left corner.
                   mf.message( "found a match at 24. Putting in place" )
                   rc.rotate_edge( 26, ANTICLOCKWISE )
                   rc.rotate_edge( 53, ANTICLOCKWISE )
                   rc.rotate_edge( 26, CLOCKWISE )
                   mf.message( "here 3" )
                   continue
               elif ( rc.get_colour( 13 ) == rc.get_colour( 26 ) ):
                   # And it is a perfect match for the front top right corner
                   mf.message( "matches on the other side so moving to top" )
                   rc.rotate_edge( 53, CLOCKWISE )
                   rc.rotate_edge( 35, ANTICLOCKWISE )
                   rc.rotate_edge( 53, ANTICLOCKWISE )
                   rc.rotate_edge( 35, CLOCKWISE )
                   mf.message( "here 4" )
                   continue
           if ( rc.get_colour( 33 ) == top_colour ):
           # Right side bottom left corner
               mf.message( "Right side bottom left corner" )
               if ( rc.get_colour ( 22 ) == rc.get_colour( 17 ) ):
                   mf.message( "Right side bottom left corner is a perfect match for front top left corner" )
                   rc.rotate_edge( 17, CLOCKWISE )
                   rc.rotate_edge( 53, ANTICLOCKWISE )
                   rc.rotate_edge( 17, ANTICLOCKWISE )
                   mf.message( "here 5" )
                   continue
               elif ( rc.get_colour ( 22 ) == rc.get_colour( 26 ) ):
                   mf.message( "Right side bottom left corner is a perfect match for front top right corner" )
                   rc.rotate_edge( 35, ANTICLOCKWISE )
                   rc.rotate_edge( 53, ANTICLOCKWISE )
                   rc.rotate_edge( 35, CLOCKWISE )
                   mf.message( "here 6" )
                   continue
           if ( rc.get_colour( 13 ) == top_colour ):
           # Left side bottom left corner
               mf.message( "left side bottom left corner" )
               if ( rc.get_colour ( 51 ) == rc.get_colour( 26 ) ):
                   mf.message( "Left side bottom right corner is a perfect match for front top right corner" )
                   rc.rotate_edge( 35, ANTICLOCKWISE )
                   rc.rotate_edge( 53, CLOCKWISE )
                   rc.rotate_edge( 35, CLOCKWISE )
                   mf.message( "here 7" )
                   continue
               elif ( rc.get_colour ( 24 ) == rc.get_colour( 26 ) ):
                   mf.message( "Left side bottom right corner is a perfect match for front top left corner" )
                   rc.rotate_edge( 17, CLOCKWISE )
                   rc.rotate_edge( 53, CLOCKWISE )
                   rc.rotate_edge( 17, ANTICLOCKWISE )
                   mf.message( "here 8" )
                   continue
           if ( rc.get_colour( 45 ) == top_colour ):
           # Bottom side right front corner
               mf.message( "bottom side right front corner" )
               if ( rc.get_colour ( 33 ) == rc.get_colour( 26 ) ):
                   mf.message( "Bottom right front corner is a perfect match for front top right corner" )
                   rc.rotate_edge( 35, ANTICLOCKWISE )
                   rc.rotate_edge( 53, CLOCKWISE )
                   rc.rotate_edge( 35, CLOCKWISE )
                   rc.rotate_edge( 26, CLOCKWISE )
                   rc.rotate_edge( 53, CLOCKWISE )
                   rc.rotate_edge( 53, CLOCKWISE )
                   rc.rotate_edge( 26, ANTICLOCKWISE )
                   mf.message( "here 9" )
                   continue
               elif ( rc.get_colour ( 22 ) == rc.get_colour( 26 ) ):
                   mf.message( "Bottom right front corner is a perfect match for front top left corner" )
                   rc.rotate_edge( 53, ANTICLOCKWISE )
                   rc.rotate_edge( 17, CLOCKWISE )
                   rc.rotate_edge( 53, ANTICLOCKWISE )
                   rc.rotate_edge( 17, ANTICLOCKWISE )
                   rc.rotate_edge( 26, ANTICLOCKWISE )
                   rc.rotate_edge( 53, CLOCKWISE )
                   rc.rotate_edge( 53, CLOCKWISE )
                   rc.rotate_edge( 26, CLOCKWISE )
                   mf.message( "here 10" )
                   continue
           if ( rc.get_colour( 51 ) == top_colour ):
           # Bottom side left front corner
               mf.message( "bottom side left front corner" )
               if ( rc.get_colour ( 13 ) == rc.get_colour( 26 ) ):
                   mf.message( "Bottom left front corner is a perfect match for front top left corner" )
                   rc.rotate_edge( 17, CLOCKWISE )
                   rc.rotate_edge( 53, ANTICLOCKWISE )
                   rc.rotate_edge( 17, ANTICLOCKWISE )
                   rc.rotate_edge( 26, ANTICLOCKWISE )
                   rc.rotate_edge( 53, CLOCKWISE )
                   rc.rotate_edge( 53, CLOCKWISE )
                   rc.rotate_edge( 26, CLOCKWISE )
                   mf.message( "here 11" )
                   continue
               elif ( rc.get_colour ( 24 ) == rc.get_colour( 26 ) ):
                   mf.message( "Bottom left front corner is a perfect match for front top right corner" )
                   rc.rotate_edge( 53, CLOCKWISE )
                   rc.rotate_edge( 35, ANTICLOCKWISE )
                   rc.rotate_edge( 53, CLOCKWISE )
                   rc.rotate_edge( 35, CLOCKWISE )
                   rc.rotate_edge( 26, CLOCKWISE )
                   rc.rotate_edge( 53, CLOCKWISE )
                   rc.rotate_edge( 53, CLOCKWISE )
                   rc.rotate_edge( 26, ANTICLOCKWISE )
                   mf.message( "here 12" )
                   continue

           # Left side top right corner
           if ( rc.get_colour ( 11 ) == top_colour ):
               mf.message( "left side top right corner" )
               if ( rc.get_colour( 18 ) == rc.get_colour( 17 ) ):
                   mf.message( "left side top right hand corner is a perfect match for front left top" )
                   rc.rotate_edge( 17, CLOCKWISE )
                   rc.rotate_edge( 53, CLOCKWISE )
                   rc.rotate_edge( 17, ANTICLOCKWISE )
                   rc.rotate_edge( 53, ANTICLOCKWISE )
                   rc.rotate_edge( 17, CLOCKWISE )
                   rc.rotate_edge( 53, CLOCKWISE )
                   rc.rotate_edge( 17, ANTICLOCKWISE )
                   mf.message( "here 13" )
                   continue
               elif ( rc.get_colour ( 18 ) == rc.get_colour( 26 ) ):
                   mf.message( "left side top right hand corner is a perfect match for front right top" )
                   rc.rotate_edge( 17, CLOCKWISE )
                   rc.rotate_edge( 35, ANTICLOCKWISE )
                   rc.rotate_edge( 53, CLOCKWISE )
                   rc.rotate_edge( 35, CLOCKWISE )
                   rc.rotate_edge( 17, ANTICLOCKWISE )
                   mf.message( "here 14" )
                   continue

       # Right side top left corner
           if ( rc.get_colour ( 27 ) == top_colour ):
               mf.message( "right side top left corner" )
               if ( rc.get_colour( 20 ) == rc.get_colour( 35 ) ):
                   mf.message( "right side top left hand corner is a perfect match for front right top" )
                   rc.rotate_edge( 35, ANTICLOCKWISE )
                   rc.rotate_edge( 53, ANTICLOCKWISE )
                   rc.rotate_edge( 35, CLOCKWISE )
                   rc.rotate_edge( 53, CLOCKWISE )
                   rc.rotate_edge( 35, ANTICLOCKWISE )
                   rc.rotate_edge( 53, ANTICLOCKWISE )
                   rc.rotate_edge( 35, CLOCKWISE )
                   mf.message( "here 16" )
                   continue
               elif ( rc.get_colour ( 20 ) == rc.get_colour( 26 ) ):
                   mf.message( "right side top left hand corner is a perfect match for front left top" )
                   rc.rotate_edge( 17, CLOCKWISE )
                   rc.rotate_edge( 35, ANTICLOCKWISE )
                   rc.rotate_edge( 53, ANTICLOCKWISE )
                   rc.rotate_edge( 35, CLOCKWISE )
                   rc.rotate_edge( 17, ANTICLOCKWISE )
                   mf.message( "here 17" )
                   continue

       # Front left top corner
           if ( rc.get_colour ( 18 ) == top_colour ):
               mf.message( "front left top corner" )
               if ( rc.get_colour( 6 ) == rc.get_colour( 17 ) ):
                   mf.message( "Front top left corner needs to be twisted anticlockwise" )
                   rc.rotate_edge( 17, CLOCKWISE )
                   rc.rotate_edge( 53, ANTICLOCKWISE )
                   rc.rotate_edge( 17, ANTICLOCKWISE )
                   rc.rotate_edge( 26, ANTICLOCKWISE )
                   rc.rotate_edge( 53, ANTICLOCKWISE )
                   rc.rotate_edge( 26, CLOCKWISE )
                   mf.message( "here 18" )
                   continue
               elif ( rc.get_colour ( 6 ) == rc.get_colour( 26 ) ):
                   mf.message( "Front top left corner is a match for top layer front right" )
                   rc.rotate_edge( 17, CLOCKWISE )
                   rc.rotate_edge( 53, ANTICLOCKWISE )
                   rc.rotate_edge( 17, ANTICLOCKWISE )
                   rc.rotate_edge( 53, CLOCKWISE )
                   rc.rotate_edge( 35, ANTICLOCKWISE )
                   rc.rotate_edge( 53, ANTICLOCKWISE )
                   rc.rotate_edge( 35, CLOCKWISE )
                   mf.message( "here 19" )
                   continue

       # Front right top corner
           if ( rc.get_colour ( 20 ) == top_colour ):
               mf.message( "front right top corner" )
               if ( rc.get_colour( 4 ) == rc.get_colour( 35 ) ):
                   mf.message( "Front top right corner needs to be twisted clockwise" )
                   rc.rotate_edge( 35, ANTICLOCKWISE )
                   rc.rotate_edge( 53, CLOCKWISE )
                   rc.rotate_edge( 35, CLOCKWISE )
                   rc.rotate_edge( 26, CLOCKWISE )
                   rc.rotate_edge( 53, CLOCKWISE )
                   rc.rotate_edge( 26, ANTICLOCKWISE )
                   mf.message( "here 20" )
                   continue
               elif ( rc.get_colour ( 4 ) == rc.get_colour( 26 ) ):
                   mf.message( "Front top right corner is a match for top layer front left" )
                   rc.rotate_edge( 35, ANTICLOCKWISE )
                   rc.rotate_edge( 53, CLOCKWISE )
                   rc.rotate_edge( 35, CLOCKWISE )
                   rc.rotate_edge( 53, ANTICLOCKWISE )
                   rc.rotate_edge( 17, CLOCKWISE )
                   rc.rotate_edge( 53, CLOCKWISE )
                   rc.rotate_edge( 17, ANTICLOCKWISE )
                   mf.message( "here 21" )
                   continue

       # Back left top corner - top matches
           if ( rc.get_colour ( 0 ) == top_colour ):
               mf.message( "back left top corner" )
               if ( rc.get_colour( 9 ) == rc.get_colour( 26 ) ):
                   mf.message( "Back left top corner matches front left top corner" )
                   rc.rotate_edge( 17, ANTICLOCKWISE )
                   rc.rotate_edge( 53, ANTICLOCKWISE )
                   rc.rotate_edge( 17, CLOCKWISE )
                   rc.rotate_edge( 53, ANTICLOCKWISE )
                   rc.rotate_edge( 53, ANTICLOCKWISE )
                   rc.rotate_edge( 17, CLOCKWISE )
                   rc.rotate_edge( 53, CLOCKWISE )
                   rc.rotate_edge( 17, ANTICLOCKWISE )
                   mf.message( "here 22" )
                   continue
               elif ( rc.get_colour ( 9 ) == rc.get_colour( 35 ) ):
                   mf.message( "Back left top corner matches front right top corner" )
                   rc.rotate_edge( 17, ANTICLOCKWISE )
                   rc.rotate_edge( 53, ANTICLOCKWISE )
                   rc.rotate_edge( 17, CLOCKWISE )
                   rc.rotate_edge( 53, ANTICLOCKWISE )
                   rc.rotate_edge( 26, CLOCKWISE )
                   rc.rotate_edge( 53, CLOCKWISE )
                   rc.rotate_edge( 26, ANTICLOCKWISE )
                   mf.message( "here 23" )
                   continue

       # Back right top corner - top matches
           if ( rc.get_colour ( 2 ) == top_colour ):
               mf.message( "back right top corner" )
               if ( rc.get_colour( 29 ) == rc.get_colour( 26 ) ):
                   mf.message( "Back right top corner matches front right top corner" )
                   rc.rotate_edge( 35, CLOCKWISE )
                   rc.rotate_edge( 53, CLOCKWISE )
                   rc.rotate_edge( 35, ANTICLOCKWISE )
                   rc.rotate_edge( 53, ANTICLOCKWISE )
                   rc.rotate_edge( 53, ANTICLOCKWISE )
                   rc.rotate_edge( 35, ANTICLOCKWISE )
                   rc.rotate_edge( 53, ANTICLOCKWISE )
                   rc.rotate_edge( 35, CLOCKWISE )
                   mf.message( "here 24" )
                   continue
               elif ( rc.get_colour ( 29 ) == rc.get_colour( 17 ) ):
                   mf.message( "Back right top corner matches front left top corner" )
                   rc.rotate_edge( 35, CLOCKWISE )
                   rc.rotate_edge( 53, CLOCKWISE )
                   rc.rotate_edge( 35, ANTICLOCKWISE )
                   rc.rotate_edge( 53, CLOCKWISE )
                   rc.rotate_edge( 26, ANTICLOCKWISE )
                   rc.rotate_edge( 53, ANTICLOCKWISE )
                   rc.rotate_edge( 26, CLOCKWISE )
                   mf.message( "here 25" )
                   continue

       # Back left top corner - side matches
           if ( rc.get_colour ( 9 ) == top_colour ):
               mf.message( "left side back top corner" )
               if ( rc.get_colour( 0 ) == rc.get_colour( 17 ) ):
                   mf.message( "Back left top corner matches front left top corner" )
                   rc.rotate_edge( 17, ANTICLOCKWISE )
                   rc.rotate_edge( 53, ANTICLOCKWISE )
                   rc.rotate_edge( 53, ANTICLOCKWISE )
                   rc.rotate_edge( 17, CLOCKWISE )
                   rc.rotate_edge( 53, ANTICLOCKWISE )
                   rc.rotate_edge( 17, CLOCKWISE )
                   rc.rotate_edge( 53, CLOCKWISE )
                   rc.rotate_edge( 17, ANTICLOCKWISE )
                   mf.message( "here 26" )
                   continue
               elif ( rc.get_colour ( 9 ) == rc.get_colour( 35 ) ):
                   mf.message( "Back left top corner matches front right top corner" )
                   rc.rotate_edge( 17, ANTICLOCKWISE )
                   rc.rotate_edge( 53, ANTICLOCKWISE )
                   rc.rotate_edge( 53, ANTICLOCKWISE )
                   rc.rotate_edge( 17, CLOCKWISE )
                   rc.rotate_edge( 17, CLOCKWISE )
                   rc.rotate_edge( 53, ANTICLOCKWISE )
                   rc.rotate_edge( 17, ANTICLOCKWISE )
                   mf.message( "here 27" )
                   continue

       # Back right top corner - side matches
           if ( rc.get_colour ( 29 ) == top_colour ):
               mf.message( "right side back top corner" )
               if ( rc.get_colour( 2 ) == rc.get_colour( 35 ) ):
                   mf.message( "Back right top corner matches front right top corner" )
                   rc.rotate_edge( 35, CLOCKWISE )
                   rc.rotate_edge( 53, ANTICLOCKWISE )
                   rc.rotate_edge( 53, ANTICLOCKWISE )
                   rc.rotate_edge( 35, ANTICLOCKWISE )
                   rc.rotate_edge( 53, CLOCKWISE )
                   rc.rotate_edge( 35, ANTICLOCKWISE )
                   rc.rotate_edge( 53, ANTICLOCKWISE )
                   rc.rotate_edge( 35, CLOCKWISE )
                   mf.message( "here 28" )
                   continue
               elif ( rc.get_colour ( 29 ) == rc.get_colour( 17 ) ):
                   mf.message( "Back right top corner matches front left top corner" )
                   rc.rotate_edge( 35, CLOCKWISE )
                   rc.rotate_edge( 53, CLOCKWISE )
                   rc.rotate_edge( 53, CLOCKWISE )
                   rc.rotate_edge( 35, ANTICLOCKWISE )
                   rc.rotate_edge( 35, ANTICLOCKWISE )
                   rc.rotate_edge( 53, CLOCKWISE )
                   rc.rotate_edge( 35, CLOCKWISE )
                   mf.message( "here 29" )


       # Back right top corner - back matches
           if ( rc.get_colour ( 36 ) == top_colour ):
               mf.message( "right side back top corner" )
               if ( rc.get_colour( 29 ) == rc.get_colour( 35 ) ):
                   mf.message( "Back right top corner matches front right top corner" )
                   rc.rotate_edge( 44, ANTICLOCKWISE )
                   rc.rotate_edge( 53, ANTICLOCKWISE )
                   rc.rotate_edge( 44, CLOCKWISE )
                   rc.rotate_edge( 35, ANTICLOCKWISE )
                   rc.rotate_edge( 53, ANTICLOCKWISE )
                   rc.rotate_edge( 35, CLOCKWISE )
                   mf.message( "here 30" )
                   continue
               elif ( rc.get_colour ( 29 ) == rc.get_colour( 26 ) ):
                   mf.message( "Back right top corner matches front left top corner" )
                   rc.rotate_edge( 44, ANTICLOCKWISE )
                   rc.rotate_edge( 53, ANTICLOCKWISE )
                   rc.rotate_edge( 44, CLOCKWISE )
                   rc.rotate_edge( 17, CLOCKWISE )
                   rc.rotate_edge( 53, ANTICLOCKWISE )
                   rc.rotate_edge( 17, ANTICLOCKWISE )
                   mf.message( "here 31" )
                   continue

       # Back left top corner - back matches
           if ( rc.get_colour ( 38 ) == top_colour ):
               mf.message( "left side back top corner" )
               if ( rc.get_colour( 9 ) == rc.get_colour( 17 ) ):
                   mf.message( "Back left top corner matches front left top corner" )
                   rc.rotate_edge( 44, CLOCKWISE )
                   rc.rotate_edge( 53, CLOCKWISE )
                   rc.rotate_edge( 44, ANTICLOCKWISE )
                   rc.rotate_edge( 17, CLOCKWISE )
                   rc.rotate_edge( 53, CLOCKWISE )
                   rc.rotate_edge( 17, ANTICLOCKWISE )
                   mf.message( "here 32" )
                   continue
               elif ( rc.get_colour ( 9 ) == rc.get_colour( 26 ) ):
                   mf.message( "Back left top corner matches front right top corner" )
                   rc.rotate_edge( 44, CLOCKWISE )
                   rc.rotate_edge( 53, CLOCKWISE )
                   rc.rotate_edge( 44, ANTICLOCKWISE )
                   rc.rotate_edge( 35, ANTICLOCKWISE )
                   rc.rotate_edge( 53, CLOCKWISE )
                   rc.rotate_edge( 35, CLOCKWISE )
                   mf.message( "here 33" )
                   continue
           if ( flipflopflap == 0 ):
               flipflopflap = 1
               rc.rotate_cube( X_LEFT )
           elif ( flipflopflap == 1 ):
               flipflopflap = 2
               rc.rotate_cube( X_LEFT )
               rc.rotate_cube( X_LEFT )
           else:
               rc.rotate_edge( 53, ANTICLOCKWISE )
               flipflopflap = 0
           mf.message( "bottom of inner loop" )

