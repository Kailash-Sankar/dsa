use strict;
use warnings;
use Data::Dumper;
# There's plenty room for improvement, please add your suggesstions as notes

# let's solve Einstein's riddle
# found this riddle thanks to Sean's post  https://medium.com/@sean.handley/

my @persons = ('brit','swede','dane','norweign','german');
my @colors = ('red','green','yellow','blue','white');
my @drinks = ('tea','coffee','milk','beer','water');
my @pets = ('dogs','cats','birds','horses','fish');
my @smokes = ('paulmall','dunhill','bluemaster','blend','prince');

our $\ ="\n";
our $count =0;
our $loop = 0;
our @combo;

# permutation sub is too OP for me to have written on my on
# http://learn.perl.org/faq/perlfaq4.html#How-do-I-permute-N-elements-of-a-list
sub permute (&@) {
        my $code = shift;
        my @idx = 0..$#_;
        while ( $code->(@_[@idx]) ) {
                my $p = $#idx;
                --$p while $idx[$p-1] > $idx[$p];
                my $q = $p or return;
                push @idx, reverse splice @idx, $p;
                ++$q while $idx[$p-1] > $idx[$q];
                @idx[$p-1,$q]=@idx[$q,$p-1];
        }
}

permute { push @combo, \@_ } 1..5;

# map initial array to permuted combo based on loop index
sub map_list {
    my ($inp,$x, $debug) = @_;
    my %op;

    @op{@$inp} = @{ $combo[$x-1] };
    return \%op;
}


# check direct relationships
sub check_direct_mapping {
    my ($a,$key1,$b,$key2) = @_;

    $count++;
    return 1 if( $a->{$key1} == $b->{$key2} );
    return 0;
}

# check position related relationships
sub check_position_mapping {
    my ($a,$key1,$pos,$b,$key2) = @_;

    $count++;

    if( $pos eq 'left' && ( $a->{$key1} + 1 == $b->{$key2} ) ) {
        return 1;
    }
    elsif( $pos eq 'right' && ( $a->{$key1}  == $b->{$key2} + 1 ) ) {
        return 1;
    }
    elsif( $pos eq 'center' && $a->{$key1} == 3 ) {
        return 1;
    }
    elsif( $pos eq 'first' && $a->{$key1} == 1 ) {
        return 1;
    }
    else {
        return 0;
    }

}

# ----- real steel -----
my ($per,$col,$dri,$pet,$smo);
my ($i,$j,$k,$l,$m);

# may the force be with the loops
FIREATWILL:for($i=1; $i<=120; $i++) { $loop++;
    $per = map_list(\@persons,$i,'Nationality'); # ----- nationality -----

    #set one
    next unless check_position_mapping($per,'norweign','first');

    for($j=1; $j<=120; $j++) { $loop++;
        $col = map_list(\@colors,$j,'Color'); # ----- color -----

        #set two
        next unless check_direct_mapping($per,'brit',$col,'red');
        next unless check_position_mapping($col,'green','left',$col,'white');
        next unless ( check_position_mapping($per,'norweign','left',$col,'blue') || check_position_mapping($per,'norweign','right',$col,'blue') );

        for($k=1; $k<=120; $k++) { $loop++;
            $dri = map_list(\@drinks,$k,'Drinks');  # ----- drinks -------

            #set three
            next unless check_direct_mapping($per,'dane',$dri,'tea');
            next unless check_direct_mapping($col,'green',$dri,'coffee');
            next unless check_position_mapping($dri,'milk','center');

            for($l=1; $l<=120; $l++) {$loop++;
                $pet = map_list(\@pets,$l,'Pets');  # ----- pets -----

            #set four
            next unless check_direct_mapping($per,'swede',$pet,'dogs');

                for($m=1; $m<=120; $m++) { $loop++;
                    $smo = map_list(\@smokes,$m,'Smokes');  # ----- smokes ------

                    next unless check_direct_mapping($smo,'paulmall',$pet,'birds');
                    next unless check_direct_mapping($smo,'dunhill',$col,'yellow');
                    next unless check_direct_mapping($smo,'bluemaster',$dri,'beer');
                    next unless check_direct_mapping($smo,'prince',$per,'german');

                    next unless ( check_position_mapping($smo,'blend','left',$pet,'cats') ||  check_position_mapping($smo,'blend','right',$pet,'cats') );
                    next unless ( check_position_mapping($smo,'dunhill','left',$pet,'horses') ||  check_position_mapping($smo,'dunhill','right',$pet,'horses') );
                    next unless ( check_position_mapping($smo,'blend','left',$dri,'water') || check_position_mapping($smo,'blend','right',$dri,'water') );

                    print "Yay! found the fish guy";
                    print "nchecks : $count | loops : $loop";
                    print "final data dump:";
                    print Dumper($per);
                    print Dumper($col);
                    print Dumper($dri);
                    print Dumper($pet);
                    print Dumper($smo);
                    last FIREATWILL;
                }
            }
        }
    }
}

#woop woop