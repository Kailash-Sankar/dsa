use strict;
use warnings;
use Data::Dumper;

# Ideal solutions consider the board as an array but here the board is a hash
# the logic is to brute force using recursion
# Uniquness of row is ensured by key
# Uniquness of column is ensured by value
# Diagionals are computed and verified


my (%board,%marked_cols,$n);

# each recursion performs checks along a row
# for each column we run 2 checks - one along the column & one along the diagonals
sub set_queen {
    my $row = shift;
    my $retrace;

    %marked_cols = ( map { $_ => 1 } values %board );

    #recursion is scary...
    for( my $col=1; $col <=$n; $col++) { #col
        next unless col_check($col);
        next unless diag_check($row,$col);

        $board{$row} = $col; #queen deployed to these coordinates.
        $retrace = set_queen( $row + 1 ) if $row < $n;
        next if $retrace;
        return 0; #all set.
    }
    #loop exits afer checking all columns
    #so we retrace back after removing the previous position.
    delete $board{$row-1};
    %marked_cols = ( map { $_ => 1 } values %board );
    return 1;
}

sub col_check {
    my $x = shift;
    return 0 if defined $marked_cols{$x};
    return 1;
}

# i know there's a better way to check diagonals
# i just haven't found it yet
sub diag_check {
    my ($x,$y)  = @_;

    #upper right
    my ($i,$j);
    for( $i=$x + 1,$j=$y + 1; $i<=$n && $j<=$n; $i++, $j++) {
        if( exists $board{$i} && $board{$i} == $j ) { #that position is occupied
            return 0;
        }
    }

    #lower left
    for( $i=$x - 1,$j=$y - 1; $i >=1 && $j >=1; $i--, $j--) {
        if( exists $board{$i} && $board{$i} == $j ) { #that position is occupied
            return 0;
        }
    }

    #upper left
    for( $i=$x + 1,$j=$y - 1; $i<=$n && $j>=1; $i++, $j--) {
        if( exists $board{$i} && $board{$i} == $j ) { #that position is occupied
            return 0;
        }
    }

    #lower right
    for( $i=$x - 1,$j=$y + 1; $i >=1 && $j <=$n ; $i--, $j++) {
        if( exists $board{$i} && $board{$i} == $j ) { #that position is occupied
            return 0;
        }
    }

    return 1;
}

sub solve_for_board {
    $n = shift;

    set_queen(1); #start from the first row

    for( my $i=$n; $i>=1; $i--) {
        for( my $j=1; $j<=$n; $j++) {
            if ( $board{$i} == $j ) { print "  X" ; }   else { print "  ="; }
        }
        print "\n";
    }
}

#8 queens
solve_for_board(8);