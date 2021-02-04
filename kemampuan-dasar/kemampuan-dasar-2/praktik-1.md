Hilarius Perdana@DESKTOP-DF14PID MINGW64 /g/praxis-academy/kemampuan-dasar/kemampuan-dasar-2 (master)
$ mkdir rhymes

Hilarius Perdana@DESKTOP-DF14PID MINGW64 /g/praxis-academy/kemampuan-dasar/kemampuan-dasar-2 (master)
$ cd rhymes

Hilarius Perdana@DESKTOP-DF14PID MINGW64 /g/praxis-academy/kemampuan-dasar/kemampuan-dasar-2/rhymes (master)
$ git init
Initialized empty Git repository in G:/praxis-academy/kemampuan-dasar/kemampuan-dasar-2/rhymes/.git/

Hilarius Perdana@DESKTOP-DF14PID MINGW64 /g/praxis-academy/kemampuan-dasar/kemampuan-dasar-2/rhymes (master)
$ touch README.txt

Hilarius Perdana@DESKTOP-DF14PID MINGW64 /g/praxis-academy/kemampuan-dasar/kemampuan-dasar-2/rhymes (master)
$ git add README.txt

Hilarius Perdana@DESKTOP-DF14PID MINGW64 /g/praxis-academy/kemampuan-dasar/kemampuan-dasar-2/rhymes (master)
$ git commit -m 'First commit.'
[master (root-commit) 188560c] First commit.
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 README.txt

Hilarius Perdana@DESKTOP-DF14PID MINGW64 /g/praxis-academy/kemampuan-dasar/kemampuan-dasar-2/rhymes (master)
$ echo 'This repo is a collection off my favorite nursery rhymes.' >> REDME.txt

Hilarius Perdana@DESKTOP-DF14PID MINGW64 /g/praxis-academy/kemampuan-dasar/kemampuan-dasar-2/rhymes (master)
$ ^C

Hilarius Perdana@DESKTOP-DF14PID MINGW64 /g/praxis-academy/kemampuan-dasar/kemampuan-dasar-2/rhymes (master)
$ echo 'this repo is a collection off my favorite nursery rhymes.' >> README.txt

Hilarius Perdana@DESKTOP-DF14PID MINGW64 /g/praxis-academy/kemampuan-dasar/kemampuan-dasar-2/rhymes (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.txt

no changes added to commit (use "git add" and/or "git commit -a")

Hilarius Perdana@DESKTOP-DF14PID MINGW64 /g/praxis-academy/kemampuan-dasar/kemampuan-dasar-2/rhymes (master)
$ git diff
warning: LF will be replaced by CRLF in README.txt.
The file will have its original line endings in your working directory
diff --git a/README.txt b/README.txt
index e69de29..9f9ea78 100644
--- a/README.txt
+++ b/README.txt
@@ -0,0 +1 @@
+this repo is a collection off my favorite nursery rhymes.

Hilarius Perdana@DESKTOP-DF14PID MINGW64 /g/praxis-academy/kemampuan-dasar/kemampuan-dasar-2/rhymes (master)
$ git add README.txt
warning: LF will be replaced by CRLF in README.txt.
The file will have its original line endings in your working directory

Hilarius Perdana@DESKTOP-DF14PID MINGW64 /g/praxis-academy/kemampuan-dasar/kemampuan-dasar-2/rhymes (master)
$ git commit -m 'Added project overview to README.txt'
[master a12a24c] Added project overview to README.txt
 1 file changed, 1 insertion(+)

Hilarius Perdana@DESKTOP-DF14PID MINGW64 /g/praxis-academy/kemampuan-dasar/kemampuan-dasar-2/rhymes (master)
$ wget https://www.acquia.com/sites/default/files/blog/hokey-pokey.txt
bash: wget: command not found

Hilarius Perdana@DESKTOP-DF14PID MINGW64 /g/praxis-academy/kemampuan-dasar/kemampuan-dasar-2/rhymes (master)
$ git remote add origin https://github.com/hilariusperdana/praxis-academy/kemampuan-dasar/kemampuan-dasar-2/rhymes

Hilarius Perdana@DESKTOP-DF14PID MINGW64 /g/praxis-academy/kemampuan-dasar/kemampuan-dasar-2/rhymes (master)
$ git push -u origin master
remote: Not Found
fatal: repository 'https://github.com/hilariusperdana/praxis-academy/kemampuan-dasar/kemampuan-dasar-2/rhymes/' not found

Hilarius Perdana@DESKTOP-DF14PID MINGW64 /g/praxis-academy/kemampuan-dasar/kemampuan-dasar-2/rhymes (master)
$
