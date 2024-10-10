#!/usr/bin/env perl

#===============================================================================
# Simple script for sorting (non-blank) lines from files or the command line in
# case-insensitive alphabetical order.
#===============================================================================

use v5.38;
use open qw(:std :encoding(utf8));

sub sort_lines_from_file($file) {
    do {
        warn "-" x 50, "\n";
        warn "Can't open $file: $!\n";
        warn "-" x 50, "\n";

        return;
    } unless open(my $fh, "<", $file);

    my @lines;

    while (<$fh>) {
        # Don't push blank lines
        push(@lines, $_) if /\S/;
    }

    close $fh;

    if (@lines) {
        # Case-insensitive sorting
        @lines = sort {fc($a) cmp fc($b)} @lines;
    }

    return @lines;
}

if (@ARGV) {
    my $last_file_sorted = 0;

    foreach my $file (@ARGV) {
        my @lines = sort_lines_from_file($file);
        next unless @lines; # Skip blank files

        # Print a separator with the filename in the middle
        say "=" x 20, " $file ", "=" x 20;

        # Print the sorted lines
        for my $i (1 .. scalar @lines) {
            print "$i. $lines[$i - 1]";
        }

        $last_file_sorted = 1 if $file eq $ARGV[-1];
    }

    say "=" x 50 if $last_file_sorted;
} else {
    # If no files are specified, sort lines from STDIN
    #
    # Useful if you want to sort lines directly from the command line; you can
    # also sort the output of other programs being piped into this script

    my @lines;

    while (<>) {
        push(@lines, $_) if /\S/;
    }

    if (@lines) {
        @lines = sort {fc($a) cmp fc($b)} @lines;

        say "=" x 50;

        for my $i (1 .. scalar @lines) {
            print "$i. $lines[$i - 1]";
        }

        say "=" x 50;
    } else {
        say "No lines provided.";
    }
}
