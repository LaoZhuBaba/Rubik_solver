#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import time
from display import mf
from rubik_class import rc
from data_def import CLOCKWISE, ANTICLOCKWISE, X_LEFT

def solve_layer2():

    level_of_completion = 0
    while ( level_of_completion <= 4 ):
        level_of_competion = 0
        progress_has_been_made = 4
        for loop2 in ( range( 8 ) ):
            mf.message( "press a key to continue from top of inner loop" )
            #t.inkey()
            if ( ( rc.get_colour( 30 ) == rc.get_colour( 35 ) ) and ( rc.get_colour( 35 ) == rc.get_colour( 34 ) ) and
                 ( rc.get_colour( 21 ) == rc.get_colour( 26 ) ) and ( rc.get_colour( 43 ) == rc.get_colour ( 44 ) ) ):
                level_of_completion += 1
                mf.message( "level_of_competion raised to %d" % ( level_of_completion ) )
                break
            else:
                level_of_completion = 0
            mf.message( "level_of_completion reset to %d" % ( level_of_completion ) )
            if ( rc.get_colour( 32 ) == rc.get_colour( 35 ) ):
                if ( rc.get_colour( 46 ) == rc.get_colour( 26 ) ):
                    mf.message( " 32 & 35 match, and 46 & 26.  Proceeding to solve edges.  Press a key" )
                    #t.inkey()
                    rc.rotate_edge( 35, ANTICLOCKWISE )
                    rc.rotate_edge( 53, ANTICLOCKWISE )
                    rc.rotate_edge( 35, ANTICLOCKWISE )
                    rc.rotate_edge( 53, ANTICLOCKWISE )
                    rc.rotate_edge( 35, ANTICLOCKWISE )
                    rc.rotate_edge( 53, ANTICLOCKWISE )
                    rc.rotate_edge( 35, CLOCKWISE )
                    rc.rotate_edge( 53, CLOCKWISE )
                    rc.rotate_edge( 35, CLOCKWISE )
                    rc.rotate_edge( 53, CLOCKWISE )
                    rc.rotate_edge( 35, ANTICLOCKWISE )
                    rc.rotate_edge( 35, ANTICLOCKWISE )
                    progress_has_been_made += 1
                if ( rc.get_colour( 46 ) == rc.get_colour( 44 ) ):
                    mf.message( " 32 & 35 match, and 46 & 44.  Proceeding to solve edges.  Press a key" )
                    #t.inkey()
                    rc.rotate_edge( 35, CLOCKWISE )
                    rc.rotate_edge( 53, CLOCKWISE )
                    rc.rotate_edge( 35, CLOCKWISE )
                    rc.rotate_edge( 53, CLOCKWISE )
                    rc.rotate_edge( 35, CLOCKWISE )
                    rc.rotate_edge( 53, CLOCKWISE )
                    rc.rotate_edge( 35, ANTICLOCKWISE )
                    rc.rotate_edge( 53, ANTICLOCKWISE )
                    rc.rotate_edge( 35, ANTICLOCKWISE )
                    rc.rotate_edge( 53, ANTICLOCKWISE )
                    rc.rotate_edge( 35, ANTICLOCKWISE )
                    rc.rotate_edge( 35, ANTICLOCKWISE )
                    progress_has_been_made += 1
