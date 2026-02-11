Topic: Merge Conflicts

Definition:
A merge conflict occurs when Git cannot automatically merge changes because the same line was modified differently in two branches.

Conflict Markers:
<<<<<<< HEAD
=======
>>>>>>> branch-name

Steps to Resolve:
1. Open conflicted file
2. Remove conflict markers
3. Choose or combine changes
4. git add file
5. git commit

Conflicts are normal in team projects.
