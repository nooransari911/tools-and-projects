# exec ssh-agent bash
# ssh-add ~/.ssh/github_key_1

echo "$(date '+%Y-%m-%d %H:%M:%S') Script started"
ssh -T git@github.com
git add .gitignore
git add .
# git remote add origin https://github.com/nooransari911/DSA4.git
git remote set-url origin git@github.com:nooransari911/tools-and-projects.git
echo "Enter commit message:"
read commit_message
echo ""
echo "Starting commit;"
git commit -m "$commit_message"
echo ""
echo "Starting push;"
git push -u origin master