###
            if ( rc.get_colour( 17 ) == rc.get_colour( 14 ) ):
                if ( rc.get_colour( 50 ) == rc.get_colour( 26 ) ):
                    mf.message( "17 & 14 match, and 50 & 26.  Proceeding to solve edges.  Press a key" )
                    #t.inkey()
                    rc.rotate_edge( 17, CLOCKWISE )
                    rc.rotate_edge( 53, CLOCKWISE )
                    rc.rotate_edge( 17, CLOCKWISE )
                    rc.rotate_edge( 53, CLOCKWISE )
                    rc.rotate_edge( 17, CLOCKWISE )
                    rc.rotate_edge( 53, CLOCKWISE )
                    rc.rotate_edge( 17, ANTICLOCKWISE )
                    rc.rotate_edge( 53, ANTICLOCKWISE )
                    rc.rotate_edge( 17, ANTICLOCKWISE )
                    rc.rotate_edge( 53, ANTICLOCKWISE )
                    rc.rotate_edge( 17, CLOCKWISE )
                    rc.rotate_edge( 17, CLOCKWISE )
                    progress_has_been_made += 1
                if ( rc.get_colour( 50 ) == rc.get_colour( 44 ) ):
                    mf.message( "17 & 14 match, and 50 & 44.  Proceeding to solve edges.  Press a key" )
                    #t.inkey()
                    rc.rotate_edge( 17, ANTICLOCKWISE )
                    rc.rotate_edge( 53, ANTICLOCKWISE )
                    rc.rotate_edge( 17, ANTICLOCKWISE )
                    rc.rotate_edge( 53, ANTICLOCKWISE )
                    rc.rotate_edge( 17, ANTICLOCKWISE )
                    rc.rotate_edge( 53, ANTICLOCKWISE )
                    rc.rotate_edge( 17, CLOCKWISE )
                    rc.rotate_edge( 53, CLOCKWISE )
                    rc.rotate_edge( 17, CLOCKWISE )
                    rc.rotate_edge( 53, CLOCKWISE )
                    rc.rotate_edge( 17, CLOCKWISE )
                    rc.rotate_edge( 17, CLOCKWISE )
                    progress_has_been_made += 1
