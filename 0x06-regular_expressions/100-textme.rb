#!/usr/bin/env ruby
x = ARGV[0].scan(/(from:)(\+?[A-Za-z0-9]+)(...)(to:)(\+?[A-Za-z0-9]+)(...)(flags:)((-?[0|1]:?)+)/)
print(x[0][1] + "," + x[0][4] + "," + x[0][7])
print("\n")
