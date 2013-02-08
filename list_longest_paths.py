#! /usr/bin/env python

def list_longest_paths(directory, minimum_length, verbose = False):
  """Return list of filepaths longer than 'minimum_length - 1' obtained 
  recusively traversing 'directory'.
  """
  import fnmatch
  import os
  longest_paths = []
  total_count = 0
  for root, dirnames, filenames in os.walk(directory):
    for filename in filenames:
      total_count = total_count + 1
      filepath = os.path.join(root, filename)
      if len(filepath) >= minimum_length:
        longest_paths.append(filepath)
        print("[%d] %s" % (len(filepath), filepath))
      elif verbose:
        print("[%d] %s" % (len(filepath), filepath))
  return (longest_paths, total_count)
    
if __name__ == '__main__':
  from optparse import OptionParser
  usage = "usage: %prog [options] <directory>"
  parser = OptionParser(usage=usage)
  parser.add_option("-l", "--minimum-length", default=259,
                    dest="minimum_length", type="int",
                    help="specify minimum length to consider when listing the longest paths")
  parser.add_option("-v", "--verbose",
                    dest="verbose", action="store_true",
                    help="Print verbose information")
  parser.add_option("--extra-verbose",
                    dest="extra_verbose", action="store_true",
                    help="Print extra verbose information")

  (options, args) = parser.parse_args()

  requiredArgumentErrorMessage = "argument '%s' is required !"
  if len(args) != 1:
    parser.error(requiredArgumentErrorMessage % '<directory>')

  if options.extra_verbose: 
    options.verbose = True

  (longest_paths, total_count) = list_longest_paths(
    args[0], options.minimum_length, options.extra_verbose)
    
  if options.verbose:
    print("\nAnalysis summary")
    print("\tFound %d files having length >= %d by recursively traversing directory [%s]" % (len(longest_paths), options.minimum_length, args[0]))
    print("\tNumber of checked paths is %d" % total_count)


