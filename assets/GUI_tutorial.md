# Running the program with GUI

1. Visit https://github.com/JazzBlaze/Shopify on your preferred browser. Click code -> download zip on top right.  
   ![tutorial1](https://raw.githubusercontent.com/Arghya-AB/Shopify/main/assets/tutorial1.png)
2. Locate the downloaded file  
   ![tutorial2](https://raw.githubusercontent.com/Arghya-AB/Shopify/main/assets/tutorial2.png)
3. Right click the file and unzip it  
   ![tutorial3](https://raw.githubusercontent.com/Arghya-AB/Shopify/main/assets/tutorial3.png)
4. Navigate into the unzipped folder and double click the powershell script  
   ![tutorial4](https://raw.githubusercontent.com/Arghya-AB/Shopify/main/assets/tutorial4.png)
5. Windows might show a security warning. Ignore and open it, you can view the source code of the file you want to [here](https://github.com/JazzBlaze/Shopify/blob/main/deploy_and_view.ps1)  
   ![tutorial5](https://raw.githubusercontent.com/Arghya-AB/Shopify/main/assets/tutorial5.png)
6. If you get an error in red text, search "Powershell" in windows search and open it. Run the following code to bypass certificate checks. Read about it [here](https://caiomsouza.medium.com/fix-for-powershell-script-not-digitally-signed-69f0ed518715).  
   ![tutorial6](https://raw.githubusercontent.com/Arghya-AB/Shopify/main/assets/tutorial6.png)  
   ![tutorial7](https://raw.githubusercontent.com/Arghya-AB/Shopify/main/assets/tutorial7.png)
7. Close the terminal and double click the file again. Windows smart screen may stop you but select "Run anyway".
8. This will automatically set up a virtual environment, download the required libraries, run the flask app and redirect the browser to the required page.  
   ![tutorial8](https://raw.githubusercontent.com/Arghya-AB/Shopify/main/assets/tutorial8.png)
9. In case it fails to open the link, simply navigate to http://127.0.0.1:5000/ on your browser.  
   ![tutorial9](https://raw.githubusercontent.com/Arghya-AB/Shopify/main/assets/tutorial9.png)
10. The frontend should be visible now.  
    ![tutorial10](https://raw.githubusercontent.com/Arghya-AB/Shopify/main/assets/tutorial10.png)
