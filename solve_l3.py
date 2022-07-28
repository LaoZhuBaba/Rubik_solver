#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import time
from display import mf
from rubik_class import Rubik as rc, CLOCKWISE, ANTICLOCKWISE
from data_def import Y_UP, Y_DOWN, X_RIGHT

def flip_edges():
    rc.rotate_cube( Y_DOWN )
    rc.rotate_cube( Y_DOWN )
    flipflop = 0
    for one2345 in ( 1, 2, 3, 4, 5 ):
        mf.message( "flip_edges inner loop with count of %d.  Hit a key to continue" % ( one2345 ) )
        if ( rc.get_colour( 5 ) != rc.get_colour( 8 ) ):
            if ( flipflop == 0 ):
                flipflop = 1
                rc.rotate_vertical_middle( Y_DOWN )
                rc.rotate_edge( 53, ANTICLOCKWISE )
                rc.rotate_vertical_middle( Y_UP )
                rc.rotate_edge( 53, CLOCKWISE )
                rc.rotate_vertical_middle( Y_DOWN )
                rc.rotate_edge( 53, CLOCKWISE )
                rc.rotate_edge( 53, CLOCKWISE )
                rc.rotate_vertical_middle( Y_UP )
            elif ( flipflop == 1 ):
                flipflop = 0
                rc.rotate_vertical_middle( Y_DOWN )
                rc.rotate_edge( 53, CLOCKWISE )
                rc.rotate_edge( 53, CLOCKWISE )
                rc.rotate_vertical_middle( Y_UP )
                rc.rotate_edge( 53, ANTICLOCKWISE )
                rc.rotate_vertical_middle( Y_DOWN )
                rc.rotate_edge( 53, CLOCKWISE )
                rc.rotate_vertical_middle( Y_UP )
        rc.rotate_edge( 8, CLOCKWISE )

def rotate_l3_edges():
    rc.rotate_cube( Y_DOWN )
    rc.rotate_cube( Y_DOWN )
    count1 = 0
    while ( count1 < 50 ): # 50 is just to prevent the loop running of control.
                          # This function should return long before that.
        mf.message( "Outer loop.  Press a key to continue" )
        #t.inkey()
        count2 = 0
        while ( count2 <= 4 ):
            mf.message( "Inner loop with count of %d.  Press a key to continue" % ( count2 ) )
            #t.inkey()
            # We are looking for an edge which is correctly aligned with its centre
            if ( rc.get_colour( 23 ) == rc.get_colour( 26 ) ):
                mf.message( "23 and 26 match" )
                #t.inkey()
                # If two other edges are also aligned then that means all four must
                # be good, in which case there is nothing to do.
                if ( ( rc.get_colour( 32 ) == rc.get_colour( 35 ) ) and ( rc.get_colour( 14 ) == rc.get_colour( 17 ) ) ):
                    mf.message( "all edges match, so returning" )
                    #t.inkey()
                    return
                # We are looking for an orientation which has one edge aligned with its centre
                # but its two rotationally adjacent edges are not aligned.  It doesn't matter
                # the opposite edge
                elif ( ( rc.get_colour( 32 ) != rc.get_colour( 35 ) ) and ( rc.get_colour( 14 ) != rc.get_colour( 17 ) ) ):
                    mf.message( "Neither 32 & 35 nor 14 & 17 match, so running the correction" )
                    #t.inkey()
                    rc.rotate_edge( 35, ANTICLOCKWISE )
                    rc.rotate_edge( 53, ANTICLOCKWISE )
                    rc.rotate_edge( 35, CLOCKWISE )
                    rc.rotate_edge( 53, ANTICLOCKWISE )
                    rc.rotate_edge( 35, ANTICLOCKWISE )
                    rc.rotate_edge( 53, CLOCKWISE )
                    rc.rotate_edge( 53, CLOCKWISE )
                    rc.rotate_edge( 35, CLOCKWISE )
                    mf.message( "continuing.  Should see inner loop message next" )
                    #t.inkey()
                    continue
            mf.message( "Nothing happening here so rotating bottom edge" )
            #t.inkey()
            rc.rotate_edge( 53, CLOCKWISE )
            count2 += 1
        mf.message( "Still nothing happening here so rotating whole cube" )
        #t.inkey()
        rc.rotate_cube( X_RIGHT )
        count1 += 1

