````
-------------------------------------------------------------------------------------f
-> Title : Git Notes
-> Author: @neeraj-singh-jr
-> Status : Ongoing...
-> Created : 05/12/2022
-> Updated : 01/06/2025
-> Summary : Notes indices are as follows (**** pending)
-------------------------------------------------------------------------------------
-> Q019 : Worktree Usages in Git lifecycle;;
-> Q018 : Open Different Branches in IDE in a Machine;;
-> Q017 : Usages for PUSH command with -U flag;;
-> Q016 : Stash Commands for Productive Work;;
-> Q015 : Git Pull and Rebase Together in One Go;;
-> Q014 : Remove Last commit from Git;;
-> Q013 : How Git Reset Command allows time-travel;;
-> Q012 : Remove the Untracked files in git project;;
-> Q011 : Update Remove Repository SSH url link;;
-> Q010 : Reset Head or Go Back & Forth in Commits History;;
-> Q009 : Tags Creation in Git;;
-> Q008 : Rename Command using Git;;
-> Q007 : Create Alias in Git;;
-> Q006 : Show commit logs in Graph Style;;
-> Q005 : Revert Changes from Staged Area ;;
-> Q004 : Difference in Manual Add and Commit with '-am' Flag;;
-> Q003 : Check code changes pulled from origin;;
-> Q002 : Git Favourite Commands;;
-> Q001 : What is Git;;
-------------------------------------------------------------------------------------
````

### GIT NOTES : BEGINNING

-------------------------------------------------------------------------------------
### Q019 : Worktree Usages in Git lifecycle;;

Suppose you have a repo: `dsa`

You want:

Branch `master` → Work normally.

Branch `feature/study_notes` → Open separately.

Instead of cloning again, use git worktree.

Step-by-Step:

#### 1. Go inside your main project folder:

```bash

cd ~/projects/my-project
```

#### 2. 2. Create a worktree (new folder) for another branch:

```bash

git worktree add study_notes_wt feature/study_notes
```

`study_notes_wt` → New folder name you want.

`feature/study_notes` → Branch name you want to work on.

> If branch `feature/study_notes` doesn't exist, Git will auto-create it for you.


#### 3. Now your setup is like:

Folder Branch inside should like this,

`root/dsa`/  -> `master`
`root/dsa/study_notes_wt/` -> `feature/study_notes`


#### Some Quick Worktree Commands

**List active worktrees:**

```bash
git worktree list

# OUTPUT
# /var/www/html/dsa                 98d66e5 [feature/neetcode_dsa]
# /var/www/html/dsa/study_notes_wt  b7c1caa [feature/study_notes
```

