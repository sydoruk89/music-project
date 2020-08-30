# Django CRUD

**Author:** Roman Sydoruk **Version:** 1.0.0

## Description

The application creates a music project with one model and wire up that model using Django Views. Also there is a possibility to create. update or delete data (CRUD).

## Architecture

* Python 3.8.3
* Poetry
* Django

## Usage 
* create music_project project
* create music app
* migrate data
* create Music model
    * add title as a CharField with maximum length of 64 characters.
    * add author ForeignKey related to Django’s built in user model with CASCADE delete option.
    * add body TextField
* add model to admin
* modify Post model have user friendly display in admin
* create migrations and migrate data
* create a super user
* Add a few posts via Admin panel
* Addtemplates folder in root of project
    * register templates folder in project settings
* Create BlogListView that extends appropriate generic view
    associated url path is an empty string
* Create BlogDetailView that extends appropriate generic view
    associated url path is post/<int:pk>/
* Create BlogCreateView that extends appropriate generic view
    associated url path is post/new/
* update url patterns for app and project
* Create BlogUpdateView that extends appropriate generic view
    associated url path is post/<int:pk>/edit/
* Create BlogDeleteView that extends appropriate generic view
    associated url path is post/<int:pk>/delete/
* add detail view
    * link post_detail.html template
    * associate Post model
* create post_detail.html template
    * template should extend base
    * content should display post title and body