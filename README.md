# Shopify

Shopify website using python, flask and web technologies.

# To run this

This readme assumes that you are on windows and have powershell installed. (Search "powershell" in windows search to check).
This also assumes that you are using powershell as shell.
Open terminal (recommended to use [winterm](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701) but any terminal works).
You can skip this part if git and python are in PATH.

## Install python and git

One of the ways to do this will be to use a package manager like [Scoop](https://scoop.sh/)
Copy paste the codes in the terminal (copy the code and right click in the terminal app)

```pwsh
Set-ExecutionPolicy RemoteSigned -scope CurrentUser
iwr -useb get.scoop.sh | iex
scoop install git python
```

## Run the code

To run this and open the frontend in browser.
Open terminal and copy paste the following.

```pwsh
git clone https://github.com/JazzBlaze/Shopify.git
cd Shopify
./util_scripts/deploy_and_view.ps1
```

# For development

Running this should set up and activate a development virtual environment for you.

```pwsh
./util_scripts/start_dev.ps1
```

Run

```
python -m pip freeze > requirements.txt
```

after development and before committing.
