````
-------------------------------------------------------------------------------------
-> Title : Techlogs
-> Author : @neeraj-singh-jr
-> Status : Ongoing
-> Created : 03/02/2025
-> Updated : 03/02/2025
-> Summary : Notes indices are as follows (**** pending)
-------------------------------------------------------------------------------------
-> Q001 : Ignore DB_Store directory in Mac-OS;;
-------------------------------------------------------------------------------------
````

### TECHLOGS : BEGINNING

-------------------------------------------------------------------------------------
### Q001 : Ignore DB_Store directory in Mac-OS;;

If `.DS_Store` was never added to your git repository, simply add it to your 
`.gitignore` file.

#### Case 1:  If you don't have one, create a file called:
```
.gitignore
```

In you're the root directory of your app and simply write
```
**/.DS_Store
```

In it. This will never allow the .DS_Store file to sneak in your git.

#### Cas 2: if it's already there, write in your terminal:
```
$ find . -name .DS_Store -print0 | xargs -0 git rm -f --ignore-unmatch
```
then commit and push the changes to remove the .DS_Store from your remote repo:
```
# git commit -m "Remove .DS_Store from everywhere"

$ git push origin master
```
And now add .DS_Store to your .gitignore file, and then again commit and push 
with the 2 last pieces of code (git commit..., git push...)


#### Other Solution

If .DS_Store already committed:
```
find . -name .DS_Store -print0 | xargs -0 git rm --ignore-unmatch
```

To ignore them in all repository: (sometimes it named ._.DS_Store)
```
echo ".DS_Store" >> ~/.gitignore_global
echo "._.DS_Store" >> ~/.gitignore_global
echo "**/.DS_Store" >> ~/.gitignore_global
echo "**/._.DS_Store" >> ~/.gitignore_global
git config --global core.excludesfile ~/.gitignore_global
```
-------------------------------------------------------------------------------------