**Remove a worktree (after you're done):**

```bash
git worktree remove study_notes_wt
```


#### Important Tips:

- Each worktree is fully independent — `commit`, `pull`, `push` separately.

- Only one `.git` is needed (inside the main repo).

- Saves a lot of disk space.

- Makes multi-branch development buttery smooth.


#### Hack for Worktree Untracked File !!!

- When you create a worktree then it will create a folder which will be shown in 
`git status` `untracked file`. So To avoid this situation add the untracked files 
to `.gitignore` version.


-------------------------------------------------------------------------------------
### Q018 : Open Different Branches in IDE in a Machine;;

Here's how you can do it:

#### Method 1: Clone (Clone Single Project Multiple times)

Make two separate folders for the same repo.

In Folder A, checkout Branch A.

In Folder B, checkout Branch B.

for eg,

```bash
git clone https://github.com/your-repo.git project-branchA

cd project-branchA

git checkout branchA
```

and one more time

```bash

git clone https://github.com/your-repo.git project-branchB

cd project-branchB

git checkout branchB
```

Now you can open project-branchA in VSCode and project-branchB in PyCharm
(or two VSCode windows, whatever).

- No conflicts.
- Different IDEs.
- No branch mixing.



#### Method 2 : Worktree (Single Clone, Different Checkouts in Different IDE)

You can technically use git worktree feature to have different branches
checked out into different folders without re-cloning.

But for now, since you asked about IDEs, simple cloning is much easier and
practical.

```bash
cd your-project

git worktree add ../branchA branchA

git worktree add ../branchB branchB
```

Now you have:

- `your-project/`

- `../branchA/`

-`../branchB/`

(And you can open both folders separately.)


-------------------------------------------------------------------------------------
### Q017 : Usages for PUSH command with -U flag;;

Difference Between `git push` and `git push -u`

#### **1 `git push`**

- Pushes your **local branch** to the remote repository.  

- If the branch **already has a remote tracking branch**, this works without
  issues.  

- **Example:**  
  ```sh
  git push origin dev
  ```
  This pushes the `dev` branch to `origin` (remote repository).  

---

#### **2 `git push -u` (or `--set-upstream`)**

- This **sets a tracking connection** between your local branch and the remote
  branch.  

- Used when pushing a **new local branch** for the first time.  

- After using `git push -u`, you can **simply use `git push`** next time
  without specifying the remote and branch.  

- **Example:**  
  ```sh
  git push -u origin dev
  ```
  This:  
  - Pushes `dev` to `origin`.  
  - Sets `origin/dev` as the **upstream** branch.  
  - Allows future `git push` and `git pull` without needing `origin dev`.  


-------------------------------------------------------------------------------------
### Q016 : Stash Commands for Productive Work;;

**CASE 1 : Push Stash with a customer message:** 

```bash
$ git stash push -m "custom-message-here"
```

**CASE 2 : List number of file changes in Stash:**

```bash
$ git stash show stash@{0}
```

**CASE 3 : Show the file content difference in Stash**

```bash
$ git stash show -p stash@{0}
```


-------------------------------------------------------------------------------------
### Q015: Git Pull and Rebase Together in One Go;;
 
Below Command to show this - On Go 

**SYNTAX : `git pull --rebase origin master`** 

#### Explained  

This command is used to **update** your current branch with the latest changes
from `master` while keeping a **clean history**.  

---	

#### **Breaking It Down:**

**1. `git pull`**

- Fetches new changes from the `origin` (remote repository).

- Merges them into your current branch by default (unless `--rebase` is
  used).

**2. `--rebase`**

- Instead of a merge commit, it **reapplies your local commits** on top of the
  latest `master` branch.

- Keeps a **linear commit history** (avoids unnecessary merge commits).

**3: `origin master`**

- `origin` → Refers to the remote repository.  

- `master` → The branch from which updates are pulled.

---

#### **What Happens Step by Step?**

1. **Fetch latest changes** from `master` into your local repository.

2. **Rewind your local commits** (temporarily saving them).

3. **Update your branch** to the latest `master` state.

4. **Replay your local commits** on top of the updated `master`.

---

### **Example Scenario:**

**(a) Before `git pull --rebase origin master`**

```
A---B---C (your branch)
     \
      D---E---F (master has new commits)
```

**(b) After `git pull --rebase origin master`**

```
D---E---F---A'---B'---C' (your branch rebased)
```

Your local commits **A, B, C** are **rebased** on top of the latest `master`.

---

#### ** Why Use This?**

- **Avoids extra merge commits** (`Merge branch 'master'` clutter).  

- **Keeps history clean** and linear.  

- **Works better for collaborative workflows** (especially when rebasing
    feature branches).  

---

#### **If You Face Conflicts:**

Git will pause and ask you to resolve conflicts in each file.  

👉 After resolving conflicts, run:

```sh
git rebase --continue
```
If things go wrong, **abort the rebase** with:

```sh
git rebase --abort
```

---

#### **When to Use It?**

Use `git pull --rebase origin master` when you:  

- Want to **update your branch** while keeping a clean history.  

- Are working in a **team** and need to avoid unnecessary merge commits.  

- Prefer **linear commit history** over merge-based commits.  


-------------------------------------------------------------------------------------
### Q014 : Remove Last commit from Git;;

--- 

#### METHOD 1 :

SYNTAX:-

```bash
$ git reset --soft HEAD^
```

**Explanation:**

- **`git reset`:** This is the main command for moving the HEAD pointer of
    your local repository.

- **`--soft`:** This option specifies that only the HEAD pointer should be
    moved. The changes introduced by the commit to be reset will remain in
    the staging area (index).

- **`HEAD^`:** This refers to the parent commit of the current HEAD. In other
   words, it moves the HEAD pointer back to the previous commit.

**How it works:**

1. **Moves HEAD:** The command moves the HEAD pointer back one commit.

2. **Changes staged:** The changes introduced by the commit that was "reset"
are now staged for the next commit.

---

#### METHOD 2: 

SYNTAX:-

```bash
$ git reset --soft HEAD~1
```

This has the same effect as `HEAD^`, but it might be more intuitive for some 
users.

**Important Notes:**

- **Uncommitted changes:** This command does not affect any uncommitted
    changes in your working tree.

- **Caution:** Use `git reset` with caution, as it can alter your commit
    history. Always understand the implications of using this command before
    executing it.

This command allows you to easily revert the most recent commit while
preserving the changes introduced by that commit in the staging area, making
it easier to amend or re-apply them in a different way.

---

#### METHOD 3: 

you can also use git commit of previous or any commit you wanted to jump on.

SYNTAX:

```bash
$ git reset --hard/--soft <SHA-COMMIT-ID>
```

**NOTE:**

- Here also the --hard/--soft will do the same thing. only notable difference
  is the commid-id which you can get from the git log command without any
  efforts.
- But here you must know which commit-id to jump. For trial purpose use
  `--soft` for not disturbing any existing code flows.


-------------------------------------------------------------------------------------
### Q013 : How Git Reset Command allows time-travel;;

Your confusion seems to be about how `git reset --hard` allows you to "go
back" to a previous commit even though you haven’t re-committed anything new.
Let me break it down.

---

#### **1. Problem Statement for Git Reset**

- Initially, your `git log` showed this commit history:

```
41f6389 (HEAD -> master) re-commit 4
ae59dee commit 3
25b4d78 commit 2
07280ad pilot commit
  ```

- Then you **reset hard** to `07280ad`:

	```
	git reset --hard 07280ad
	```

	- This **removed all commits after** `07280ad` from your branch history.
	- Your `git log` now only showed:

    ```
    07280ad (HEAD -> master) pilot commit
    ```

  - This means commits `41f6389`, `ae59dee`, and `25b4d78` were **not lost**,
    but they were **removed from the branch history**.

- You then made a new commit (`e6d56e8`):

  ```
  [master e6d56e8] Re-Commit Hitory
  ```

  So, now your commit history looked like:

  ```
  e6d56e8 (HEAD -> master) Re-Commit Hitory
  07280ad pilot commit
  ```

---

#### **2. How Did You Get Back to `41f6389` (Refer Initial Commit)?**

After that, you ran:

```
git reset --hard 41f6389
```

Since `41f6389` was a previous commit in your history, Git was able to find
it **even though it was removed from the branch earlier**.

Git keeps track of past commits in the **reflog** (a record of previous HEAD
positions), so `41f6389` was still recoverable.

After this reset, your commit history was back to:

```
41f6389 (HEAD -> master) re-commit 4
ae59dee commit 3
25b4d78 commit 2
07280ad pilot commit
```

This is why it **looks like you "traveled back in time"** without
re-committing anything.

---

#### **3. Why Was This Possible? (`git reflog`)**

Git maintains an internal log of every action that moves `HEAD`. 

You can view it using:

```sh
$ git reflog
```

You'll see something like:

```
e6d56e8 HEAD@{0}: reset: moving to 41f6389
07280ad HEAD@{1}: commit: Re-Commit Hitory
41f6389 HEAD@{2}: reset: moving to 07280ad
```

This is why even after `reset --hard`, you could return to an earlier commit.

---

### **4. Key Takeaways**

- `git reset --hard <commit>` **moves HEAD** to that commit and discards all
  later commits **from branch history**.

- The old commits **are not deleted**; they are still stored in Git’s database
  and retrievable through `git reflog`.

- If you accidentally reset and want to recover lost commits, use:

- for eg, 

```sh
git reflog
git reset --hard <SHA of lost commit>
```


-------------------------------------------------------------------------------------
### Q012 : Remove the Untracked files in git project;;

To remove the untracked files from the git project

````
# List untracked files using git;;
$ git clean -n

# Remove untracked file with interaction;;
$ git clean -i

# Forcefully remove untracked file;;
$ git clean -f

# If there are folder which needs to be removed,
$ git clean -f -d 
````

NOTE: `Checkout` only remove the modified changes only.


-------------------------------------------------------------------------------------
### Q011 : Update Remove Repository SSH url link;; 

This Scenario can be used to update the existing remote link with the newer
one. 

Like this,

````
# Intial SSH URL 
$ git remote add origin git@bitbucket.org:sqrrl-fintech/repo1.git
$ git remote -v

# OUTPUT:
origin	git@bitbucket.org:sqrrl-fintech/repo1.git (fetch)
origin	git@bitbucket.org:sqrrl-fintech/repo1.git (push)
````

#### New SSH URL
````
$ git remote set-url origin git@bitbucket.org:sqrrl-fintech/repo2.git
$ git remote -v

# OUTPUT:
origin	git@bitbucket.org:sqrrl-fintech/repo2.git (fetch)
origin	git@bitbucket.org:sqrrl-fintech/repo2.git (push)
````

#### To Remove Existing Remote Url

> SYNTAX: git remote rm remote_name

Refer example below,

````
$ git remote -v 

# OUTPUT :
origin  git@bitbucket.org:sqrrl-fintech/repo2.git (fetch)
Here remote_name = origin,
and remote_url = git@bitbucket.org:sqrrl-fintech/repo2.git

$ git remote rm origin

````


-------------------------------------------------------------------------------------
### Q010 : Reset Head or Go Back & Forth in Commits History

`Reset command` is used to move changes back and forth from git commits
timeline. Suppose you've a git timeline is like this,

````
# Commit Timeline, Initially
* ace6055 (HEAD -> master, tag: v1) added c <-- HEAD NOW
* 860ce77 staged commit
* 8172daf 2 files
* 0aab975 author
* 3b6b754 added first file
````

Suppose now you want to go the first commit, but you want to keep the
latest changes. Basically you just want to move point your head on the
first commit then prefer soft reset. Like this,

````
$ git reset --soft 3b6b754

# Commits Timeline, Soft Reset
* ace6055 (tag: v1) added c
* 860ce77 staged commit
* 8172daf 2 files
* 0aab975 author
* 3b6b754 (HEAD -> master) added first files <-- HEAD NOW
````

for this same case, now you want to move all your changes back to the very
first commit changes then prefer the hard reset. In this all the files
structure move back to the first commit changes, But you commits history
will be maintained. Like this, 

````
$ git reset --hard 3b6b754

# Commit Timeline, Hard Reset
* ace6055 (tag: v1) added c
* 860ce77 staged commit
* 8172daf 2 files
* 0aab975 author
* 3b6b754 (HEAD -> master) added first file
````

now suppose you have fixed few changes from the first commit and then you
want to go back to the latest commit then, do the similar step with hard.

````
$ git reset --hard ace6055

# Commit Timeline, Like Initially
* ace6055 (HEAD -> master, tag: v1) added c
* 860ce77 staged commit
* 8172daf 2 files
* 0aab975 author
* 3b6b754 added first file
````

-------------------------------------------------------------------------------------
### Q009 : Tags Creation in Git;;

Tags are use to label the branch tracking the changes till current specific
requirements.

#### Create Tags:

> $  git tag your-new-tags

or, you can pass message as well

> $ git tag -a v1 -m "your new message"

#### List Tags: 	

> $ git tag --list

#### Delete Tags:

````
# FROM REMOVE REPO:-
$ git push origin :your-remote-tag
````
````
From LOCAL REPO:
$ git tag -d your-local-tag
````

#### Create Tag for a specific Commit:-

> $ git tag -a v1 -m "previous release" ac34522e

#### Create tag for current or any other branch

> $ git tag stable-release master

or, for another branch

> $ git tag unstable-release develop

#### Push tag to Remote Repo 

if you wanted to push all the tags, then this command,

> $ git push --tags

for single tag push, use this command

> $ git push origin tag-name

for eg,
````
$ git push origin stable
$ git push origin unstable
````

#### Renaming Tag in Git

This will rename the git tag.

> $ git tag -f stable master


-------------------------------------------------------------------------------------
### Q008 : Rename & Delete Command using Git;;

**NOTE: Even if you have stage the changes then the changes will be reflect
there as well. Renamed file will be shown there.**

#### CASE : RENAME COMMAND

Suppose you have file using temp.txt => demo.txt, then and no changes will be
shown, everything will be up to date.

for eg,
````
# you can use this command;
$ git mv temp.txt demo.txt
````

**NOTE: git mv vs linux mv**

Fyi, in any case if you're thing that this renaming with mv git command can be
easilty achievable using the normal mv command, then in that case the
behaviour would be different. 

For an instance, 

````
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	new file:   deltest.txt
	new file:   rentest.txt

# Then, move(mv) commands, 
$ mv rentest.txt ren_test.txt 

# Result would be, like

$ git status
On branch master
Changes to be committed:
	new file:   deltest.txt
	new file:   rentest.txt

Changes not staged for commit:
	deleted:    rentest.txt

Untracked files:
	ren_test.txt

````

#### CASE : DELETE COMMAND
For deleting a file or stage files, you can use this command

for eg,
````
$ git rm demo.txt
````

-------------------------------------------------------------------------------------
### Q007 : Create Alias in Git;;

Git gives you alias command to make alias for long commands, like this 

Example 1: Git about "your message
````
git config --global --add alias.remark '
	!describe() { 
		msg="$1"; 
		git config branch."$(git branch --show-current)".description ${msg:+"$msg"}; 
	}; describe'
````

Example 2: Add pretty logs in graph style
````
git config --global --add alias.plogs 
	'!describe() {
		git log --oneline --graph --decorate --all;
	}; describe'
