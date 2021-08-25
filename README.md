# What is this? 

A CLI to read a directory full of markdown files (recursively) and take the contents of the markdown file into a SQLite database


for f in $(find ~/Documents/ryancheley.com/content -name '*.md' | sed 's/ /\\ /g'); do markdown-to-sqlite docs.db posts $f || echo $f >> error.log; done
