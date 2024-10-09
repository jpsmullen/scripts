#!/usr/bin/env perl

#==============================================
# Stupidly simple script for making decisions.
#==============================================

use v5.38;
use open qw(:std :encoding(utf8));

my @options;

# Read (non-blank) options line by line from STDIN
while (<>) {
    push(@options, $_) if /\S/;
}

if (@options) {
    say "=" x 30;

    # Choose a random option
    print $options[rand(scalar @options)];

    say "=" x 30;
} else {
    say "No options provided.";
}
