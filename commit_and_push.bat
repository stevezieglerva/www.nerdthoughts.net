title Git nerdthoughts.net
call git diff
call set /p msg=Commit Message: 
call git commit -a -m "  %msg%
call git push

