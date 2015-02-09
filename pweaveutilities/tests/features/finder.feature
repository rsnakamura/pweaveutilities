Feature:: A `Finder` function that generates names that match the files of interest
 Scenario Outline: Finder file matching
   Given a finder with a root set to a directory with <count> matching file(s)
   When the finder's outcome is checked
   Then the finder's outcome matches the expected

 Examples: files
 | count   |
 | one     |
 | no      |
 | several |

 Scenario: Sub-folder matching
   Given a finder with a set of nested folders
   When the finder's outcome is checked
   Then the finder's outcome matches the expected
