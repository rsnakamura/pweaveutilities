Feature: A file-tree-structure mover.
 Scenario: Flat file structure
   Given a flat file structure for the mover
   When the mover is run
   Then the new file structure has the old files
   And the old file structure doesn't have the old files

 Scenario: A Tree folder structure
   Given a tree structure for the mover
   When the mover is run
   Then the new tree file structure has the old files
   And the old file structure doesn't have the old files
