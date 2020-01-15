#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import time
import random
from display import t, print_info_block, mf
from rubik_class import rc
from solve_l1 import solve_layer1_edges, solve_layer1_corners
from solve_l2 import solve_layer2
from solve_l3 import flip_edges, rotate_l3_edges, reposition_l3_corners, spin_l3_corners
from data_def import X_RIGHT, X_LEFT, Y_UP, Y_DOWN, Z_ANTICLOCKWISE, Z_CLOCKWISE, CLOCKWISE, ANTICLOCKWISE

with t.fullscreen():
    with t.hidden_cursor():
        with t.raw():
            print_info_block()
            rc.draw_2d_absolute_cube() 
            rc.draw_2d_relative_cube() 
            while( True ):
                key = t.inkey()
                if ( key == "u" ):
                    mf.message( "UP" )
                    rc.rotate_cube( Y_UP )
                elif ( key == "d" ):
                    mf.message( "DOWN" )
                    rc.rotate_cube( Y_DOWN )
                elif ( key == "l" ):
                    mf.message( "LEFT" )
                    rc.rotate_cube( X_LEFT )
                elif ( key == "r" ):
                    mf.message( "RIGHT" )
                    rc.rotate_cube( X_RIGHT )
                elif ( key == "c" ):
                    mf.message( "CLOCKWISE" )
                    rc.rotate_cube( Z_CLOCKWISE )
                elif ( key == "a" ):
                    mf.message( "ANTICLOCKWISE" )
                    rc.rotate_cube( Z_ANTICLOCKWISE )
                elif ( key == "b" ):
                    mf.message( "Rotating bottom edge clockwise" )
                    rc.rotate_edge( 53, CLOCKWISE )
                elif ( key == "m" ):
                    mf.message( "Muddling cube with 20 random moves" )
                    for n in range( 20 ):
                        rc.rotate_edge( ( random.randint( 0, 5) * 9 ) + 8, random.randint( 0, 1 ) )
                elif ( key == "1" ):
                    rc.rotate_top_2_layers( ANTICLOCKWISE )
                elif ( key == "2" ):
                    rc.rotate_bottom_2_layers( CLOCKWISE )
                elif ( key == "3" ):
                    rc.rotate_horizontal_middle( X_RIGHT )
                elif ( key == "s" ):
                    solve_layer1_edges()
                    mf.message( "Press any key. Solve_layer1_edges() has completed" )
                    #t.inkey()
                    solve_layer1_corners()
                    mf.message( "Press any key. Solve_layer1_corners() has completed" )
                    #t.inkey()
                    solve_layer2()
                    mf.message( "Press any key. Solve_layer2() has completed" )
                    #t.inkey()
                    flip_edges()
                    mf.message( "Press any key. flip_edges() has completed" )
                    #t.inkey()
                    rotate_l3_edges()
                    mf.message( "Press any key. rotate_l3_edges() has completed" )
                    #t.inkey()
                    reposition_l3_corners()
                    mf.message( "Press any key. reposition_l3_corners() has completed" )
                    #t.inkey()
                    spin_l3_corners()
                    mf.message( "Press any key. spin_l3_corners() has completed" )
                    #t.inkey()

                else:
                    break
                    mf.message( "Not understood" )
            
