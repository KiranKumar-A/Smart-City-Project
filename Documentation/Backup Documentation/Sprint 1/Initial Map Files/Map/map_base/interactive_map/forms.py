from django import forms


class MapForm(forms.Form):
    ## This sections shows the GUI and selection process to the user
    ## based on the selections from these aspects, the solution should
    ## then use the "get_google_url" method (interactive_map/views) to
    ## generate the embeded link to the google map and refresh the map
    ## html insert with the new link!

    ## the lists below that have the city_locaitons and general_options
    ## should, in the final release, be connected to the db so that the
    ## admin can edit the selected cities/general options.

    ## in next strints, this GUI should be expanded so that users can
    ## pick from 'student', 'tourist', etc and get more options (this,
    ## as well, should be connected to the database!


    ## LOCATIONS
    city_locations = (('', 'Select City'), 
                      ('brisbane', 'Brisbane'))
        
    ## GENERAL CITY INFORMATION USER STORY
    general_options = ( 
        ("park", "Parks"),
        ("zoo", "Zoos"),
        ("tourist attractions", "Tourist Attractions"),
        ("mall", "Malls"),
        ("museum", "Museums"),
        ("restaurant", "Restaurants")
        )
        
        
    location = forms.ChoiceField(label = "location",
                                 initial = 'Brisbane',
                                 choices = city_locations,
                                 required = True)

    selected_options = forms.MultipleChoiceField(widget=
                                                 forms.CheckboxSelectMultiple,
                                                 choices = general_options)

    


    