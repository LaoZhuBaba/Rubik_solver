#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from data_def import CLOCKWISE, ANTICLOCKWISE
from display import t                          # Used in: draw_absolute_square(), draw_relative_square(), draw_2d_relative_cube()
from display import mf                         # Used in: draw_2d_relative_cube
from data_def import orientations, pathways    # Used in: rotate_cube
from data_def import MOVES                     # Used in: exec_absolute_move()
from data_def import ABSOLUTE_CUBE_2D_XY       # Used in: draw_2d_absolute_cube()
from data_def import X_LEFT, X_RIGHT           # Used in: rotate_horizonal_middle()
from data_def import Y_UP, Y_DOWN              # Used in: rotate_vertical_middle()

if sys.version_info[0] >= 3:
    unicode = str

COLOURS = RED, GREEN, YELLOW, BLUE, WHITE, MAGENTA = range(6) 

UP_ARROW = u'↑'
RIGHT_ARROW =   u'→'
DOWN_ARROW =  u'↓'
LEFT_ARROW =  u'←'

class Rubik:

    # I don't expect there will ever be multiple instances of this class
    # so we can safely initialise these at the class level

    arrows = [ UP_ARROW, RIGHT_ARROW, DOWN_ARROW, LEFT_ARROW ]
    # This list keeps track of the direction of arrows we draw on each centre square
    arrow_direction = [ 0, 0, 0, 0, 0, 0 ]
    # Initialise the colours of the cube for its starting position
    absolute_cube = [ RED, RED, RED, RED, RED, RED, RED, RED, RED,
                      GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN,
                      YELLOW, YELLOW, YELLOW, YELLOW, YELLOW, YELLOW, YELLOW, YELLOW, YELLOW,
                      BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE,
                      WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE,
                      MAGENTA, MAGENTA, MAGENTA, MAGENTA, MAGENTA, MAGENTA, MAGENTA, MAGENTA, MAGENTA ] 

    # Initialise logical to match physical cube's starting position
    orientation = 0
    relative_cube = orientations[ orientation ]
    COLOUR_DESCRIPTIONS = [ "RED", "GREEN", "YELLOW", "BLUE", "WHITE", "MAGENTA" ]

    @classmethod
    def draw_absolute_square( cls, x, y, colour, str ):
        
        SQUARE_WIDTH = 5 # Can't be easily changed
        SQUARE_HEIGHT = 3 # Can't be easily changed
        Y_OFFSET = 1
        X_OFFSET = 4

        if ( len( str ) == 1 ):
            str = ' ' + str
        centre_row_str = ( ( ' ' * ( SQUARE_WIDTH // 2 ) + str + (  ( SQUARE_WIDTH // 2 ) * ' ' ) ) )
        other_row_str = ( u'─' * SQUARE_WIDTH )
        top_row =  u'┌───┐'
        middle_row = u'│' + str + u' │'
        bottom_row = u'└───┘'
    
        if ( colour == BLUE ):
            sys.stdout.write( t.move( y + Y_OFFSET, x + X_OFFSET ) +  t.on_blue( top_row ) )
            sys.stdout.write( t.move( y + Y_OFFSET + 1, x + X_OFFSET ) +  t.on_blue( middle_row ) )
            sys.stdout.write( t.move( y + Y_OFFSET + 2, x + X_OFFSET ) +  t.on_blue( bottom_row ) )
    
        if ( colour == GREEN ):
            sys.stdout.write( t.move( y + Y_OFFSET, x + X_OFFSET ) +  t.on_green( top_row ) )
            sys.stdout.write( t.move( y + Y_OFFSET + 1, x + X_OFFSET ) +  t.on_green( middle_row ) )
            sys.stdout.write( t.move( y + Y_OFFSET + 2, x + X_OFFSET ) +  t.on_green( bottom_row ) )
    
        if ( colour == RED ):
            sys.stdout.write( t.move( y + Y_OFFSET, x + X_OFFSET ) +  t.on_red( top_row ) )
            sys.stdout.write( t.move( y + Y_OFFSET + 1, x + X_OFFSET ) +  t.on_red( middle_row ) )
            sys.stdout.write( t.move( y + Y_OFFSET + 2, x + X_OFFSET ) +  t.on_red( bottom_row ) )
    
        if ( colour == YELLOW ):
            sys.stdout.write( t.move( y + Y_OFFSET, x + X_OFFSET ) +  t.black_on_yellow( top_row ) )
            sys.stdout.write( t.move( y + Y_OFFSET + 1, x + X_OFFSET ) +  t.black_on_yellow( middle_row ) )
            sys.stdout.write( t.move( y + Y_OFFSET + 2, x + X_OFFSET ) +  t.black_on_yellow( bottom_row ) )
    
        if ( colour == MAGENTA ):
            sys.stdout.write( t.move( y + Y_OFFSET, x + X_OFFSET ) +  t.on_magenta( top_row ) )
            sys.stdout.write( t.move( y + Y_OFFSET + 1, x + X_OFFSET ) +  t.on_magenta( middle_row ) )
            sys.stdout.write( t.move( y + Y_OFFSET + 2, x + X_OFFSET ) +  t.on_magenta( bottom_row ) )
    
        if ( colour == WHITE ):
            sys.stdout.write( t.move( y + Y_OFFSET, x + X_OFFSET ) +  t.black_on_white( top_row ) )
            sys.stdout.write( t.move( y + Y_OFFSET + 1, x + X_OFFSET ) +  t.black_on_white( middle_row ) )
            sys.stdout.write( t.move( y + Y_OFFSET + 2, x + X_OFFSET ) +  t.black_on_white( bottom_row ) )
    
        sys.stdout.flush()

    @classmethod
    def draw_relative_square( cls, x, y, colour, str ):
    
        Y_OFFSET = 1
        X_OFFSET = 68
        if ( len( str ) == 1 ):
            str = ' ' + str
        top_row =  u'┌───┐'
        middle_row = u'│' + str + u' │'
        bottom_row = u'└───┘'
    
        if ( colour == BLUE ):
            sys.stdout.write( t.move( y + Y_OFFSET, x + X_OFFSET ) +  t.on_blue( top_row ) )
            sys.stdout.write( t.move( y + Y_OFFSET + 1, x + X_OFFSET ) +  t.on_blue( middle_row ) )
            sys.stdout.write( t.move( y + Y_OFFSET + 2, x + X_OFFSET ) +  t.on_blue( bottom_row ) )
    
        if ( colour == GREEN ):
            sys.stdout.write( t.move( y + Y_OFFSET, x + X_OFFSET ) +  t.on_green( top_row ) )
            sys.stdout.write( t.move( y + Y_OFFSET + 1, x + X_OFFSET ) +  t.on_green( middle_row ) )
            sys.stdout.write( t.move( y + Y_OFFSET + 2, x + X_OFFSET ) +  t.on_green( bottom_row ) )
    
        if ( colour == RED ):
            sys.stdout.write( t.move( y + Y_OFFSET, x + X_OFFSET ) +  t.on_red( top_row ) )
            sys.stdout.write( t.move( y + Y_OFFSET + 1, x + X_OFFSET ) +  t.on_red( middle_row ) )
            sys.stdout.write( t.move( y + Y_OFFSET + 2, x + X_OFFSET ) +  t.on_red( bottom_row ) )
    
        if ( colour == YELLOW ):
            sys.stdout.write( t.move( y + Y_OFFSET, x + X_OFFSET ) +  t.black_on_yellow( top_row ) )
            sys.stdout.write( t.move( y + Y_OFFSET + 1, x + X_OFFSET ) +  t.black_on_yellow( middle_row ) )
            sys.stdout.write( t.move( y + Y_OFFSET + 2, x + X_OFFSET ) +  t.black_on_yellow( bottom_row ) )

        if ( colour == MAGENTA ):
            sys.stdout.write( t.move( y + Y_OFFSET, x + X_OFFSET ) +  t.on_magenta( top_row ) )
            sys.stdout.write( t.move( y + Y_OFFSET + 1, x + X_OFFSET ) +  t.on_magenta( middle_row ) )
            sys.stdout.write( t.move( y + Y_OFFSET + 2, x + X_OFFSET ) +  t.on_magenta( bottom_row ) )

        if ( colour == WHITE ):
            sys.stdout.write( t.move( y + Y_OFFSET, x + X_OFFSET ) +  t.black_on_white( top_row ) )
            sys.stdout.write( t.move( y + Y_OFFSET + 1, x + X_OFFSET ) +  t.black_on_white( middle_row ) )
            sys.stdout.write( t.move( y + Y_OFFSET + 2, x + X_OFFSET ) +  t.black_on_white( bottom_row ) )

        sys.stdout.flush()

    @classmethod
    def rotate_cube( cls, direction ):

        cls.orientation = pathways[ cls.orientation ][ direction ]
        cls.relative_cube = orientations[ cls.orientation ]
        cls.draw_2d_relative_cube()
 

    @classmethod
    def exec_absolute_move( cls, number ):

        temp_colour_list = [ None ] * 20

        for count in range( len( MOVES[ number ] ) ):
            temp_colour_list[ count ] = cls.absolute_cube[ MOVES[ number ][count][ 0 ] ]

        for count in range( len( MOVES[ number ] ) ):
            cls.absolute_cube[ MOVES[ number ][count][ 1 ] ] = temp_colour_list[ count ]


    @classmethod
    def draw_2d_absolute_cube( cls ):
    
        for square in range(54):
    
            if ( ( square % 9 ) == 8 ):
                cls.draw_absolute_square( ABSOLUTE_CUBE_2D_XY[square][0],
                                           ABSOLUTE_CUBE_2D_XY[square][1],
                                           cls.absolute_cube[square],
                                           unicode( cls.arrows[ cls.arrow_direction[ cls.absolute_cube[ square ] ] ] ) )

            #    arrow_direction[ physical_cube[ square ] ] = ( arrow_direction[ physical_cube[ square ] ] + 1 ) % 4
            else:
                cls.draw_absolute_square( ABSOLUTE_CUBE_2D_XY[square][0],
                                           ABSOLUTE_CUBE_2D_XY[square][1],
                                           cls.absolute_cube[square],
                                           "  " )
    
    @classmethod
    def draw_2d_relative_cube( cls ):

        key = t.inkey( timeout=0.1 )
        if ( key == 'q' ):
            mf.message( "exit has been requested" )
            sys.exit( 0 )
        # If you don't actually want to display the relative version of the
        # cube on the screen then uncomment the next line
        return
        for square in range(54):
    
            cls.draw_relative_square( ABSOLUTE_CUBE_2D_XY[square][0],
                                       ABSOLUTE_CUBE_2D_XY[square][1],
                                       cls.absolute_cube[ cls.relative_cube[square] ],
                                       str(square) )


    @classmethod
    def get_colour( cls, square ):
    
       return( cls.absolute_cube[ cls.relative_cube[ square ] ] )
    
    @classmethod
    def rotate_edge( cls, middle_square, clock_anti ):
    
        colour = cls.get_colour( middle_square )
    
        if ( clock_anti == CLOCKWISE ):
            cls.arrow_direction[ colour ] = ( ( cls.arrow_direction[ colour ] + 1 ) % 4 )
        else:
            cls.arrow_direction[ colour ] = ( ( cls.arrow_direction[ colour ] + 3 ) % 4 )
    
        if ( clock_anti == CLOCKWISE ):
            cls.exec_absolute_move( colour )
        else:
            cls.exec_absolute_move( colour + 6 )
        cls.draw_2d_relative_cube()
        cls.draw_2d_absolute_cube()
    
    @classmethod
    def get_edges_of_colour( cls, middle_square, colour ):
    
        return_list = []
        for e in ( 1, 3, 5, 7 ):
            if ( ( cls.get_colour( middle_square - 8 + e ) == colour ) ):
                return_list.append( middle_square - 8 + e )
        return return_list
    
    @classmethod
    def rotate_top_2_layers( cls, direction ):
    
        # bottom middle square is 53
    
         if ( direction == CLOCKWISE ):
            cls.rotate_edge( 53, ANTICLOCKWISE )
            cls.rotate_cube( CLOCKWISE )
         else:
            cls.rotate_edge( 53, CLOCKWISE )
            cls.rotate_cube( ANTICLOCKWISE )
    
    @classmethod
    def rotate_bottom_2_layers( cls, direction ):
    
        # top middle square is 8
    
         if ( direction == CLOCKWISE ):
            cls.rotate_edge( 8, ANTICLOCKWISE )
            cls.rotate_cube( CLOCKWISE )
         else:
            cls.rotate_edge( 8, CLOCKWISE )
            cls.rotate_cube( ANTICLOCKWISE )
    
    @classmethod
    def rotate_horizontal_middle( cls, direction ):
         # top middle square is 8
         # bottom middle is 53

        if ( direction == X_LEFT ):
            cls.rotate_edge( 8, ANTICLOCKWISE )
            cls.rotate_edge( 53, CLOCKWISE )
            cls.rotate_cube( X_LEFT )
        else:
            cls.rotate_edge( 8, CLOCKWISE )
            cls.rotate_edge( 53, ANTICLOCKWISE )
            cls.rotate_cube( X_RIGHT )

    @classmethod
    def rotate_vertical_middle( cls, direction ):

        if ( direction == Y_UP ):
            cls.rotate_edge( 17, CLOCKWISE )
            cls.rotate_edge( 35, ANTICLOCKWISE )
            cls.rotate_cube( Y_UP )
        else:
            cls.rotate_edge( 17, ANTICLOCKWISE )
            cls.rotate_edge( 35, CLOCKWISE )
            cls.rotate_cube( Y_DOWN )