###
            # The following moves are only necessary if we have got into a deadlock
            if ( progress_has_been_made == 0 ):
                progress_has_been_made += 1
                if ( ( rc.get_colour( 34 ) == rc.get_colour( 53 ) ) or ( rc.get_colour( 21 ) == rc.get_colour( 53 ) ) ):
                    mf.message( "Moving a bottom matching piece 21/34.  Press a key" )
                    #t.inkey()
                    rc.rotate_edge( 35, ANTICLOCKWISE )
                    rc.rotate_edge( 53, ANTICLOCKWISE )
                    rc.rotate_edge( 35, ANTICLOCKWISE )
                    rc.rotate_edge( 53, ANTICLOCKWISE )
                    rc.rotate_edge( 35, ANTICLOCKWISE )
                    rc.rotate_edge( 53, ANTICLOCKWISE )
                    rc.rotate_edge( 35, CLOCKWISE )
                    rc.rotate_edge( 53, CLOCKWISE )
                    rc.rotate_edge( 35, CLOCKWISE )
                    rc.rotate_edge( 53, CLOCKWISE )
                    rc.rotate_edge( 35, ANTICLOCKWISE )
                    rc.rotate_edge( 35, ANTICLOCKWISE )
                    continue
                if ( ( rc.get_colour( 34 ) == rc.get_colour( 26 ) ) and ( rc.get_colour( 21 ) == rc.get_colour( 35 ) ) ):
                    mf.message( "Moving a flipped piece from 21/34.  Press a key" )
                    #t.inkey()
                    rc.rotate_edge( 35, ANTICLOCKWISE )
                    rc.rotate_edge( 53, ANTICLOCKWISE )
                    rc.rotate_edge( 35, ANTICLOCKWISE )
                    rc.rotate_edge( 53, ANTICLOCKWISE )
                    rc.rotate_edge( 35, ANTICLOCKWISE )
                    rc.rotate_edge( 53, ANTICLOCKWISE )
                    rc.rotate_edge( 35, CLOCKWISE )
                    rc.rotate_edge( 53, CLOCKWISE )
                    rc.rotate_edge( 35, CLOCKWISE )
                    rc.rotate_edge( 53, CLOCKWISE )
                    rc.rotate_edge( 35, ANTICLOCKWISE )
                    rc.rotate_edge( 35, ANTICLOCKWISE )
                    continue
                if ( ( rc.get_colour( 30 ) == rc.get_colour( 53 ) ) or ( rc.get_colour( 43 ) == rc.get_colour( 53 ) ) ):
                    mf.message( "Moving a bottom matching piece 30/43.  Press a key" )
                    #t.inkey()
                    rc.rotate_edge( 35, CLOCKWISE )
                    rc.rotate_edge( 53, CLOCKWISE )
                    rc.rotate_edge( 35, CLOCKWISE )
                    rc.rotate_edge( 53, CLOCKWISE )
                    rc.rotate_edge( 35, CLOCKWISE )
                    rc.rotate_edge( 53, CLOCKWISE )
                    rc.rotate_edge( 35, ANTICLOCKWISE )
                    rc.rotate_edge( 53, ANTICLOCKWISE )
                    rc.rotate_edge( 35, ANTICLOCKWISE )
                    rc.rotate_edge( 53, ANTICLOCKWISE )
                    rc.rotate_edge( 35, ANTICLOCKWISE )
                    rc.rotate_edge( 35, ANTICLOCKWISE )
                    continue
                if ( ( rc.get_colour( 30 ) == rc.get_colour( 44 ) ) and ( rc.get_colour( 43 ) == rc.get_colour( 35 ) ) ):
                    mf.message( "Moving out a piece which is flipped: 30/43.  Press a key" )
                    #t.inkey()
                    rc.rotate_edge( 35, CLOCKWISE )
                    rc.rotate_edge( 53, CLOCKWISE )
                    rc.rotate_edge( 35, CLOCKWISE )
                    rc.rotate_edge( 53, CLOCKWISE )
                    rc.rotate_edge( 35, CLOCKWISE )
                    rc.rotate_edge( 53, CLOCKWISE )
                    rc.rotate_edge( 35, ANTICLOCKWISE )
                    rc.rotate_edge( 53, ANTICLOCKWISE )
                    rc.rotate_edge( 35, ANTICLOCKWISE )
                    rc.rotate_edge( 53, ANTICLOCKWISE )
                    rc.rotate_edge( 35, ANTICLOCKWISE )
                    rc.rotate_edge( 35, ANTICLOCKWISE )
                    continue
                if ( ( rc.get_colour( 30 ) != rc.get_colour( 35 ) ) or ( rc.get_colour( 43 ) != rc.get_colour( 44 ) ) ):
                    mf.message( "Moving out piece 30/43 because it isn't right.  Press a key" )
                    #t.inkey()
                    rc.rotate_edge( 35, CLOCKWISE )
                    rc.rotate_edge( 53, CLOCKWISE )
                    rc.rotate_edge( 35, CLOCKWISE )
                    rc.rotate_edge( 53, CLOCKWISE )
                    rc.rotate_edge( 35, CLOCKWISE )
                    rc.rotate_edge( 53, CLOCKWISE )
                    rc.rotate_edge( 35, ANTICLOCKWISE )
                    rc.rotate_edge( 53, ANTICLOCKWISE )
                    rc.rotate_edge( 35, ANTICLOCKWISE )
                    rc.rotate_edge( 53, ANTICLOCKWISE )
                    rc.rotate_edge( 35, ANTICLOCKWISE )
                    rc.rotate_edge( 35, ANTICLOCKWISE )
                    continue
                if ( ( rc.get_colour( 34 ) != rc.get_colour( 35 ) ) or ( rc.get_colour( 21 ) != rc.get_colour( 26 ) ) ):
                    mf.message( "Moving out piece 21/34 because it isn't right.  Press a key" )
                    #t.inkey()
                    rc.rotate_edge( 35, ANTICLOCKWISE )
                    rc.rotate_edge( 53, ANTICLOCKWISE )
                    rc.rotate_edge( 35, ANTICLOCKWISE )
                    rc.rotate_edge( 53, ANTICLOCKWISE )
                    rc.rotate_edge( 35, ANTICLOCKWISE )
                    rc.rotate_edge( 53, ANTICLOCKWISE )
                    rc.rotate_edge( 35, CLOCKWISE )
                    rc.rotate_edge( 53, CLOCKWISE )
                    rc.rotate_edge( 35, CLOCKWISE )
                    rc.rotate_edge( 53, CLOCKWISE )
                    rc.rotate_edge( 35, ANTICLOCKWISE )
                    rc.rotate_edge( 35, ANTICLOCKWISE )
                    continue
    ##
            progress_has_been_made -= 1
            rc.rotate_edge( 53, ANTICLOCKWISE )
        rc.rotate_cube( X_LEFT )
