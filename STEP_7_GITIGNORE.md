Topic: .gitignore

Definition:
.gitignore tells Git which files or folders to ignore.

Why use it:
- Avoid pushing sensitive files
- Avoid pushing large unnecessary files
- Keep repository clean

Common Patterns:
*.log → ignore all log files
folder/ → ignore folder
.env → ignore environment file

Important:
If file is already committed, use:
git rm --cached filename
