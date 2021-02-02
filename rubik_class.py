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

class rubik:

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

    def __init__( self ):
        pass

    def draw_absolute_square( self, x, y, colour, str ):
        
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

    def draw_relative_square( self, x, y, colour, str ):
    
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

    def rotate_cube( self, direction ):

        self.orientation = pathways[ self.orientation ][ direction ]
        self.relative_cube = orientations[ self.orientation ]
        self.draw_2d_relative_cube()
 

    def exec_absolute_move( self, number ):

        temp_colour_list = [ None ] * 20

        for count in range( len( MOVES[ number ] ) ):
            temp_colour_list[ count ] = self.absolute_cube[ MOVES[ number ][count][ 0 ] ]

        for count in range( len( MOVES[ number ] ) ):
            self.absolute_cube[ MOVES[ number ][count][ 1 ] ] = temp_colour_list[ count ]


    def draw_2d_absolute_cube( self ):
    
        for square in range(54):
    
            if ( ( square % 9 ) == 8 ):
                self.draw_absolute_square( ABSOLUTE_CUBE_2D_XY[square][0],
                                           ABSOLUTE_CUBE_2D_XY[square][1],
                                           self.absolute_cube[square],
                                           unicode( self.arrows[ self.arrow_direction[ self.absolute_cube[ square ] ] ] ) )

            #    arrow_direction[ physical_cube[ square ] ] = ( arrow_direction[ physical_cube[ square ] ] + 1 ) % 4
            else:
                self.draw_absolute_square( ABSOLUTE_CUBE_2D_XY[square][0],
                                           ABSOLUTE_CUBE_2D_XY[square][1],
                                           self.absolute_cube[square],
                                           "  " )
    
    def draw_2d_relative_cube( self ):

        key = t.inkey( timeout=0.1 )
        if ( key == 'q' ):
            mf.message( "exit has been requested" )
            sys.exit( 0 )
        # If you don't actually want to display the relative version of the
        # cube on the screen then uncomment the next line
        return
        for square in range(54):
    
            self.draw_relative_square( ABSOLUTE_CUBE_2D_XY[square][0],
                                       ABSOLUTE_CUBE_2D_XY[square][1],
                                       self.absolute_cube[ self.relative_cube[square] ],
                                       str(square) )


    def get_colour( self, square ):
    
       return( self.absolute_cube[ self.relative_cube[ square ] ] )
    
    def rotate_edge( self, middle_square, clock_anti ):
    
        colour = self.get_colour( middle_square )
    
        if ( clock_anti == CLOCKWISE ):
            self.arrow_direction[ colour ] = ( ( self.arrow_direction[ colour ] + 1 ) % 4 )
        else:
            self.arrow_direction[ colour ] = ( ( self.arrow_direction[ colour ] + 3 ) % 4 )
    
        if ( clock_anti == CLOCKWISE ):
            self.exec_absolute_move( colour )
        else:
            self.exec_absolute_move( colour + 6 )
        self.draw_2d_relative_cube()
        self.draw_2d_absolute_cube()
    
    def get_edges_of_colour( self, middle_square, colour ):
    
        return_list = []
        for e in ( 1, 3, 5, 7 ):
            if ( ( self.get_colour( middle_square - 8 + e ) == colour ) ):
                return_list.append( middle_square - 8 + e )
        return return_list
    
    def rotate_top_2_layers( self, direction ):
    
        # bottom middle square is 53
    
         if ( direction == CLOCKWISE ):
            self.rotate_edge( 53, ANTICLOCKWISE )
            self.rotate_cube( CLOCKWISE )
         else:
            self.rotate_edge( 53, CLOCKWISE )
            self.rotate_cube( ANTICLOCKWISE )
    
    def rotate_bottom_2_layers( self, direction ):
    
        # top middle square is 8
    
         if ( direction == CLOCKWISE ):
            self.rotate_edge( 8, ANTICLOCKWISE )
            self.rotate_cube( CLOCKWISE )
         else:
            self.rotate_edge( 8, CLOCKWISE )
            self.rotate_cube( ANTICLOCKWISE )
    
    def rotate_horizontal_middle( self, direction ):
         # top middle square is 8
         # bottom middle is 53

        if ( direction == X_LEFT ):
            self.rotate_edge( 8, ANTICLOCKWISE )
            self.rotate_edge( 53, CLOCKWISE )
            self.rotate_cube( X_LEFT )
        else:
            self.rotate_edge( 8, CLOCKWISE )
            self.rotate_edge( 53, ANTICLOCKWISE )
            self.rotate_cube( X_RIGHT )

    def rotate_vertical_middle( self, direction ):

        if ( direction == Y_UP ):
            self.rotate_edge( 17, CLOCKWISE )
            self.rotate_edge( 35, ANTICLOCKWISE )
            self.rotate_cube( Y_UP )
        else:
            self.rotate_edge( 17, ANTICLOCKWISE )
            self.rotate_edge( 35, CLOCKWISE )
            self.rotate_cube( Y_DOWN )

rc = rubik()

