# Search the Entire Git History for a String

Search every commit in a repository for a string and save the matches to a file with a timestamped name.

## 1. Set up Bash in IntelliJ (Windows)

These commands need Bash, not PowerShell or cmd.

1. In IntelliJ, open **File > Settings > Tools > Terminal**.
2. Set **Shell path** to:
   ```
   C:\Users\J1008607\AppData\Local\Programs\Git\bin\bash.exe
   ```
3. Open a new terminal tab and `cd` into the repository root.

## 2. Run the search

Replace `alexander.lisak` with the string you want to find.

### Matching lines only

```bash
git rev-list --all | while read -r commit; do
    git grep -n -i -F "alexander.lisak" "$commit" -- 2>/dev/null || true
done > "git-history_$(date '+%Y%m%d_%H%M%S').txt"
```

### With 5 lines of context above and below

```bash
git rev-list --all | while read -r commit; do
    git grep -n -i -F -C 5 "alexander.lisak" "$commit" -- 2>/dev/null || true
done > "git-history_$(date '+%Y%m%d_%H%M%S').txt"
```

### With 10 lines above and 20 below

```bash
git rev-list --all | while read -r commit; do
    git grep -n -i -F -B 10 -A 20 "alexander.lisak" "$commit" -- 2>/dev/null || true
done > "git-history_$(date '+%Y%m%d_%H%M%S').txt"
```

## 3. Read the output

The results go to a file in the current directory, for example `git-history_20261117_143005.txt`. Each line has the form:

```
<commit-hash>:<file-path>:<line-number>:<line content>
```

With context options, context lines use `-` in place of `:` after the line number, and `--` separates the groups of matches.

## What each part does

| Part | Purpose |
|------|---------|
| `git rev-list --all` | Lists every commit on all branches and tags |
| `while read -r commit` | Loops over the commits one at a time |
| `git grep ... "$commit"` | Searches the files as they were in that commit |
| `-n` | Shows line numbers |
| `-i` | Ignores case |
| `-F` | Treats the search string as plain text, not a regex (so `.` matches only a literal dot) |
| `-C 5` | Shows 5 lines of context above and below |
| `-B 10` / `-A 20` | Shows 10 lines before / 20 lines after |
| `--` | Ends the options so the commit isn't read as a path |
| `2>/dev/null` | Hides error messages |
| `\|\| true` | Keeps the loop going when a commit has no matches |
| `> "git-history_$(date ...).txt"` | Writes everything to a file named with the current date and time |

## Notes

- The same line shows up once for every commit that contains it. Unchanged files repeat across many commits, so the output can be large.
- On big repositories this can take a long time, because it searches every commit in full.
- Add the output files to `.gitignore` (`git-history_*.txt`) so they don't get committed by accident.