````

Example 3: Add alias to show conflicts in files
````
git config --global --add alias.conflicts '
	!describe() { 
		git diff --name-only --diff-filter=u; 
	}; describe'
````


-------------------------------------------------------------------------------------
### Q006 : Show commit logs in Graph Style;;

Use this command to show logs in Graph style,
````
$ git log --oneline --graph --decorate --all
````

-------------------------------------------------------------------------------------
### Q005 : Revert Changes from Staged Area ;;

Suppose you made a few changes in your profile files(a.txt), then

you've added it to staging area
````
$ git add .
````

but now you want to add few more changes to the same commit, then
````
$ git reset HEAD
````

This will revert you stages changes to unstages state.


-------------------------------------------------------------------------------------
### Q004 : Difference in Manual Add and Commit with '-am' Flag;;

#### Case 1 : Manually Add using Git

In this you, manually saying git to add all my changes to staging area

Your changes can include - Modified, Untraced, Updated etc.

You can do so by 
````
$ git add .
$ git commit -m "your-msg"
````

#### Case 2 : Automatic Add using Git

In this case, you are just using commit and add in the same commit command and
saying the git to first add all changes then commit the changes

**NOTE: Here is a catch. Which says, this automatic add and commit wont work
  when you've  new untraced files in your changes. --Use Old School Style**

