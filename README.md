This is a Python learning project.  I started with no python skills and wanted to learn how to
use the language, particularly to gain some understanding of how to create a class from scratch.

The project models a 3x3x3 Rubik's cube in a 2D "net".  It provides the ability to muddle the
cube and then solve it.

Python's blessed library is required.  I have tested only on Linux but I believe that blessed
now works with Windows too.

I have made very little attempt to accommodate different terminal screen sizes so expect messy
results unless your terminal supports about 50 rows and a reasonably large number of
columns.

Note that speed of both muddling and solving are deliberately slowed by timeout=0.1 parameter
below.  This effectively adds a 0.1 second sleep every time a redraw occurs.  And you can enable
simultaneously displaying a second "relative" view of the cube by removing the "return" statement
below.  This requires a wider terminal screen to display and is mainly useful for debugging.

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

