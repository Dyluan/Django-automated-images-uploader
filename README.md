# Django-automated-images-uploader
This little program allows you to automatically upload images to your Django website (if you have an upload page on your admin of course).

## Creating the correct setup for the script
First of all, you'll need to install Geckodriver (https://github.com/mozilla/geckodriver/releases/tag/v0.29.1), a headless browser allowing the selenium package to perform actions.

Then, you'll need to have an Excel file containing the name of each images you wish to upload on your website. 
In that folder, create a sub-folder named 'images' containing the images.

## How to use the script
As you can see, the script is based on a class Upload that takes multiples arguments as inputs. in order to make it work for you, just change the arguments.

filename: is the name of the Excel file containing the name of your images.

column_name: is the name of the column in your Excel file, containing the name of your images.

img_format: .png, .jpg,..

admin_upload_url: the url where to uplaod the images.

master_user: the admin user.

master_pass: the admin password.

path_to_geckodriver: the path to the geckodriver you installed.

path_to_redo_button: the path to the 'redo' button (can be found using the console mode on every browser and by inspecting the redo button)
