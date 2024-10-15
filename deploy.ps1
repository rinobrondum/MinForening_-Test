$url = "https://heroku:" + $env:pat + "@git.heroku.com/minforening-web-production.git"
git checkout $env:Build.SourceBranchName
git remote add heroku $url
git push heroku $env:Build.SourceBranchName
