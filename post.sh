#/bin/bash

name=$1
if [ "${name}x" = "x" ]; then echo "Give a name" && exit; fi

cat > /tmp/$1.md << EOF
+++
title = "$1"
date = $(date -Isecond)
draft = false
+++

![](result.png)

EOF

echo '```python' >> /tmp/$1.md
cat generate.py >> /tmp/$1.md
echo '```' >> /tmp/$1.md

scp /tmp/$1.md $LOGIN@$HOST:~/art_gen/content/posts/$1.md
ssh $LOGIN@$HOST mkdir art_gen/static/posts/$1
scp result.png $LOGIN@$HOST:~/art_gen/static/posts/$1/result.png
ssh $LOGIN@$HOST 'cd art_gen && ./generate.sh'
git commit -a -m "$1"
