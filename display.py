#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import time
from blessed import Terminal

t = Terminal()

class message_frame:

    current_line = 0
    def __init__( self, array_size, line_length, left_margin, t ):
        self.array_size = array_size
        self.line_length = line_length
        self.left_margin = left_margin
        self.msg_buffer = [ None ] * ( array_size + 1 )
        self.t = t
    def message( self, msg ):
        if ( ( len( msg ) ) > self.line_length ):
            msg = msg[ :self.line_length ]
        else:
            msg = ( msg.ljust( self.line_length ) )
        if ( self.current_line < self.array_size ):
            self.current_line += 1
            self.msg_buffer[ self.current_line ] = msg
            sys.stdout.write( t.move( t.height - ( 2 + self.array_size + 1 - self.current_line ), self.left_margin ) + msg )
        else:
            for line in range( ( len( self.msg_buffer ) - 1 ) ):
                self.msg_buffer[ line ] = self.msg_buffer[ line + 1 ]

            self.msg_buffer[ self.array_size ] = msg
            count = self.array_size 
            for m in self.msg_buffer:

                sys.stdout.write( t.move( t.height - ( 2 + count ), self.left_margin ) + m )
                count -= 1

        sys.stdout.flush()

mf = message_frame( 11, 80, 4, t )

def print_info_block():
    top_row =    u'┌───────────────────────────────────────────────────────────────┐'
    middle_row = u'│ Press m to muddle the cube, press s to solve, press q to quit │'
    bottom_row = u'└───────────────────────────────────────────────────────────────┘'
    sys.stdout.write( t.move( 29, 2 ) + top_row )
    sys.stdout.write( t.move( 30, 2 ) + middle_row )
    sys.stdout.write( t.move( 31, 2 ) + bottom_row )