def reposition_l3_corners():
    rc.rotate_cube( Y_DOWN )
    rc.rotate_cube( Y_DOWN )
    count1 = 0

    # This is just an easy way of comparing two sets of corner colours which may be in
    # a different order to see if they are the same
    #
    # Originally implemented as local function, but switched to lambda
    # def return_corner_hash( a, b, c ):
    #    return ( ( rc.get_colour( a ) ** 2 ) + ( rc.get_colour( b ) ** 2 ) + ( rc.get_colour( c ) ** 2 ) )
    return_corner_hash = lambda a, b, c: ( ( rc.get_colour( a ) ** 2 ) + ( rc.get_colour( b ) ** 2 ) + ( rc.get_colour( c ) ** 2 ) )

    while ( count1 < 50 ): # 50 is just to prevent the loop running of control.
                          # This function should return long before that.
        mf.message( "Loop with count of %d.  Press a key to continue" % ( count1 ) )
        #t.inkey()
        # Use a "corner hash" to see whether top right front corner has the correct three
        # colours, without worrying about rotational orientation.
        # Most time we don't need this section but there are some combinations which don't
        # work out without running at least corner rotation.  So if we have tried all
        # four sides without making progress then do a rotation anyway.
        if ( count1 > 4 ):
            count1 = 0
            mf.message( "Not progressing after a full rotation so continuing to action anyway" )
            #t.inkey()
            rc.rotate_edge( 17, ANTICLOCKWISE )
            rc.rotate_edge( 8, CLOCKWISE )
            rc.rotate_edge( 35, CLOCKWISE )
            rc.rotate_edge( 8, ANTICLOCKWISE )
            rc.rotate_edge( 17, CLOCKWISE )
            rc.rotate_edge( 8, CLOCKWISE )
            rc.rotate_edge( 35, ANTICLOCKWISE )
            rc.rotate_edge( 8, ANTICLOCKWISE )
            mf.message( "continuing.  Should see inner loop message next" )
            #t.inkey()
            continue
        if ( ( return_corner_hash( 26, 35, 8 ) ) == ( return_corner_hash( 20, 4, 27 ) ) ):
            mf.message( "The top right front corner is correctly positioned, so checking further..." )
            #t.inkey()
            if ( ( return_corner_hash( 26, 17, 8 ) ) == ( return_corner_hash( 18, 6, 11 ) ) ):
                if ( ( return_corner_hash( 44, 35, 8 ) ) == ( return_corner_hash( 36, 2, 29 ) ) ):
                    # Reaching this point means three corners are in the location, which means
                    # the fourth must be too.  So no work to do.  Return.
                    mf.message( "all corners are located correctly, so returning" )
                    #t.inkey()
                    return
            elif ( ( return_corner_hash( 26, 17, 8 ) ) != ( return_corner_hash( 18, 6, 11 ) ) ):
                mf.message( "26, 17, 8 does not match 18, 6, 11 so continuing to next check" )
                if ( ( return_corner_hash( 44, 35, 8 ) ) != ( return_corner_hash( 36, 2, 29 ) ) ):
                    mf.message( "44, 35, 8 does not match 32, 2, 29, so continuing to action" )
                    # Reaching here means that the front right hand top corner is the only
                    # correctly positioned corner.  So do a corner rotation.
                    mf.message( "Left front top and right back top are wrong, so running the correction" )
                    #t.inkey()
                    rc.rotate_edge( 17, ANTICLOCKWISE )
                    rc.rotate_edge( 8, CLOCKWISE )
                    rc.rotate_edge( 35, CLOCKWISE )
                    rc.rotate_edge( 8, ANTICLOCKWISE )
                    rc.rotate_edge( 17, CLOCKWISE )
                    rc.rotate_edge( 8, CLOCKWISE )
                    rc.rotate_edge( 35, ANTICLOCKWISE )
                    rc.rotate_edge( 8, ANTICLOCKWISE )
                    mf.message( "continuing.  Should see inner loop message next" )
                    #t.inkey()
                    continue
        mf.message( "Still nothing happening here so rotating whole cube" )
        #t.inkey()
        rc.rotate_cube( X_RIGHT )
        count1 += 1
#

def spin_l3_corners():
    count1 = 0
    while ( count1 < 4 ):
        mf.message( "Loop with count of %d.  Press a key to continue" % ( count1 ) )
        #t.inkey()
        if ( rc.get_colour( 20 ) == rc.get_colour( 19 ) ):
            mf.message( "20 == 19, so corner looks good.  Press a key to continue" )
            #t.inkey()
        elif ( rc.get_colour( 20 ) == rc.get_colour( 8 ) ):
            # Need to be rotated clockwise
            mf.message( "20 == 8, so rotate clockwise.  Press a key to continue" )
            #t.inkey()
            rc.rotate_edge( 35, ANTICLOCKWISE )
            rc.rotate_edge( 53, CLOCKWISE )
            rc.rotate_edge( 35, CLOCKWISE )
            rc.rotate_edge( 53, ANTICLOCKWISE )
            rc.rotate_edge( 35, ANTICLOCKWISE )
            rc.rotate_edge( 53, CLOCKWISE )
            rc.rotate_edge( 35, CLOCKWISE )
            rc.rotate_edge( 53, ANTICLOCKWISE )
        else:
            # Need to be rotated anticlockwise
            mf.message( "20 != 8, so must need rotating anticlockwise.  Press a key to continue" )
            #t.inkey()
            rc.rotate_edge( 53, CLOCKWISE )
            rc.rotate_edge( 35, ANTICLOCKWISE )
            rc.rotate_edge( 53, ANTICLOCKWISE )
            rc.rotate_edge( 35, CLOCKWISE )
            rc.rotate_edge( 53, CLOCKWISE )
            rc.rotate_edge( 35, ANTICLOCKWISE )
            rc.rotate_edge( 53, ANTICLOCKWISE )
            rc.rotate_edge( 35, CLOCKWISE )
        mf.message( "Still nothing happening here so rotating whole cube" )
        #t.inkey()
        rc.rotate_edge( 8, CLOCKWISE )
        count1 += 1
    mf.message( "Exiting after checking/correcting all four faces.  Press a key" )
    #t.inkey()