In this case it will fail to add the files changes.

````
# You can check if you're file is alread tracked by git or not using below command
# This will list you the tracked files names.
$ git ls-files


# If you 've not Untraced files, then go for it
$ git commit -am "your-msg"
````


-------------------------------------------------------------------------------------
### Q003 : Check code changes pulled from origin;;

Problem statments says:
Suppose you are coming back to project after few days. But you are not sure
that what types of changes have been commited in your absencies then prefer
the below method for `fetch-diff`.

Assuming you are on develop branch of your project,

Then proceed as following

````
// On Terminal

# Fetch everything from the remote/develop branch;;
$ git fetch origin develop

# Check the difference using the diff command;;
$ git diff origin/develop 

# If everything ok, then merge 
# make sure u're on develop branch before
$ git merge origin/develop

````


-------------------------------------------------------------------------------------
### Q002 : Git Favourite Commands;;;;

#### GIT FAVOURITE COMMANDS :-

````
//--- Delete remote branch;;
$ git push origin :branch-name

//--- Set upstream for local branch to remote;;
$ git branch --set-upstream-to origin feature-branch

//--- Short version to set upstream with very first push;;
$ git push -u origin local-branch

//--- Show up which remote branch a local branch is tracking;;
$ git branch -a

//--- Show local branch sync;;
$ git branch -v

