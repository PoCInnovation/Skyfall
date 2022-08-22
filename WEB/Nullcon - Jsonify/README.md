# Jsonify
```
Type: Web
Plateform : Nullcon
Difficulty : [x] [] [] [] []
Tools : web-console
```

#### DESCRIPTION
Everyone's telling me that serialize/unserialize should not be used with user-supplied input.</br>
Alright, I implemented my own JSON-based (un)serializer, so all potential vulnerabilities are gone, right?

#### STEP 1
```
if(isset($_GET['show'])&&isset($_GET['obj'])&&isset($_GET['flagfile']))
$f->readFlag();
```
