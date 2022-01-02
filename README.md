# Shopify

Shopify website using python, flask and web technologies.

# To run this

## CLI way

This readme assumes that you are on windows and have powershell installed. (Search "powershell" in windows search to check).
This also assumes that you are using powershell as shell.
Open terminal (recommended to use [winterm](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701) but any terminal works).
You can skip this part if git and python are in PATH.

### Install python and git

One of the ways to do this will be to use a package manager like [Scoop](https://scoop.sh/).
Copy paste the codes in the terminal (copy the code and right click in the terminal app).

```pwsh
Set-ExecutionPolicy RemoteSigned -scope CurrentUser
iwr -useb get.scoop.sh | iex
scoop install git python
```

### Run the code

To run this and open the frontend in browser.
Open terminal and copy paste the following.

```pwsh
git clone https://github.com/JazzBlaze/Shopify.git
cd Shopify
./util_scripts/deploy_and_view.ps1
```

## GUI way

Visit https://github.com/Arghya-AB/Shopify on your preferred browser. Click code -> download zip on top right.  
![tutorial1](https://github.com/Arghya-AB/Shopify/tree/main/assets/tutorial1.png?raw=True)  
Locate the downloaded file  
![tutorial2](https://github.com/Arghya-AB/Shopify/tree/main/assets/tutorial2.png)  
Right click the file and unzip it  
![tutorial3](https://github.com/Arghya-AB/Shopify/tree/main/assets/tutorial3.png)  
Navigate into the unzipped folder and double click the powershell script  
![tutorial4](https://github.com/Arghya-AB/Shopify/tree/main/assets/tutorial4.png)
Windows might show a security warning. Ignore and open it, you can view the source code of the file you want to [here](https://github.com/Arghya-AB/Shopify/blob/main/deploy_and_view.ps1)  
![tutorial5](https://github.com/Arghya-AB/Shopify/tree/main/assets/tutorial5.png)  
If you get an error in red text, search "Powershell" in windows search and open it. Run the following code to bypass certificate checks. Read about it [here](https://caiomsouza.medium.com/fix-for-powershell-script-not-digitally-signed-69f0ed518715).  
![tutorial6](https://github.com/Arghya-AB/Shopify/tree/main/assets/tutorial6.png)  
![tutorial7](https://github.com/Arghya-AB/Shopify/tree/main/assets/tutorial7.png)  
Close the terminal and double click the file again. Windows smart screen may stop you but select "Run anyway".  
This will automatically set up a virtual environment, download the required libraries, run the flask app and redirect the browser to the required page.  
![tutorial8](https://github.com/Arghya-AB/Shopify/tree/main/assets/tutorial8.png)  
In case it fails to open the link, simply navigate to http://127.0.0.1:5000/ on your browser.  
![tutorial9](https://github.com/Arghya-AB/Shopify/tree/main/assets/tutorial9.png)  
The frontend should be visible now.  
![tutorial10](https://github.com/Arghya-AB/Shopify/tree/main/assets/tutorial10.png)

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
