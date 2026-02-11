Topic: Undoing Changes

1. git restore file → undo file changes
2. git restore --staged file → unstage file
3. git reset --soft HEAD~1 → remove commit but keep changes
4. git reset --hard HEAD~1 → remove commit and delete changes
5. git revert commit-id → safely undo commit

Reset rewrites history.
Revert preserves history.
