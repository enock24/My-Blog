# Blog Post
## Author
[Towett Enock](https://github.com/enock24/My-Blog)
# Description
This is an application that allows users to sign in or sign up and post blogs abroad.It also allows them to comment and delete on the blogs they have created
## User Story
- Comment on the different blogs posted by other users.
- See the blogs posted by other uses.
- See the random quotes on the landing page
- Register to be allowed to log in to the application
- View blogs from the different categories.
- Submit a pitch to a specific category of their choice.
## BDD
| Behaviour             |                Input                |                                                                       Output |
| :-------------------- | :---------------------------------: | ---------------------------------------------------------------------------: |
| Load the page         |          **On page load**           |                               Get all posts, Select between signup and login |
| Select SignUp         | **Email**,**Username**,**Password** |                                                            Redirect to login |
| Select Login          |    **Username** and **password**    | Redirect to page with app blogs based on  commenting section |
| Select comment button |             **Comment**             |                                             Form that you input your comment |
| Click on submit       |                                     |       Redirect to all comments tamplate with your comment and other comments |
## Development Installation
To get the code..
1. Cloning the repository:
```bash
https://github.com/enock24/My-Blog.git
```
2. Move to the folder and install requirements
```bash
cd blog-post
pip install -r requirements.txt
```
3. Exporting Configurations
```bash
export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}
```
4. Running the application
```bash
./start.sh
```
Open the application on your browser `127.0.0.1:5000`.
## Technology used
- [Python3.8](https://www.python.org/)
- [Flask](http://flask.pocoo.org/)
- [Heroku](https://heroku.com)
## Contact Information
enookimuu@gmail.com
## License
 
 Licensed under[MIT license](license)