//--- Fetch and pull branch;;
$ git fetch origin BAC-2633-transaction-apis-create-lumpsum
$ git checkout BAC-2633-transaction-apis-create-lumpsum

//--- Push from different local branch to different remote branch;;
git push <remote> <branch with new changes>:<branch you are pushing to>
for eg, $ git push origin branch-1:branch-2

//--- fetch origin;;
$ git fetch --all

//--- Pull with origin master (refer Q015 for Details);;
$ git pull --rebase origin master

//--- Setup Email for Local Repo;;
$ git config --local user.email <your_email>

//--- Clone Single branch from Repo:
$ git clone -b <branch_name> <repo_url>
$ git clone -b <branch_name> --single-branch <repo_url>

//--- view all settings
$ git config --list --show-origin

//--- Global configurations for your git
$ git config --global user.name "John Doe"
$ git config --global user.email johndoe@example.com
$ git config --global init.defaultBranch main

//--- View all the merge conflicts:
git diff

//--- View the conflicts against the base file
git diff --base <filename>

//--- Preview changes, before merging
git diff <sourcebranch> <targetbranch>
for eg, git diff origin/develop develop

//--- Show all changes made in last commit in any branch;
git show BAC-2667

//--- Add description to a branch;
git branch BAC-2667
git branch --edit-description "NEW BRANCH DESCRIPTION"
or,
git config branch.BAC-2667.description "NEW DESCRIPTION"

