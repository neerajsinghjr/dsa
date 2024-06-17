````
-------------------------------------------------------------------------------------
-> Title : My Notes
-> Author : @neeraj-singh-jr
-> Status : Ongoing
-> Created : 02/11/2023
-> Updated : 21/11/2024
-> Summary : Notes indices are as follows (**** pending)
-------------------------------------------------------------------------------------
-> Q003 : Ignore DB_Store directory in MacoOs;;
-> Q002 : Increase Reach in online Job Portal;;
-> Q001 : Resume Make Tips and Tricks;;
-------------------------------------------------------------------------------------
````

### MY NOTES : BEGINNING 

-------------------------------------------------------------------------------------
### Q003 : Ignore DB_Store directory in Mac-OS;;

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
### Q002 : Increase Reach in online Job Portal;;

(Refer : https://www.youtube.com/watch?v=bMD-um6FkcA)

1) Make your profile 100% 

2) Regular updating your profile minimum 3 times a week (will show you as eagerly 
active state)

3) Resume headlines important include keywords 	
    - who you are
    - skills you possess
    - type of job you want

    - `eg1`, travel aspirant looking for job in amadeus gds, visa, 
    design travel packages. Well aware of hospitality and tourism 

    - eg2, HR human resource aspirant trained in practical aspect of 
    taking interview, all the important aspect of salary performance 
    management, training and development looking for job in the mentioned field.

4) keywords are extremely important
    - Key skills 
    - Hard Skills - knowledge you have.
    - Soft Skills - Way to doing the job

5) Apply for all the relevant Jobs (Don't ignore any jobs ignore the CTC). This will 
gonna to help you lifting your profile and improve your profile ranking as well.

6) Get your mobile and email verified


-------------------------------------------------------------------------------------
### Q001 : Resume Make Tips and Tricks;;

- There 3 C's important things 
1) Concise 
2) Clean  
3) Consistent 


#### Design 
- 1 or 2 pages only (preferrred 1 page only)
- proper spacing and proper formatting
    - Proper font 
    - Proper size 
    - Dark / Black-ink
- pdf format for sharing purposes

#### Provide only necessary information

- bullet points and avoid spelling mistakes 

#### Resume 7 sections:
- `Header`: 
	- name 
	- contact information, linked-in profile, mobile information
	- dob optional

- `Education`:
  - Education stuffs in reverse chronological order only with highlights

  - There are 4 points in education highlights
     1. name of the institute 
     2. majors 
     3. date of graduation or expected date if not complete 
     4. grades

- `Experience` :
  - for fresher
     1. bootcamp
     2. hackathons 
	 3. competitive coding

  - for experienced
    1. name of the firm
    2. timeline of employment
    3. location 
    4. job description
       - what did you achieve 
       - by what amount
       - how did you achieve that
       - eg 1 : Reduced the manual efforts of the Ops team by 
         90% by automating the sales of packs
         - what did you achieve : Reduced the manual efforts
         - by what amount : 90% 
         - how did you achieve that : automating the sales of packs 

       - eg2 : Increased the coach-to-customer ratio by 25% by 
         implementing an important feature called habit journey.

- `Projects`:
	- Mention max 1 to 3 projects only for highlighting stuffs.
	  - name of the project
      - tech stack of the project
      - description (similar to job description)
      - provide the link, github or deployment

- `Achievements`:
	- any awards in job, academic, school
	- can mention coding rank as well.
    - can mention office achievements as well.

- `Skills`:
	- programming skills 
		Language 
			- Advance: C++
			- Intermediate:
			- Novice : Javascript
- `Coursework`:
	- can mention the course with ceritification, offline or Online as well.

-------------------------------------------------------------------------------------