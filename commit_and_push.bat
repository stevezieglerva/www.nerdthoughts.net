title Git nerdthoughts.net
call git diff
call set /p msg=Commit Message: 
call git add --all
call git commit -a -m "git %msg%""
call git push