//--- Reveal branch description;
git config branch. <branch name>. description

//--- Config level alias with function ~v1;
git config --global --add alias.about '
	!describe() { 
		msg="$1"; 
		git config branch."$(git rev-parse --abbrev-ref HEAD)".description ${msg:+"$msg"}; 
	}; describe' 

//--- Config level alias with function ~v2:
git config --global --add alias.remark '
	!describe() { 
		msg="$1"; 
		git config branch."$(git branch --show-current)".description ${msg:+"$msg"}; 
	}; describe'

//--- Know the name of the branch;
git rev-parse --abbrev-ref HEAD
or,
git branch --show-current

//--- Undo last commit
git reset --soft HEAD^

//--- Undo last commit : KEEP CHANGES;
git reset --soft HEAD~1

//--- Undo last commit : REMOVE CHANGES
git reset --hard HEAD~1

//--- Fetch list of filename changed during git fetch
git fetch && git diff --name-only ..origin/develop
git fetch && git diff --name-only develop develop@{u}

// Copy commit history of one branch to another
git branch -m master main

// Git Restore Stage Changes
git restore --staged <file>...

// Alias to print only conflict files
git config --global --add alias.conflicts '!describe() { git diff --name-only --diff-filter=u; }; describe'

// Push Stash with a customer message 
git stash push -m "custom-message-here"

// List number of file changes in Stash
git stash show stash@{0}

// Show the file content difference in Stash
git stash show -p stash@{0}

````


-------------------------------------------------------------------------------------
### Q001 : What is Git;;

Git is a distributed version control system: tracking changes in any set of
files, usually used for coordinating work among programmers collaboratively
developing source code during software development.

Its goals include speed, data integrity, and support for distributed,
non-linear workflows.


-------------------------------------------------------------------------------------